from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):

    # program: declarationList EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.declarationList()))

    # declarationList: declaration declarationList | declaration;
    def visitDeclarationList(self, ctx: MT22Parser.DeclarationListContext):
        if ctx.declarationList():
            return self.visit(ctx.declaration()) + self.visit(ctx.declarationList())
        else:
            return self.visit(ctx.declaration())

    # declaration: varDeclaration | funcDeclaration;
    def visitDeclaration(self, ctx: MT22Parser.DeclarationContext):
        if ctx.varDeclaration():
            return self.visit(ctx.varDeclaration())
        elif ctx.funcDeclaration():
            return [self.visit(ctx.funcDeclaration())]

    # varDeclaration: initVarDeclaration | fullVarDeclaration;
    def visitVarDeclaration(self, ctx: MT22Parser.VarDeclarationContext):
        if ctx.initVarDeclaration():
            return self.visit(ctx.initVarDeclaration())
        elif ctx.fullVarDeclaration():
            return self.visit(ctx.fullVarDeclaration())

    # initVarDeclaration : idList COLON typeSpecifier SEMI;
    def visitInitVarDeclaration(self, ctx: MT22Parser.InitVarDeclarationContext):
        idList = self.visit(ctx.idList())
        type = self.visit(ctx.typeSpecifier())
        return [VarDecl(x, type) for x in idList]

    # fullVarDeclaration : helper SEMI;
    def visitFullVarDeclaration(self, ctx: MT22Parser.FullVarDeclarationContext):
        helper = self.visit(ctx.helper())
        if len(helper) == 1:
            return [VarDecl(helper[0]["name"], self.visit(helper[0]["type"]), self.visit(helper[0]["expr"]))]
        result = []
        typ = self.visit(helper[0]["type"])
        for i in range(len(helper)):
            result.append(VarDecl(helper[len(helper) - i - 1]["name"], typ, self.visit(helper[i]["expr"])))
        return result

    # baseCase : IDENTIFIER COLON typeSpecifier ASSIGN expression;
    def visitBaseCase(self, ctx: MT22Parser.BaseCaseContext):
        name = ctx.IDENTIFIER().getText()
        typ = ctx.typeSpecifier()
        expr = ctx.expression()
        return [{
            "name": name,
            "type": typ,
            "expr": expr
        }]

    # helper : IDENTIFIER COMMA helper COMMA expression | baseCase;
    def visitHelper(self, ctx: MT22Parser.HelperContext):
        if ctx.COMMA():
            return self.visit(ctx.helper()) + [{
                "name": ctx.IDENTIFIER().getText(),
                "type": None,
                "expr": ctx.expression()
            }]
        else:
            return self.visit(ctx.baseCase())

    # idList : IDENTIFIER COMMA idList | IDENTIFIER;
    def visitIdList(self, ctx: MT22Parser.IdListContext):
        if ctx.COMMA():
            return [ctx.IDENTIFIER().getText()] + self.visit(ctx.idList())
        else:
            return [ctx.IDENTIFIER().getText()]

    # atomicType : INTEGER | FLOAT | BOOLEAN | STRING;
    def visitAtomicType(self, ctx: MT22Parser.AtomicTypeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.STRING():
            return StringType()

    # arrayType : ARRAY LBRACKET dimensions RBRACKET OF atomicType;
    def visitArrayType(self, ctx: MT22Parser.ArrayTypeContext):
        return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.atomicType()))

    # voidType : VOID;
    def visitVoidType(self, ctx: MT22Parser.VoidTypeContext):
        return VoidType()

    # autoType : AUTO;
    def visitAutoType(self, ctx: MT22Parser.AutoTypeContext):
        return AutoType()

    # dimensions : INTLIT COMMA dimensions | INTLIT;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        if ctx.COMMA():
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimensions())
        else:
            return [int(ctx.INTLIT().getText())]

    # typeSpecifier : autoType | atomicType | arrayType;
    def visitTypeSpecifier(self, ctx: MT22Parser.TypeSpecifierContext):
        if ctx.autoType():
            return AutoType()
        elif ctx.atomicType():
            return self.visit(ctx.atomicType())
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())

    # arrayCell : IDENTIFIER LBRACKET expressionList RBRACKET;
    def visitArrayCell(self, ctx: MT22Parser.ArrayCellContext):
        return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.expressionList()))

    # funcDeclaration : IDENTIFIER COLON FUNCTION returnType LPAREN parameters RPAREN functionBody |
    #                   IDENTIFIER COLON FUNCTION returnType LPAREN parameters RPAREN INHERIT IDENTIFIER functionBody;
    def visitFuncDeclaration(self, ctx: MT22Parser.FuncDeclarationContext):
        name = ctx.IDENTIFIER(0).getText()
        typ = self.visit(ctx.returnType())
        param = self.visit(ctx.parameters())
        body = self.visit(ctx.functionBody())
        if ctx.IDENTIFIER(1):
            return FuncDecl(name, typ, param, ctx.IDENTIFIER(1).getText(), body)
        else:
            return FuncDecl(name, typ, param, None, body)

    # returnType : atomicType | voidType | arrayType | autoType;
    def visitReturnType(self, ctx: MT22Parser.ReturnTypeContext):
        if ctx.atomicType():
            return self.visit(ctx.atomicType())
        elif ctx.voidType():
            return self.visit(ctx.voidType())
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        elif ctx.autoType():
            return self.visit(ctx.autoType())

    # parameters : parameterList |;
    def visitParameters(self, ctx: MT22Parser.ParametersContext):
        if ctx.parameterList():
            return self.visit(ctx.parameterList())
        else:
            return []

    # parameterList : parameter COMMA parameterList | parameter;
    def visitParameterList(self, ctx: MT22Parser.ParameterListContext):
        if ctx.COMMA():
            return [self.visit(ctx.parameter())] + self.visit(ctx.parameterList())
        else:
            return [self.visit(ctx.parameter())]

    # parameter : IDENTIFIER COLON typeSpecifier
    #             | INHERIT IDENTIFIER COLON typeSpecifier
    #             | OUT IDENTIFIER COLON typeSpecifier
    #             | INHERIT OUT IDENTIFIER COLON typeSpecifier;
    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        if ctx.INHERIT():
            if ctx.OUT():
                return ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.typeSpecifier()), True, True)
            else:
                return ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.typeSpecifier()), False, True)
        elif ctx.OUT():
            return ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.typeSpecifier()), True)
        else:
            return ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.typeSpecifier()))

    # blockStatement : LBRACE statements RBRACE;
    def visitBlockStatement(self, ctx: MT22Parser.BlockStatementContext):
        return BlockStmt(self.visit(ctx.statements()))

    # functionBody : blockStatement;
    def visitFunctionBody(self, ctx: MT22Parser.FunctionBodyContext):
        return self.visit(ctx.blockStatement())

    # statements : statementList |;
    def visitStatements(self, ctx: MT22Parser.StatementsContext):
        if ctx.statementList():
            return self.visit(ctx.statementList())
        else:
            return []

    # statementList : statement statementList |;
    def visitStatementList(self, ctx: MT22Parser.StatementListContext):
        if ctx.statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.statementList())
        else:
            return []

    # statement : varDeclarationStatement | assignmentStatement | ifStatement | forStatement | whileStatement |
    # doWhileStatement | breakStatement | continueStatement | returnStatement | callStatement | blockStatement;
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitVarDeclarationStatement(self, ctx: MT22Parser.VarDeclarationStatementContext):
        return BlockStmt(self.visit(ctx.varDeclaration()))

    # assignmentStatement : leftHandSide ASSIGN expression SEMI;
    def visitAssignmentStatement(self, ctx: MT22Parser.AssignmentStatementContext):
        return AssignStmt(self.visit(ctx.leftHandSide()), self.visit(ctx.expression()))

    # leftHandSide : IDENTIFIER | arrayCell;
    def visitLeftHandSide(self, ctx: MT22Parser.LeftHandSideContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.arrayCell():
            return self.visit(ctx.arrayCell())

    # ifStatement : IF LPAREN expression RPAREN statement | IF LPAREN expression RPAREN statement ELSE statement;
    def visitIfStatement(self, ctx: MT22Parser.IfStatementContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expression()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)))
        else:
            return IfStmt(self.visit(ctx.expression()), self.visit(ctx.statement(0)))

    # forStatement : FOR LPAREN IDENTIFIER ASSIGN expression COMMA expression COMMA expression RPAREN statement;
    def visitForStatement(self, ctx: MT22Parser.ForStatementContext):
        return ForStmt(AssignStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression(0))),
                       self.visit(ctx.expression(1)),
                       self.visit(ctx.expression(2)), self.visit(ctx.statement()))

    # whileStatement : WHILE LPAREN expression RPAREN statement;
    def visitWhileStatement(self, ctx: MT22Parser.WhileStatementContext):
        return WhileStmt(self.visit(ctx.expression()), self.visit(ctx.statement()))

    # doWhileStatement : DO statement WHILE LPAREN expression RPAREN SEMI;
    def visitDoWhileStatement(self, ctx: MT22Parser.DoWhileStatementContext):
        return DoWhileStmt(self.visit(ctx.statement()), self.visit(ctx.expression()))

    # breakStatement : BREAK SEMI;
    def visitBreakStatement(self, ctx: MT22Parser.BreakStatementContext):
        return BreakStmt()

    # continueStatement : CONTINUE SEMI;
    def visitContinueStatement(self, ctx: MT22Parser.ContinueStatementContext):
        return ContinueStmt()

    # returnStatement : RETURN (expression |) SEMI;
    def visitReturnStatement(self, ctx: MT22Parser.ReturnStatementContext):
        if ctx.expression():
            return ReturnStmt(self.visit(ctx.expression()))
        else:
            return ReturnStmt()

    # callStatement : specialFunctionCall SEMI | call SEMI;
    def visitCallStatement(self, ctx: MT22Parser.CallStatementContext):
        return self.visit(ctx.getChild(0))

    # call : IDENTIFIER LPAREN expressions RPAREN;
    def visitCall(self, ctx: MT22Parser.CallContext):
        return CallStmt(ctx.IDENTIFIER().getText(), self.visit(ctx.expressions()))

    # expressions : expressionList |;
    def visitExpressions(self, ctx: MT22Parser.ExpressionsContext):
        if ctx.expressionList():
            return self.visit(ctx.expressionList())
        else:
            return []

    # expressionList : expression COMMA expressionList | expression;
    def visitExpressionList(self, ctx: MT22Parser.ExpressionListContext):
        if ctx.COMMA():
            return [self.visit(ctx.expression())] + self.visit(ctx.expressionList())
        else:
            return [self.visit(ctx.expression())]

    # expression : expression1 CONCAT expression1 | expression1;
    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        if ctx.CONCAT():
            return BinExpr(ctx.CONCAT().getText(), self.visit(ctx.expression1(0)), self.visit(ctx.expression1(1)))
        else:
            return self.visit(ctx.expression1(0))

    # expression1 : expression2 COMPARE expression2 | expression2;
    def visitExpression1(self, ctx: MT22Parser.Expression1Context):
        if ctx.COMPARE():
            return BinExpr(ctx.COMPARE().getText(), self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
        else:
            return self.visit(ctx.expression2(0))

    # expression2 : expression2 ANDOR expression3 | expression3;
    def visitExpression2(self, ctx: MT22Parser.Expression2Context):
        if ctx.ANDOR():
            return BinExpr(ctx.ANDOR().getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        else:
            return self.visit(ctx.expression3())

    # expression3 : expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx: MT22Parser.Expression3Context):
        if ctx.ADD() :
            return BinExpr(ctx.ADD().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        elif ctx.SUB():
            return BinExpr(ctx.SUB().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        else:
            return self.visit(ctx.expression4())

    # expression4 : expression4 MULDIVMOD expression5 | expression5;
    def visitExpression4(self, ctx: MT22Parser.Expression4Context):
        if ctx.MULDIVMOD():
            return BinExpr(ctx.MULDIVMOD().getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))
        else:
            return self.visit(ctx.expression5())

    # expression5 : CLAIM expression5 | expression6;
    def visitExpression5(self, ctx: MT22Parser.Expression5Context):
        if ctx.CLAIM():
            return UnExpr(ctx.CLAIM().getText(), self.visit(ctx.expression5()))
        else:
            return self.visit(ctx.expression6())

    # expression6 : SUB expression6 | expression7;
    def visitExpression6(self, ctx: MT22Parser.Expression6Context):
        if ctx.SUB():
            return UnExpr(ctx.SUB().getText(), self.visit(ctx.expression6()))
        else:
            return self.visit(ctx.expression7())

    # expression7 : IDENTIFIER LBRACKET expressionList RBRACKET | expression8;
    def visitExpression7(self, ctx: MT22Parser.Expression7Context):
        if ctx.IDENTIFIER():
            return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.expressionList()))
        else:
            return self.visit(ctx.expression8())

    # expression8 : INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | IDENTIFIER | subExpression | callExpression | arrayLit;
    def visitExpression8(self, ctx: MT22Parser.Expression8Context):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.BOOLEANLIT():
            return BooleanLit(True if ctx.BOOLEANLIT().getText() == "true" else False)
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.subExpression():
            return self.visit(ctx.subExpression())
        elif ctx.callExpression():
            return self.visit(ctx.callExpression())
        elif ctx.arrayLit():
            return self.visit(ctx.arrayLit())

    # arrayLit : LBRACE expressions RBRACE;
    def visitArrayLit(self, ctx: MT22Parser.ArrayLitContext):
        return ArrayLit(self.visit(ctx.expressions()))

    # subExpression : LPAREN expression RPAREN;
    def visitSubExpression(self, ctx: MT22Parser.SubExpressionContext):
        return self.visit(ctx.expression())

    # callExpression : specialFunctionExpression | IDENTIFIER LPAREN expressions RPAREN;
    def visitCallExpression(self, ctx: MT22Parser.CallExpressionContext):
        if ctx.specialFunctionExpression():
            return self.visit(ctx.specialFunctionExpression())
        else:
            return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.expressions()))

    # specialFunctionExpression : readIntegerExpression
    #             | printIntegerExpression
    #             | readFloatExpression
    #             | writeFloatExpression
    #             | readBooleanExpression
    #             | printBooleanExpression
    #             | readStringExpression
    #             | printStringExpression
    #             | superExpression
    #             | preventDefaultExpression;
    def visitSpecialFunctionExpression(self, ctx: MT22Parser.SpecialFunctionExpressionContext):
        return self.visit(ctx.getChild(0))

    # readIntegerExpression: READINTEGER LPAREN RPAREN;
    def visitReadIntegerExpression(self, ctx: MT22Parser.ReadIntegerExpressionContext):
        return FuncCall("readInteger", [])

    # printIntegerExpression: PRINTINTEGER LPAREN expression RPAREN;
    def visitPrintIntegerExpression(self, ctx: MT22Parser.PrintIntegerExpressionContext):
        return FuncCall("printInteger", [self.visit(ctx.expression())])

    # readFloatExpression: READFLOAT LPAREN RPAREN;
    def visitReadFloatExpression(self, ctx: MT22Parser.ReadFloatExpressionContext):
        return FuncCall("readFloat", [])

    # writeFloatExpression: WRITEFLOAT LPAREN expression RPAREN;
    def visitWriteFloatExpression(self, ctx: MT22Parser.WriteFloatExpressionContext):
        return FuncCall("writeFloat", [self.visit(ctx.expression())])

    # readBooleanExpression: READBOOLEAN LPAREN RPAREN;
    def visitReadBooleanExpression(self, ctx: MT22Parser.ReadBooleanExpressionContext):
        return FuncCall("readBoolean", [])

    # printBooleanExpression: PRINTBOOLEAN LPAREN expression RPAREN;
    def visitPrintBooleanExpression(self, ctx: MT22Parser.PrintBooleanExpressionContext):
        return FuncCall("printBoolean", [self.visit(ctx.expression())])

    # readStringExpression: READSTRING LPAREN RPAREN;
    def visitReadStringExpression(self, ctx: MT22Parser.ReadStringExpressionContext):
        return FuncCall("readString", [])

    # printStringExpression: PRINTSTRING LPAREN expression RPAREN;
    def visitPrintStringExpression(self, ctx: MT22Parser.PrintStringExpressionContext):
        return FuncCall("printString", [self.visit(ctx.expression())])

    # superExpression: SUPER LPAREN expressions RPAREN;
    def visitSuperExpression(self, ctx: MT22Parser.SuperExpressionContext):
        return FuncCall("super", self.visit(ctx.expressions()))

    # preventDefaultExpression: PREVENTDEFAULT LPAREN RPAREN;
    def visitPreventDefaultExpression(self, ctx: MT22Parser.PreventDefaultExpressionContext):
        return FuncCall("preventDefault", [])

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
        return self.visit(ctx.getChild(0))

    # readIntegerCall: READINTEGER LPAREN RPAREN;
    def visitReadIntegerCall(self, ctx: MT22Parser.ReadIntegerCallContext):
        return CallStmt("readInteger", [])

    # printIntegerCall: PRINTINTEGER LPAREN expression RPAREN;
    def visitPrintIntegerCall(self, ctx: MT22Parser.PrintIntegerCallContext):
        return CallStmt("printInteger", [self.visit(ctx.expression())])

    # readFloatCall: READFLOAT LPAREN RPAREN;
    def visitReadFloatCall(self, ctx: MT22Parser.ReadFloatCallContext):
        return CallStmt("readFloat", [])

    # writeFloatCall: WRITEFLOAT LPAREN expression RPAREN;
    def visitWriteFloatCall(self, ctx: MT22Parser.WriteFloatCallContext):
        return CallStmt("writeFloat", [self.visit(ctx.expression())])

    # readBooleanCall: READBOOLEAN LPAREN RPAREN;
    def visitReadBooleanCall(self, ctx: MT22Parser.ReadBooleanCallContext):
        return CallStmt("readBoolean", [])

    # printBooleanCall: PRINTBOOLEAN LPAREN expression RPAREN;
    def visitPrintBooleanCall(self, ctx: MT22Parser.PrintBooleanCallContext):
        return CallStmt("printBoolean", [self.visit(ctx.expression())])

    # readStringCall: READSTRING LPAREN RPAREN;
    def visitReadStringCall(self, ctx: MT22Parser.ReadStringCallContext):
        return CallStmt("readString", [])

    # printStringCall: PRINTSTRING LPAREN expression RPAREN;
    def visitPrintStringCall(self, ctx: MT22Parser.PrintStringCallContext):
        return CallStmt("printString", [self.visit(ctx.expression())])

    # superCall: SUPER LPAREN expressions RPAREN;
    def visitSuperCall(self, ctx: MT22Parser.SuperCallContext):
        return CallStmt("super", self.visit(ctx.expressions()))

    # preventDefaultCall: PREVENTDEFAULT LPAREN RPAREN;
    def visitPreventDefaultCall(self, ctx: MT22Parser.PreventDefaultCallContext):
        return CallStmt("preventDefault", [])