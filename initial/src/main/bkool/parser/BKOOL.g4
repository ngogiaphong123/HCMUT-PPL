grammar BKOOL;
//
@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

//
//program :  EOF ;
//IDENTIFIER : [a-z][a-z0-9]*;
////fragment DECIMAL_POINT_FLOAT : [0-9]+ '.' [0-9]+ ;
////fragment SCIENTIFIC_NOTATION : [0-9]+ ('.')? [0-9]* ( 'e' | 'E' ) ('-') ? [0-9]+ ;
////REAL : (DECIMAL_POINT_FLOAT | SCIENTIFIC_NOTATION);
////fragment INTPART : [0-9]+;
////fragment FRACPART : '.' [0-9]+;
////fragment EXPONENT : ('e' | 'E') ('+' | '-')? [0-9]+;
////REAL : INTPART FRACPART | INTPART FRACPART? EXPONENT;
////fragment SINGLE_QUOTE : ['];
////STRINGLIT : SINGLE_QUOTE (~['] | SINGLE_QUOTE SINGLE_QUOTE)* SINGLE_QUOTE;
//INTLIT : '0' | [1-9][0-9]* ('_' [0-9]+)* {
//    self.text = self.text.replace("_", "")
//};
////fragment OCTECT : [0-9] | [1-9][0-9] | [1][0-9][0-9] | [2][0-4][0-9] | [2][5][0-5];
////IPV4 : OCTECT '.' OCTECT '.' OCTECT '.' OCTECT;
//fragment SHEXA_START : [1-9];
//fragment CHAR : [a-zA-Z];
//fragment DIGIT : [0-9];
//fragment SHEXA_LAST : [02468aAcCeE];
//SHEXA : SHEXA_START (CHAR | DIGIT)* SHEXA_LAST;
//fragment FRISTPART : [a-z]+;
//fragment SECONDPART : [a-z]+;
//fragment OPTIONPART : [a-z0-9_.]?[a-z0-9_.]?[a-z0-9_.]?[a-z0-9_.]?[a-z0-9_];
//fragment Point : [.] ;
//BKNetID : FRISTPART Point SECONDPART OPTIONPART;

//WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
//
//ERROR_CHAR: . {raise ErrorToken(self.text)};
//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;

//program : declarationList EOF;// write your rule for program here
//
//declarationList : declaration declarationList | ;
//
//declaration : varDeclaration | funcDeclaration;
//
//varDeclaration : type_specifier varList SEMI;
//
//type_specifier : INT | FLOAT;
//
//varList : ID COMMA varList | ID ;
//
//funcDeclaration : type_specifier ID LPAREN params RPAREN body;
//
//params : paramList | ;
//
//paramList : param SEMI paramList | param;
//
//param : type_specifier varList;
//
//body : LBRACE statementList RBRACE;
//
//statementList : statement statementList | ;
//
//statement : varDeclaration | assignmentStatement | callStatement | returnStatement;
//
//assignmentStatement : ID ASSIGN expression SEMI;
//
//returnStatement : RETURN expression SEMI;
//
//callStatement : ID LPAREN expressDeclaration RPAREN SEMI;
//
//expressDeclaration : expressionList | ;
//
//expressionList : expression COMMA expressionList | expression ;
//
//expression : expression1 ADD expression | expression1 ;
//
//expression1 : expression2 MINUS expression2 | expression2;
//
//expression2 : expression2 (MUL | DIV) expression3 | expression3;
//
//expression3 : subexpression | callExpression | INTLIT | FLOATLIT | ID;
//
//subexpression : LPAREN expression RPAREN;
//
//callExpression : ID LPAREN expressDeclaration RPAREN;
//
//
//// KEYWORDS
//INT : 'int';
//FLOAT : 'float';
//RETURN : 'return';
//CALL : 'call';
//COMMA : ',';
//SEMI : ';';
//LPAREN : '(';
//RPAREN : ')';
//LBRACE : '{';
//RBRACE : '}';
//ADD : '+';
//MINUS : '-';
//MUL : '*';
//DIV : '/';
//ASSIGN : '=';
//
//// TOKENS
//ID : [a-zA-Z][a-zA-Z0-9]*;
//INTLIT : [0-9]+;
//FLOATLIT : [0-9]+ '.' [0-9]+;
//
//WS: [ \t\r\n] -> skip;
//
//ERROR_CHAR: . {raise ErrorToken(self.text)};

program : declarationList EOF;

declarationList : declaration declarationList | ;

declaration : varDeclaration;

varDeclaration : VARNAME EQ expr SEMI;

exprDeclaration : exprList | ;

exprList : expr COMMA exprList | expr ;

expr : expr1 DQUES expr1 | expr1;

expr1 : expr2 (ADD | SUB) expr1 | expr2;

expr2 : expr2 (MUL | DIV | MOD) expr3 | expr3;

expr3 : expr3 DOT expr4 | expr4;

expr4 : expr5 DSTAR expr4 | expr5;

expr5 : subexpr | VARNAME | INTLIT | STRINGLIT | indexedArray | associativeArray;

subexpr : LP expr RP;

indexedArray : ARRAY LP exprDeclaration RP;

associativeArray : ARRAY LP pairDeclaration RP;

pairDeclaration : pairList | ;

pairList : pair COMMA pairList | pair;

pair : VARNAME ARROW expr;

SEMI : ';';
COMMA : ',';
DSTAR : '**';
LP : '(';
RP : ')';
DQUES : '??';
DOT : '.';
MUL : '*';
DIV : '/';
MOD : '%';
ADD : '+';
SUB : '-';
ARRAY : 'array';
ARROW : '=>';
EQ : '=';


VARNAME : [a-zA-Z][a-zA-Z0-9]*;
INTLIT : [0-9]+;
STRINGLIT : '"' (~["] | '\\"')* '"';

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};