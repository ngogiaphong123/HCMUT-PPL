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


    # Visit a parse tree produced by MT22Parser#noAssignVarDeclaration.
    def visitNoAssignVarDeclaration(self, ctx:MT22Parser.NoAssignVarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignVarDeclaration.
    def visitAssignVarDeclaration(self, ctx:MT22Parser.AssignVarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#recursiveAssignVarDeclaration.
    def visitRecursiveAssignVarDeclaration(self, ctx:MT22Parser.RecursiveAssignVarDeclarationContext):
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


    # Visit a parse tree produced by MT22Parser#type_specifier.
    def visitType_specifier(self, ctx:MT22Parser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayCell.
    def visitArrayCell(self, ctx:MT22Parser.ArrayCellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcDeclaration.
    def visitFuncDeclaration(self, ctx:MT22Parser.FuncDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionPrototype.
    def visitFunctionPrototype(self, ctx:MT22Parser.FunctionPrototypeContext):
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


    # Visit a parse tree produced by MT22Parser#indexedArray.
    def visitIndexedArray(self, ctx:MT22Parser.IndexedArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpression.
    def visitSubexpression(self, ctx:MT22Parser.SubexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callExpression.
    def visitCallExpression(self, ctx:MT22Parser.CallExpressionContext):
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