import threading

def timer_led():
    print('perid lighting led')
    threading.Timer(1, timer_led).start()

timer_led()
