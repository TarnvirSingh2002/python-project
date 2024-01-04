from threading import Thread
class a(Thread):
    def run(self):
        for i in range(3):
            print("kk")
class b(Thread):
    def run(self):
        for i in range(3):
            print("kotlin")
t1=a()
t2=b()
t1.start()
t2.start()
t1.join()
t2.join()
print("end")
