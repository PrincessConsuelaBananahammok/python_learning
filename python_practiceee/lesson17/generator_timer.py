import time

def do_something(counter):
    for _ in range(counter):
        print("Sending requests to server . . .")
        time.sleep(2)
        print("end of sending")
        yield "request was successful"

for result in do_something(5):
    print(result)
