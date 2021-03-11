import threading

import signal

import sys

def timer_led():
    print('perid lighting led')
    global timer_hander
    timer_hander = threading.Timer(1, timer_led)
    timer_hander.start()

def handler(signum, frame):
    global is_exit
    is_exit = True
    timer_hander.cancel()
    print("receive a signal %d, is_exit = %d" % (signum, is_exit))
    sys.exit()

timer_led()


signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

while True:
  try:
    # 你想做的事情
    # import time
    # print ("start .............")
    # time.sleep(2)
    continue
  except:
      break
