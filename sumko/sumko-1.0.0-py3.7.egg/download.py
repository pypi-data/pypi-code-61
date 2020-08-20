import threading


def hello():
    print('hello')


for i in range(3):
    t = threading.Thread(target=hello)
    print(t.name.split('-')[1])
