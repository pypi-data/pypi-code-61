%matplotlib ipympl
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from mpl_interactions import interactive_plot, interactive_plot_factory

x = np.linspace(0,np.pi,100)
tau = np.linspace(1,10, 100)
beta = np.linspace(1,10)
def f(x, tau, beta):
    return np.sin(x*tau)*x**beta

def foo(x, **kwargs):
    return x

a = np.linspace(0,10)
b = (0, 10, 15)
c = {'this', 'set will be', 'unordered'}
d = {('this', 'set will be', 'ordered')}
e = 0 # this will not get a slider
f = widgets.Checkbox(value=True, description='A checkbox!!')
display(interactive_plot(foo, x=x, a=a, b=b, c=c, d=d, e=e, f_=f, display=False)[-1])