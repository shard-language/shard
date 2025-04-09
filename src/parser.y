%{
    #include <stdio.h>
    #include <stdlib.h>
    extern int yylex(void);
    extern int yylineno;
    extern char* yytext;
    extern FILE *yyin;
    void yyerror(const char* msg);
%}

%token INTEGER LPAR RPAR SEMI

%left PLUS MINUS
%left STAR SLASH

%%
program:
    statements
    ;

statements:
    statement
    | statement SEMI statements
    ;

statement:
    empty
    | expression                            { printf("%d\n", $1); }
    ;

empty:
    ;

expression:
    INTEGER                                 { $$ = $1; }
    | expression PLUS expression            { $$ = $1 + $3; }
    | expression MINUS expression           { $$ = $1 - $3; }
    | expression STAR expression            { $$ = $1 * $3; }
    | expression SLASH expression           { $$ = $1 / $3; }
    | LPAR expression RPAR                  { $$ = $2; }
    | PLUS expression                       { $$ = +$2; }
    | MINUS expression                      { $$ = -$2; }
    ;
%%

void yyerror(const char* msg) {
    fprintf(stderr, "Error: %s at line %d\n", msg, yylineno);
}

int yywrap(void)
{
    return 1;
}