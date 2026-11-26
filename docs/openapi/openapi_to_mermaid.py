#!/usr/bin/env python3.14
"""Generate a Mermaid endpoint diagram from openapi-v1.yaml.

Uses only the Python standard library, so it does not parse general YAML.
It reads the layout used by openapi-v1.yaml: a top level `security:` list,
then `paths:` with two space indented paths, four space indented methods,
and `tags:`, `security:`, `summary:`, and `x-diagram-notes:` keys inside each
method. Each note is a `to:` (client, database, or email) and a `label:`, and
is drawn as a dotted line from the endpoint to that node.

Usage: openapi_to_mermaid.py openapi-v1.yaml api.mmd
"""

import sys
from pathlib import Path

METHODS = {"get", "post", "put", "patch", "delete"}

# Nodes that a note can point at: key -> (node id, label, style).
TARGETS = {
    "client": ("C", None, "client"),
    "database": ("DB", '[("Database")]', "store"),
    "email": ("EM", '(["Email service"])', "client"),
}

# Group order, title, and node style.
GROUPS = [
    ("wellknown", "Well Known (no JWT)", "open"),
    ("optional", "Unauthenticated (JWT optional)", "open"),
    ("auth", "Authenticated (JWT required)", "auth"),
    ("admin", "Admin role required", "admin"),
]

STYLES = {
    "client": "fill:#dff1e6,stroke:#92b69e",
    "open": "fill:#e0edfc,stroke:#9bb7da",
    "auth": "fill:#eee3f6,stroke:#bba2cc",
    "admin": "fill:#fff3ce,stroke:#d7be78",
    "store": "fill:#fff5d9,stroke:#ccb77e",
}


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def parse_security(lines: list[str]) -> str:
    """Classify a security block: none, optional, or bearer."""
    text = " ".join(line.strip() for line in lines)
    if "bearerAuth" in text and "- {}" in text:
        return "optional"
    if "bearerAuth" in text:
        return "bearer"
    return "none"


def parse(path: Path):
    lines = path.read_text().splitlines()
    default_security = "bearer"
    operations = []
    in_paths = False
    current_path = None
    current_op = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        indent = indent_of(line)

        if indent == 0:
            in_paths = stripped == "paths:"
            if stripped.startswith("security:"):
                if stripped == "security: []":
                    default_security = "none"
                else:
                    block = []
                    j = i + 1
                    while j < len(lines) and (not lines[j].strip() or indent_of(lines[j]) > 0):
                        block.append(lines[j])
                        j += 1
                    default_security = parse_security(block)
            i += 1
            continue

        if not in_paths:
            i += 1
            continue

        if indent == 2 and stripped.endswith(":") and stripped.startswith("/"):
            current_path = stripped[:-1]
            current_op = None
        elif indent == 4 and stripped.rstrip(":") in METHODS and current_path:
            current_op = {
                "method": stripped.rstrip(":").upper(),
                "path": current_path,
                "tags": [],
                "security": None,
                "notes": [],
            }
            operations.append(current_op)
        elif indent == 6 and current_op is not None:
            if stripped.startswith("tags:"):
                current_op["tags"] = [t.strip() for t in stripped[len("tags:"):].strip().strip("[]").split(",") if t.strip()]
            elif stripped.startswith("x-diagram-notes:"):
                j = i + 1
                while j < len(lines) and (not lines[j].strip() or indent_of(lines[j]) > 6):
                    item = lines[j].strip()
                    if item.startswith("- to:"):
                        current_op["notes"].append({"to": item[len("- to:"):].strip(), "label": ""})
                    elif item.startswith("label:") and current_op["notes"]:
                        current_op["notes"][-1]["label"] = item[len("label:"):].strip()
                    j += 1
            elif stripped == "security: []":
                current_op["security"] = "none"
            elif stripped.startswith("security:"):
                block = []
                j = i + 1
                while j < len(lines) and (not lines[j].strip() or indent_of(lines[j]) > 6):
                    block.append(lines[j])
                    j += 1
                current_op["security"] = parse_security(block)
        i += 1

    for op in operations:
        if op["security"] is None:
            op["security"] = default_security
    return operations


def group_of(op: dict) -> str:
    if "Well Known" in op["tags"]:
        return "wellknown"
    if op["security"] in ("none", "optional"):
        return "optional"
    if "Admin" in op["tags"]:
        return "admin"
    return "auth"


def render(operations: list[dict]) -> str:
    out = [
        "---",
        'title: "Golden Eagle Flight Plan: API Endpoints (v1)"',
        "---",
        "%% Generated by openapi_to_mermaid.py from openapi-v1.yaml. Do not edit by hand.",
        "flowchart LR",
        '    C(["Front End<br/>(browser)"])',
        "",
    ]
    grouped = {key: [] for key, _, _ in GROUPS}
    for number, op in enumerate(operations, start=1):
        op["id"] = f"E{number}"
        grouped[group_of(op)].append(op)

    for key, title, _ in GROUPS:
        if not grouped[key]:
            continue
        out.append(f'    subgraph {key.upper()} ["{title}"]')
        for op in grouped[key]:
            out.append(f'        {op["id"]}["{op["method"]} {op["path"]}"]')
        out.append("    end")
        out.append("")

    for key, _, _ in GROUPS:
        ids = " & ".join(op["id"] for op in grouped[key])
        if not ids:
            continue
        label = '|"Bearer JWT"|' if key in ("auth", "admin") else ""
        out.append(f"    C -->{label} {ids}")
    out.append("")

    used = []
    for op in operations:
        for note in op["notes"]:
            if note["to"] not in TARGETS:
                raise SystemExit(f'{op["path"]}: unknown note target "{note["to"]}"')
            if note["to"] != "client" and note["to"] not in used:
                used.append(note["to"])
    for to in used:
        out.append(f"    {TARGETS[to][0]}{TARGETS[to][1]}")
    for op in operations:
        for note in op["notes"]:
            out.append(f'    {op["id"]} -.->|"{note["label"]}"| {TARGETS[note["to"]][0]}')
    out.append("")

    out.append(f'    classDef client {STYLES["client"]},stroke-width:1.4px,color:#253047')
    for style in ("open", "auth", "admin"):
        out.append(f"    classDef {style} {STYLES[style]},stroke-width:1.4px,color:#253047")
    out.append(f'    classDef store {STYLES["store"]},stroke-width:1.4px,color:#253047')
    out.append("    class C client")
    for to in used:
        out.append(f"    class {TARGETS[to][0]} {TARGETS[to][2]}")
    for key, _, style in GROUPS:
        if grouped[key]:
            out.append(f'    class {",".join(op["id"] for op in grouped[key])} {style}')
    out.append("    linkStyle default stroke:#667085,stroke-width:2px")
    return "\n".join(out) + "\n"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    operations = parse(Path(sys.argv[1]))
    if not operations:
        print(f"No operations found in {sys.argv[1]}", file=sys.stderr)
        return 1
    Path(sys.argv[2]).write_text(render(operations))
    print(f"Wrote {sys.argv[2]} with {len(operations)} operations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
