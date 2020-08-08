from pyvmodule.develope import *
class SingleRamInit(VStruct):
    def __init__(self,width,io='auto',**kwargs):
        VStruct.__init__(self,**kwargs)
        self.valid = Wire()
        self.index = Wire(width)
class RamInit(VStruct):
    def __init__(self,width,reset=None,io='auto',**kwargs):
        VStruct.__init__(self,**kwargs)
        if reset is None:
            self.index = Wire(width,io=io)
            self.valid = Wire(width,io=io)
        else:
            self.index = Reg(width,io=io)
            self.valid = Reg(width,io=io)
            self.valid.next = Wire(width)
            self.enable_ssa('more')
            self.more = self.index[0]
            for i in range(width):
                self.more = Wire(self.index[i]|self.more)
                self.valid.next[i] = self.valid[i] & self.more
            set = When(reset)[self.index:-1][self.valid:-1].\
                When(self.valid[-1])[self.index:self.index-1][self.valid:self.valid.next]
    def __call__(self,width,init=None):
        if init is None:x = SingleRamInit(width,io=None)
        else:x = init
        x.valid[:] = self.valid[ width-1]
        x.index[:] = self.index[:width  ]
        return x
            
