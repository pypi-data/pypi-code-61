from argox.argo import Argo

argo = Argo("https://github.com/PUFF")
data = argo.fuzzer()
print(data)

