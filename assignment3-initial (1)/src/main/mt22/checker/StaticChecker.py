from Visitor import *
from StaticError import *
from AST import *
from abc import ABC

class Symbol:
    def __init__(self, name, typ, kind = Function(), inherit = False):
        """
        Class for symbol
        name : name of symbol
        typ : type of symbol
        kind : kind of symbol
        inherit : inherit for parameter Kind
        """
        self.name = name
        self.typ = typ
        self.kind = kind
        self.inherit = inherit
        
    def __str__(self) -> str:
        return "Symbol({}, Type : {}, Kind : {}, Inherit : {})".format(self.name, self.typ, self.kind, self.inherit)
class FuncType: 
    """
    Class for function type
    param: list of parameter (name, type, inherit)
    ret : return type
    inherit : parent function
    """
    def __init__(self, param : Symbol, ret, inherit = None):
        self.param = param
        self.ret = ret
        self.inherit = inherit
        
    def __str__(self) -> str:
        return "FuncType(ParamList : {}, ReturnType : {}, Parent : {})".format(
            ", ".join([str(x) for x in self.param]) if self.param else "None", self.ret,self.inherit if self.inherit else "None")
class GetEnv(Visitor):
    def visitProgram(self, ast: Program, o):
        o = []
        for x in ast.decls:
            self.visit(x, o)
        return o

    def visitFuncDecl(self, ast: FuncDecl, o):
        paramList = []
        for x in ast.params:
            paramList += [self.visit(x, o)]
        o += [Symbol(ast.name, FuncType(paramList, ast.return_type, ast.inherit), kind = Function())]
        
    def visitParamDecl(self, ast : ParamDecl, o):
        return Symbol(ast.name, ast.typ, kind = Parameter(), inherit = ast.inherit)
        
class Checker() :
    pass
class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.isInLoop = []
        self.globalEnv = [
            Symbol("readInteger", FuncType([], IntegerType()), kind = Function()),
            Symbol("printInteger", FuncType([IntegerType()], VoidType()), kind = Function()),
            Symbol("readFloat", FuncType([], FloatType()), kind = Function()),
            Symbol("writeFloat", FuncType([FloatType()], VoidType()), kind = Function()),
            Symbol("readBoolean", FuncType([], BooleanType()), kind = Function()),
            Symbol("printBoolean", FuncType([BooleanType()], VoidType()), kind = Function()),
            Symbol("readString", FuncType([], StringType()), kind = Function()),
            Symbol("printString", FuncType([StringType()], VoidType()), kind = Function()),
            Symbol("super", FuncType([], VoidType()), kind = Function()),
            Symbol("preventDefault", FuncType([], VoidType()), kind = Function()),
        ]
        self.scope = [[]]
    
    def printScope(self):
        for env in self.scope:
            for symbol in env:
                print(str(symbol))
            print("=====================================")
        
    def lookupGlobal(self, name):
        for env in self.scope :
            for symbol in env :
                if symbol.name == name :
                    return symbol
        return None
    def lookupLocal(self, name):
        for symbol in self.scope[0]:
            if symbol.name == name :
                return symbol
        return None
    def inferType(self, name, typ):
        for env in self.scope :
            for symbol in env :
                if symbol.name == name :
                    symbol.typ = typ
                    return typ
        return None

    def lookupGlobalFunc(self, name):
        for func in self.globalEnv :
            if func.name == name :
                return func
        
    def check(self):
        return self.visitProgram(self.ast, [])
    
    def visitProgram(self, ast : Program, param): 
        self.globalEnv += GetEnv().visitProgram(ast, [])
        for x in ast.decls:
            self.visit(x, self.scope)
        mainFunc = self.lookupGlobalFunc("main")
        if mainFunc is None:
            raise NoEntryPoint()
        elif type(mainFunc.typ.ret) is not VoidType:
            raise NoEntryPoint()
        elif len(mainFunc.typ.param) != 0:
            raise NoEntryPoint()
        # self.printScope()

    def visitFuncCall(self, ast, param): pass
    def visitAssignStmt(self, ast : AssignStmt, param):
        rhsType = self.visit(ast.rhs, param)
        lhsType = self.visit(ast.lhs, param)
        if type(lhsType) in [ArrayType, VoidType] :
            raise TypeMismatchInStatement(ast)
        if type(rhsType) is not type(lhsType):
            if type(rhsType) is IntegerType and type(lhsType) is FloatType:
                return lhsType
            else:
                raise TypeMismatchInStatement(ast)
        else :
            return lhsType
        
        
    def visitBlockStmt(self, ast : BlockStmt, param):
        # if param[1] == "func" :
        #     for x in ast.body:
        #         self.visit(x, param)
        # else :
        #     self.scope = [[], *self.scope]
        #     for x in ast.body:
        #         self.visit(x, param)
        # self.printScope()
        # self.scope = self.scope[1:]
        if type(param) is tuple:
            if param[1] == "func" :
                for x in ast.body:
                    self.visit(x, param)
            elif param[1] == "for" or param[1] == "while" or param[1] == "doWhile":
                self.isInLoop.append(True)
                self.scope = [[], *self.scope]
                for x in ast.body:
                    self.visit(x, param)
                self.isInLoop.pop()
            elif param[1] == "if":
                self.scope = [[], *self.scope]
                for x in ast.body:
                    self.visit(x, param)
        else :
            for x in ast.body:
                self.visit(x, param)
        self.scope = self.scope[1:]
            
    
    
    def visitIfStmt(self, ast : IfStmt, param):
        condType = self.visit(ast.cond, param)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        if type(ast.tstmt) is BlockStmt:
            self.visit(ast.tstmt, (param, "if"))
        else :
            self.visit(ast.tstmt, param)
        if ast.fstmt is not None:
            if type(ast.fstmt) is BlockStmt:
                self.visit(ast.fstmt, (param, "if"))
            else :
                self.visit(ast.fstmt, param)

    def visitForStmt(self, ast : ForStmt, param):
        initType = self.visit(ast.init, param)
        if type(initType) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        updType = self.visit(ast.upd, param)
        if type(updType) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        condType = self.visit(ast.cond, param)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        if type(ast.stmt) is BlockStmt:
            self.visit(ast.stmt, (param, "for"))
        else :
            self.visit(ast.stmt, param)
        
        
    def visitWhileStmt(self, ast : WhileStmt, param):
        condType = self.visit(ast.cond, param)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        if type(ast.stmt) is BlockStmt:
            self.visit(ast.stmt, (param, "while"))
        else :
            self.visit(ast.stmt, param)
        
    def visitDoWhileStmt(self, ast, param): 
        condType = self.visit(ast.exp, param)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        if type(ast.stmt) is BlockStmt:
            self.visit(ast.stmt, (param, "doWhile"))
        else:
            self.visit(ast.stmt, param)
        
    def visitBreakStmt(self, ast, param):
        if len(self.isInLoop) == 0:
            raise MustInLoop(ast)
        
    def visitContinueStmt(self, ast, param):
        if len(self.isInLoop) == 0:
            raise MustInLoop(ast)
        
    def visitReturnStmt(self, ast : ReturnStmt, param):
        if ast.expr is not None:
            return self.visit(ast.expr, param)
        
    def visitCallStmt(self, ast, param): pass

    def visitVarDecl(self, ast : VarDecl, param):
        duplicate = self.lookupLocal(ast.name)
        if duplicate is not None:
            raise Redeclared(Variable(), duplicate.name)
        if ast.init is not None:
            initType = self.visit(ast.init, param)
            if type(ast.typ) is AutoType :
                ast.typ = initType
            if type(initType) is not type(ast.typ):
                if type(initType) is IntegerType and type(ast.typ) is FloatType:
                    if ast.init.name :
                        self.inferType(ast.init.name, FloatType())
                    self.scope[0] += [Symbol(ast.name, ast.typ, kind = Variable())]
                else : raise TypeMismatchInStatement(ast)
            else :
                if type(ast.typ) is AutoType :
                    raise Invalid(Variable(), ast.name)
                self.scope[0] += [Symbol(ast.name, ast.typ, kind = Variable())]
        else : self.scope[0]+= [Symbol(ast.name, ast.typ, kind = Variable())]
        
    def visitParamDecl(self, ast : ParamDecl, param):
        duplicate = self.lookupLocal(ast.name)
        if duplicate is not None:
            raise Redeclared(Parameter(), duplicate.name)
        self.scope[0] += [Symbol(ast.name, ast.typ, kind = Parameter(), inherit = ast.inherit)]
    
    def visitFuncDecl(self, ast : FuncDecl, param):
        duplicate = self.lookupLocal(ast.name)
        if duplicate is not None:
            raise Redeclared(Function(), duplicate.name)
        self.scope[0] += [Symbol(ast.name, FuncType([Symbol(x.name,x.typ,Parameter(),inherit=x.inherit) for x in ast.params], ast.return_type), kind = Function(), inherit = ast.inherit)]
        self.scope = [[], *self.scope]
        for x in ast.params:
            self.visit(x, param)
        self.visit(ast.body, (param, "func"))
    
    def visitBinExpr(self, ast : BinExpr, param):
        leftType = self.visit(ast.left,param)
        rightType = self.visit(ast.right, param)
        if ast.op in ['+', '-', '*', '/']:
            if type(leftType) is FloatType and type(rightType) is FloatType:
                return FloatType()
            elif type(leftType) is IntegerType and type(rightType) is IntegerType:
                return IntegerType()
            elif type(leftType) is FloatType and type(rightType) is IntegerType:
                if ast.right.name :
                    self.inferType(ast.right.name, leftType)
                return FloatType()
            elif type(leftType) is IntegerType and type(rightType) is FloatType:
                if ast.left.name :
                    self.inferType(ast.left.name, rightType)
                return FloatType()
            else :
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['%'] :
            if type(leftType) is IntegerType and type(rightType) is IntegerType:
                return IntegerType()
            else :
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['&&', '||'] :
            if type(leftType) is BooleanType and type(rightType) is BooleanType:
                return BooleanType()
            else :
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['::'] :
            if type(leftType) is StringType and type(rightType) is StringType:
                return StringType()
            else :
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['<', '>', '<=', '>='] :
            if type(leftType) is IntegerType and type(rightType) is IntegerType:
                return BooleanType()
            elif type(leftType) is FloatType and type(rightType) is FloatType:
                return BooleanType()
            elif type(leftType) is FloatType and type(rightType) is IntegerType:
                return BooleanType()
            elif type(leftType) is IntegerType and type(rightType) is FloatType:
                return BooleanType()
            else :
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['==', '!='] :
            if type(leftType) is IntegerType and type(rightType) is IntegerType:
                return BooleanType()
            elif type(leftType) is BooleanType and type(rightType) is BooleanType:
                return BooleanType()
                
        
    def visitUnExpr(self, ast : UnExpr, param): 
        eType = self.visit(ast.val, param)
        if ast.op in ['!'] :
            if type(eType) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            else : 
                return BooleanType()
        elif ast.op in ['-'] :
            if type(eType) is IntegerType or type(eType) is FloatType:
                return eType
            else :
                raise TypeMismatchInExpression(ast)

    def visitId(self, ast : Id, param):
        symbol = self.lookupGlobal(ast.name)
        if symbol is None:
            raise Undeclared(Identifier(), ast.name)
        return symbol.typ
    
    def visitArrayCell(self, ast : ArrayCell, param): 
        symbol = self.lookupGlobal(ast.name)
        if symbol is None:
            raise Undeclared(Identifier(), ast.name)
        if type(symbol.typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        if len(ast.cell) != len(symbol.typ.dimensions):
            raise TypeMismatchInExpression(ast)
        for x in ast.cell:
            xType = self.visit(x, param)
            if type(xType) is not IntegerType:
                raise TypeMismatchInExpression(ast)
        return symbol.typ.typ
    
    def visitIntegerLit(self, ast, param): 
        return IntegerType()
    def visitFloatLit(self, ast, param): 
        return FloatType()
    def visitStringLit(self, ast, param): 
        return StringType()
    def visitBooleanLit(self, ast, param): 
        return BooleanType()
    def visitArrayLit(self, ast : ArrayLit, param):
        # {{1,2},{2,3},{4,5}}
        # ArrayType([3,2], IntegerType()) // 3x2 array of int
        # for x in ast.explist:
        #     if type(x) is not ArrayLit:
        #         return ArrayType([len(ast.explist)], self.visit(x, param))
        #     else:
        #         return ArrayType([len(ast.explist)] + self.visit(x, param).dimensions, self.visit(x.explist[0], param))
        # return ArrayType([len(ast.explist)], self.visit(ast.explist[0], param))
        # Infer the shape of the array from its elements recursively
        if len(ast.explist) == 0:
            raise TypeMismatchInExpression(ast)
        elif all(isinstance(e, ArrayLit) for e in ast.explist):
            # Recursive case
            shapes = [self.visit(e, param).dimensions for e in ast.explist]
            if not all(shape == shapes[0] for shape in shapes):
                raise TypeMismatchInExpression(ast)
            return ArrayType([len(ast.explist)] + shapes[0], self.visit(ast.explist[0].explist[0], param))
        else:
            # Base case
            shape = [len(ast.explist)]
            element_type = None
            for e in ast.explist:
                t = self.visit(e, param)
                if not element_type:
                    element_type = t
                elif element_type != t:
                    raise IllegalArrayLiteral(ast)
            return ArrayType(shape, element_type)
