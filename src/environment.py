import tree
import sys
import const

class Environment:
    def __init__(self):
        self.c_code = []
        self.variables = {}

    def __repr__(self):
        return f"Environment(c_code={self.c_code}, variables={self.variables})"

    def evaluate(self, node):
        if isinstance(node, tree.Value):
            return f"{node.value}"

        elif isinstance(node, tree.UnaryOp):
            if node.operator == '+':
                return f"+{self.evaluate(node.value)}"
            elif node.operator == '-':
                return f"-{self.evaluate(node.value)}"

        elif isinstance(node, tree.BinaryOp):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            if node.operator == '+':
                return f"({left} + {right})"
            elif node.operator == '-':
                return f"({left} - {right})"
            elif node.operator == '*':
                return f"({left} * {right})"
            elif node.operator == '/':
                if float(right) == 0:
                    print(f"ERROR: tried to divide {left} by 0")
                    sys.exit(1)
                return f"({left} / {right})"
            elif node.operator == '%':
                if float(right) == 0:
                    print(f"ERROR: expression modulo 0")
                    sys.exit(1)
                return f"({left} % {right})"

        elif isinstance(node, tree.Group):
            return f"({self.evaluate(node.expression)})"

        elif isinstance(node, tree.VariableDeclaration):
            if node.name in self.variables:
                print(f"ERROR: cannot redeclare variable '{node.name}' with type {self.variables[node.name]}")
                sys.exit(1)
            self.variables[node.name] = node._type
            if node._type == "byte": return f"char {node.name}"
            elif node._type == "word": return f"short {node.name}"
            elif node._type == "dword": return f"int {node.name}"
            elif node._type == "qword": return f"long long {node.name}"
            elif node._type == "float": return f"float {node.name}"
            elif node._type == "double": return f"double {node.name}"

        elif isinstance(node, tree.VariableAssignment):
            if node.name not in self.variables:
                print(f"ERROR: cannot access to undeclared variable '{node.name}'")
                sys.exit(1)
            value = self.evaluate(node.value)

            if self.variables[node.name] == "byte" and value > const.BYTE_MAX_VAL:
                print(f"ERROR: data type 'byte' is not appropriated for value {value}")
                sys.exit(1)
            elif self.variables[node.name] == "word" and value > const.WORD_MAX_VAL:
                print(f"ERROR: data type 'word' is not appropriated for value {value}")
                sys.exit(1)
            elif self.variables[node.name] in ["dword", "float"] and value > const.DWORD_MAX_VAL:
                print(f"ERROR: data type 'dword' is not appropriated for value {value}")
                sys.exit(1)
            elif self.variables[node.name] in ["qword", "double"] and value > const.QWORD_MAX_VAL:
                print(f"ERROR: data type 'qword' is not appropriated for value {value}")
                sys.exit(1)

            if node.operator == '=': return f"{node.name} = ({value})"
            elif node.operator == '+=': return f"{node.name} += ({value})"
            elif node.operator == '-=': return f"{node.name} -= ({value})"
            elif node.operator == '*=': return f"{node.name} *= ({value})"
            elif node.operator == '/=':
                if float(value) == 0:
                    print(f"ERROR: tried to divide '{node.name}' by 0")
                    sys.exit(1)
                return f"{node.name} /= ({value})"
            elif node.operator == '%=':
                if float(value) == 0:
                    print(f"ERROR: '{node.name}' modulo 0")
                    sys.exit()
                return f"{node.name} %= ({value})"

        elif isinstance(node, tree.VariableValue):
            if node.name not in self.variables:
                print(f"ERROR: cannot access to undeclared variable '{node.name}'")
                sys.exit(1)
            return f"({node.name})"

    def write_c(self, file):
        with open(file, 'w') as f:
            f.write("/*\n")
            f.write("   This file has been automatically generated by the Shard compiler.\n")
            f.write("   Do not edit instead if you need to edit the generated code.\n")
            f.write("*/\n\n")

            f.write("int main() {\n")
            
            for line in self.c_code:
                if line is not None:
                    f.write(f"  {line};\n")

            f.write("   return 0;\n")
            f.write("}\n")