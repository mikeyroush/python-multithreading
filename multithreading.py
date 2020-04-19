import concurrent.futures
import time

start = time.perf_counter()
temp = 0

def do_something():
    global temp
    time.sleep(1)
    temp += 1
    return temp
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')