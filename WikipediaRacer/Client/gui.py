from tkinter import *
import requests
from os import system
import threading
from time import sleep

serverUp = False
connected = False

ip = ''
username = ''

def server():
    global serverUp
    f = open('test.txt', 'a')
    f.write('weed')
    f.close()
    serverUp = True
    system('py clientServer.py')


def attemptConnect(num):
    global connected
    if(num > 5):
        return 'didnt work'
    r = requests.post('http://127.0.0.1:5000/setHostIP', params={'ip':ip})
    if(r.status_code == 200):
        r = requests.post('http://127.0.0.1:5000/playerName', params={'player':username})
        if(r.status_code == 200):
            connected = True
    else: attemptConnect(num + 1)


def startServer():
    global ip, username, serverUp
    if not serverUp:
        x = threading.Thread(target=server, daemon=True)
        x.start()
    sleep(1)
    ip = hostEntry.get()
    username = nameEntry.get()
    
    attemptConnect(0)



#not my code, but I changed it a bit :D
class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

root = Tk()
root.geometry('400x300')
#making frames
topFrame = Frame(root,width=400, height=100)
topFrame.pack(side=TOP)
middleFrame = Frame(root)
middleFrame.pack()

#making elements
funnyLabel = Label(topFrame, text='Wikipedia Racer', font=14)
funnyLabel.pack(pady=10)
nameEntry = EntryWithPlaceholder(middleFrame, placeholder='Username')
nameEntry.pack()
hostEntry = EntryWithPlaceholder(middleFrame, placeholder='Host')
hostEntry.pack()
input = Button(middleFrame,text="Connect", command=startServer)
input.pack(side=BOTTOM)
root.update()

root.mainloop()