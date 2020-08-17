# Basic test for multihistogram.py using trivial Boltzmann distributions


import numpy as np
import dlmontepython.htk.multihistogram as multihistogram

#import matplotlib.pyplot as plt




def old_test_gen_nvt():
    # kT values
    kTarray=np.array([ [0.98], [0.99], [1.0], [1.01], [1.02] ])
    
    # -beta values
    nbetaarray=-1.0/kTarray
    #print("nbetaarray shape = ", nbetaarray.shape)

    # Construct some test data - pretty close to the Boltzmann distribution
    # of integral energies between 0.
    # The probability of the energy being E is exp(-E/kT)
    emax=100
    edata=[]
    nE0=10000
    
    for kT in kTarray:
        erundata = []
        for E in range(0,emax):
            # Number of points to include in data set
            nE = int(round(nE0*np.exp(-E/kT)))
            
            for i in range(0,nE):
                erundata.append( [E*1.0] )
    
        erundata = np.asarray(erundata)
        #print("kT, number of data points = ",kT,len(erundata))
        #print("kT, erundata.shape = ",kT,erundata.shape)
    
    #    hist, binedges = np.histogram(erundata, bins=emax, range=(0,emax))
    #    print hist
    #    print binedges    
    #    plt.plot(hist)
    #    plt.show()
        
        edata.append(np.array(erundata))

        
    # Calculate the free energies
    f = multihistogram.free_energies(nbetaarray, edata)
    
    #print("Free energies = ",f)
    
       
    # Calculate the expected energy for each data set
    obs = edata
    for i in range(len(kTarray)):
        #print("kT = ", kTarray[i])
        obstrue = np.exp(-1.0/kTarray[i])/(1-np.exp(-1.0/kTarray[i]))  # Can be derived
        obsdata = np.sum(edata[i])/len(edata[i])
        obsreweighted = multihistogram.reweight_observable(nbetaarray, edata, obs, nbetaarray[i], fe=f )
        
        #print("  observable (true, data, reweighted, diff) = ", obstrue, obsdata, obsreweighted, obstrue-obsreweighted)
                          



def old_test_reweight_observable_nvt():

    kTarray=np.array([ 0.98, 0.99, 1.0, 1.01, 1.02 ])
    #print("kTarray shape = ", kTarray.shape)
    
    # Construct some test data - pretty close to the Boltzmann distribution
    # of integral energies between 0.
    # The probability of the energy being E is exp(-E/kT)
    emax=100
    edata=[]
    nE0=1000
    
    for kT in kTarray:
        erundata = []
        for E in range(0,emax):
            # Number of points to include in data set
            nE = int(round(nE0*np.exp(-E/kT)))
            
            for i in range(0,nE):
                erundata.append( E*1.0 )
    
        erundata = np.asarray(erundata)
        #print("kT, number of data points = ",kT,len(erundata))
        #print("kT, erundata.shape = ",kT,erundata.shape)
    
    #    hist, binedges = np.histogram(erundata, bins=emax, range=(0,emax))
    #    print hist
    #    print binedges    
    #    plt.plot(hist)
    #    plt.show()
        
        edata.append(np.array(erundata))

    
    # Calculate the expected energy for each data set
    obs = edata
    for i in range(len(kTarray)):
        #print("kT = ", kTarray[i])
        obstrue = np.exp(-1.0/kTarray[i])/(1-np.exp(-1.0/kTarray[i]))  # Can be derived
        obsdata = np.sum(edata[i])/len(edata[i])
        obsreweighted = multihistogram.reweight_observable_nvt(kTarray, edata, obs, kT )
        
        #print("  observable (true, data, reweighted, diff) = ", obstrue, obsdata, obsreweighted, obstrue-obsreweighted)











def test_reweight_observable_nvt():    


    kTarray=np.array([ 0.98, 0.99, 1.0, 1.01, 1.02 ])
    #print("kTarray shape = ", kTarray.shape)
    
    # Construct some test data - a Boltzmann distribution
    # of integral energies between 0.
    # The probability of the energy being E is exp(-E/kT)
    # I generate energies from 0 to emax, and weight them
    # with appropriate probabilities
    emax=100
    egrid=np.arange(emax)
    edata = []
    weights = []
    
    for kT in kTarray:
        erundata = []
        weights.append(np.exp(-egrid/kT))
        edata.append(egrid)

    #print("weights = ",weights)
    #print("edata = ",edata)
        
    #    hist, binedges = np.histogram(erundata, bins=emax, range=(0,emax))
    #    print hist
    #    print binedges    
    #    plt.plot(hist)
    #    plt.show()
        
        
    # Calculate the expected energy for each data set
    obs = edata
    for i in range(len(kTarray)):
        #print("kT = ", kTarray[i])
        obstrue = np.exp(-1.0/kTarray[i])/(1-np.exp(-1.0/kTarray[i]))  # Can be derived
        obsdata = np.sum(np.dot(edata[i],weights[i]))/np.sum(weights[i])
        obsreweighted = multihistogram.reweight_observable_nvt(kTarray, edata, obs, kTarray[i], weights)
        
        #print("  observable (true, data, reweighted, diff) = ", obstrue, obsdata, obsreweighted, obstrue-obsreweighted)



test_reweight_observable_nvt()



