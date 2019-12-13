from tkinter import *

root = Tk()

equal = ""
calc = StringVar()
calcLabel = StringVar()

def window(main):
    main.title("calc")
    main.update_idletasks()
    width = 340  
    height = 450
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}+{}+{}'.format(width,height,x,y))  
    
window(root)

def pressa(num):
    global equal
    equal = equal + str(num)
    equation = calc.set(equal)
    
def answer26():
    global equal
    
    try:
        ans = round(eval(equal),2)
        total = str(ans)
        calc.set(total)
        equal = ""
        
    except:
        if equal == "":
            calc.set("")
        else:    
          calc.set("MathOrPythonError")
          equal = ""
           
           
def answer09(event):
    global equal
    
    try:
        exp = calcLabel.get()
        total = str(eval(exp))
        calc.set(total)
        equal = ""
    except:
        if equal == "":
          calc.set("")
          equal = ""
        else:    
          calc.set("MathOrPythonError")
          equal = ""
           
def clear12():
    global equal
    equal = ""
    calc.set("")
    
def backspace():
    global equal
    equal = equal[:-1]
    calc.set(equal)
    
calcLabel = Entry(root, textvariable = calc, fg = 'blue', bd=20, font = 50, insertwidth = 1)
calcLabel.place(x=43,y=20)
calcLabel.bind("<Return>",answer09)

butt7 = Button(root, text = "7", fg = "red", padx = 16, pady = 16, bd = 8, command = lambda: pressa(7))
butt7.place(x=50,y=155)

butt8 = Button(root, text = "8", fg = "red",  padx = 16, pady = 16, bd = 8, command = lambda: pressa(8))
butt8.place(x=110,y=155)

butt9 = Button(root, text = "9", fg = "red",  padx = 16, pady = 16, bd = 8, command = lambda: pressa(9))    
butt9.place(x=170,y=155)
#
butt4 = Button(root, text = "4", fg = "red",  padx = 16, pady = 16, bd = 8, command = lambda: pressa(4))    
butt4.place(x=50,y=225)

butt5 = Button(root, text = "5", fg = "red", padx = 16, pady = 16, bd = 8, command = lambda: pressa(5))    
butt5.place(x=110,y=225)

butt6 = Button(root, text = "6", fg = "red", padx = 16, pady = 16, bd = 8, command = lambda: pressa(6))    
butt6.place(x=170,y=225)
#
butt1 = Button(root, text = "1", fg = "red", padx = 16, pady = 16, bd = 8, command = lambda: pressa(1))    
butt1.place(x=50,y=295)

butt2 = Button(root, text = "2", fg = "red", padx = 16, pady = 16, bd = 8, command = lambda: pressa(2))    
butt2.place(x=110,y=295)

butt3 = Button(root, text = "3", fg = "red", padx = 16, pady = 16, bd = 8, command = lambda: pressa(3))    
butt3.place(x=170,y=295)
#
butt0 = Button(root, text = "0", fg = "red", padx = 16, pady = 16, bd = 8, command = lambda: pressa(0))    
butt0.place(x=110,y=365)



butt001 = Button(root, text = "/", fg = "black", padx = 16, pady = 16, bd = 8, command = lambda: pressa("/"))
butt001.place(x=230,y=155)

butt002 = Button(root, text = "*", fg = "black", padx = 16, pady = 16, bd = 8, command = lambda: pressa("*"))
butt002.place(x=230,y=225)

butt003 = Button(root, text = "-", fg = "black", padx = 16, pady = 16, bd = 8, command = lambda: pressa("-"))
butt003.place(x=230,y=295)

butt004 = Button(root, text = "+", fg = "black", padx = 16, pady = 16, bd = 8, command = lambda: pressa("+"))
butt004.place(x=230,y=365)

butt005 = Button(root, text = "=", fg = "black", padx = 16, pady = 16, bd = 8, command = answer26)
butt005.place(x=170,y=365)

butt006 = Button(root, text = ".", fg = "black", padx = 16, pady = 16, bd = 8, command = lambda: pressa("."))
butt006.place(x=50,y=365)

butt007 = Button(root,text = "(", fg = "black", padx = 16, pady = 16, bd = 8, command = lambda: pressa("("))
butt007.place(x=177,y=85)

back = Button(root, text = "C", fg = "black", padx = 16, pady = 16, bd = 8, command = backspace)
back.place(x=48,y=85)

butt008 = Button(root,text = ")", fg = "black", padx = 16, pady = 16, bd = 8, command = lambda: pressa(")"))
butt008.place(x=235,y=85)

clear = Button(root, text = "CE", fg = "black", padx = 16, pady = 16, bd = 8, command = clear12)
clear.place(x=110,y=85) 

root.mainloop()

