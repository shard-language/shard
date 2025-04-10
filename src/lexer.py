import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS', 'MINUS', 'STAR', 'SLASH',
    'LPAR', 'RPAR', 'SEMI'
)

t_ignore = ' \t\r'

t_NUMBER = r'\d+(\.\d+)?'

t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'

t_LPAR = r'\('
t_RPAR = r'\)'
t_SEMI = r';'

def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

def t_error(t):
    print(f"ERROR: illegal character '{t.value[0]}' found at line {t.lineno} and position {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()