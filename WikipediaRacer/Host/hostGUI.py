from tkinter import *
import requests
import json

def getIP():
    r = requests.get('https://ip.seeip.org/jsonip?')
    ipLabel.config(text='Your ip is: ' + str(r.json()['ip']))


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




#funny setup
root = Tk()
root.geometry('400x300')
root.title('Wikipedia Race Host')

#frames
topFrame = Frame(root)
topFrame.pack(side=TOP)
middleFrame = Frame(root)
middleFrame.pack(side=TOP)

#elements
ipLabel = Label(middleFrame, text='Your ip is: ')
getIP()
postEntry = EntryWithPlaceholder(middleFrame, placeholder='Port')
ipLabel.pack()
postEntry.pack()


root.mainloop()
