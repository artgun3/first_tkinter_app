from tkinter import *
window = Tk()
window.title(" Моё первое GUI приложение")
window.geometry("300x250")

label = Label(text="Здравствуйте")
label.pack()
button = Button(text="|")
button.pack()
window.mainloop()