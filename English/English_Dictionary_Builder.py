 # -*- coding: utf-8 -*-
import sys  
from tkinter import *

import os.path


root = Tk()
root.tk.call('encoding', 'system', 'utf-8')

root.title("English_Dictonary_Builder")
isav=0
#sys.setdefaultencoding('utf-8')
sz=13


def isa():
  
  global isav
  if isav ==1:
    EP.configure(bg = "#c42727")
    isav=0
    return 0

  isav=1
  EP.configure(bg = "#50c427")

  



def add():
    global isav
    if len(e.get())==0 or len(f.get())==0:
     err=Tk()
     Label(err, text="Error Invallid Entry",font=(None, sz)).grid(row=0,column=0)
     Button(err, text='Ok',command=err.destroy,font=(None, sz)).grid(row=1,column=0)

     
     return 0
    
     
     if isav==0:
      err=Tk()
      Label(err, text="Word Already Exists\n",font=(None, sz)).grid(row=0,column=0)
      Button(err, text='Ok',command=err.destroy,font=(None, sz)).grid(row=1,column=0)
      return 0

    

  
   
    F = open(e.get(),'w') 
    F.write(f.get())
    f.delete(0,'end')
    e.delete(0,'end')
   

def read(x):
    f.delete(0,'end')
    T.delete('1.0', END)
    if len(e.get())==0:
     err.geometry('10x10+0+0') 
     err=Tk()
     Label(err, text="Error: Invalid Entry",font=(None, sz)).grid(row=0,column=0)
     Button(err, text='Ok',command=err.destroy,font=(None, sz)).grid(row=1,column=0)
     
     return 0
    if os.path.exists(e.get())==False:
           err=Tk()
           Label(err, text="Word Not In Dictionary",font=(None, sz)).grid(row=0,column=0)
           Button(err, text='Ok',command=err.destroy,font=(None, sz)).grid(row=1,column=0)

    F = open(e.get(),'r') 
    st=F.read()
    f.insert(0,st)
    T.insert(END, e.get()+": "+st+"\n")
    

def printall():
    F = open(e.get(),'r') 
    


def listall():
    ms=''
    T.delete('1.0', END)
    import glob, os
#    os.chdir("/home/himanshu/dm")
    for f in glob.glob("*"):
      if f=="h1.py":
        continue  
      if f=="final.txt":
        continue 
      print(f)
      ms=ms+f+' '

       
      
      
    w=ms.split()  
    w.sort()
    
    for word in w:
      print(word)
      F = open(word,'r')
      T.insert(END, word+": "+F.read()+"\n")
      G = open('final.txt','a')
      G.write(word+": "+F.read()+"\n")

Label(root, text="Word",font=(None, sz)).grid(row=1)
Label(root, text="Meaning",font=(None, sz)).grid(row=2)
e = Entry(root,font=(None, sz))
f = Entry(root,font=(None, sz))


e.grid(row=1, column=1)

f.grid(row=2, column=1)
status=Label(root, text="",font=(None, sz)).grid(row=1,column=2)






T = Text(root, height=20, width=30,font=(None, sz))
T.grid(row=4,column=1)
Label(root, text="English Dictionary Builder",font=(None, 15)).grid(row=0,column=1)


Button(root, text='Search',command=read,font=(None, sz)).grid(row=3,column=0)
Button(root, text='View All',command=listall,font=(None, sz)).grid(row=3,column=1)
Button(root, text='Save',command=add,font=(None, sz)).grid(row=3,column=2)
EP=Button(root, text='auth',command=isa,font=(None, sz))
EP.grid(row=5,column=1)
Label(root, text="(c) Himanshu Attri\nv 1.10",font=(None, 5)).grid(row=5,column=2)

#Radiobutton(root, text="One", command=en(1), value=1).grid(row=6,column=1)


#r=Tk()
#app = App(master = r)

mainloop()






