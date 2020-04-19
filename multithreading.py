import concurrent.futures
import time

start = time.perf_counter()
temp = 0

def do_something():
    global temp
    time.sleep(1)
    temp += 1
    return temp

# results = [do_something() for _ in range(10)]  # takes 10 seconds
# for num in results:
#     print(num)

with concurrent.futures.ThreadPoolExecutor() as executor: #takes 1 second
    results = [executor.submit(do_something) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')