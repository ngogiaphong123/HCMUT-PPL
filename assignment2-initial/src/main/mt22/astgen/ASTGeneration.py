from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):

    # program: declarationList EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return self.visitChildren(ctx)

    # declarationList: declaration declarationList | declaration;
    def visitDeclarationList(self, ctx: MT22Parser.DeclarationListContext):
        return self.visitChildren(ctx)

    # declaration: varDeclaration | funcDeclaration;
    def visitDeclaration(self, ctx: MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)

    # varDeclaration: initVarDeclaration | fullVarDeclaration;
    def visitVarDeclaration(self, ctx: MT22Parser.VarDeclarationContext):
        return self.visitChildren(ctx)

    # initVarDeclaration : idList COLON type_specifier SEMI;
    def visitInitVarDeclaration(self, ctx: MT22Parser.InitVarDeclarationContext):
        return self.visitChildren(ctx)

    # fullVarDeclaration : helper SEMI;
    def visitFullVarDeclaration(self, ctx: MT22Parser.FullVarDeclarationContext):
        return self.visitChildren(ctx)

    # baseVarDeclaration : IDENTIFIER COLON type_specifier ASSIGN expression;
    def visitBaseVarDeclaration(self, ctx: MT22Parser.BaseVarDeclarationContext):
        return self.visitChildren(ctx)

    # helper : IDENTIFIER COMMA helper COMMA expression | baseVarDeclaration;
    def visitHelper(self, ctx: MT22Parser.HelperContext):
        return self.visitChildren(ctx)

    # idList : IDENTIFIER COMMA idList | IDENTIFIER;
    def visitIdList(self, ctx: MT22Parser.IdListContext):
        return self.visitChildren(ctx)

    # atomicType : INTEGER | FLOAT | BOOLEAN | STRING;
    def visitAtomicType(self, ctx: MT22Parser.AtomicTypeContext):
        return self.visitChildren(ctx)

    # arrayType : ARRAY LBRACKET dimensions RBRACKET OF atomicType;
    def visitArrayType(self, ctx: MT22Parser.ArrayTypeContext):
        return self.visitChildren(ctx)

    # voidType : VOID;
    def visitVoidType(self, ctx: MT22Parser.VoidTypeContext):
        return self.visitChildren(ctx)

    # autoType : AUTO;
    def visitAutoType(self, ctx: MT22Parser.AutoTypeContext):
        return self.visitChildren(ctx)

    # dimensions : INTLIT COMMA dimensions | INTLIT;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)

    # typeSpecifier : autoType | atomicType | arrayType;
    def visitTypeSpecifier(self, ctx: MT22Parser.TypeSpecifierContext):
        return self.visitChildren(ctx)

    # arrayCell : IDENTIFIER LBRACKET expressions RBRACKET;
    def visitArrayCell(self, ctx: MT22Parser.ArrayCellContext):
        return self.visitChildren(ctx)

    # funcDeclaration : functionPrototype functionBody;
    def visitFuncDeclaration(self, ctx: MT22Parser.FuncDeclarationContext):
        return self.visitChildren(ctx)

    # functionPrototype : IDENTIFIER COLON FUNCTION returnType LPAREN parameters RPAREN |
    #                     IDENTIFIER COLON FUNCTION returnType LPAREN parameters RPAREN INHERIT IDENTIFIER;
    def visitFunctionPrototype(self, ctx: MT22Parser.FunctionPrototypeContext):
        return self.visitChildren(ctx)

    # returnType : atomicType | voidType | arrayType | autoType;
    def visitReturnType(self, ctx: MT22Parser.ReturnTypeContext):
        return self.visitChildren(ctx)

    # parameters : parameterList |;
    def visitParameters(self, ctx: MT22Parser.ParametersContext):
        return self.visitChildren(ctx)

    # parameterList : parameter COMMA parameterList | parameter;
    def visitParameterList(self, ctx: MT22Parser.ParameterListContext):
        return self.visitChildren(ctx)

    # parameter : IDENTIFIER COLON typeSpecifier
    #             | INHERIT IDENTIFIER COLON typeSpecifier
    #             | OUT IDENTIFIER COLON typeSpecifier
    #             | INHERIT OUT IDENTIFIER COLON typeSpecifier;
    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        return self.visitChildren(ctx)

    # blockStatement : LBRACE statements RBRACE;
    def visitBlockStatement(self, ctx: MT22Parser.BlockStatementContext):
        return self.visitChildren(ctx)

    # functionBody : blockStatement;
    def visitFunctionBody(self, ctx: MT22Parser.FunctionBodyContext):
        return self.visitChildren(ctx)

    # statements : statementList |;
    def visitStatements(self, ctx: MT22Parser.StatementsContext):
        return self.visitChildren(ctx)

    # statementList : statement statementList |;
    def visitStatementList(self, ctx: MT22Parser.StatementListContext):
        return self.visitChildren(ctx)

    # statement : varDeclaration | assignmentStatement | ifStatement | forStatement | whileStatement | doWhileStatement
    # | breakStatement | continueStatement | returnStatement | callStatement | blockStatement;
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        return self.visitChildren(ctx)

    # assignmentStatement : leftHandSide ASSIGN expression SEMI;
    def visitAssignmentStatement(self, ctx: MT22Parser.AssignmentStatementContext):
        return self.visitChildren(ctx)

    # leftHandSide : IDENTIFIER | arrayCell;
    def visitLeftHandSide(self, ctx: MT22Parser.LeftHandSideContext):
        return self.visitChildren(ctx)

    # ifStatement : IF LPAREN expression RPAREN statement | IF LPAREN expression RPAREN statement ELSE statement;
    def visitIfStatement(self, ctx: MT22Parser.IfStatementContext):
        return self.visitChildren(ctx)

    # forStatement : FOR LPAREN IDENTIFIER ASSIGN expression COMMA expression COMMA expression RPAREN statement;
    def visitForStatement(self, ctx: MT22Parser.ForStatementContext):
        return self.visitChildren(ctx)

    # whileStatement : WHILE LPAREN expression RPAREN statement;
    def visitWhileStatement(self, ctx: MT22Parser.WhileStatementContext):
        return self.visitChildren(ctx)

    # doWhileStatement : DO statement WHILE LPAREN expression RPAREN SEMI;
    def visitDoWhileStatement(self, ctx: MT22Parser.DoWhileStatementContext):
        return self.visitChildren(ctx)

    # breakStatement : BREAK SEMI;
    def visitBreakStatement(self, ctx: MT22Parser.BreakStatementContext):
        return self.visitChildren(ctx)

    # continueStatement : CONTINUE SEMI;
    def visitContinueStatement(self, ctx: MT22Parser.ContinueStatementContext):
        return self.visitChildren(ctx)

    # returnStatement : RETURN expressions SEMI;
    def visitReturnStatement(self, ctx: MT22Parser.ReturnStatementContext):
        return self.visitChildren(ctx)

    # callStatement : specialFunctionCall SEMI | call SEMI;
    def visitCallStatement(self, ctx: MT22Parser.CallStatementContext):
        return self.visitChildren(ctx)

    # call : IDENTIFIER LPAREN expressions RPAREN;
    def visitCall(self, ctx: MT22Parser.CallContext):
        return self.visitChildren(ctx)

    # expressions : expressionList |;
    def visitExpressions(self, ctx: MT22Parser.ExpressionsContext):
        return self.visitChildren(ctx)

    # expressionList : expression COMMA expressionList | expression;
    def visitExpressionList(self, ctx: MT22Parser.ExpressionListContext):
        return self.visitChildren(ctx)

    # expression : expression1 CONCAT expression1 | expression1;
    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)

    # expression1 : expression2 COMPARE expression2 | expression2;
    def visitExpression1(self, ctx: MT22Parser.Expression1Context):
        return self.visitChildren(ctx)

    # expression2 : expression2 ANDOR expression3 | expression3;
    def visitExpression2(self, ctx: MT22Parser.Expression2Context):
        return self.visitChildren(ctx)

    # expression3 : expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx: MT22Parser.Expression3Context):
        return self.visitChildren(ctx)

    # expression4 : expression4 MULDIVMOD expression5 | expression5;
    def visitExpression4(self, ctx: MT22Parser.Expression4Context):
        return self.visitChildren(ctx)

    # expression5 : CLAIM expression5 | expression6;
    def visitExpression5(self, ctx: MT22Parser.Expression5Context):
        return self.visitChildren(ctx)

    # expression6 : SUB expression6 | expression7;
    def visitExpression6(self, ctx: MT22Parser.Expression6Context):
        return self.visitChildren(ctx)

    # expression7 : IDENTIFIER LBRACKET expressionList RBRACKET | expression8;
    def visitExpression7(self, ctx: MT22Parser.Expression7Context):
        return self.visitChildren(ctx)

    # expression8 : INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | IDENTIFIER | subExpression | callExpression | arrayLit;
    def visitExpression8(self, ctx: MT22Parser.Expression8Context):
        return self.visitChildren(ctx)

    # arrayLit : LBRACE expressions RBRACE;
    def visitArrayLit(self, ctx: MT22Parser.ArrayLitContext):
        return self.visitChildren(ctx)

    # subExpression : LPAREN expression RPAREN;
    def visitSubExpression(self, ctx: MT22Parser.SubExpressionContext):
        return self.visitChildren(ctx)

    # callExpression : specialFunctionCall | IDENTIFIER LPAREN expressions RPAREN;
    def visitCallExpression(self, ctx: MT22Parser.CallExpressionContext):
        return self.visitChildren(ctx)

    # specialFunctionCall: readIntegerCall
    #             | printIntegerCall
    #             | readFloatCall
    #             | writeFloatCall
    #             | readBooleanCall
    #             | printBooleanCall
    #             | readStringCall
    #             | printStringCall
    #             | superCall
    #             | preventDefaultCall;
    def visitSpecialFunctionCall(self, ctx: MT22Parser.SpecialFunctionCallContext):
        return self.visitChildren(ctx)

    # readIntegerCall: READINTEGER LPAREN RPAREN;
    def visitReadIntegerCall(self, ctx: MT22Parser.ReadIntegerCallContext):
        return self.visitChildren(ctx)

    # printIntegerCall: PRINTINTEGER LPAREN expression RPAREN;
    def visitPrintIntegerCall(self, ctx: MT22Parser.PrintIntegerCallContext):
        return self.visitChildren(ctx)

    # readFloatCall: READFLOAT LPAREN RPAREN;
    def visitReadFloatCall(self, ctx: MT22Parser.ReadFloatCallContext):
        return self.visitChildren(ctx)

    # writeFloatCall: WRITEFLOAT LPAREN expression RPAREN;
    def visitWriteFloatCall(self, ctx: MT22Parser.WriteFloatCallContext):
        return self.visitChildren(ctx)

    # readBooleanCall: READBOOLEAN LPAREN RPAREN;
    def visitReadBooleanCall(self, ctx: MT22Parser.ReadBooleanCallContext):
        return self.visitChildren(ctx)

    # printBooleanCall: PRINTBOOLEAN LPAREN expression RPAREN;
    def visitPrintBooleanCall(self, ctx: MT22Parser.PrintBooleanCallContext):
        return self.visitChildren(ctx)

    # readStringCall: READSTRING LPAREN RPAREN;
    def visitReadStringCall(self, ctx: MT22Parser.ReadStringCallContext):
        return self.visitChildren(ctx)

    # printStringCall: PRINTSTRING LPAREN expression RPAREN;
    def visitPrintStringCall(self, ctx: MT22Parser.PrintStringCallContext):
        return self.visitChildren(ctx)

    # superCall: SUPER LPAREN expressions RPAREN;
    def visitSuperCall(self, ctx: MT22Parser.SuperCallContext):
        return self.visitChildren(ctx)

    # preventDefaultCall: PREVENTDEFAULT LPAREN RPAREN;
    def visitPreventDefaultCall(self, ctx: MT22Parser.PreventDefaultCallContext):
        return self.visitChildren(ctx)
