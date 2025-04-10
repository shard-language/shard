import tree
import sys

class Environment:
    def __init__(self):
        self.c_code = []

    def __repr__(self):
        return f"Environment(c_code={self.c_code})"

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
                if right == '0':
                    print(f"ERROR: tried to divide {left} by 0")
                    sys.exit(1)
                return f"({left} / {right})"

        elif isinstance(node, tree.Group):
            return f"({self.evaluate(node.expression)})"

    def write_c(self, file):
        with open(file, 'w') as f:
            f.write("int main() {\n")
            
            for line in self.c_code:
                if line is not None:
                    f.write(f"  {line};\n")

            f.write("   return 0;\n")
            f.write("}\n")