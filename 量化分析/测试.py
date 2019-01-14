from concurrent.futures import ThreadPoolExecutor


def fun1(i):
    print(i)


with ThreadPoolExecutor(16) as executor:
    for i in range(3000000):
        executor.submit(fun1,i)

