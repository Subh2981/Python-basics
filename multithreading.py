import threading as th
import time as t

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    t.sleep(seconds)
    
    
# func(4)
# func(2)
# func(1)

t1=th.Thread(target=func,args=[4])
t2=th.Thread(target=func,args=[3])
t3=th.Thread(target=func,args=[2])

t1.start()
t2.start()
t3.start()