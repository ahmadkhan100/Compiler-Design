%{
#include <stdio.h>
#include <stdlib.h>
#include "symbol_table.h"
#include "tac_generator.h"

void yyerror(const char *s);
int yylex();
%}

%token IF WHILE IDENTIFIER NUMBER
%left '+' '='

%%

program:
    declarations statements
    ;

declarations:
    | declarations declaration
    ;

declaration:
    type IDENTIFIER ';' {
        insert_symbol($2);
    }
    ;

statements:
    | statements statement
    ;

statement:
    IF '(' expression ')' statement {
        generate_if_statement($3, $5);
    }
    | WHILE '(' expression ')' statement {
        generate_while_statement($3, $5);
    }
    | '{' statements '}' 
    | expression ';' {
        generate_expression($1);
    }
    ;

expression:
    IDENTIFIER '=' expression {
        $$ = generate_assignment($1, $3);
    }
    | expression '+' expression {
        $$ = generate_addition($1, $3);
    }
    | NUMBER {
        $$ = generate_number($1);
    }
    ;

%%

int main() {
    return yyparse();
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
