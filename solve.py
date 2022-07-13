import threading 


def main():

    my_data = None # bug to be fixed 

    def callback():
        assert not hasattr(my_data, 'x')
        my_data.x = 1
        print(my_data.x)
        
    t1 = threading.Thread(target=callback, args=())
    t2 = threading.Thread(target=callback, args=())
    t3 = threading.Thread(target=callback, args=())

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

main()