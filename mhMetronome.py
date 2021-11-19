import time
from winsound import Beep
import threading
import queue


q = queue.Queue()

def thread_function():
    while True:
        sound = q.get()
        if sound is None:
            break
        mesure(sound['upper'], sound['lower'], sound['bpm'], sound['repeat'])

def slide_tempo(origin, toward, mesure, upper, style = 'linear'):
    if origin > toward:
        gap = origin - toward
        bpm_change = gap / (mesure * upper)
        
        slide = []
        
        move = origin
        for i in range(mesure * upper):
            move -= bpm_change
            slide.append(move)
        
        return [60/tempo for tempo in slide]
        
    elif toward > origin:
        gap = toward - origin
        bpm_change = gap / (mesure * upper)
        
        slide = []
        
        move = origin
        for i in range(mesure * upper):
            move += bpm_change
            slide.append(move)
        
        return [60/tempo for tempo in slide]
    
    else:
        return None
    
def mesure(upper = 4, lower = 4, bpm = 120, repeat = 4, duration = None, slide = None):
    if not duration:
        note = bpm * (lower/4)
        duration = (60 / note)
        
    if not slide:
        for i in range(repeat):
            for j in range(upper):
                if j == 0:
                    Beep(466,100)
                    time.sleep(duration - 0.1)
                else:
                    Beep(415,100)
                    time.sleep(duration - 0.1)
    
if __name__ == "__main__":
    a = {'upper': 3, 'lower': 4, 'bpm': 135, 'repeat': 2}
    b = {'upper': 6, 'lower': 8, 'bpm': 120, 'repeat': 1}
    c = {'upper': 9, 'lower': 8, 'bpm': 120, 'repeat': 1}
    d = {'upper': 5, 'lower': 4, 'bpm': 150, 'repeat': 2}
    
    t = threading.Thread(target=thread_function)
    t.start()
    
    q.put(a)
    q.put(b)
    q.put(c)
    q.put(d)
    q.put(None)