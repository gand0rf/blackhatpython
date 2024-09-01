import time 
import requests
import sys
import threading
import queue

THREADS = 10
with open('target','r') as f:
    TARGET = f.readline()
    TARGET = TARGET.strip('\n')

web_paths = queue.Queue()

def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = f"{TARGET}/{path}"
        time.sleep(2)
        r = requests.get(url)
        if r.status_code == 200:
            print(f"Found: {path}")

def run():
    mythreads = list()
    for i in range(THREADS):
        print(f'Spawing thread {i}')
        t = threading.Thread(target=test_remote)
        mythreads.append(t)
        t.start()

    for thread in mythreads:
        thread.join()

if __name__ == '__main__':
    with open("/home/gand0rf/git/blackhatpython/Chap05/wordpress.txt",'r') as f:
        wordlists = f.readlines()
    for word in wordlists:
        web_paths.put(word.strip('\n'))
    run()
        


