grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declarationList EOF;

declarationList: declaration declarationList |;

declaration : varDeclaration | funcDeclaration;

// 5.1 Variables Declaration
varDeclaration : noAssignVarDeclaration | assignVarDeclaration;

noAssignVarDeclaration : idList COLON type_specifier SEMI;

assignVarDeclaration : idList COLON type_specifier ASSIGN expressions SEMI ;

idList : IDENTIFIER COMMA idList | IDENTIFIER;

atomicType : INTEGER | FLOAT | BOOLEAN | STRING;

arrayType : ARRAY LBRACKET dimensions RBRACKET OF atomicType;

voidType : VOID;

autoType : AUTO;

dimensions : INTLIT COMMA dimensions | INTLIT;

type_specifier : voidType | autoType | atomicType | arrayType;

arrayCell : IDENTIFIER LBRACKET expressions RBRACKET;
// 5.2 Function Declaration

funcDeclaration : functionPrototype functionBody;

functionPrototype : IDENTIFIER COLON FUNCTION returnType LPAREN parameters RPAREN (INHERIT IDENTIFIER RBRACKET)?;

returnType : atomicType | voidType | arrayType;

parameters : parameterList |;

parameterList : parameter COMMA parameterList | parameter;

parameter : (INHERIT)? (OUT)? IDENTIFIER COLON type_specifier;

// 7 Statements
blockStatement : LBRACE statements RBRACE;

functionBody : blockStatement;

statements : statementList |;

statementList : statement statementList |;

statement : varDeclaration | assignmentStatement | ifStatement | forStatement | whileStatement | doWhileStatement | breakStatement | continueStatement | returnStatement | callStatement | blockStatement | commentStatement;

commentStatement : CSTYLE | LINECOMMENT;

assignmentStatement : leftHandSide ASSIGN expression SEMI;

leftHandSide : IDENTIFIER | arrayCell;

ifStatement : IF LPAREN expression RPAREN statement (ELSE statement)?;

forStatement : FOR LPAREN (IDENTIFIER ASSIGN expression) (COMMA expression) (COMMA expression) RPAREN statement;

whileStatement : WHILE LPAREN expression RPAREN statement;

doWhileStatement : DO blockStatement WHILE LPAREN expression RPAREN SEMI;

breakStatement : BREAK SEMI;

continueStatement : CONTINUE SEMI;

returnStatement : RETURN expressions SEMI;

callStatement : (specialFunctionCall | call) SEMI;

call : IDENTIFIER LPAREN expressions RPAREN;

expressions : expressionList |;

expressionList : expression COMMA expressionList | expression;

expression : expression1 CONCAT expression1 | expression1;

expression1 : expression2 (EQ | NEQ | LT | GT | LTE | GTE ) expression2 | expression2;

expression2 : expression2 (AND | OR) expression3 | expression3;

expression3 : expression3 (ADD | SUB) expression4 | expression4;

expression4 : expression4 (MUL | DIV | MOD) expression5 | expression5;

// Logical Not Unary Prefix Right Associative
expression5 : CLAIM expression5 | expression6;

expression6 : SUB expression6 | expression7;

//Index operator, Postfix, unary, left associative

expression7 : IDENTIFIER LBRACKET expression8 RBRACKET | expression8;

expression8 : INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | IDENTIFIER | subexpression | callExpression | indexedArray | arrayCell;

indexedArray : LBRACE expressions RBRACE;

subexpression : LPAREN expression RPAREN;

callExpression : specialFunctionCall | (IDENTIFIER LPAREN expressions RPAREN)| ;

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

superCall: SUPER LPAREN RPAREN;

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
CSTYLE : '/*' .*? '*/'; // .*? is a non-greedy match
LINECOMMENT : '//' ~[\r\n]*; // ~[] is a negated character set
BOOLEANLIT : TRUE | FALSE;
// IDENTIFIERS
IDENTIFIER : [a-z_][a-zA-Z0-9_]* ;
// LITERALS
INTLIT : [1-9][0-9]* ('_' [0-9]+)* | '0' {
    self.text = self.text.replace("_", "")
};
fragment INTPART : '0' | [1-9][0-9]* ('_' [0-9]+)* ;
fragment DECIMALPART : '.' [0-9]+;
fragment EXPONENTPART : [eE] [+-]? [0-9]+;
FLOATLIT : INTPART DECIMALPART | INTPART DECIMALPART? EXPONENTPART {
    self.text = self.text.replace("_", "")
};


fragment ESC : '\\' ( 'b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\' | '"' );
STRINGLIT : '"' ( ~ ('"' | '\\') | ESC )* '"';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;