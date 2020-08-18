import csv
from tabulate import tabulate
import sys



def MBTCU(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S):
    
    FT60=[0,1.155,1.080,1.00,0.913,0.816,0.707,0.577,0.408,0,0,0,0]
    FT75=[0,1.106,1.054,1.00,0.943,0.882,0.816,0.745,0.667,0.577,0.471,0.333,0]
    FT90=[0,1.080,1.041,1.00,0.957,0.913,0.866,0.816,0.764,0.707,0.645,0.577,0.5]
    SITM=[0,15,20,25,30,35,40,45,50,60,70,80,90,100,110,125,150,175,200,225,250,300,350,400,450,500,600,700,800,1000,1200,1600,2000,2500,3000,4000,5000,6000]

    
    if Type==1:
        #Conductores en ducto de PVC
        db=['0','db20cu01.csv','db25cu01.csv','db30cu01.csv','db35cu01.csv','db40cu01.csv','db45cu01.csv','db50cu01.csv','db55cu01.csv','db60cu01.csv','db65cu01.csv','db70cu01.csv','db75cu01.csv']
    elif Type==2:
         #Conductores en ducto de Alumunio
        db=['0','db20cu02.csv','db25cu02.csv','db30cu02.csv','db35cu02.csv','db40cu02.csv','db45cu02.csv','db50cu02.csv','db55cu02.csv','db60cu02.csv','db65cu02.csv','db70cu02.csv','db75cu02.csv']
    elif Type==3:
         #Conductores en ducto de Acero
        db=['0','db20cu03.csv','db25cu03.csv','db30cu03.csv','db35cu03.csv','db40cu03.csv','db45cu03.csv','db50cu03.csv','db55cu03.csv','db60cu03.csv','db65cu03.csv','db70cu03.csv','db75cu03.csv']
        
    try:
        bd=sys.path[6]
        with open(bd+'\PyEWS\\db\\'+db[Ta]) as file:
            reader = csv.reader(file)
            datos = []
            for row in reader:
                #print(row)
                datos.append(row)
    except IndexError:
        bd=sys.path[5]
        with open(bd+'\PyEWS\\db\\'+db[Ta]) as file:
            reader = csv.reader(file)
            datos = []
            for row in reader:
                #print(row)
                datos.append(row)
    #print(tabulate(datos))

    In=In/Nc

    LIn=L*In

    for i in range(len(datos)):

        if S==1:
            
            D1=LIn/(float(datos[i][1])*VF)
            datos[i].append(round(D1,3))
        
            D2=LIn/(float(datos[i][2])*VF)
            datos[i].append(round(D2,3))

            D3=LIn/(float(datos[i][3])*VL)
            datos[i].append(round(D3,3))

            D4=LIn/(float(datos[i][4])*VL)
            datos[i].append(round(D4,3))
            
            datos[i].append(Nc)
            datos[i].append(round(In,2))
            
            datos[i].append(round(float(datos[i][5]),3)*FA*float(FT60[Ta]))
            datos[i].append(round(float(datos[i][6]),3)*FA*float(FT75[Ta]))
            datos[i].append(round(float(datos[i][7]),3)*FA*float(FT90[Ta]))
            
            if Vd > D1:
                
                if (round(float(datos[i][5]),3)*FA*float(FT60[Ta])>In or round(float(datos[i][5]),3)*FA*float(FT75[Ta])>In or round(float(datos[i][5]),3)*FA*float(FT90[Ta])>In):
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
                    
            else:
                datos[i].append('Not')
                
            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
                    
                    
            
        elif S==2:
            
            D1=LIn/(float(datos[i][1])*VF)
            datos[i].append(round(D1,3))

            D2=LIn/(float(datos[i][2])*VF)
            datos[i].append(round(D2,3))

            D3=LIn/(float(datos[i][3])*VL)
            datos[i].append(round(D3,3))

            D4=LIn/(float(datos[i][4])*VL)
            datos[i].append(round(D4,3))

            datos[i].append(Nc)
            datos[i].append(round(In,2))
            
            datos[i].append(round(float(datos[i][5]),3)*FA*float(FT60[Ta]))
            datos[i].append(round(float(datos[i][6]),3)*FA*float(FT75[Ta]))
            datos[i].append(round(float(datos[i][7]),3)*FA*float(FT90[Ta]))

            if Vd > D2:
                
                if (round(float(datos[i][5]),3)*FA*float(FT60[Ta])>In or round(float(datos[i][5]),3)*FA*float(FT75[Ta])>In or round(float(datos[i][5]),3)*FA*float(FT90[Ta])>In):
                    
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
            else:
                datos[i].append('Not')
            
            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
                     

                    
        
        elif S==3:
            
            D1=LIn/(float(datos[i][1])*VF)
            datos[i].append(round(D1,3))

            D2=LIn/(float(datos[i][2])*VF)
            datos[i].append(round(D2,3))

            D3=LIn/(float(datos[i][3])*VL)
            datos[i].append(round(D3,3))

            D4=LIn/(float(datos[i][4])*VL)
            datos[i].append(round(D4,3))

            datos[i].append(Nc)
            datos[i].append(round(In,2))
            
            datos[i].append(round(float(datos[i][5]),3)*FA*float(FT60[Ta]))
            datos[i].append(round(float(datos[i][6]),3)*FA*float(FT75[Ta]))
            datos[i].append(round(float(datos[i][7]),3)*FA*float(FT90[Ta]))
            
            if Vd > D3:
                
                if (round(float(datos[i][5]),3)*FA*float(FT60[Ta])>In or round(float(datos[i][5]),3)*FA*float(FT75[Ta])>In or round(float(datos[i][5]),3)*FA*float(FT90[Ta])>In):
                    
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
                    
            else:
                datos[i].append('Not')

            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
                                    
        
        elif S==4:
            
            D1=LIn/(float(datos[i][1])*VF)
            datos[i].append(round(D1,3))

            D2=LIn/(float(datos[i][2])*VF)
            datos[i].append(round(D2,3))

            D3=LIn/(float(datos[i][3])*VL)
            datos[i].append(round(D3,3))

            D4=LIn/(float(datos[i][4])*VL)
            datos[i].append(round(D4,3))

            datos[i].append(Nc)
            datos[i].append(round(In,2))
            
            datos[i].append(round(float(datos[i][5]),3)*FA*float(FT60[Ta]))
            datos[i].append(round(float(datos[i][6]),3)*FA*float(FT75[Ta]))
            datos[i].append(round(float(datos[i][7]),3)*FA*float(FT90[Ta]))
            
            if Vd > D4:
                
                if (round(float(datos[i][5]),3)*FA*float(FT60[Ta])>In or round(float(datos[i][5]),3)*FA*float(FT75[Ta])>In or round(float(datos[i][5]),3)*FA*float(FT90[Ta])>In):
                    
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
            else:
                datos[i].append('Not')
                    
            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
                                        
    print(tabulate(datos, headers=["AWG/KCM","1F/2H", "2F/3H","3F/3H","3F/4H", "60", "75", "90","%Vd/1F", "%Vd/2F","%Vd/3F","%Vd/3F","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))

