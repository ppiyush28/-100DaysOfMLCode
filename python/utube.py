import webbrowser
import time
everyhours=12
breakcount=0
#webbrowser.open('https://www.youtube.com/watch?v=nwFdD4iFdvo')
print(time.ctime())
while (breakcount < everyhours):
    time.sleep(60)
    webbrowser.open('https://www.youtube.com/watch?v=nwFdD4iFdvo')
    breakcount+=1
