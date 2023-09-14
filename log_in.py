import os
from tkinter import*
import messagebox
import sign_up
from tkinter import ttk
root=Tk()
root.configure(bg="#9EB384")
root.geometry(("%dx%d+%d+%d")%(400,400,100,100))
#def
def sign_up1(e):

    sign_up.showmsg()
def onclicklogin(e):
    result=login()

    if result:
         os.system(f"python register.py")
    else:
        messagebox.showwarning("warning","خظایی رخ داده است!")

def login():
    for item in sign_up.users:
        if item["user"]==txt_users.get() and item["password"]==txt_password.get():
            return True
    return False

#txt
txt_users=Entry(root,justify="center")
txt_users.configure(width=24,bd=5)
txt_users.place(x=80,y=50)
txt_password=Entry(root,justify="center")
txt_password.configure(width=24,bd=5)
txt_password.place(x=80,y=100)
#lbl
lbl_users=Label(root,text="User name")
lbl_users.configure(bg="#9EB384")
lbl_users.place(x=15,y=50)
lbl_password=Label(root,text="Password")
lbl_password.configure(bg="#9EB384")
lbl_password.place(x=20,y=100)
lbl_title=Label(root,text=".به صفحه ورود خوش آمدید.")
lbl_title.pack(side="top",fill=BOTH)
lbl_title.configure(bg="#9EB384")
#btn
btn_login=Button(root,text="Login",width=20)
btn_login.bind("<Button-1>",onclicklogin)
btn_login.place(x=80,y=170)
#lbllink
lbl_link=ttk.Label(root,text="Click for signup",width=16,font=20)
lbl_link.bind("<Button-1>",sign_up1)
lbl_link.place(x=80,y=200)
root.mainloop()
