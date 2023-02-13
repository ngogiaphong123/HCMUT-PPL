grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF;

// Keywords
AUTO : 'auto' ;
BREAK : 'break' ;
BOOLEAN : 'boolean' ;
DO : 'do' ;
ELSE : 'else' ;
FALSE : 'false' ;
FLOAT : 'float' ;
FOR : 'for' ;
FUNCTION : 'function' ;
IF : 'if' ;
INTEGER : 'integer' ;
RETURN : 'return' ;
STRING : 'string' ;
TRUE : 'true' ;
WHILE : 'while' ;
VOID : 'void' ;
OUT : 'out' ;
CONTINUE : 'continue' ;
OF : 'of' ;
INHERIT : 'inherit' ;
ARRAY : 'array' ;
// SEPARATORS
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LBRACKET : '[' ;
RBRACKET : ']' ;
SEMI : ';' ;
COMMA : ',' ;
DOT : '.' ;
COLON : ':' ;
ASSIGN : '=' ;
// OPERATORS
ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;
MOD : '%' ;
CLAIM : '!' ;
AND : '&&' ;
OR : '||' ;
EQ : '==' ;
NEQ : '!=' ;
LT : '<' ;
LTE : '<=' ;
GT : '>' ;
GTE : '>=' ;
DOUBLECOLON : '::' ;
// IDENTIFIERS
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ;
// LITERALS
INTLIT : '0' | [1-9][0-9]* ('_' [0-9]+)* {
    self.text = self.text.replace("_", "")
};
fragment INTPART : '0' | [1-9][0-9]* ('_' [0-9]+)* ;
fragment DECIMALPART : '.' [0-9]+;
fragment EXPONENTPART : [eE] [+-]? [0-9]+;
FLOATLIT : INTPART DECIMALPART | INTPART DECIMALPART? EXPONENTPART {
    self.text = self.text.replace("_", "")
};
BOOLEANLIT : TRUE | FALSE ;
fragment ESC : '\\' ( 'b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\' | '"' );
STRINGLIT : '"' ( ~ ('"' | '\\') | ESC )* '"';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;