import threading



def main():

    GLOBAL_COUNTER = 0

    def increment():
       nonlocal GLOBAL_COUNTER  
       GLOBAL_COUNTER  += 1
       print(GLOBAL_COUNTER)
        
    t1 = threading.Thread(target=increment, args=())
    t2 = threading.Thread(target=increment, args=())
    t3 = threading.Thread(target=increment, args=())

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

main()