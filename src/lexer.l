%{
    #include <stdio.h>
    #include <stdlib.h>
    #include "parser.tab.h"
%}

%%
[ \t\r]+

[0-9]+        { yylval = atoi(yytext); return INTEGER; }
\n            { yylineno++; }

\+            { return PLUS; }
-             { return MINUS; }
\*            { return STAR; }
\/            { return SLASH; }

\(            { return LPAR; }
\)            { return RPAR; }
;             { return SEMI; }

.             { fprintf(stderr, "Illegal character '%c'. Exiting...\n", yytext[0]); exit(0); }
%%