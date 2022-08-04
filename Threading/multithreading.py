import threading
import time

def hello_from_thread():
    time.sleep(20)
    print(f'hello from thread {threading.current_thread()}')

print(f'Current thread is {threading.current_thread().name}')

for _ in range(1000):
    new_thread = threading.Thread(target=hello_from_thread, daemon=False)
    new_thread.start()
    
    # join will cause program to pause until the thread
    # we started completes
    # new_thread.join()
    
print(f'total active threads: {threading.active_count()}')
    



