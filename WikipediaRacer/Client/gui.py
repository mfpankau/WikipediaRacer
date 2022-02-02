from tkinter import *
import requests
from os import system
import threading
from time import sleep
from PIL import Image, ImageTk

serverUp = False    #is hosting client server
connected = False   #is connected to host server

ip = ''
username = ''

#runs on seperate thread to start client server
def server(): 
    global serverUp
    serverUp = True
    system('py clientServer.py')

#send player name and host ip to client server
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

#update log label with funny text
def updateLog(str):
    global logText
    logText.config(text=str)
    print('weed updateLog')

#start client server
def startServer():
    global ip, username, serverUp
    if not serverUp:
        x = threading.Thread(target=server, daemon=True)
        x.start()
    sleep(1)
    ip = hostEntry.get()
    username = nameEntry.get()
    attemptConnect(0)
    if connected: updateLog(f'Connected to {ip}\nName set to {username}\n')

#mhm... idk starts host or smthn
def startHost():
    pass

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
root.title('Wikipedia Racer')
#making frames
topFrame = Frame(root,width=400)
topFrame.pack(side=TOP)
middleFrame = Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(pady=10)

#making elements
logo = Image.open('wikiRaceIcon.jpg')
logo = logo.resize((80, 100))
logo = ImageTk.PhotoImage(logo) 
funnyLogo = Label(topFrame, image=logo)
funnyLogo.pack(pady=5)
root.iconphoto(True, PhotoImage(file='wikiLogo.png')) 
funnyLabel = Label(topFrame, text='Wikipedia Racer', font=14)
funnyLabel.pack(pady=10)
nameEntry = EntryWithPlaceholder(middleFrame, placeholder='Username')
nameEntry.pack()
hostEntry = EntryWithPlaceholder(middleFrame, placeholder='Host')
hostEntry.pack()
connectButton = Button(middleFrame,text="Connect", command=startServer, relief='groove')
connectButton.pack(side=LEFT, pady=10)
hostButton = Button(middleFrame, text='Host Lobby', command=startHost, relief='groove')
hostButton.pack(side=LEFT, pady=10)
logText = Label(bottomFrame, text='')
logText.pack(side=TOP, pady=7)
root.update()

root.mainloop()