"""Run in Houdini's Python Shell with runpy.run_path (see README).

Creates nine native L-System SOPs in a new Geometry object. It does not clear
the current scene or save over a HIP file. No third-party packages are needed.
Tested with Houdini Apprentice 22.0.466.
"""

import json
import re
from pathlib import Path

import hou

ROOT = Path(__file__).resolve().parents[1]


def normalized(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def parameter(node, label, names=()):
    # Use visible parameter labels so internal-name differences fail clearly.
    matches = [p for p in node.parms()
               if normalized(p.parmTemplate().label()) == normalized(label)]
    if len(matches) == 1:
        return matches[0]
    for name in names:
        parm = node.parm(name)
        if parm is not None:
            return parm
    raise RuntimeError(f"Cannot find {label!r} on {node.path()}")


def rule_lines(path):
    return [line.strip() for line in path.read_text().splitlines()
            if line.strip() and not line.lstrip().startswith("#")]


def configure(node, config, generation):
    parameter(node, "Generations", ("generations",)).set(generation)
    parameter(node, "Premise", ("premise",)).set(config["premise"])
    parameter(node, "Angle", ("angleinit",)).set(config["angle"])
    parameter(node, "Step Size", ("stepinit",)).set(config["step"])
    parameter(node, "Random Scale", ("randscale",)).set(0)
    kind = parameter(node, "Type", ("type",))
    labels = list(kind.menuLabels())
    if "Skeleton" not in labels:
        raise RuntimeError(f"No Skeleton geometry option on {node.path()}")
    token = kind.menuItems()[labels.index("Skeleton")]
    if kind.parmTemplate().type() == hou.parmTemplateType.String:
        kind.set(token)
    else:
        kind.set(labels.index("Skeleton"))

    source = ROOT / "grammars" / config["rules_file"]
    rules = rule_lines(source)
    read_file = parameter(node, "Read Rules From File", ("usefile",))
    rule_count = node.parm("numrules")
    if rule_count is not None:
        rule_count.set(len(rules))

    # Prefer editable inline rules. Some versions expose their fields differently;
    # the documented Rule File path remains a usable fallback in that case.
    fields = []
    for parm in node.parms():
        if parm.parmTemplate().type() != hou.parmTemplateType.String:
            continue
        match = re.fullmatch(r"rule(\d+)", parm.name(), re.IGNORECASE)
        if not match:
            match = re.fullmatch(r"Rule\s*(\d+)", parm.parmTemplate().label(), re.IGNORECASE)
        if match:
            fields.append((int(match.group(1)), parm))
    fields.sort(key=lambda pair: pair[0])
    if len(fields) >= len(rules):
        for i, (_, parm) in enumerate(fields):
            parm.set(rules[i] if i < len(rules) else "")
        for index, _ in fields:
            toggle = node.parm(f"userule{index}")
            if toggle is not None:
                toggle.set(1)
        read_file.set(0)
        parameter(node, "Rule File", ("rulefile",)).set("")
        mode = "inline rules"
    else:
        parameter(node, "Rule File", ("rulefile",)).set(source.as_posix())
        read_file.set(1)
        mode = "rule file"
    node.setComment("\n".join([config["title"], f"Generation {generation}",
                               f"Premise: {config['premise']}", *rules]))
    node.cook(force=True)
    if node.errors():
        raise RuntimeError(f"{node.path()}: {'; '.join(node.errors())}")
    geo = node.geometry()
    if geo is None or len(geo.prims()) == 0:
        raise RuntimeError(f"{node.path()} generated no primitives")
    return {"node": node.path(), "rules": mode, "primitives": len(geo.prims()),
            "warnings": list(node.warnings())}


def build_lab():
    config = json.loads((ROOT / "grammars/settings.json").read_text())
    container = hou.node("/obj").createNode("geo", "lab05_grammars")
    # Only remove default children of the object just created by this script.
    for child in container.children():
        child.destroy()
    report = []
    try:
        for row, (key, settings) in enumerate(config.items()):
            for column, generation in enumerate(settings["generations"]):
                node = container.createNode("lsystem", f"{key}_n{generation:02d}")
                node.setPosition(hou.Vector2(column * 4, -row * 3))
                node.setDisplayFlag(False)
                node.setRenderFlag(False)
                report.append(configure(node, settings, generation))
        selected = container.node("fern_n12")
        selected.setDisplayFlag(True)
        selected.setRenderFlag(True)
        selected.setCurrent(True, clear_all_selected=True)
        container.moveToGoodPosition()
    except Exception:
        print(f"Import stopped. Incomplete nodes are available at {container.path()} for inspection.")
        raise
    print(json.dumps(report, indent=2))
    print(f"Created {container.path()}. Select a node, set its display flag, and use Front view.")
    print("Save the scene with File > Save As after checking the output.")
    return container


if __name__ == "__main__":
    build_lab()
