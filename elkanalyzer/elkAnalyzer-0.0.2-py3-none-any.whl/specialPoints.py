import pandas as pd
import numpy as np
import copy

def calcStandard(path):
    '''
	Calculates the coordinates of standard special points using the reciprocal lattice vectors elk decides to use. This is basically a change of basis calculator
	Parameters
    ----------
    path : STRING ending in //
        DESCRIPTION. Full path to folder where INFO.OUT is found

    Returns
    -------
    newPts : list
        DESCRIPTION. each row of the list contains the kx, ky, and kz coordinates of the special point designated by the fourth column value following 
		C. Bradley and A.P. Cracknell's (Chapter 3) "The mathematical theory of symmetry in solids: representation theory for point groups and space groups": 
		https://www.maa.org/publications/maa-reviews/the-mathematical-theory-of-symmetry-in-solids-representation-theory-for-point-groups-and-space). 
	'''

    file=open(path+'INFO.OUT', 'r')
    d=file.readlines()
    file.close()
    #d=pd.read_csv(path+'INFO.OUT', sep=',')
    L=len(d)
    
    row=0
    
    while d[row][0:3]!='Rec':
        row=row+1
    
    astar=[float(i) for i in d[row+1].split(maxsplit=3)]
    bstar=[float(i) for i in d[row+2].split(maxsplit=3)]
    cstar=[float(i) for i in d[row+3].split(maxsplit=3)]
    
    
    #find space groupand cast to int
    elkin=pd.read_csv(path+'elk.in', header=None, names='Lines')
    nLinesElkin=len(elkin)
    cnt=0
    while cnt<nLinesElkin and str(elkin['L'][cnt][0:7])!='!  Herm':
        cnt=cnt+1
    
    cnt=cnt+3
    L=elkin['L'][cnt]
    fst=L.find(':')
    SG=L[fst+1:]
    scnd=L[fst+1:].find(':')
    if scnd<0:
        spaceGroup=int(SG)
    else:
        spaceGroup=int(SG[:scnd])
    
    
    
    #find lattice constants from spacegroup
    lnLatCnst=elkin['n'][cnt+1]
    lnAng=elkin['n'][cnt+2]
    
    
    latConstConvL=lnLatCnst.split(maxsplit=4)
    AngL=lnAng.split(maxsplit=4)
    latCon=latConstConvL[2:5]
    Ang=AngL[2:5]
    Ang=np.asarray([float(i) for i in Ang])
    latCon=np.asarray([float(i) for i in latCon])
    
    
    #Ang[::-1].sort()

    print(Ang)
    
    #find odd angle out
    if Ang[0]==Ang[1]:
        gamma=Ang[2]
    elif Ang[0]==Ang[2]:
        gamma=Ang[1]
    else:
        gamma=Ang[0]
    #find odd angle out and assign it to c if spacegroup has a=b and c different (tetragonal, trigonal, hexagonal)
    if spaceGroup>74 and  spaceGroup<195:
        latCon[::-1].sort()
        if latCon[0]==latCon[1]:
            a=latCon[0]
            b=latCon[1]
            c=latCon[2]
        else:
            a=latCon[1]
            b=latCon[2]
            c=latCon[0]
    elif spaceGroup>3 and spaceGroup<16:
        if Ang[0]==Ang[1]:
            a=latCon[0]
            b=latCon[1]
            c=latCon[2]
        elif Ang[0]==Ang[2]:
            a=latCon[0]
            b=latCon[2]
            c=latCon[1]
        else:
            a=latCon[0]
            b=latCon[1]
            c=latCon[2]
    else:
        a=latCon[0]
        b=latCon[1]
        c=latCon[2]
    print([a, b, c])
    print(gamma)
    """
    find traditional basis of space group
    Store in array [[0,0,0,'gamma'],[0.5, 0.5, 0.5]]
    
    """
    #pts=[[]]
    
    #initialize conventional basis set
    asc=[None]*3
    bsc=[None]*3
    csc=[None]*3
    
    #triclinic
    if spaceGroup<3:
        pts=[[0.5,0,0,'B']
              [0,0,0,'\Gamma'],
              [0,0,0.5,'G'],
              [0,0,0,'\Gamma'],
              [0,0.5,0,'F']]
        asc=np.array(astar)
        bsc=np.array(bstar)
        csc=np.array(cstar)
        #asc=
    #monoclinic
    elif spaceGroup<16:
        #P
        Pmono=[3, 4, 6, 7, 10, 11, 13, 14]
        if spaceGroup in Pmono:
            pts=[[0,0,0,'\Gamma'],
              [0,0,0.5,'Z'],
              [-0.5,0,0,'B'],
              [-0.5,0,0.5,'D'],
              [0,0.5,0,'Y'],
              [0,0.5,0.5, 'C'],
              [0.5, 0.5, 0, 'A'],
              [0.5, 0.5, 0.5, 'E']]
            asc=2*np.pi/b*np.array([-1/np.tan(gamma/180*np.pi), -1, 0])
            bsc=2*np.pi/a*np.array([1/np.sin(gamma/180*np.pi), 0, 0])
            csc=2*np.pi/c*np.array([0,0,1])
        else :
        #C or B
            pts=[[0, 0, 0.5, 'V'],
                  [0, -0.5, 0.5, 'Z'],
                  [0,0,0,'\Gamma'],
                  [-0.5, 0, 0, 'A'],
                  [-0.5, -0.5, 0.5, 'M'],
                  [-0.5, 0, 0.5, 'L']]
            asc=2*np.pi/b*np.array([-1/np.tan(gamma/180*np.pi), -1, 0])
            bsc=2*np.pi/(a*c)*np.array([c/np.sin(gamma/180*np.pi), 0, -a])
            csc=2*np.pi/(a*c)*np.array([c/np.sin(gamma/180*np.pi), 0, a])
    #orthorhombic
    elif spaceGroup<75:
        #C or A
        Corth=[20, 21, 35, 36, 37, 38, 39, 40, 41, 63, 64, 65, 66, 67, 68]
        Forth=[22, 42, 43, 69, 70]
        Iorth=[23, 24, 44, 45, 46, 71, 72, 73, 74]
        if spaceGroup in Corth:
    
            #for a>b (fig 3.6 a)
    
            pts=[[0,0,0,'\Gamma'],
                  [0, 0, 0.5, 'Z'],
                  [0.5, 0.5, 0.5, 'T'],
                  [0.5, 0.5, 0, 'Y'],
                  [0,0,0,'\Gamma'],
                  [0, 0.5, 0, 'S'],
                  [0, 0.5, 0.5, 'R']]
            asc=2*np.pi/(b*a)*np.array([b, -a, 0])
            bsc=2*np.pi/(b*a)*np.array([b, a, 0])
            csc=2*np.pi/c*np.array([0, 0, 1])
        #F
        elif spaceGroup in Forth:
            #ordered so 1/a^2<1/b^2+c^2, 1/b^2<1/c^2+1/a^2, and 1/c^2<1/a^2+1/b^2
            pts=[[0.5, 0.5, 0, 'Z'],
                  [0,0,0,'\Gamma'],
                  [0.5, 0, 0.5, 'X'],
                  [0.5, 0, 0, 'L'],
                  [0,0,0,'\Gamma']
                  [0, -0.5, -0.5, 'Y']]
            asc=2*np.pi*np.array([1/a, 1/b, 1/c])
            bsc=2*np.pi*np.array([-1/a, -1/b, 1/c])
            csc=2*np.pi*np.array([1/a, -1/b, -1/c])
        #I
        elif  spaceGroup in Iorth:
            #ordered so a>b>c
            pts=[[0.5, -0.5, 0.5, 'X'],
                  [0,0,0,'\Gamma'],
                  [0.5, 0, 0, 'R'],
                  [0.75, -0.25, -0.25, 'W'],
                  [0.5, 0, -0.5, 'S'],
                  [0,0,0,'\Gamma'],
                  [0.5, -0.5, 0, 'T'],
                  [0.75, -0.25, -0.25, 'W'],
                  [0,0,0,'\Gamma']]
            asc=2*np.pi/(a*c)*np.array([c, 0, a])
            bsc=2*np.pi/(b*c)*np.array([0, -c, b])
            csc=2*np.pi/(b*a)*np.array([b, -a, 0])
        #P
        else:
            #for P
            
            pts=[[0,0,0,'\Gamma'],
                  [0, 0, 0.5, 'Z'],
                  [-0.5, 0, 0.5, 'T'],
                  [-0.5, 0, 0, 'Y'],
                  [0,0,0,'\Gamma'],
                  [0, 0.5, 0, 'X'],
                  [0.5, 0.5, 0, 'S'],
                  [-0.5, 0.5, 0.5, 'R'],
                  [0, 0.5, 0.5, 'U']]
            asc=2*np.pi/(b)*np.array([0, -1, 0])
            bsc=2*np.pi/(a)*np.array([1,0, 0])
            csc=2*np.pi/(c)*np.array([0, 0, 1])
        
    #tetragonal
    elif spaceGroup<143:
        #assume a>c
        #I
        Itet=[79, 80, 82, 87, 88, 97, 98, 107, 108, 109, 110, 119, 120, 121, 122, 139, 140, 141, 142]
        if spaceGroup in Itet:
            pts=[[-0.5, 0.5, 0.5, 'Z'],
                  [0,0,0,'\Gamma'],
                  [0, 0, 0.5, 'X'],
                  [0.25, 0.25, 0.25, 'P'],
                  [0, 0.5, 0, 'N']]
            asc=2*np.pi/(c*a)*np.array([0, c, a])
            bsc=2*np.pi/(c*a)*np.array([c, 0, a])
            csc=2*np.pi/a*np.array([1,1,0])
        #P
        else:
            pts=[[0,0,0,'\Gamma'],
                  [0, 0.5, 0, 'X'],
                  [0.5, 0.5, 0, 'M'],
                  [0,0,0,'\Gamma'],
                  [0, 0, 0.5, 'Z'],
                  [0, 0.5, 0.5, 'R'],
                  [0.5, 0.5, 0.5, 'A'],
                  [0.5, 0.5, 0, 'M']]
            asc=2*np.pi/a*np.array([1, 0, 0])
            bsc=2*np.pi/b*np.array([0,1,0])
            csc=2*np.pi/c*np.array([0,0,1])
    #trigonal
    elif spaceGroup<168:
        pts=[[0,0,0,'\Gamma'],
              [-1/3, 2/3, 0.5, 'K'],
              [0, 0.5, 0, 'M'],
              [0,0,0,'\Gamma'],
              [0, 0, 0.5, 'A'],
              [0, 0.5, 0.5, 'L'],
              [-1/3, 2/3, 0.5, 'H'],
              [0, 0, 0.5, 'A']]
        if a==b:
            aS=a
            cS=c
        elif b==c:
            aS=b
            cS=a
        else:
            aS=a
            cS=b
        asc=2*np.pi/aS*np.array([1/np.sqrt(3), -1, 0])
        bsc=2*np.pi/aS*np.array([2/np.sqrt(3), 0, 0])
        csc=2*np.pi/cS*np.array([0,0,1])
    #hexagonal
    elif spaceGroup<195:
        pts=[[0,0,0,'\Gamma'],
              [-1/3, 2/3, 0.5, 'K'],
              [0, 0.5, 0, 'M'],
              [0,0,0,'\Gamma'],
              [0, 0, 0.5, 'A'],
              [0, 0.5, 0.5, 'L'],
              [-1/3, 2/3, 0.5, 'H'],
              [0, 0, 0.5, 'A']]
            #determine which is the odd angle out (c)
        if a==b:
            aS=a
            cS=c
        elif b==c:
            aS=b
            cS=a
        else:
            aS=a
            cS=b
        asc=2*np.pi/aS*np.array([1/np.sqrt(3), -1, 0])
        bsc=2*np.pi/aS*np.array([2/np.sqrt(3), 0, 0])
        csc=2*np.pi/cS*np.array([0,0,1])
    #cubic
    else:
        #F
        Fcub=[196, 202, 203, 209, 210, 216, 219, 225, 226, 227, 228]
        Icub=[197, 199, 204, 206, 211, 214, 217, 220, 229, 230]
        if spaceGroup in Fcub:
            pts=[[0.5, 0.5, 0.5, 'L'],
                  [0,0,0,'\Gamma'],
                  [0.5, 0, 0.5, 'X'],
                  [0.5, 0.25, 0.75, 'W'],
                  [0.5, 0.5, 0.5, 'L'],
                  [3/8, 3/8, 3/4, 'K'],
                  [0,0,0,'\Gamma']]
            asc=2*np.pi/a*np.array([-1, 1, 1])
            bsc=2*np.pi/a*np.array([1, -1, 1])
            csc=2*np.pi/a*np.array([1, 1, -1])
        #I
        elif spaceGroup in Icub:
            pts=[[0,0,0,'\Gamma'],
                  [0, 0, 0.5, 'N'],
                  [0.25, 0.25, 0.25, 'P'],
                  [0,0,0,'\Gamma'],
                  [0.5, -0.5, 0.5, 'H'],
                  [0, 0, 0.5, 'N']]
            asc=2*np.pi/a*np.array([0, 1, 1])
            bsc=2*np.pi/a*np.array([1, 0, 1])
            csc=2*np.pi/a*[1,1,0]
        #P
        else:
            pts=[[0,0,0,'\Gamma'],
                  [0.5, 0.5, 0, 'M'],
                  [0, 0.5, 0, 'X'],
                  [0,0,0,'\Gamma'],
                  [0.5, 0.5, 0.5, 'R']]
            asc=2*np.pi/a*np.array([1, 0, 0])
            bsc=2*np.pi/a*np.array([0,1,0])
            csc=2*np.pi/a*np.array([0,0,1])
    
    #monoclinic
    print(asc)
    print(bsc)
    print(csc)
    
    
    """
    Represent traditional representation in actual basis used
    """

    ptsArr=np.array(pts)[:, 0:3].astype(float)
    Mstandard=np.matrix([asc, bsc, csc]).transpose()
    Melk=np.matrix([astar, bstar, cstar]).transpose()
    newM=np.matmul(np.linalg.inv(Melk), Mstandard)
    newPts=copy.deepcopy(pts)

    for k in range(len(ptsArr)):
        newPtsV=newM.dot(ptsArr[k])[0]
        
        newPts[k][0]=newPtsV[0,0]
        newPts[k][1]=newPtsV[0, 1]
        newPts[k][2]=newPtsV[0, 2]
        
    return newPts