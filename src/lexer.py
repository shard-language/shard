import ply.lex as lex

keywords = {
    "byte": "BYTE",
    "word": "WORD",
    "dword": "DWORD",
    "qword": "QWORD",
    "float": "FLOAT",
    "double": "DOUBLE",
}

tokens =  tuple(keywords.values()) + (
    'NUMBER', 'IDENTIFIER',
    'PLUS', 'MINUS', 'STAR', 'SLASH', 'PERCENT',
    'LPAR', 'RPAR', 'SEMI',
    'EQUAL', 'PLUS_EQUAL', 'MINUS_EQUAL', 'STAR_EQUAL', 'SLASH_EQUAL', 'PERCENT_EQUAL'
)

t_ignore = ' \t\r'

t_NUMBER = r'\d+(\.\d+)?'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_PERCENT = r'%'

t_LPAR = r'\('
t_RPAR = r'\)'
t_SEMI = r';'

t_EQUAL = r'='
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_STAR_EQUAL = r'\*='
t_SLASH_EQUAL = r'/='
t_PERCENT_EQUAL = r'%='

def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

def t_error(t):
    print(f"ERROR: illegal character '{t.value[0]}' found at line {t.lineno} and position {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()