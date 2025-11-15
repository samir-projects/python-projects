import threading
while True:
    def helloworld():
        print('HelloWorld!')

    t1=threading.Thread(target=helloworld)
    t1.start()    