import synacell.cmodule
import synacell.signal as signal
import random as rnd
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.colors as colors
from scipy.io import wavfile
import synacell.examples.example_train_dft as extrain


def run_plot_emas_valids():
    freq_li = [0, 20, 130, 150, 500]
    amp_li = [100, 100, 100, 300, 200]
    sig, valid = extrain.create_signal(len(freq_li), random=False, freq_li=freq_li, amp_li=amp_li)

    fig, ax = plt.subplots(2, 1, sharex='all')
    fig.suptitle('EMAs and Validators')

    ax[0].plot([i * 1.0 / 16000.0 for i in range(len(sig))], sig)
    ax[0].set_title(f"Random func f(t) freq_li={freq_li}, amp_li={amp_li}")
    ax[0].grid(True)
    ax[0].legend()

    api = synacell.cmodule.SnnAPI
    net = api.new_net()
    net.add_part("id=0,type=CellMultiData")
    net.set_params_dbarr(0, f"fid=0,size={len(sig)}", sig)
    cid = 1
    sid = 1000000
    rs = 1000
    rp = 1000
    freq_res = 8000//(valid.shape[1] - 1)
    for i in range(valid.shape[1]):
        if i > 0:
            cp = 1.0 / (2.0 * math.pi * (i - 0.5) * freq_res * rs)
        else:
            cp = 1.0e-6
        cs = 1.0 / (2.0 * math.pi * (i + 0.5) * freq_res * rp)
        net.add_part(f"id={cid},type=CellEMA,alpha=0.02,sum=1")
        net.add_part(f"id={sid},type=SynaRCA,ciid=0,coid={cid},cs={cs}, "
                     f"cp={cp},rs={rs},rp={rp},a=5")
        cid += 1
        sid += 1

    net.connect_syna()
    net.set_recorder("id=0,pid=0,value=vo,beg=0,size=16000")
    net.set_recorder("id=1,pid=1,value=vo,beg=0,size=16000")
    net.set_recorder("id=2,pid=20,value=vo,beg=0,size=16000")
    net.reset()
    net.run(16000, 1.0 / 16000.0)
    record = [
        net.get_record(0),
        net.get_record(1),
        net.get_record(2)
    ]
    # plot 2
    ax[1].plot([i * 1.0 / 16000.0 for i in record[1].pc], record[1].data, '-',
               label="CellEMA 0 (0-75Hz)")
    ax[1].plot([i * 1.0 / 16000.0 for i in record[2].pc], record[2].data, '-',
               label="CellEMA 1 (75-125Hz)")
    ax[1].plot([i * 1.0 / 16000.0 for i in range(valid.shape[0])], valid[:, 0], '-',
               label="Validator 0Hz")
    ax[1].plot([i * 1.0 / 16000.0 for i in range(valid.shape[0])], valid[:, 1], '-',
               label="Validator 50Hz")
    ax[1].grid(True)
    ax[1].legend()

    plt.show()


if __name__ == '__main__':
    '''
    1. If the module is ran (not imported) the interpreter sets this at the top of your module:
    ```
    __name__ = "__main__"
    ```
    2. If the module is imported: 
    ```
    import rk
    ```
    The interpreter sets this at the top of your module:
    ```
    __name__ = "rk"
    ```
    '''
    run_plot_emas_valids()
