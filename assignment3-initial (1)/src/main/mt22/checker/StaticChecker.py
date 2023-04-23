# 2014121 - Ngo Gia Phong
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
    def __init__(self,ast) :
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast, [])
    
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
        
class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.isInLoop = []
        self.isInIf = []
        self.currFunc = None
        self.firstReturn = False
        self.globalEnv = [
            Symbol("readInteger", FuncType([], IntegerType()), kind = Function()),
            Symbol("printInteger", FuncType([Symbol("a", IntegerType())], VoidType()), kind = Function()),
            Symbol("readFloat", FuncType([], FloatType()), kind = Function()),
            Symbol("printFloat", FuncType([Symbol("a", FloatType())], VoidType()), kind = Function()),
            Symbol("readBoolean", FuncType([], BooleanType()), kind = Function()),
            Symbol("printBoolean", FuncType([(Symbol("a", BooleanType()))], VoidType()), kind = Function()),
            Symbol("readString", FuncType([], StringType()), kind = Function()),
            Symbol("printString", FuncType([Symbol("a",StringType())], VoidType()), kind = Function()),
            Symbol("preventDefault", FuncType([], VoidType()), kind = Function()),
        ]
        self.scope = [[]]
    def check(self):
        return self.visitProgram(self.ast, [])
    
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
    def inferReturnType(self, name, typ):
        for func in self.globalEnv:
            if func.name == name :
                func.typ.ret = typ
                return typ
        return None

    def visitProgram(self, ast : Program, param): 
        self.globalEnv += GetEnv(ast).check()
        for x in ast.decls:
            self.visit(x, self.scope)
        mainFunc = self.lookupGlobalFunc("main")
        if mainFunc is None:
            raise NoEntryPoint()
        elif type(mainFunc.typ.ret) is not VoidType:
            raise NoEntryPoint()
        elif len(mainFunc.typ.param) != 0:
            raise NoEntryPoint()
        
    # expression function call
    def visitFuncCall(self, ast : FuncCall, param):
        func = self.lookupGlobalFunc(ast.name)
        if func is None:
            raise Undeclared(Function(), ast.name)
        if len(ast.args) != len(func.typ.param):
            raise TypeMismatchInExpression(ast)
        for i in range(len(ast.args)):
            argType = self.visit(ast.args[i], param)
            if type(argType) is not type(func.typ.param[i].typ):
                if type(argType) is IntegerType and type(func.typ.param[i].typ) is FloatType:
                    continue
                if type(func.typ.param[i].typ) is AutoType and type(argType) is not VoidType:
                    func.typ.param[i].typ = argType
                    continue
                raise TypeMismatchInExpression(ast)
        return func.typ.ret
    
    def visitCallStmt(self, ast : CallStmt, param):
        if ast.name == "preventDefault" or ast.name == "super": 
            raise InvalidStatementInFunction(self.currFunc.name)
        func = self.lookupGlobalFunc(ast.name)
        if func is None:
            raise Undeclared(Function(), ast.name)
        if len(ast.args) != len(func.typ.param):
            raise TypeMismatchInStatement(ast)
        for i in range(len(ast.args)):
            argType = self.visit(ast.args[i], param)
            if type(argType) is not type(func.typ.param[i].typ):
                if type(argType) is IntegerType and type(func.typ.param[i].typ) is FloatType:
                    continue
                if type(func.typ.param[i].typ) is AutoType and type(argType) is not VoidType:
                    func.typ.param[i].typ = argType
                    continue
                raise TypeMismatchInStatement(ast)
        return func.typ.ret
     
    def visitAssignStmt(self, ast : AssignStmt, param):
        rhsType = self.visit(ast.rhs, param)
        lhsType = self.visit(ast.lhs, param)
        if type(lhsType) in [ArrayType, VoidType]:
            raise TypeMismatchInStatement(ast)
        if type(rhsType) is not type(lhsType):
            if type(rhsType) is IntegerType and type(lhsType) is FloatType:
                return lhsType
            elif type(lhsType) is AutoType and type(rhsType) is not VoidType:
                self.inferType(ast.lhs.name, rhsType)
                return rhsType
            elif type(rhsType) is AutoType and type(lhsType) is not VoidType:
                if type(ast.rhs) is Id:
                    self.inferType(ast.rhs.name, lhsType)
                elif type(ast.rhs) is FuncCall:
                    self.inferReturnType(ast.rhs.name, lhsType)
                return lhsType
            else:
                raise TypeMismatchInStatement(ast)
        else :
            return lhsType
        
        
    def visitBlockStmt(self, ast : BlockStmt, param):
        if type(param) is tuple:
            if param[1] == "for" or param[1] == "while" or param[1] == "doWhile" or param[1] == "block":
                self.scope = [[], *self.scope]
                for x in ast.body:
                    if type(x) is BlockStmt: self.visit(x, (param, "block"))
                    else : self.visit(x, param)
            if param[1] == "if":
                self.scope = [[], *self.scope]
                for x in ast.body:
                    if type(x) is BlockStmt: self.visit(x, (param, "block"))
                    else : self.visit(x, param)
            if param[1][0] == "func":
                funcInfo = param[1][1]
                if funcInfo.typ.inherit is not None:
                    parent = self.lookupGlobalFunc(funcInfo.typ.inherit)
                    if parent is None:
                        raise Undeclared(Function(), funcInfo.typ.inherit)
                    else :
                        # parent exist
                        # check duplicate param in parent
                        parentParams = []
                        for i in range(len(parent.typ.param)):
                            if parent.typ.param[i].name in parentParams:
                                raise Redeclared(Parameter(), parent.typ.param[i].name)
                            parentParams.append(parent.typ.param[i].name)
                        # check super or prevent default is first stmt
                        if len(ast.body) == 0:
                            if len(parent.typ.param) != 0:
                                raise InvalidStatementInFunction(funcInfo.name)
                        elif type(ast.body[0]) is not CallStmt:
                            # auto call super();
                            if len(parent.typ.param) != 0:
                                raise InvalidStatementInFunction(funcInfo.name)
                        else : 
                            if ast.body[0].name != "super" and ast.body[0].name != "preventDefault":
                                # auto call super();
                                if len(parent.typ.param) != 0:
                                    raise InvalidStatementInFunction("")
                                # raise InvalidStatementInFunction(ast.body[0])
                            elif ast.body[0].name == "super": # call super(<args>)
                                if len(ast.body[0].args) > len(parent.typ.param):
                                    raise TypeMismatchInExpression(ast.body[0].args[len(parent.typ.param)])
                                elif len(ast.body[0].args) < len(parent.typ.param):
                                    raise TypeMismatchInExpression("")
                                for i in range(len(ast.body[0].args)):
                                    argType = self.visit(ast.body[0].args[i], param)
                                    if type(argType) is not type(parent.typ.param[i].typ):
                                        if type(argType) is IntegerType and type(parent.typ.param[i].typ) is FloatType:
                                            # check inherit parameter and add to scope
                                            if parent.typ.param[i].inherit is True:
                                                duplicate = self.lookupLocal(parent.typ.param[i].name)
                                                if duplicate is not None:
                                                    raise Invalid(Parameter(), parent.typ.param[i].name)
                                                self.scope[0].append(Symbol(parent.typ.param[i].name, parent.typ.param[i].typ, kind = Parameter(),inherit=True))
                                            continue
                                        if type(parent.typ.param[i].typ) is AutoType and type(argType) is not VoidType:
                                            parent.typ.param[i].typ = argType
                                            if parent.typ.param[i].inherit is True:
                                                duplicate = self.lookupLocal(parent.typ.param[i].name)
                                                if duplicate is not None:
                                                    raise Invalid(Parameter(), parent.typ.param[i].name)
                                                self.scope[0].append(Symbol(parent.typ.param[i].name, parent.typ.param[i].typ, kind = Parameter(),inherit=True))
                                            continue
                                        raise TypeMismatchInExpression(ast.body[0].args[i])
                                    else :
                                        if parent.typ.param[i].inherit is True:
                                            duplicate = self.lookupLocal(parent.typ.param[i].name)
                                            if duplicate is not None:
                                                raise Invalid(Parameter(), parent.typ.param[i].name)
                                            self.scope[0].append(Symbol(parent.typ.param[i].name, parent.typ.param[i].typ, kind = Parameter(),inherit=True))
                            elif ast.body[0].name == "preventDefault": pass # call preventDefault(), prevent call super()
                            if len(ast.body) > 1:
                                for x in ast.body[1:]:
                                    if type(x) is BlockStmt:
                                        self.visit(x, (param, "block"))
                                    else : self.visit(x, param)
                else :
                    for x in ast.body:
                        if type(x) is BlockStmt: self.visit(x, (param, "block"))
                        else : self.visit(x, param)
        self.scope = self.scope[1:]
        
            
    def visitIfStmt(self, ast : IfStmt, param):
        condType = self.visit(ast.cond, param)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.isInIf.append(True)
        if type(ast.tstmt) is BlockStmt:
            self.visit(ast.tstmt, (param, "if"))
        else :
            self.visit(ast.tstmt, param)
        if ast.fstmt is not None:
            if type(ast.fstmt) is BlockStmt:
                self.visit(ast.fstmt, (param, "if"))
            else :
                self.visit(ast.fstmt, param)
        self.isInIf.pop()

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
        self.isInLoop.append(True)
        if type(ast.stmt) is BlockStmt:
            self.visit(ast.stmt, (param, "for"))
        else :
            self.visit(ast.stmt, param)
        self.isInLoop.pop()
        
    def visitWhileStmt(self, ast : WhileStmt, param):
        condType = self.visit(ast.cond, param)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.isInLoop.append(True)
        if type(ast.stmt) is BlockStmt:
            self.visit(ast.stmt, (param, "while"))
        else :
            self.visit(ast.stmt, param)
        self.isInLoop.pop()
        
    def visitDoWhileStmt(self, ast : DoWhileStmt, param): 
        condType = self.visit(ast.cond, param)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.isInLoop.append(True)
        if type(ast.stmt) is BlockStmt:
            self.visit(ast.stmt, (param, "doWhile"))
        else:
            self.visit(ast.stmt, param)
        self.isInLoop.pop()
        
    def visitBreakStmt(self, ast, param):
        if len(self.isInLoop) == 0:
            raise MustInLoop(ast)
        
    def visitContinueStmt(self, ast, param):
        if len(self.isInLoop) == 0:
            raise MustInLoop(ast)
        
    def visitReturnStmt(self, ast : ReturnStmt, param):
        if self.firstReturn is True: pass
        elif self.firstReturn is False:
            if len(self.isInIf) > 0 :
                if ast.expr is None:
                    if type(self.currFunc.typ.ret) is not VoidType:
                        if type(self.currFunc.typ.ret) is AutoType:
                            self.currFunc.typ.ret = VoidType()
                        else : raise TypeMismatchInStatement(ast)
                else :
                    retType = self.visit(ast.expr, param)
                    if type(retType) is not type(self.currFunc.typ.ret) :
                        if type(retType) is IntegerType and type(self.currFunc.typ.ret) is FloatType: pass
                        elif type(self.currFunc.typ.ret) is AutoType and type(retType) is not VoidType:
                            self.currFunc.typ.ret = retType
                        elif type(retType) is AutoType and type(self.currFunc.typ.ret) is not VoidType:
                            if type(ast.expr) is Id:
                                self.inferType(ast.expr.name, self.currFunc.typ.ret)
                            elif type(ast.expr) is FuncCall:
                                self.inferReturnType(ast.expr.name, self.currFunc.typ.ret)
                        else : raise TypeMismatchInStatement(ast)
            elif len(self.isInIf) == 0:
                if ast.expr is None:
                    if type(self.currFunc.typ.ret) is not VoidType:
                        if type(self.currFunc.typ.ret) is AutoType:
                            self.currFunc.typ.ret = VoidType()
                        else : raise TypeMismatchInStatement(ast)
                else :
                    retType = self.visit(ast.expr, param)
                    if type(retType) is not type(self.currFunc.typ.ret) :
                        if type(retType) is IntegerType and type(self.currFunc.typ.ret) is FloatType: pass
                        elif type(self.currFunc.typ.ret) is AutoType and type(retType) is not VoidType:
                            self.currFunc.typ.ret = retType
                        elif type(retType) is AutoType and type(self.currFunc.typ.ret) is not VoidType:
                            if type(ast.expr) is Id:
                                self.inferType(ast.expr.name, self.currFunc.typ.ret)
                            elif type(ast.expr) is FuncCall:
                                self.inferReturnType(ast.expr.name, self.currFunc.typ.ret)
                        else : raise TypeMismatchInStatement(ast)
                self.firstReturn = True
      

    def visitVarDecl(self, ast : VarDecl, param):
        duplicate = self.lookupLocal(ast.name)
        if duplicate is not None:
            raise Redeclared(Variable(), duplicate.name)
        if ast.init is not None:
            self.scope[0] += [Symbol(ast.name, ast.typ, kind = Variable())]
            initType = self.visit(ast.init, param)
            retTyp = ast.typ
            if type(ast.typ) is AutoType :
                retTyp = self.inferType(ast.name, initType)
            if type(initType) is not type(retTyp):
                if type(initType) is IntegerType and type(ast.typ) is FloatType:
                    pass
                elif type(initType) is AutoType and type(ast.typ) is not VoidType:
                    if type(ast.init) is FuncCall:
                        self.inferReturnType(ast.init.name, ast.typ)
                    elif type(ast.init) is Id:
                        self.inferType(ast.init.name, ast.typ)
                else : raise TypeMismatchInVarDecl(ast)
            else :
                if type(ast.typ) is ArrayType :
                    if ast.typ.dimensions != initType.dimensions:
                        raise TypeMismatchInVarDecl(ast)
                    if type(ast.typ.typ) != type(initType.typ):
                        raise TypeMismatchInVarDecl(ast)
                self.scope[0] += [Symbol(ast.name, ast.typ, kind = Variable())]
        else : 
            if type(ast.typ) is AutoType:
                raise Invalid(Variable(),ast.name)
            self.scope[0]+= [Symbol(ast.name, ast.typ, kind = Variable())]
        
    def visitParamDecl(self, ast : ParamDecl, param):
        duplicate = self.lookupLocal(ast.name)
        if duplicate is not None:
            raise Redeclared(Parameter(), duplicate.name)
        self.scope[0] += [Symbol(ast.name, ast.typ, kind = Parameter(), inherit = ast.inherit)]
    
    def visitFuncDecl(self, ast : FuncDecl, param):
        duplicate = self.lookupLocal(ast.name)
        if duplicate is not None:
            raise Redeclared(Function(), duplicate.name)
        func = self.lookupGlobalFunc(ast.name)
        self.scope[0] += [func]
        self.currFunc = func
        self.scope = [[], *self.scope]
        if func.typ.inherit is not None:
            parent = self.lookupGlobalFunc(func.typ.inherit)
            if parent is None:
                raise Undeclared(Function(), func.typ.inherit)
        prevParam = []
        for x in func.typ.param:
            # check duplicate
            if x.name in prevParam:
                raise Redeclared(Parameter(), x.name)
            self.scope[0] += [x]
            prevParam += [x.name]
        self.visit(ast.body, (param, ("func", func)))
        self.currFunc = None
        self.firstReturn = False
    
    def visitBinExpr(self, ast : BinExpr, param):
        leftType = self.visit(ast.left,param)
        rightType = self.visit(ast.right, param)
        if ast.op in ['+', '-', '*', '/']:
            if type(leftType) is FloatType and type(rightType) is FloatType:
                return FloatType()
            elif type(leftType) is IntegerType and type(rightType) is IntegerType:
                return IntegerType()
            elif type(leftType) is FloatType and type(rightType) is IntegerType:
                return FloatType()
            elif type(leftType) is IntegerType and type(rightType) is FloatType:
                return FloatType()
            elif type(leftType) is AutoType and type(rightType) in [FloatType, IntegerType]:
                if type(ast.left) is Id :
                    self.inferType(ast.left.name, rightType)
                    return rightType    
                elif type(ast.left) is FuncCall:
                    self.inferReturnType(ast.left.name, rightType)
                    return rightType
            elif type(leftType) in [FloatType, IntegerType] and type(rightType) is AutoType:
                if type(ast.right) is Id :
                    self.inferType(ast.right.name, leftType)
                    return leftType    
                elif type(ast.right) is FuncCall:
                    self.inferReturnType(ast.right.name, leftType)
                    return leftType
            else :
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['%'] :
            if type(leftType) is IntegerType and type(rightType) is IntegerType:
                return IntegerType()
            elif type(leftType) is AutoType and type(rightType) is IntegerType:
                if type(ast.left) is Id :
                    self.inferType(ast.left.name, rightType)
                    return rightType
                elif type(ast.left) is FuncCall:
                    self.inferReturnType(ast.left.name, rightType)
                    return rightType
            elif type(leftType) is IntegerType and type(rightType) is AutoType:
                if type(ast.right) is Id :
                    self.inferType(ast.right.name, leftType)
                    return leftType
                elif type(ast.right) is FuncCall:
                    self.inferReturnType(ast.right.name, leftType)
                    return leftType
            else :
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['&&', '||'] :
            if type(leftType) is BooleanType and type(rightType) is BooleanType:
                return BooleanType()
            elif type(leftType) is AutoType and type(rightType) is BooleanType:
                if type(ast.left) is Id :
                    self.inferType(ast.left.name, rightType)
                    return rightType
                elif type(ast.left) is FuncCall:
                    self.inferReturnType(ast.left.name, rightType)
                    return rightType
            elif type(leftType) is BooleanType and type(rightType) is AutoType:
                if type(ast.right) is Id :
                    self.inferType(ast.right.name, leftType)
                    return leftType
                elif type(ast.right) is FuncCall:
                    self.inferReturnType(ast.right.name, leftType)
                    return leftType
            else :
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['::'] :
            if type(leftType) is StringType and type(rightType) is StringType:
                return StringType()
            elif type(leftType) is AutoType and type(rightType) is StringType:
                if type(ast.left) is Id :
                    self.inferType(ast.left.name, rightType)
                    return rightType
                elif type(ast.left) is FuncCall:
                    self.inferReturnType(ast.left.name, rightType)
                    return rightType
            elif type(leftType) is StringType and type(rightType) is AutoType:
                if type(ast.right) is Id :
                    self.inferType(ast.right.name, leftType)
                    return leftType
                elif type(ast.right) is FuncCall:
                    self.inferReturnType(ast.right.name, leftType)
                    return leftType
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
            elif type(leftType) is AutoType and type(rightType) in [FloatType, IntegerType]:
                if type(ast.left) is Id :
                    self.inferType(ast.left.name, rightType)
                    return BooleanType()
                elif type(ast.left) is FuncCall:
                    self.inferReturnType(ast.left.name, rightType)
                    return BooleanType()
            elif type(leftType) in [FloatType, IntegerType] and type(rightType) is AutoType:
                if type(ast.right) is Id :
                    self.inferType(ast.right.name, leftType)
                    return BooleanType()
                elif type(ast.right) is FuncCall:
                    self.inferReturnType(ast.right.name, leftType)
                    return BooleanType()
            else :
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['==', '!='] :
            if type(leftType) is IntegerType and type(rightType) is IntegerType:
                return BooleanType()
            elif type(leftType) is BooleanType and type(rightType) is BooleanType:
                return BooleanType()
            elif type(leftType) is IntegerType and type(rightType) is BooleanType:
                return BooleanType()
            elif type(leftType) is BooleanType and type(rightType) is IntegerType:
                return BooleanType()
            elif type(leftType) is AutoType and type(rightType) in [BooleanType, IntegerType]:
                if type(ast.left) is Id :
                    self.inferType(ast.left.name, rightType)
                    return BooleanType()
                elif type(ast.left) is FuncCall:
                    self.inferReturnType(ast.left.name, rightType)
                    return BooleanType()
            elif type(leftType) in [BooleanType, IntegerType] and type(rightType) is AutoType:
                if type(ast.right) is Id :
                    self.inferType(ast.right.name, leftType)
                    return BooleanType()
                elif type(ast.right) is FuncCall:
                    self.inferReturnType(ast.right.name, leftType)
                    return BooleanType()
            else :
                raise TypeMismatchInExpression(ast)
                
        
    def visitUnExpr(self, ast : UnExpr, param): 
        eType = self.visit(ast.val, param)
        if ast.op in ['!'] :
            if type(eType) is not BooleanType:
                if type(eType) is AutoType:
                    if type(ast.val) is Id :
                        self.inferType(ast.val.name, BooleanType())
                        return BooleanType()
                    elif type(ast.val) is FuncCall:
                        self.inferReturnType(ast.val.name, BooleanType())
                        return BooleanType()
                raise TypeMismatchInExpression(ast)
            else : 
                return BooleanType()
        elif ast.op in ['-'] :
            if type(eType) is IntegerType or type(eType) is FloatType:
                return eType
            elif type(eType) is AutoType:
                if type(ast.val) is Id :
                    self.inferType(ast.val.name, IntegerType())
                    return IntegerType()
                elif type(ast.val) is FuncCall:
                    self.inferReturnType(ast.val.name, IntegerType())
                    return IntegerType()
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
        if len(ast.cell) > len(symbol.typ.dimensions):
            raise TypeMismatchInExpression(ast)
        elif len(ast.cell) < len(symbol.typ.dimensions):
            for x in ast.cell:
                xType = self.visit(x, param)
                if type(xType) is not IntegerType:
                    raise TypeMismatchInExpression(ast)
            dimen = symbol.typ.dimensions[len(ast.cell):]
            typ = symbol.typ.typ
            return ArrayType(dimen, typ)
        else: 
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
        def supportArrayLit(ctx,param):
            if type(ctx) is ArrayLit:
                if len(ctx.explist) == 0:
                    return [None,0]
                firstElement = supportArrayLit(ctx.explist[0], param) # (Integer(), 0)
                dimensions = [len(ctx.explist)]
                for exp in ctx.explist:
                    memberType = supportArrayLit(exp, param)
                    if type(firstElement[0]) is type(memberType[0]):
                        if len(firstElement[1]) != len(memberType[1]):
                            raise IllegalArrayLiteral(ast)
                        for i in range(0, len(firstElement[1])):
                            if firstElement[1][i] != memberType[1][i]:
                                raise IllegalArrayLiteral(ast)
                    else:
                        raise IllegalArrayLiteral(ast)
                if firstElement[1] != [0]:
                    dimensions += firstElement[1]
                return (firstElement[0], dimensions)
            else:
                atomicLit = self.visit(ctx, param)
                return (atomicLit, [0])
        result = supportArrayLit(ast, param)
        arrTyp = result[0]
        arrDim = result[1]
        return ArrayType(arrDim, arrTyp)
