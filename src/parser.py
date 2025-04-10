import ply.yacc as yacc
import tree

from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'STAR', 'SLASH'),
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
                 | expression'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_expression_value(p):
    '''expression : NUMBER'''
    p[0] = tree.Value(p[1])

def p_expression_unary(p):
    '''expression : PLUS expression %prec POSITIVE
                  | MINUS expression %prec NEGATIVE'''
    p[0] = tree.UnaryOp(p[1], p[2])

def p_expression_binary(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression STAR expression
                  | expression SLASH expression'''
    p[0] = tree.BinaryOp(p[1], p[2], p[3])

def p_expression_group(p):
    '''expression : LPAR expression RPAR'''
    p[0] = tree.Group(p[2])

def p_error(p):
    if p:
        print(f"ERROR: syntax error at '{p.value}' found at line {t.lineno}")
    else:
        print("ERROR: missing semicolon")

parser = yacc.yacc(outputdir="src/parser_out")