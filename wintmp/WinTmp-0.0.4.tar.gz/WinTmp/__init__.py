import clr
import os
import win32api

#List for hardware types and sensor types that our DLL can open
OHM_hwtypes = [ 'Mainboard', 'SuperIO', 'CPU', 'RAM', 'GpuNvidia', 'GpuAti', 'TBalancer', 'Heatmaster', 'SSD' ]
OHM_sensortypes = [
 'Voltage', 'Clock', 'Temperature', 'Load', 'Fan', 'Flow', 'Control', 'Level', 'Factor', 'Power', 'Data', 'SmallData'
]


def init_OHM():
    clr.AddReference('./OpenHardwareMonitorLib.dll')
    from OpenHardwareMonitor import Hardware
    hw = Hardware.Computer()
    hw.MainboardEnabled, hw.CPUEnabled, hw.RAMEnabled, hw.GPUEnabled, hw.HDDEnabled = True, True, True, True, True
    hw.Open()
    return hw


def fetch_data( handle ) :
    out = []
    for i in handle.Hardware :
        i.Update()
        for sensor in i.Sensors :
            thing = parse_sensor( sensor )
            if thing is not None :
                out.append( thing )
        for j in i.SubHardware :
            j.Update()
            for subsensor in j.Sensors :
                thing = parse_sensor( subsensor )
                out.append( thing )
    return out


def parse_sensor( snsr ) :
    if snsr.Value is not None :
        if snsr.SensorType == OHM_sensortypes.index( 'Temperature' ) :
            HwType = OHM_hwtypes[ snsr.Hardware.HardwareType ]
            return { "Type" : HwType, "Name" : snsr.Hardware.Name, "Sensor" : snsr.Name, "Reading" : u'%s\xb0C' % snsr.Value }


for i in fetch_data(init_OHM()):
    if i['Type'] == 'GpuNvidia':
        nvidia = True

try:
    tmp123 = nvidia
except:
    nvidia = False

def tmps():

    temps = {}

    data = fetch_data(init_OHM())

    for each in data:
        if each['Type'] == 'CPU':
            temps['CPU'][each['Sensor']] = each['Reading']
        elif 'Gpu' in each['Type']:
            if not nvidia:
                tmp_avg = 0
                for each in temps['Gpu']:
                    tmp_avg+=int(each)
                tmp_avg += int(each['Reading'])
                temps['Gpu'] = tmp_avg

    return temps


def GPU_Temp():

    if nvidia:
        things = [i for i in list(os.popen('nvidia-smi').readlines())[8].split(' ') if i != '' and i != '|' and i != '/' and i != '!\n']
        return things[1]
    else:
        try:
            return tmps()['Gpu']
        except:
            return ''


def CPU_Temp():

    try:
        return tmps()['CPU']
    except:
        return ''
