# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declarationList.
    def visitDeclarationList(self, ctx:MT22Parser.DeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varDeclaration.
    def visitVarDeclaration(self, ctx:MT22Parser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initVarDeclaration.
    def visitInitVarDeclaration(self, ctx:MT22Parser.InitVarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fullVarDeclaration.
    def visitFullVarDeclaration(self, ctx:MT22Parser.FullVarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#helper.
    def visitHelper(self, ctx:MT22Parser.HelperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#baseCase.
    def visitBaseCase(self, ctx:MT22Parser.BaseCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idList.
    def visitIdList(self, ctx:MT22Parser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomicType.
    def visitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayType.
    def visitArrayType(self, ctx:MT22Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#voidType.
    def visitVoidType(self, ctx:MT22Parser.VoidTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#autoType.
    def visitAutoType(self, ctx:MT22Parser.AutoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:MT22Parser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayCell.
    def visitArrayCell(self, ctx:MT22Parser.ArrayCellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcDeclaration.
    def visitFuncDeclaration(self, ctx:MT22Parser.FuncDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnType.
    def visitReturnType(self, ctx:MT22Parser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameters.
    def visitParameters(self, ctx:MT22Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterList.
    def visitParameterList(self, ctx:MT22Parser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStatement.
    def visitBlockStatement(self, ctx:MT22Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionBody.
    def visitFunctionBody(self, ctx:MT22Parser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statements.
    def visitStatements(self, ctx:MT22Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statementList.
    def visitStatementList(self, ctx:MT22Parser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varDeclarationStatement.
    def visitVarDeclarationStatement(self, ctx:MT22Parser.VarDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MT22Parser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#leftHandSide.
    def visitLeftHandSide(self, ctx:MT22Parser.LeftHandSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifStatement.
    def visitIfStatement(self, ctx:MT22Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStatement.
    def visitForStatement(self, ctx:MT22Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStatement.
    def visitWhileStatement(self, ctx:MT22Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:MT22Parser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStatement.
    def visitBreakStatement(self, ctx:MT22Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStatement.
    def visitContinueStatement(self, ctx:MT22Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStatement.
    def visitReturnStatement(self, ctx:MT22Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStatement.
    def visitCallStatement(self, ctx:MT22Parser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call.
    def visitCall(self, ctx:MT22Parser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressions.
    def visitExpressions(self, ctx:MT22Parser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressionList.
    def visitExpressionList(self, ctx:MT22Parser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression1.
    def visitExpression1(self, ctx:MT22Parser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression2.
    def visitExpression2(self, ctx:MT22Parser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression3.
    def visitExpression3(self, ctx:MT22Parser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression4.
    def visitExpression4(self, ctx:MT22Parser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression5.
    def visitExpression5(self, ctx:MT22Parser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression6.
    def visitExpression6(self, ctx:MT22Parser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression7.
    def visitExpression7(self, ctx:MT22Parser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression8.
    def visitExpression8(self, ctx:MT22Parser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayLit.
    def visitArrayLit(self, ctx:MT22Parser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subExpression.
    def visitSubExpression(self, ctx:MT22Parser.SubExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callExpression.
    def visitCallExpression(self, ctx:MT22Parser.CallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specialFunctionExpression.
    def visitSpecialFunctionExpression(self, ctx:MT22Parser.SpecialFunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readIntegerExpression.
    def visitReadIntegerExpression(self, ctx:MT22Parser.ReadIntegerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printIntegerExpression.
    def visitPrintIntegerExpression(self, ctx:MT22Parser.PrintIntegerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloatExpression.
    def visitReadFloatExpression(self, ctx:MT22Parser.ReadFloatExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFloatExpression.
    def visitWriteFloatExpression(self, ctx:MT22Parser.WriteFloatExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBooleanExpression.
    def visitReadBooleanExpression(self, ctx:MT22Parser.ReadBooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBooleanExpression.
    def visitPrintBooleanExpression(self, ctx:MT22Parser.PrintBooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readStringExpression.
    def visitReadStringExpression(self, ctx:MT22Parser.ReadStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printStringExpression.
    def visitPrintStringExpression(self, ctx:MT22Parser.PrintStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#superExpression.
    def visitSuperExpression(self, ctx:MT22Parser.SuperExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventDefaultExpression.
    def visitPreventDefaultExpression(self, ctx:MT22Parser.PreventDefaultExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specialFunctionCall.
    def visitSpecialFunctionCall(self, ctx:MT22Parser.SpecialFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readIntegerCall.
    def visitReadIntegerCall(self, ctx:MT22Parser.ReadIntegerCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printIntegerCall.
    def visitPrintIntegerCall(self, ctx:MT22Parser.PrintIntegerCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloatCall.
    def visitReadFloatCall(self, ctx:MT22Parser.ReadFloatCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFloatCall.
    def visitWriteFloatCall(self, ctx:MT22Parser.WriteFloatCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBooleanCall.
    def visitReadBooleanCall(self, ctx:MT22Parser.ReadBooleanCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBooleanCall.
    def visitPrintBooleanCall(self, ctx:MT22Parser.PrintBooleanCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readStringCall.
    def visitReadStringCall(self, ctx:MT22Parser.ReadStringCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printStringCall.
    def visitPrintStringCall(self, ctx:MT22Parser.PrintStringCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#superCall.
    def visitSuperCall(self, ctx:MT22Parser.SuperCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventDefaultCall.
    def visitPreventDefaultCall(self, ctx:MT22Parser.PreventDefaultCallContext):
        return self.visitChildren(ctx)



del MT22Parser