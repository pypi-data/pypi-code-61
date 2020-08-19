from argox.argo import Argo

argo = Argo("httos://github.com")
data = argo.scanport("127.0.0.1")
print(data)

