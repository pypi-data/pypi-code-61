import synacell.cmodule
import synacell.signal as signal
import random as rnd
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import matplotlib.colors as colors
import os
from shutil import copy2
import pkg_resources


def create_signal(sig_cnt=1, random=True, freq_li=None, amp_li=None, freq_range=4000, freq_res=50):
    sig_li = dict()
    sig_li["freq"] = []
    sig_li["amp"] = []
    sig_li["phase"] = []
    sig_li["tmin"] = []
    sig_li["tmax"] = []
    func_arr = np.zeros(16000)
    # Generate wav file
    for i in range(sig_cnt):
        if random:
            freq = rnd.random() * freq_range
            amp = rnd.random() * 1000.0
        else:
            freq = freq_li[i]
            amp = amp_li[i]
        sig_li["freq"].append(freq)
        sig_li["amp"].append(amp)
        if freq > 0:
            phase = 2.0 * math.pi * rnd.random()
        else:
            phase = 0.5 * math.pi
        sig_li["phase"].append(phase)
        tmin = rnd.random() * 0.5
        tmax = 0.5 + rnd.random() * 0.5
        tmax = 1.0 if tmax > 1.0 else tmax
        sig_li["tmin"].append(tmin)
        sig_li["tmax"].append(tmax)
        func = signal.func_generator(func_name="sin", freq=freq, amp=amp, phase=phase)
        func_arr += signal.func_to_nparray(func=func, t_min=tmin, t_max=tmax, size=16000,
                                           fixed_size=True)

    window = 16000 // freq_res
    yv = signal.nparray_to_fft_spectrum(func_arr, window=window)

    return func_arr, yv


def run_create_wav(one_freq=False, freq=250, amp=100):
    freq_li = []
    amp_li = []
    freq_range = 2000
    freq_res = 25
    if one_freq:
        freq_li.append(freq)
        amp_li.append(amp)
    else:
        for freq in range(700, freq_range + 1, freq_res):
            freq_li.append(freq)
            amp_li.append(100)
            print(f"freq={freq_li[-1]}, amp={amp_li[-1]}")

    sig, valid = create_signal(len(freq_li), random=False, freq_li=freq_li, amp_li=amp_li,
                               freq_range=freq_range, freq_res=freq_res)

    if one_freq:
        signal.make_wav(sig, "./train_simple_onefreq.wav")
    else:
        signal.make_wav(sig, "./train_simple.wav")


def run_train_resonant_rlc():

    # Create net
    rcl_cnt = 500
    freq_res = 10
    train, net = create_rlc_resonators(rcl_cnt=rcl_cnt, freq_res=freq_res)
    net.save_net("./initial.net")

    # Get data
    # filename = "004ae714_nohash_0.wav"
    # filename = "00176480_nohash_0.wav"
    filename = "03cf93b1_nohash_1.wav"

    # Copy file in working dir
    fname = f"../data/audio/down/{filename}"
    if os.path.isfile(fname) is False:
        fname = pkg_resources.resource_filename('synacell', f'data/audio/down/{filename}')
    copy2(fname, f'./{filename}')
    sample_rate, sig = wavfile.read(f'./{filename}')

    # You can also create data
    # run_create_wav(one_freq=True, freq=500, amp=1000)
    # sample_rate, sig = wavfile.read("./train_simple_onefreq.wav")
    window = 16000//freq_res
    sig_fft = signal.nparray_to_fft_spectrum(sig, window=window)

    # Load data in net
    net.set_params_dbarr(0, f"fid=0,size={len(sig)}", sig)

    # Set recorders
    for i in range(rcl_cnt):
        net.set_recorder(f"id={i},pid={3*i + 2},value=vo,beg={0.25*len(sig)},size={len(sig)}")

    # Run net
    net.connect_syna()
    net.reset()
    net.run(2*len(sig), 1.0 / 16000.0)
    record = np.zeros_like(sig_fft)
    for i in range(rcl_cnt):
        record[:, i] = net.get_record(i).data

    # Plot data
    fig, ax = plt.subplots(3, 1, sharex='all', sharey='all')
    fig.suptitle('Train simple')

    ax[0].plot([i * 1.0 / 16000.0 for i in range(len(sig))], sig, label="signal")
    ax[0].plot([i * 1.0 / 16000.0 for i in range(len(sig))], record[:, 11], label="record 0")
    ax[0].set_title(f"Random func f(t)")
    ax[0].grid(True)
    ax[0].legend()

    # Color map for fft
    cm_spec = plt.get_cmap('jet')
    cm_spec.set_under(color=(0.0, 0.0, 0.0), alpha=1.0)
    cm_spec.set_over(color=(1.0, 1.0, 1.0), alpha=1.0)
    # Select rect of the form x0,x1,y0,y1
    ext = [0, sig_fft.shape[0] / 16000, rcl_cnt*freq_res, 0]

    # Draw spectrogram
    ax[1].imshow(
        sig_fft[:, 0:rcl_cnt].transpose(),
        interpolation='none',
        norm=colors.PowerNorm(gamma=0.5, vmin=sig_fft.min(), vmax=sig_fft.max()),
        extent=ext,
        cmap=cm_spec,
        aspect='auto',
    )
    ax[1].set_title(f"FFT window={window}, freq. res.={16000 / window}Hz")

    # sqrt_record = np.sqrt(2.0 * record[:, 0:rcl_cnt])
    sqrt_record = record[:, 0:rcl_cnt]
    # Draw spectrogram
    ax[2].imshow(
        sqrt_record.transpose(),
        interpolation='none',
        norm=colors.PowerNorm(gamma=0.5, vmin=sig_fft.min(), vmax=sig_fft.max()),
        extent=ext,
        cmap=cm_spec,
        aspect='auto',
    )
    ax[2].set_title(f"FFT window={window}, freq. res.={16000 / window}Hz")

    plt.xlim(0, sig_fft.shape[0] / 16000)

    plt.show()


def create_rlc_resonators(rcl_cnt, freq_res):
    api = synacell.cmodule.SnnAPI
    net = api.new_net()

    # Make net
    net.add_part("id=0,type=CellMultiData")
    cid = 1
    for i in range(rcl_cnt):
        lp = 1.0/(((2.0*math.pi*(i+0.5)*freq_res)**2)*50e-6)
        # lp = 1e-3
        net.add_part(f"id={cid},type=CellRLC,lp={lp},c=50e-6,rs=1000,rp=100e3")
        net.add_part(f"id={1_000_000 + cid},type=SynaRCA,ciid=0,coid={cid}")
        net.add_part(f"id={cid + 1},type=CellEMA,alpha=0.01,sum=2")
        net.add_part(f"id={1_000_000 + 1000 * cid + (cid + 1)},"
                     f"type=SynaRCA,ciid={cid},coid={(cid + 1)},a={0.5 + (2.5e-3*(i+0.5)*freq_res)**2}")
        net.add_part(f"id={cid + 2},type=CellEMA,alpha=0.01,sum=1")
        net.add_part(f"id={1_000_000 + 1000 * (cid + 1) + (cid + 2)},"
                     f"type=SynaBuffer,ciid={(cid + 1)},coid={(cid + 2)}")
        cid += 3

    # Params for training
    pid_li = []
    key_li = ['cs', 'cp', 'rs', 'rp', 'a']
    del_li = {'cs': 1.0e-9, 'cp': 1.0e-9, 'rs': 1, 'rp': 1, 'a': 0.001}
    train = dict()
    train['pid_li'] = pid_li
    train['xmax'] = 0.0
    train['ymax'] = 0.0
    train['dwr'] = 0.0
    train['dwl'] = 0.0
    train['dw'] = 0.0
    for pid in pid_li:
        train[pid] = dict()
        train[pid]['key_li'] = key_li
        for key in key_li:
            train[pid][key] = dict()
            train[pid][key]['del'] = del_li[key]
            train[pid][key]['dx'] = 0.0
            train[pid][key]['diffxmax'] = 0.0
            train[pid][key]['diffymax'] = 0.0
            train[pid][key]['nxmax'] = 0.0
            train[pid][key]['nymax'] = 0.0
            train[pid][key]['ndwr'] = 0.0
            train[pid][key]['ndwl'] = 0.0
            train[pid][key]['ndw'] = 0.0

    return train, net


def run_test_breakdown():
    api = synacell.cmodule.SnnAPI
    net = api.new_net()
    rs = 1000
    rp = 1000
    cp = 1.9e-6
    cs = 1.0e-9
    a = 1

    # Make net
    net.add_part("id=0,type=CellMultiData")
    net.add_part(f"id=1,type=CellBuffer")
    net.add_part(f"id=1000001,type=SynaRCA,ciid=0,coid=1,cs={cs},cp={cp},rs={rs},rp={rp}")
    net.add_part(f"id=2,type=CellEMA,alpha=0.001,sum=2")
    net.add_part(f"id=1001002,type=SynaBuffer,ciid=1,coid=2")
    net.add_part(f"id=3,type=CellEMA,alpha=0.001,sum=1")
    net.add_part(f"id=1002003,type=SynaBuffer,ciid=2,coid=3")
    func = signal.func_generator(func_name="sin", freq=100, amp=100)
    sig = signal.func_to_nparray(func=func, t_min=0, t_max=1, size=16000, fixed_size=True)
    # Load data
    net.set_params_dbarr(0, f"fid=0,size={len(sig)}", sig)

    net.connect_syna()
    sid = 1000001
    key = 'cp'
    dval = -1.0e-9
    start_val = net.get_param(sid, key)
    val = start_val
    retval = 0.0
    while True:
        # Run net
        net.reset()
        net.run(16000, 1.0 / 16000.0)
        retval = net.get_vo(3)
        if math.isinf(retval) or math.isnan(retval):
            break
        val += dval
        net.set_params(sid, f'{key}={val}')

    print(f"Break occured for {key} = {val}")
    print(f"Now try with it adjustment")

    it = 1
    net.set_params(sid, f'{key}={start_val}')
    val = start_val
    while val > 1e-9:
        # Run net
        net.set_params(1000001, f"it={it}")
        net.reset()
        net.run(16000, 1.0 / 16000.0)
        retval = net.get_vo(3)
        if math.isinf(retval) or math.isnan(retval):
            if it < 50:
                it += 1
            else:
                break
        val += dval
        net.set_params(sid, f'{key}={val}')

    if it >= 50:
        print(f"Break occured for {key} = {val}, for it = {it}")
    else:
        print(f"Solution converged {key} = {val}, for it = {it}")


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
    # run_create_wav()
    # run_create_wav(one_freq=True)
    # run_test_breakdown()
    run_train_resonant_rlc()

