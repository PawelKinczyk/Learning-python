import threading, time

# Simple multithreading

print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap) # add thread
threadObj.start()

print('End of program.')

# Passings arguments to the thread target

print('Cats', 'Dogs', 'Frogs', sep=' & ') # Idea

threadObj = threading.Thread(target=print, 
args=['Cats', 'Dogs', 'Frogs'],kwargs={'sep': ' & '})
threadObj.start()