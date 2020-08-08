__all__ = ['expr_generate_funcs','cblk_generate_funcs','inst_generate','decl_generate','meta_generate']
from pyvmodule import viterator as viter
from .code_align import align_expr_area,align_mat,align_assign
import warnings
precedences_list = {
    0:('const','wire','reg','[]','{}','{{}}'),
    1:('~','!',' -',' &',' ^',' |'),
    2:('**',),
    3:('*','/','%'),
    4:('+','-',),
    5:('<<','>>',),
    6:('<=','<','>=','>',),
    7:('==','!='),
    8:('&',),
    9:('^',),
    10:('|',),
    11:('&&',),
    12:('||',),
    13:('?:',)}
precedences = {}
for level in range(len(precedences_list)):
    for op in precedences_list[level]:
        precedences[op] = level
def gen_braket(gen_func):
    def gen_func_with_braket(self,indent,p_precedence):
        contents,precedence = gen_func(self,indent)
        if p_precedence < precedence:
            contents[0].insert(0,'(')
            contents[-1].append(')')
        return contents
    return gen_func_with_braket
def joining_subexpr_long(exprs,spliter):
    contents = exprs[0]
    for i in range(1,len(exprs)):
        exprs[i][0][0:0] = spliter
    for i in range(1,len(exprs)):contents.extend(exprs[i])
    return contents
def joining_subexpr(exprs,spliter):
    contents = exprs[0]
    for i in range(1,len(exprs)):exprs[i][0].insert(0,spliter)
    for i in range(1,len(exprs)):contents[-1].extend(exprs[i][0])
    return contents
def append_inline(target,source):
    target[-1].extend(source[0])
    target.extend(source[1:])
@gen_braket
def gen_default(expr,indent):return [[str(expr)]],0
# inline
not_precedence = precedences['!']
invert_precedence = precedences['~']
@gen_braket
def gen_not_operator(expr,indent):
    if expr.width==1:op,precedence = '!',not_precedence
    else:op,precedence = '~',invert_precedence
    rhs = expr.rhs._generate(indent,precedence-1)
    rhs[0].insert(0,op)
    return rhs,precedence
def gen_left_operator(op):
    # inline
    precedence = precedences[op]
    @gen_braket
    def gen(expr,indent):
        rhs = expr.rhs._generate(indent,precedence-1)
        rhs[0].insert(0,op)
        return rhs,precedence
    return gen
def gen_binary_operator(op,left2right=False):
    # multi-line
    lspliter = op+' '
    spliter  = ' '+lspliter
    precedence = precedences[op]
    @gen_braket
    def gen(expr,indent):
        exprs = [
            expr.lhs._generate(indent  ,precedence if left2right and expr.lhs._typename== expr.rhs._typename else precedence-1),
            expr.rhs._generate(indent+4,precedence-1)]
        if expr._need_split_line(exprs):contents = joining_subexpr_long(exprs,[lspliter] if indent<=0 else ['',' '*indent,lspliter])
        else:contents = joining_subexpr(exprs,spliter)
        return contents,precedence
    return gen
def gen_associative_operator(op):
    # multi-line
    lspliter = op+' '
    spliter  = ' '+lspliter
    precedence = precedences[op]
    @gen_braket
    def gen(expr,indent):
        exprs = [child._generate(indent+4,precedence-1) for child in expr.childs]
        if expr._display_as_long or expr._need_split_line(exprs):contents = joining_subexpr_long(exprs,[lspliter] if indent<=0 else ['',' '*indent,lspliter])
        else:contents = joining_subexpr(exprs,spliter)
        return contents,precedence
    return gen
andn_precedence = precedences['&']
and1_precedence = precedences['&&']
orn_precedence = precedences['|']
or1_precedence = precedences['||']
def gen_and1_operator(expr,indent):
    exprs = [child._generate(indent+4,and1_precedence-1) for child in expr.childs]
    if expr._display_as_long or expr._need_split_line(exprs):
        contents = joining_subexpr_long(exprs,['&& '] if indent<=0 else ['',' '*indent,'&& '])
    else:contents = joining_subexpr(exprs,' && ')
    return contents,and1_precedence
def gen_and_operator(expr,indent):
    if expr.width==1:return gen_and1_operator(expr,indent)
    exprs = [child._generate(indent+4,andn_precedence-1) for child in expr.childs]
    if expr._display_as_long or expr._need_split_line(exprs):
        contents = joining_subexpr_long(exprs,['& '] if indent<=0 else ['',' '*indent,'& '])
    else:contents = joining_subexpr(exprs,' & ')
    return contents,andn_precedence
@gen_braket
def gen_validif(expr,indent):
    if expr.width==1:return gen_and1_operator(expr,indent)
    cond = expr.lhs._generate(indent)
    cond[ 0].insert(0,'{%d{'%len(expr.rhs))
    cond[-1].append('}}')
    exprs = [cond,expr.rhs._generate(indent+4,andn_precedence-1)]
    if expr._need_split_line(exprs):contents = joining_subexpr_long(exprs,['& '] if indent<=0 else ['',' '*indent,'& '])
    else:contents = joining_subexpr(exprs,' & ')
    return contents,andn_precedence
gen_and_operator = gen_braket(gen_and_operator)
@gen_braket
def gen_or_operator(expr,indent):
    precedence = or1_precedence if expr.width==1 else orn_precedence
    exprs = [child._generate(indent+4,precedence-1) for child in expr.childs]
    if expr._display_as_long or expr._need_split_line(exprs):
        spliter_r = '|| ' if expr.width==1 else '| '
        contents = joining_subexpr_long(exprs,[spliter_r] if indent<=0 else ['',' '*indent,spliter_r])
    else:
        spliter = ' || ' if expr.width==1 else ' | '
        contents = joining_subexpr(exprs,spliter)
    return contents,precedence
@gen_braket
def gen_concatenate(expr,indent):
    # multi-line
    exprs = [expr.childs[i]._generate(indent+4) for i in range(len(expr.childs)-1,-1,-1)]
    if expr._display_as_long or expr._need_split_line(exprs):contents = joining_subexpr_long(exprs,['',' '*indent,','])
    else:contents = joining_subexpr(exprs,',')
    contents[0].insert(0,'{')
    contents[-1].append('}')
    return contents,0
@gen_braket
def gen_replication(expr,indent):
    # braket
    contents = expr.rhs._generate(indent)
    contents[0].insert(0,'{%d{'%expr.count)
    contents[-1].append('}}')
    return contents,0
fetch_precedence = precedences['[]']
@gen_braket
def gen_fetch(expr,indent):
    # braket
    lhs = expr.lhs._generate(indent,fetch_precedence)
    rhs = expr.rhs._generate(indent,fetch_precedence)
    lhs[-1].append('[')
    rhs[-1].append(']')
    lhs[-1].extend(rhs[0])
    lhs.extend(rhs[1:])
    return lhs,fetch_precedence
mux_precedence = precedences['?:']
@gen_braket
def gen_mux(expr,indent):
    # multi-line
    def _gen_mux(expr,indent):
        contents = [[]]
        cond = expr.cond._generate(indent,mux_precedence-1)
        lhs = expr.lhs._generate(indent+4)
        append_inline(contents,cond)
        contents[-1].append(' ? ')
        append_inline(contents,lhs)
        contents[-1].append(' : ')
        return contents
    contents = _gen_mux(expr,indent)
    expr = expr.rhs
    myindent = ' '*indent
    while expr.typename=='?:':
        nextline = _gen_mux(expr,indent)
        nextline[0].insert(0,'')
        nextline[0].insert(0,myindent)
        contents.extend(nextline)
        expr = expr.rhs
    rhs = expr._generate(indent+4,mux_precedence-1)
    append_inline(contents,rhs)
    return contents,mux_precedence
expr_generate_funcs = {
        'parameter':gen_default,
        'const'  :gen_default,
        'wire'   :gen_default,
        'reg'    :gen_default,
        '~'      :gen_not_operator,
        ' -'     :gen_left_operator(' -'),
        ' &'     :gen_left_operator(' &'),
        ' |'     :gen_left_operator(' |'),
        ' ^'     :gen_left_operator(' ^'),
        '-'      :gen_binary_operator('-',left2right=True),
        '*'      :gen_binary_operator('*',left2right=True),
        '/'      :gen_binary_operator('/'),
        '%'      :gen_binary_operator('%'),
        '<<'     :gen_binary_operator('<<'),
        '>>'     :gen_binary_operator('>>'),
        '=='     :gen_binary_operator('=='),
        '!='     :gen_binary_operator('!='),
        '<'      :gen_binary_operator('<'),
        '>'      :gen_binary_operator('>'),
        '>='     :gen_binary_operator('>='),
        '<='     :gen_binary_operator('<='),
        '+'      :gen_associative_operator('+'),
        '&'      :gen_and_operator,
        '|'      :gen_or_operator,
        '^'      :gen_associative_operator('^'),
        '{}'     :gen_concatenate,
        '{{}}'   :gen_replication,
        '[]'     :gen_fetch,
        '?:'     :gen_mux,
        'validif':gen_validif}
def gen_begin(obj,myindent):
    contents = [[myindent,'begin']]
    if not obj.name is None:contents[-1].extend([':',obj.name])
    return contents
def gen_body(obj,indent):
    contents = []
    assignments = sorted([(str(y),x._generate(indent=indent)) for y,x in obj.assignments],key=lambda a:a[0])
    for target,assignment in assignments:
        assignment[0][0:0] = [' '*indent,target,'<=']
        assignment[-1].append(';')
        contents.extend(assignment)
    align_expr_area(contents)
    for f in obj.functions:
        expr_mat = f._generate(indent=indent)
        contents.extend(expr_mat)
    body = obj.body
    if not body is None and body.typename == 'if':
        contents.extend(body._generate(indent))
    return contents
def gen_end(obj,myindent,pairing=None):
    contents = [[myindent,'end']]
    if not pairing is None:
        contents[-1].append('// ')
        contents[-1].extend(pairing[0])
        for i in range(1,len(pairing)):
            contents.append([myindent,'// ']+pairing[i])
    return contents
def gen_begin_end(obj,indent,contents):
    myindent = ' '*indent
    contents.extend(gen_begin(obj,myindent))
    contents.extend(gen_body (obj,indent+4))
    contents.extend(gen_end  (obj,myindent))
    return contents
    
def gen_clock(obj,indent=0):
    if obj.cond is None:raise SyntaxError('Clock signal is not specified.')
    if obj.edge not in {'posedge','negedge'}:raise SyntaxError('Invalid sample edge "%s"'%str(obj.edge))
    contents = obj.cond._generate(indent=indent+4)
    contents[ 0][0:0] = ['always@(',obj.edge,' ']
    contents[-1].append(')')
    gen_begin_end(obj,indent,contents)
    return contents
def gen_delay(obj,indent=0):return gen_begin_end(obj,indent,[['always #%d'%obj.delay]])
def gen_init (obj,indent=0):return gen_begin_end(obj,indent,[['initial']])
def gen_if(obj,indent=0):
    if not isinstance(indent,int):raise TypeError(type(indent))
    if obj.cond is None:raise SyntaxError('condition signal of If-statement is not specified.')
    condition = obj.cond._generate(indent=indent+4)
    myindent = ' '*indent
    bodyblock = gen_body (obj,indent+4)
    end_lines = gen_end  (obj,myindent,condition if len(bodyblock)>type(obj).lines_show_pairing else None)
    condition[ 0][0:0] = [myindent,'if(']
    condition[-1].append(')')
    contents = condition
    contents.extend(gen_begin(obj,myindent))
    contents.extend(bodyblock)
    contents.extend(end_lines)
    if not obj.next is None:
        contents.append([myindent,'else'])
        contents.extend(obj.next._generate(indent=indent))
    return contents
def gen_else(obj,indent=0):
    condition = obj.prev.cond._generate(indent=indent+4)
    condition[ 0].insert(0,'else - if(')
    condition[-1].append(')')
    myindent = ' '*indent
    bodyblock = gen_body (obj,indent+4)
    end_lines = gen_end  (obj,myindent,condition if len(bodyblock)>type(obj).lines_show_pairing else None)
    contents = gen_begin(obj,myindent)
    contents.extend(bodyblock)
    contents.extend(end_lines)
    return contents
cblk_generate_funcs = {
        'always#':gen_delay,
        'always@':gen_clock,
        'initial':gen_init ,
        'if'     :gen_if   ,
        'else'   :gen_else }
io_details = {'input':'// I, ','output':'// O, ','inout':'// X, '}
def inst_port_generate(m,ports,is_wire=True):
    contents = []
    for i in range(len(ports)):
        val = ports[i]
        vname = val.ins_name
        line = ['    .',vname,'(',str(m.__dict__.get(vname,'')),')','' if i+1==len(ports) else ',']
        if is_wire:line.extend([io_details[val.io],str(val.width)])
        contents.append(line)
    contents = align_mat(contents)
    return contents
def inst_generate(m,myindent=''):
    cls = type(m)
    ins_name = m.ins_name
    mod_name = cls.mod_name
    
    param = [val for val in viter.parameters(cls)]
    
    contents = [[mod_name]]
    if len(param)>0:
        contents.append('#(')
        contents.extend(inst_port_generate(m,param,is_wire=False))
        contents.append(')')
        contents.append([ins_name])
    else:
        contents[-1].extend([' ',ins_name])
        
    ports = [val for val in viter.ports(cls,force_determined=True)]
    if len(ports)<=0:warnings.warn('No port defined in module "%s".'%mod_name)
    if len(ports)>0:
        contents.append(['('])
        contents.extend(inst_port_generate(m,ports,is_wire=True))
        contents.append([])
    else:
        contents[-1].append('(')
    contents[-1].append(');')
    return contents
def decl_generate(self,myindent='',last=True,mark=True):
    if self.typename == 'parameter':
        line = [myindent,'localparam' if self.io is None else 'parameter',' ',self.name,' = ',str(self.default_value)]
        line.append(';' if self.io is None else (' ' if last else ','))
        return line
    else:
        line = [myindent,'' if self.io is None else self.io.ljust(7),self.typename.ljust(4)]
        if not self._width_expr is None:
            gen = self._width_expr._generate(0,4 if self._width_expr._typename== '-' else 3)
            w = ''.join(word for words in gen for word in words)
            line.extend([' [',w,' - 1:0] '])
        else:line.extend([' [',str(self.width-1),':0] '] if self.width!=1 else ['','',' '])
        line.append(self.ins_name)
        if self.length>1:line.extend(['[',str(self.length-1),':0]'])
        line.extend(self._verilator_gen_pragmas())
        line.append(';' if self.io is None else (' ' if last else ','))
        if mark:line.append(self._verilog_comment_driven())
        return line
def gen_comments(comments,myindent=''):
    contents = []
    for comment in comments:
        for line in comment.split('\n'):
            if len(line)==0:contents.append([myindent])
            elif len(line)>=2 and line[:2]=='//':contents.append([myindent,line])
            else:contents.append([myindent,'// ',line])
    return contents
def compare_same_cond(w,v):
    return (v.io is None) == (w.io is None) and (v.length>1) == (w.length>1)
def get_block_same_cond(w,var):
    return [k for k,v in var if v.typename in {'wire','reg'} and compare_same_cond(w,v)]
def gen_decl_block(ws,indent=0):
    myindent = ' '*indent
    n = len(ws)
    code_mat = align_mat([ws[i]._decl_generate(myindent,last=i==n-1,mark=True) for i in range(n)])
    for i in range(n-1,-1,-1):
        w = ws[i]
        if w.typename == 'parameter':continue
        code_mat[i:i] = w._synopsys_gen_pragmas(myindent)
        code_mat[i:i] = w._verilog_gen_pragmas(myindent)
        code_mat[i:i] = gen_comments(w.comments,myindent)
        
        a = w._naming_ancestor
        next_a = ws[i-1]._naming_ancestor if i > 0 else None
        if not a is next_a:
            num = len(get_block_same_cond(w,a._naming_var.items()))
            if num > 4 and num + 4 < len(ws):
                code_mat[i:i] = [[myindent,'// group ',str(a)]]
    return code_mat
def gen_assignments(ws):
    contents = []
    insertions = []
    last_a = None
    for i in range(len(ws)):
        w = ws[i]
        a = w._naming_ancestor
        if not a is last_a:
            num = sum(len(v.assignments) for k,v in a._naming_var.items() if v.typename == 'wire')
            if len(a._naming_var) > 4 and len(a._naming_var)+4 < len(ws)  and num > 4:
                insertions.append((len(contents),[['// group ',str(a)]]))
        last_a = a
        for key,val in w.assignments:
            contents.extend(w._verilog_gen_assignment(key,val))
    contents = align_assign(contents)
    sft = 0
    for i,lines in insertions:
        contents[i+sft:i+sft] = lines
        sft += len(lines)
    return contents
def meta_generate(self,*args,**kwargs):
    contents = []
    contents.extend(gen_comments(self.module.copyright))
    if len(self.parameters) == 0:
        contents.append(['module %s('%self.module.mod_name])
    else:
        contents.append(['module %s#('%self.module.mod_name])
        contents.extend(gen_decl_block(self.parameters,indent=4))
        contents.append([')('])
    contents.extend(gen_decl_block(self.ports,indent=4))
    contents.append([');'])
    contents.extend(gen_decl_block(self.localparams))
    contents.extend(gen_comments(self.module.comments))
    contents.extend(gen_decl_block(self.inner_signals))
    if len(self.rams)>0 and len(self.inner_signals) > 0:
        contents.append(['// Declaring RAM','s' if len(self.rams)>1 else ''])
    contents.extend(gen_decl_block(self.rams))
    contents.extend(gen_assignments(self.wires))
    if len(self.controlblocks) > 0 and len(contents) > 200:
        contents.append(['// Writing Register','s' if len(self.controlblocks)>1 else ''])
    for ptr,blk in self.controlblocks.items():
        contents.extend(blk._generate(indent=0))
    if len(self.modules)>0 and len(contents) > 200:
        contents.append(['// Instancing Sub-Module','s' if len(self.modules)>1 else ''])
    for ins in self.modules:
        contents.extend(ins._generate())
    if hasattr(self.module,'_extra_code_'):
        contents.append([self.module._extra_code_])
    contents.append(['endmodule // '+self.module.mod_name])
    lines = []
    for words in contents:
        line = ''.join(words)
        lines.append(line)
    result = '\n'.join(lines)
    return result
