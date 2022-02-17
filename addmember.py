from contextlib import nullcontext
from turtle import clear
import pip._vendor.requests
from time import sleep
from pynput.keyboard import Key, Controller
from pynput import keyboard
import pip._vendor.requests

keyboardOut = Controller()

address = input("Enter Address:")
username = input("Enter Member's MC Username:")
response = pip._vendor.requests.get("https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress=0xB81Cf242671eDAE57754B1a061F62Af08B32926A&address=%s&tag=latest&apikey=FVT9I5ZQFFCRR151I9NNVF8BBP9BSAH1J4" % address)
plots = response.json()

dataV = []

''' PLOT LIST '''
if plots['status'] == '1':
    plotCount=0
    for plot in plots['result']:
        if plot['to'].upper() == address.upper():
            dataV.append(plot['tokenID'])
            plotCount += 1 
        else:
            dataV.remove
            plotCount -= 1

''' MENU OUTPUT '''
for token in dataV:
    print(token)

print("-- MENU --")
print("PRESS [5] WHEN YOU OPEN MINECRAFT TO ADD MEMBER")
print("PRESS [0] TO CANCEL")

''' KEY LISTENER '''
def on_press(key):
    try: k = key.char
    except: k = key.name
    if k == '0':
        # Cancel
        return False
    if k == '5':
        print("Adding %s to %i plots" % (username, plotCount))
        for token in dataV:
            keyboardOut.press('t')
            sleep(1);
            keyboardOut.type('/rg addmember -w "Critterz" %s %s\n' % (token, username))
        print("COMPLETED")
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()