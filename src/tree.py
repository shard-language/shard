class Value:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Value(value={self.value})"

class UnaryOp:
    def __init__(self, operator, value):
        self.operator = operator
        self.value = value

    def __repr__(self):
        return f"UnaryOp(operator={self.operator}, value={self.value})"

class BinaryOp:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryOp(left={self.left}, operator={self.operator}, right={self.right})"

class Group:
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"Group(expression={self.expression})"