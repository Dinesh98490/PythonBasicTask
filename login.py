from tkinter import*
def login():
    username = 'Dinesh'
    password = 'Dinesh1234'
    if username == 'Dinesh' and password == 'Dinesh1234':
        print('Hello')
        d.config(text='Hello')
    else:
        print('Invalid password and username')

dk=Tk()
global entry1 
global entry2
dk.title('Login')
dk.geometry('400x300')
dk.resizable(1,1)
a=Label(dk,text='Signup')
a.place(x=90, y=100)
a=Label(dk, text='Username')
a.place(x=0, y=10)
b=Label(dk,text='Password')
b.place(x=0, y=40)
d=Label(dk,text="dinesh")
d.place(x=0,y=100)
entry1 = Entry(dk,bd=1)
entry1.place(x=80,y=10)
entry2 = Entry(dk, bd=1)
entry2.place(x=80, y=40)
Button(dk, text='login', command=login,  height=1, width= 10, bd=1).place(x=80, y=100)
dk.mainloop()




from tkinter import*
from tkinter import messagebox 
def login():
    username = entry1.get()
    password = entry2.get()
    if username == 'Dinesh' and password == 'password':
        print('sucess login')
        # messagebox.showinfo('', 'Login Sucess')
        dk.destroy()
        
    elif username == '' and password == '':
        messagebox.showinfo('','Blank not allowed')
    else:
        messagebox.showinfo('', 'Incorrect password and username')
dk = Tk()
global entry1
global entry2
dk.title('Login')
dk.geometry('1200x1500')
dk.config(bg='blue')
facebook = Label(dk,text='Facebook', font=1000)
facebook.pack()
dk.resizable(1,1)
a=Label(dk, text='username', fg='red')
entry1=Entry(dk)
a.pack()
a.place(x=200, y=206)
a=Label(dk, text='password', fg='red')
a.place(x=212, y=306)
entry1 = Entry(dk, bd=3)
entry1.insert(0,"username")
entry1.place(x=300, y=200)
entry2 = Entry(dk, bd=3)
entry2.insert(0,'****')
entry2.bind('<FocusIn>', login)
entry2.place(x=300, y=300)

Button(dk, text='Login',command = login,  height= 2, width= 13, bd=4).place(x=300, y=400)


dk.mainloop()

from tkinter import*
root = Tk()
root.title('tk')
root.geometry('400x400')
#creating a button widget
redbutton = Button(root,text='LEFT', fg='green')

#shoving it onto the screen
redbutton.pack(side = LEFT)

greenbutton =Button(root, text= 'RIGHT', fg='black')
greenbutton.pack(side=RIGHT)

bluebutton=Button(root, text='TOP', fg='blue')
bluebutton.pack(side=TOP)

bluebutton = Button(root, text='BOTTOM', fg='black')
bluebutton.pack(side=BOTTOM)
root.mainloop()


name = Label(root, text='Name').grid(row=0, column=0)
e1=Entry(root).grid(row=0, column=1)

password=Label(root,text='Password').grid(row=1, column=0)
e2=Entry(root).grid(row=1, column=1)

submit=Button(root, text='Submit').grid(row=4, column=1)
root.mainloop()
 
from tkinter import*
top = Tk()
top.geometry('400x250')
name = Label(top, text='Name').place(x=30, y=50)
Address=Label(top,text='Address').place(x=40, y=80)
contact= Label(top, text='Contact').place(x=30, y=130)
e1= Entry(top).place(x=80, y=50)
e1.insert(0, 'Name')
e2=Entry(top).place(x=80, y=90)
e2.insert(0,'Address')
e3=Entry(top).place(x=95, y=130)
e3.insert(0,'Contact')
top.mainloop()


from tkinter import*
from tkinter import messagebox
window = Tk()
window.maxsize(width=300, height=300)
window.minsize(width=300, height=300)
def func():
    print('Button is clicked')
    
btn=Button(window, text='Login', command=func)
btn.pack(side='top')
window.mainloop()



from tkinter import*
window =Tk()
def myclick():
    mylabel=Label(window, text='Look!, i clicked a button', fg='red', bg='#000099', font=50)
    mylabel.pack()
button1 = Button(window, text='click me', padx=20, pady=20, command = myclick, fg='red', bg='blue')
button1.pack()
window.mainloop()


from tkinter import*
root=Tk()
root.title('Login')
mybutton=Button(root, text= 'Click me')
mybutton.pack()

mybutton=Button(root, text='click me', padx=50, state = DISABLED)
mybutton.pack()

root.mainloop()

from tkinter import*
window = Tk()
e=Entry(window, width=50, bg='blue', fg='white', borderwidth=5, font= 20)
e.pack()

def myclick():
    mylabel=Label(window, text='Hello' + e.get())
    mylabel.config(text=e)
    mylabel.pack()
    
btn=Button(window, text= 'Click me', padx=10, pady=10, command=myclick)
btn.pack()
window.mainloop()

from tkinter import*
from tkinter import messagebox
def myclick():
    username=entry1.get()
    if username=='':
        print('login')
        messagebox.showinfo(entry1.get())
    # else:
    #     print('hello')
        
    
window=Tk()
window.title('Login')
window.geometry('400x400')
window.resizable(0,0)
a=Label(window, text='Username')
a.pack()
entry1=Entry(window, bd=2)
entry1.pack()
btn=Button(window, text='login', padx=10, pady=10,command=myclick)
btn.pack()
window.mainloop()


from tkinter import*
root=Tk()
root.title('GUI')
root.maxsize(width=600, height=300)
root.minsize(width=600, height=300)

def add():
    x=ent.get()
    print(x)
    mylabell.config(text=x, bg='green')
    
mylabell=Label(root, text='User name', fg='red', bg='yellow')
mylabell.place(x=40, y=120)

mylabell=Label(root, text='nothing', fg='red', bg='yellow')
mylabell.place(x=40, y=120)

var=StringVar()
ent=Entry(root, bg='black', fg='white', textvariable=var)
ent.place(x=80, y=120)


btn=Button(root, text='Submit', bg='green', fg='white', command=add)
btn.place(x=20,y=80)



root.mainloop()



from tkinter import*
root=Tk()

def click():
    text1='Address :'+ mytext.get('1.0', END)
    lbl.config(text=str(text1))
    
mytext=Text(root, font=20, width=20, height=10)
mytext.place(x=0, y=50)

btn=Button(root, text='Click Me', font=30, command = click)
btn.place(x=400, y=300)

lbl=Label(root, text='', font=30)
lbl.place(x=200, y=300)

root.mainloop()



from tkinter import*
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()
    if username == 'Dinesh' and password == 'password':
        print('Login')
        messagebox.showinfo('Sucessfully login', 'Sucessfully login')
        root.destroy()
    elif username == '' and password == '':
        messagebox.showinfo('', 'Blank not allowed')
        
    else:
        messagebox.showinfo('', 'Sorry username and password are wrong')
        
root = Tk()
root.title('Login')
root.geometry('400x300')
root.resizable(0,0)
global entry1
global entry2
root.config(bg='white')
a=Label(root,text='Username', fg='white', font=60).pack()
entry1 =Entry(root,  bd=4).pack()
a=Label(root,text='Password', fg='white', font=60).pack() 
entry2 =Entry(root, bd=4).pack()
btn=Button(root, text='Login', command = login, height=1, width= 1 ).place(x=180, y=120)




root.mainloop()


    


