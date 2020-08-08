import functools

def recursion(func):
    def wapper(*args, **kwargs):
        try:
            kwargs['count'] += 1
            if kwargs['count'] == kwargs['upper-limit']:
                return args, kwargs
            return func(*args, **kwargs)
        except Exception:
            pass
    return wapper

def recursionCall(func, upper_limit:int=200, *args, **wargs):
    wargs['count'] = 1
    wargs['upper-limit'] = upper_limit
    wargs['break'] = False
    while True:
        args, wargs = func(*args, **wargs)
        if not wargs['break']:
            wargs['upper-limit'] = wargs['count']+upper_limit
        else:
            break
    return args, wargs


    
if __name__ == "__main__":
    @recursion
    def gggd(*args, **kwargs):
        if kwargs['bbb'] == 3001:
            kwargs['break']= True
            return args, kwargs
        print(kwargs['bbb'])
        kwargs['bbb']+=1
        return gggd(*args, **kwargs)
        
    kwargs={'bbb':1}
    eee=recursionCall(gggd,**kwargs)
    eeee=""