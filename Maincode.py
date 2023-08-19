from tkinter import *
import string
import random

window = Tk()
window.title("PASSWORD GENERATOR")
window.geometry("450x350")
window.resizable(0,0)
window.config(bg="light blue")

def reset():
  length_field.delete(0,END)
  pwd_field.delete(0, END)
  length_field.focus_set()

def clear_all() :
  user_field.delete(0, END) 
  length_field.delete(0,END)
  pwd_field.delete(0, END)
  user_field.focus_set()

def calculate_pw():
  username = str(user_field.get())
  plength = int(length_field.get())

  charaters = list(string.printable)
  for i in range(16):
    charaters.pop()
  charaters.remove('"')
  charaters.remove(',')
  charaters.remove('.')
  charaters.remove(';')
  charaters.remove(':')
  charaters.remove("'")
  charaters.remove('(')
  charaters.remove(')')
  charaters.remove('>')
  charaters.remove('<')
  charaters.remove('=')
  charaters.remove('/')
  charaters.remove('+')
  charaters.remove('-')
  charaters.remove('*')
  
  password=[]
  def generatepwd(length):
    for i in range(length):
      a=random.choice(charaters)
      password.append(a)
    return password
     
  password = generatepwd(plength)
  generatedpassword=""
  for i in password:
    generatedpassword += i
  PW = generatedpassword
  pwd_field.insert(10,PW)

if _name_ == "_main_" :
  label=Label(window,text="Password Generator",fg='blue',bg="light blue",font=("Arial", 15, "normal", "italic"))
  label1 = Label(window, text = "Enter user name : ",fg = 'black',bg="light blue",font=("Arial", 15, "normal", "italic"))
  label2 = Label(window, text = "Enter password length : ",fg = 'black',bg="light blue",font=("Arial", 15, "normal", "italic"))
  label3 = Label(window, text = "Generated password : ",fg = 'black',bg="light blue",font=("Arial", 15, "normal", "italic"))

  label.grid(row=1,column=0,padx=10,pady=10)
  label1.grid(row = 2, column = 0, padx = 10, pady = 10) 
  label2.grid(row = 3, column = 0, padx = 10, pady = 10) 
  label3.grid(row = 4, column = 0, padx = 10, pady = 10)
  
  user_field = Entry(window,font=20) 
  length_field = Entry(window,font=20) 
  pwd_field = Entry(window,font=20)
  
  user_field.grid(row = 2, column = 1, padx = 10, pady = 10) 
  length_field.grid(row = 3, column = 1, padx = 10, pady = 10) 
  pwd_field.grid(row = 4, column = 1, padx = 10, pady = 10)
  
  button1 = Button(window, text = "GENERATE PASSWORD", bg = "blue", fg = "white",font=20, command = calculate_pw)
  button2 = Button(window, text = "Clear",bg = "beige", fg = "blue",font=20, command = clear_all)
  button3 = Button(window, text = "Reset",bg = "beige", fg = "blue",font=20, command = reset)
     
  button1.grid(row = 5, column = 1, pady = 10)
  button2.grid(row = 8, column = 1, pady = 10)
  button3.grid(row = 7, column = 1, pady = 10) 
  
window.mainloop()
