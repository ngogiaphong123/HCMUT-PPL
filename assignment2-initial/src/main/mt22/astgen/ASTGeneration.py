from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from src.main.mt22.utils.AST import *


class ASTGeneration(MT22Visitor):

    def visitProgram(ctx: MT22Parser.ProgramContext):
        return Program([])


