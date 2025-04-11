import ply.yacc as yacc
import tree
import os
import sys

from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'STAR', 'SLASH', 'PERCENT'),
    ('left', 'EQUAL', 'PLUS_EQUAL', 'MINUS_EQUAL', 'STAR_EQUAL', 'SLASH_EQUAL', 'PERCENT_EQUAL'),
    ('right', 'POSITIVE', 'NEGATIVE')
)

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement SEMI statement_list'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[3]

def p_statement(p):
    '''statement : empty
                 | expression
                 | declaration'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_expression_value(p):
    '''expression : NUMBER'''
    p[0] = tree.Value(p[1])

def p_expression_variable_value(p):
    '''expression : IDENTIFIER'''
    p[0] = tree.VariableValue(p[1])

def p_expression_unary(p):
    '''expression : PLUS expression %prec POSITIVE
                  | MINUS expression %prec NEGATIVE'''
    p[0] = tree.UnaryOp(p[1], p[2])

def p_expression_binary(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression STAR expression
                  | expression SLASH expression
                  | expression PERCENT expression'''
    p[0] = tree.BinaryOp(p[1], p[2], p[3])

def p_expression_group(p):
    '''expression : LPAR expression RPAR'''
    p[0] = tree.Group(p[2])

def p_expression_assignment_variable(p):
    '''expression : IDENTIFIER EQUAL expression
                  | IDENTIFIER PLUS_EQUAL expression
                  | IDENTIFIER MINUS_EQUAL expression
                  | IDENTIFIER STAR_EQUAL expression
                  | IDENTIFIER SLASH_EQUAL expression
                  | IDENTIFIER PERCENT_EQUAL expression'''
    p[0] = tree.VariableAssignment(p[1], p[2], p[3])

def p_declaration_variable(p):
    '''declaration : BYTE IDENTIFIER
                   | WORD IDENTIFIER
                   | DWORD IDENTIFIER
                   | QWORD IDENTIFIER
                   | FLOAT IDENTIFIER
                   | DOUBLE IDENTIFIER'''
    p[0] = tree.VariableDeclaration(p[1], p[2])

def p_error(p):
    if p:
        print(f"ERROR: syntax error at '{p.value}' found at line {p.lineno}")
    else:
        print("ERROR: missing semicolon")

sys.stderr = open(os.devnull, 'w')
parser = yacc.yacc(outputdir="src/parser_out")
sys.stderr = sys.__stderr__