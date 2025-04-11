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

class VariableDeclaration:
    def __init__(self, _type, name):
        self._type = _type
        self.name = name

    def __repr__(self):
        return f"VariableDeclaration(type={self._type}, name={self.name})"

class VariableAssignment:
    def __init__(self, name, operator, value):
        self.name = name
        self.operator = operator
        self.value = value

    def __repr__(self):
        return f"VariableAssignment(name={self.name}, operator={self.operator}, value={self.value})"

class VariableValue:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"VariableValue(name={self.name})"