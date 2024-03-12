#shit why this not working
import debugger, pyautogui, time

debugger.info('version check will be added.')
debugger.sinput('Select your message. (%d is not working)')
msg = input(">>> ")
has = "%d" in msg
ran=0
debugger.wait("Starting in 5 second", 5)
write=""
def seta():
    global write, msg, ran
    if has:
        write = str(msg % int(ran))
    else:
        write = str(msg)
while True:
    seta()
    for i in range(0, 6):
        pyautogui.write(" " * i+write+f"{ran}%\n")
        time.sleep(0.5)
        ran += 1
        seta()
    for i in range(5, 0, -1):
        pyautogui.write(" " * i+write+f"{ran}%\n")
        time.sleep(0.5)
        ran += 1
        seta()
    
