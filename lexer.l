%{
#include "y.tab.h"
%}

%%

"if"        return IF;
"while"     return WHILE;
[a-zA-Z_][a-zA-Z0-9_]*  return IDENTIFIER;
[0-9]+      return NUMBER;
"=="        return EQUAL;
"+"         return '+';
"="         return '=';
"{"         return '{';
"}"         return '}';
";"         return ';';
[ \t\n]     ;  // Ignore whitespace
.           return yytext[0];  // Single character tokens

%%
