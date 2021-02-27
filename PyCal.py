from tkinter import *
import datetime
import time


root= Tk()
root.title("Quick-Cal")
root.geometry("600x600")

# On Grid
"""label_1= Label(root, text="Name", padx=2, fg="grey")
label_2= Label(root, text="Password", padx=2, fg="grey")
entry_1= Entry(root, bg="grey") #Entry() in Tkinter is like 'input()'. We're tryna get a text frm the user
entry_2= Entry(root)

label_1.grid(row=0, sticky=S) #Sticky is a Grid parameter for alignment. 'E' for East(right), 'N' for North(up), 'S' for South(down), W for West(right)
label_2.grid(row=1, sticky=S)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c= Checkbutton(root, text="Keep Me Logged In")
c.grid(columnspan=2)"""


def iCalc(source, side):
    storeObj = Frame(source, borderwidth=2, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand= YES, fill=BOTH)
        self.master.title('Calculator')
        display= StringVar() # StringVar() is used for display. It shows us the result of calculations, say the cal's face
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg='powder blue').pack(side=TOP, expand=YES, fill=BOTH)

        # adding a 'clear' button widget
        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))

        # adding numbers and symbols
        for numButton in ("789/", "456*", "123-", ".0+"):
            FunctionNum= iCalc(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda storeObj= display, q=iEquals: storeObj.set(storeObj.get() + q))

        # Adding Equal Button
        EqualButton= iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals= button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals= button(EqualButton, LEFT, iEquals, lambda storeObj=display, s=' %s ' % iEquals: storeObj.set(storeObj.get() + s))

    # Applying Event trigger on widget
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

    # time and date
def yuri():

    ti= time.asctime()
    #ti = time.time()
    Fra= Frame(root, height=50, width=300)
    Fra.pack(fill=X, side=BOTTOM)
    Label(Fra, font=('courier', 24), text=ti, bg="gray").pack(fill=X, anchor=S)

yuri()







# Start the GUI
if __name__=='__main__':
    app().mainloop()



# root.mainloop()
