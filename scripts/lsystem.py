"""Small deterministic 2D interpreter for the syntax used in this lab.

This is a portable preview, not a replacement for Houdini's L-System SOP.
Supports simultaneous parametric rewriting, F/f, +/- angles, branches,
and polygon vertices. Unsupported commands and expressions fail explicitly.
"""

import ast
import json
import math
import operator
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPERATORS = {ast.Add: operator.add, ast.Sub: operator.sub,
             ast.Mult: operator.mul, ast.Div: operator.truediv}


def evaluate(expression, variables):
    def walk(node):
        if isinstance(node, ast.Constant) and type(node.value) in (float, int):
            return node.value
        if isinstance(node, ast.Name) and node.id in variables:
            return variables[node.id]
        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](walk(node.left), walk(node.right))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -walk(node.operand)
        raise ValueError(f"Unsupported expression: {expression}")
    value = float(walk(ast.parse(expression, mode="eval").body))
    if not math.isfinite(value):
        raise ValueError(f"Non-finite expression: {expression}")
    return value


def tokenize(text):
    result, i = [], 0
    while i < len(text):
        symbol = text[i]
        i += 1
        if symbol.isspace():
            continue
        args = []
        if i < len(text) and text[i] == "(":
            end = text.find(")", i)
            if end < 0:
                raise ValueError("Unclosed argument list")
            args = [arg.strip() for arg in text[i + 1:end].split(",")]
            i = end + 1
        result.append((symbol, args))
    return result


def load_rules(path):
    rules = {}
    for line in Path(path).read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        lhs, rhs = line.split("=", 1)
        tokens = tokenize(lhs.strip())
        if len(tokens) != 1 or tokens[0][0] in rules:
            raise ValueError(f"Invalid or duplicate rule: {lhs}")
        symbol, parameters = tokens[0]
        rules[symbol] = (parameters, tokenize(rhs))
    return rules


def load_config():
    return json.loads((ROOT / "grammars/settings.json").read_text())


def expand(config, generation):
    if not isinstance(generation, int) or not 0 <= generation <= 16:
        raise ValueError("Use an integer generation between 0 and 16")
    rules = load_rules(ROOT / "grammars" / config["rules_file"])
    word = [(c, [evaluate(a, {}) for a in args])
            for c, args in tokenize(config["premise"])]
    for _ in range(generation):
        output = []
        for symbol, args in word:
            if symbol not in rules:
                output.append((symbol, args))
                continue
            parameters, replacement = rules[symbol]
            if len(parameters) != len(args):
                raise ValueError(f"Wrong argument count for {symbol}")
            variables = dict(zip(parameters, args))
            output.extend((c, [evaluate(a, variables) for a in expressions])
                          for c, expressions in replacement)
            if len(output) > 500_000:
                raise ValueError("Preview expansion exceeds 500,000 symbols")
        word = output
    return word, set(rules)


def geometry(config, generation):
    word, nonterminals = expand(config, generation)
    x, y, heading = 0.0, 0.0, 0.0  # +Y is forward; + turns right.
    stack, lines, polygons = [], [], []
    polygon = None
    for symbol, args in word:
        if symbol in "Ff":
            length = args[0] if args else config["step"]
            width = args[1] if len(args) > 1 else 0.015
            radians = math.radians(heading)
            nx, ny = x + length * math.sin(radians), y + length * math.cos(radians)
            if symbol == "F":
                lines.append(((x, y), (nx, ny), width))
            x, y = nx, ny
        elif symbol in "+-":
            heading += (1 if symbol == "+" else -1) * (args[0] if args else config["angle"])
        elif symbol == "[":
            stack.append((x, y, heading))
        elif symbol == "]":
            if not stack:
                raise ValueError("Unmatched closing bracket")
            x, y, heading = stack.pop()
        elif symbol == "{":
            if polygon is not None:
                raise ValueError("Nested polygons are unsupported")
            polygon = []
        elif symbol == ".":
            if polygon is None:
                raise ValueError("Vertex outside polygon")
            polygon.append((x, y))
        elif symbol == "}":
            if polygon is None or len(polygon) < 3:
                raise ValueError("Invalid polygon")
            polygons.append(polygon)
            polygon = None
        elif symbol not in nonterminals:
            raise ValueError(f"Unsupported turtle command: {symbol}")
    if stack or polygon is not None:
        raise ValueError("Unclosed branch or polygon")
    return lines, polygons


def write_obj(path, lines, polygons):
    text = ["# Lab 05 portable L-system preview; XY plane, +Y up"]
    index = 1
    for start, end, _ in lines:
        text += [f"v {x:.9f} {y:.9f} 0" for x, y in (start, end)]
        text.append(f"l {index} {index + 1}")
        index += 2
    for polygon in polygons:
        text += [f"v {x:.9f} {y:.9f} 0" for x, y in polygon]
        # Houdini/front view looks down -Z. Use counterclockwise leaf faces.
        area = sum(polygon[i][0] * polygon[(i + 1) % len(polygon)][1]
                   - polygon[(i + 1) % len(polygon)][0] * polygon[i][1]
                   for i in range(len(polygon)))
        indices = list(range(index, index + len(polygon)))
        if area < 0:
            indices.reverse()
        text.append("f " + " ".join(map(str, indices)))
        index += len(polygon)
    Path(path).write_text("\n".join(text) + "\n")
