import Reader
import urx
import rhino3dm

rd = Reader.Reader("/home/ayoub/Desktop/testModel.adm")
mdl = rd.Load()

print (mdl.guid)

point = rhino3dm.Point3d(0, 0, 0)
