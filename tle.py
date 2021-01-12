import multiprocessing
import time

# Your foo function
def foo(n):
    while True:
        i=0
        i+=1
def p2():
    print ('Suprise Shawty')

if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    px = multiprocessing.Process(target=p2)
    p.start()
    px.start()
    x=p.join(5)

# If thread is active
    if p.is_alive():
        print ("foo is running... let's kill it...")

    # Terminate foo
        p.terminate()
        p.join()

