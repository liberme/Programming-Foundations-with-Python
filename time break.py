import time
import webbrowser

break_times = 3
break_counter = 0

while break_times > break_counter:
    time.sleep(5)
    webbrowser.open('https://www.youtube.com/watch?v=qX2GsMj7154')
    break_counter = break_counter + 1
