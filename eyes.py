import time
import winsound
import ctypes

while True:
    time.sleep(20*60)
    winsound.PlaySound('sound.wav',winsound.SND_FILENAME)
    ctypes.windll.user32.MessageBoxW(0, "Time to see object at 20 feet away for 20 seconds ", "Eyes Rest Time", 1)
    time.sleep(20)
    winsound.PlaySound('sound.wav',winsound.SND_FILENAME)
	
