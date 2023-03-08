/* 2014121 */
/* Ngo Gia Phong */
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declarationList EOF;

declarationList: declaration declarationList | declaration;

declaration : varDeclaration | funcDeclaration;

// 5.1 Variables Declaration
varDeclaration : initVarDeclaration | fullVarDeclaration;

initVarDeclaration : idList COLON type_specifier SEMI;

fullVarDeclaration : helper SEMI;

baseVarDeclaration : IDENTIFIER COLON type_specifier ASSIGN expression;

helper : IDENTIFIER COMMA helper COMMA expression | baseVarDeclaration;

idList : IDENTIFIER COMMA idList | IDENTIFIER;

atomicType : INTEGER | FLOAT | BOOLEAN | STRING;

arrayType : ARRAY LBRACKET dimensions RBRACKET OF atomicType;

voidType : VOID;

autoType : AUTO;

dimensions : INTLIT COMMA dimensions | INTLIT;

type_specifier : autoType | atomicType | arrayType;

arrayCell : IDENTIFIER LBRACKET expressions RBRACKET;
// 5.2 Function Declaration

funcDeclaration : functionPrototype functionBody;

functionPrototype : IDENTIFIER COLON FUNCTION returnType LPAREN parameters RPAREN |
                    IDENTIFIER COLON FUNCTION returnType LPAREN parameters RPAREN INHERIT IDENTIFIER;

returnType : atomicType | voidType | arrayType | autoType;

parameters : parameterList |;

parameterList : parameter COMMA parameterList | parameter;

parameter : IDENTIFIER COLON type_specifier
            | INHERIT IDENTIFIER COLON type_specifier
            | OUT IDENTIFIER COLON type_specifier
            | INHERIT OUT IDENTIFIER COLON type_specifier;

// 7 Statements
blockStatement : LBRACE statements RBRACE;

functionBody : blockStatement;

statements : statementList |;

statementList : statement statementList |;

statement : varDeclaration | assignmentStatement | ifStatement | forStatement | whileStatement | doWhileStatement | breakStatement | continueStatement | returnStatement | callStatement | blockStatement;

assignmentStatement : leftHandSide ASSIGN expression SEMI;

leftHandSide : IDENTIFIER | arrayCell;

ifStatement : IF LPAREN expression RPAREN statement | IF LPAREN expression RPAREN statement ELSE statement;

forStatement : FOR LPAREN IDENTIFIER ASSIGN expression COMMA expression COMMA expression RPAREN statement;

whileStatement : WHILE LPAREN expression RPAREN statement;

doWhileStatement : DO statement WHILE LPAREN expression RPAREN SEMI;

breakStatement : BREAK SEMI;

continueStatement : CONTINUE SEMI;

returnStatement : RETURN expressions SEMI;

callStatement : specialFunctionCall SEMI | call SEMI;

call : IDENTIFIER LPAREN expressions RPAREN;

expressions : expressionList |;

expressionList : expression COMMA expressionList | expression;

expression : expression1 CONCAT expression1 | expression1;

expression1 : expression2 COMPARE expression2 | expression2;

expression2 : expression2 ANDOR expression3 | expression3;

expression3 : expression3 (ADD | SUB) expression4 | expression4;

expression4 : expression4 MULDIVMOD expression5 | expression5;

expression5 : CLAIM expression5 | expression6;

expression6 : SUB expression6 | expression7;

expression7 : IDENTIFIER LBRACKET expressionList RBRACKET | expression8;

expression8 : INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | IDENTIFIER | subexpression | callExpression | indexedArray;
COMPARE : EQ | NEQ | LT | GT | LTE | GTE;

ANDOR : AND | OR;

MULDIVMOD : MUL | DIV | MOD;

indexedArray : LBRACE expressions RBRACE;

subexpression : LPAREN expression RPAREN;

callExpression : specialFunctionCall | IDENTIFIER LPAREN expressions RPAREN;

// special features IO
specialFunctionCall: readIntegerCall
            | printIntegerCall
            | readFloatCall
            | writeFloatCall
            | readBooleanCall
            | printBooleanCall
            | readStringCall
            | printStringCall
            | superCall
            | preventDefaultCall;

readIntegerCall: READINTEGER LPAREN RPAREN;

printIntegerCall: PRINTINTEGER LPAREN expression RPAREN;

readFloatCall: READFLOAT LPAREN RPAREN;

writeFloatCall: WRITEFLOAT LPAREN expression RPAREN;

readBooleanCall: READBOOLEAN LPAREN RPAREN;

printBooleanCall: PRINTBOOLEAN LPAREN expression RPAREN;

readStringCall: READSTRING LPAREN RPAREN;

printStringCall: PRINTSTRING LPAREN expression RPAREN;

superCall: SUPER LPAREN expressions RPAREN;

preventDefaultCall: PREVENTDEFAULT LPAREN RPAREN;

// Keywords
AUTO : 'auto' ;
BREAK : 'break' ;
BOOLEAN : 'boolean' ;
DO : 'do' ;
ELSE : 'else' ;
fragment TRUE : 'true' ;
fragment FALSE : 'false' ;
FLOAT : 'float' ;
FOR : 'for' ;
FUNCTION : 'function' ;
IF : 'if' ;
INTEGER : 'integer' ;
RETURN : 'return' ;
STRING : 'string' ;
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
QUOTE : ['] ;
DQUOTE : ["];
COLON : ':' ;
ASSIGN : '=' ;
// OPERATORS
ADD : '+' ;
SUB : '-' ;
fragment MUL : '*' ;
fragment DIV : '/' ;
fragment MOD : '%' ;
CLAIM : '!' ;
fragment AND : '&&' ;
fragment OR : '||' ;
fragment EQ : '==' ;
fragment NEQ : '!=' ;
fragment LT : '<' ;
fragment LTE : '<=' ;
fragment GT : '>' ;
fragment GTE : '>=' ;
CONCAT : '::' ;
// SPECIAL FUNCTION NAME
READINTEGER : 'readInteger' ;
PRINTINTEGER : 'printInteger' ;
READFLOAT : 'readFloat' ;
WRITEFLOAT : 'writeFloat' ;
READBOOLEAN : 'readBoolean' ;
PRINTBOOLEAN : 'printBoolean' ;
READSTRING : 'readString' ;
PRINTSTRING : 'printString' ;
SUPER : 'super' ;
PREVENTDEFAULT : 'preventDefault' ;
// COMMENTS
CSTYLE : '/*' .*? '*/' -> skip; // .*? is a non-greedy match
LINECOMMENT : '//' ~[\r\n]* -> skip; // ~[] is a negated character set
BOOLEANLIT : TRUE | FALSE;
// IDENTIFIERS
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ;
// LITERALS
INTLIT : '0' | [1-9][0-9]* ('_' [0-9]+)* {
self.text = self.text.replace("_", "")
};
fragment INTPART : '0' | [1-9][0-9]* ('_' [0-9]+)* ;
fragment DECIMALPART : DOT [0-9]*;
fragment EXPONENTPART : [eE] [+-]? [0-9]+;
FLOATLIT : INTPART DECIMALPART {
self.text = self.text.replace("_", "")
} | INTPART EXPONENTPART {
self.text = self.text.replace("_", "")
} | DECIMALPART EXPONENTPART {
self.text = self.text.replace("_", "")
} | INTPART DECIMALPART EXPONENTPART {
self.text = self.text.replace("_", "")
};
DOT : '.' ;
fragment ESC : '\\' [btnrf\\'"];
STRINGLIT : '"' (ESC | ~('\\'| '\n' | '"'))* '"' {
self.text = self.text[1:-1]
};
UNCLOSE_STRING:
'"' (~('\\'| '\n' | '"') | ESC )* (EOF | '\n') {
temp=str(self.text)
newLineChar ='\n'
if temp[-1] in newLineChar:
	raise UncloseString(temp[1:-1])
else:
	raise UncloseString(temp[1:])
};
ILLEGAL_ESCAPE:
'"' (~('\\'| '\n' | '"') | ESC )* '\\' ~[bntrf\\'"] {
	raise IllegalEscape(str(self.text[1:]))
};

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};