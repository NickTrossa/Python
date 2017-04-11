import time

a = open("prueba","a")
for i in range(20):
    a.write(i)
    time.sleep(0.2)
a.close()
