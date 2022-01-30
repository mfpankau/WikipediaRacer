from tkinter import * 

def getData():
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
input = Button(middleFrame,text="Exit")
input.pack(side=BOTTOM)
root.update()

root.mainloop()