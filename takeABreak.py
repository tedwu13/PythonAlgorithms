import webbrowser
import time

total_breaks = 5
break_count = 0
#time sleeps for five seconds

while break_count < total_breaks:
    time.sleep(4)
    webbrowser.open("https://www.youtube.com/watch?v=VPRjCeoBqrI")
    break_count += 1

