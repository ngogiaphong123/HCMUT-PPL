# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declarationList.
    def visitDeclarationList(self, ctx:BKOOLParser.DeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declaration.
    def visitDeclaration(self, ctx:BKOOLParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDeclaration.
    def visitVarDeclaration(self, ctx:BKOOLParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprDeclaration.
    def visitExprDeclaration(self, ctx:BKOOLParser.ExprDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprList.
    def visitExprList(self, ctx:BKOOLParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subexpr.
    def visitSubexpr(self, ctx:BKOOLParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexedArray.
    def visitIndexedArray(self, ctx:BKOOLParser.IndexedArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#associativeArray.
    def visitAssociativeArray(self, ctx:BKOOLParser.AssociativeArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#pairDeclaration.
    def visitPairDeclaration(self, ctx:BKOOLParser.PairDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#pairList.
    def visitPairList(self, ctx:BKOOLParser.PairListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#pair.
    def visitPair(self, ctx:BKOOLParser.PairContext):
        return self.visitChildren(ctx)



del BKOOLParser