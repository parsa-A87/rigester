from tkinter import*
import messagebox
users=[]

def showmsg():

        root=Tk()
        root.configure(bg="#9EB384")
        root.geometry(("%dx%d+%d+%d")%(400,400,100,100))

        #def
        def sign_up(e):
            b=False
            for item in users:
                if item["user"]==txt_user.get():
                    messagebox.showinfo("","Tekrari!")
                    b=True
                    break
            if b==False:
                if txt_password.get()==txt_repassword.get():
                    dic={"user":txt_user.get(),"password":txt_password.get()}
                    users.append(dic)
                    print(users)
                else:
                    messagebox.showerror("","please check your password!")



        #txt
        txt_user=Entry(root,justify="center")
        txt_user.configure(width=24,bd=5)
        txt_user.place(x=80,y=50)
        txt_password=Entry(root,justify="center")
        txt_password.configure(width=24,bd=5)
        txt_password.place(x=80,y=100)
        txt_repassword=Entry(root,justify="center")
        txt_repassword.configure(width=24,bd=5)
        txt_repassword.place(x=80,y=150)
        #lbl
        lbl_users=Label(root,text="User name")
        lbl_users.configure(bg="#9EB384")
        lbl_users.place(x=15,y=50)
        lbl_password=Label(root,text="Password")
        lbl_password.configure(bg="#9EB384")
        lbl_password.place(x=20,y=100)
        lbl_repassword=Label(root,text="Repassword")
        lbl_repassword.configure(bg="#9EB384")
        lbl_repassword.place(x=10,y=150)
        lbl_title=Label(root,text=".به صفحه ورود خوش آمدید.")
        lbl_title.pack(side="top",fill=BOTH)
        lbl_title.configure(bg="#9EB384")
        #btn
        btn_login=Button(root,text="Signup",width=20)
        btn_login.bind("<Button-1>",sign_up)
        btn_login.place(x=80,y=210)
        root.mainloop()

