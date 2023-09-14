import os
from tkinter import *
from tkinter import ttk
import messagebox
root = Tk()
root.iconbitmap()
root.title("Register")
root.configure(bg="#9EB384")
root.geometry(("%dx%d+%d+%d")%(500,300,400,200))

users=[]
#def

def onclickregister(e):
    try:
        if btn_register.cget("state")==NORMAL:
            dic = {"name": txt_name.get(), "family": txt_family.get(), "age": int(txt_age.get()), "gender": txt_gender.get()}
            if exist(dic)==False:
                register(dic)
                insert(dic)
                cleartxt()
                messagebox.showinfo("Register","با موفقیت انجام شد")
            else:messagebox.showwarning("تکراری","فرد تکراری میباشد")
    except:
        messagebox.showwarning("Warning","خطایی رخ داده است!")
def register(value):
    users.append(value)
def insert(value):
    tbl.insert('',"end",values=[value["name"],value["family"],str(value["age"]),value["gender"]])
def cleartxt():
    txt_name.focus_set()
    txtnamevar.set("")
    txtfamilyvar.set("")
    txtagevar.set("")

def activebtn(e):
    if txt_name.get()==(""):
        btn_register.configure(state=DISABLED)
    else:
        btn_register.configure(state=NORMAL)
def getselection(e):
    selection=tbl.selection()
    if selection!=():
        s=tbl.item(selection)["values"]
        txtnamevar.set(s[0])
        txtfamilyvar.set(s[1])
        txtagevar.set(s[2])

def onclicksearch(e):
    a1=txt_search.get()
    result=search(a1)
    clear()
    for item in result:
        insert(item)


def search(value):
    resultlis = []
    for item in users:
        if item["name"] == txt_search.get() or item["family"] == txt_search.get() or str(item["age"]) == txt_search.get() or item["gender"] == txt_gender.get():
            resultlis.append(item)

    return resultlis
def clear():
    for item in tbl.get_children():
        sel = str(item,)
        tbl.delete(sel)
def load_and_clear(value):
    for item in tbl.get_children():
        sel = str(item, )
        tbl.delete(sel)
    for item in value:
        tbl.insert('', "end", values=[value["name"], value["family"], str(value["age"]),value["gender"]])
def exist(value):
    for item in users:
        if item["name"]==value["name"] and item["family"]==value["family"] and item["age"]==value["age"] and item["gender"]==value["gender"]:
            return True
    return False
def onclickdelete(e):
    os.system(f"python msj.py")
    dialog= messagebox.askyesno("Delete warning","آیا برای پاک کردن اظمینان دارید؟")
    if dialog==True:
        dic={"name":txt_name.get(),"family":txt_family.get(),"age":int(txt_age.get()),"gender":txt_gender.get()}
        delete(dic)
        remove_tbl()
        cleartxt()

def delete(value):
    for item in users:
        if item["name"] == value["name"]  and item["family"] == value["family"]  and item["age"] == value["age"]  and item["gender"] == value["Gender"]:
            users.remove(value)
def remove_tbl():
    selection = tbl.selection()
    if selection != ():
        tbl.delete(selection)

txtnamevar=StringVar()
txtfamilyvar=StringVar()
txtagevar=StringVar()
txtsearchvar=StringVar()
txtgendervar=StringVar()

#txt
txt_name=Entry(root,justify="center",textvariable=txtnamevar)
txt_name.configure(bd=5)
txt_name.bind("<KeyRelease>",activebtn)
txt_name.place(x=80,y=45)
txt_family=Entry(root,justify="center",textvariable=txtfamilyvar)
txt_family.configure(bd=5)
txt_family.place(x=80,y=90)
txt_age=Entry(root,justify="center",textvariable=txtagevar)
txt_age.configure(bd=5)
txt_age.place(x=80,y=130)
txt_search=Entry(root,justify="center",textvariable=txtsearchvar)
txt_search.configure(bd=5)
txt_search.place(x=310,y=10)
txt_gender=Entry(root,justify="center",textvariable=txtgendervar)
txt_search.place(x=310,y=10)

#lbl
lbl_name=Label(root,text="Name")
lbl_name.place(x=40,y=50)
lbl_family=Label(root,text="Family")
lbl_family.place(x=37,y=90)
lbl_age=Label(root,text="Age")
lbl_age.place(x=50,y=130)
lbl_search=Label(root,text="Search")
lbl_search.configure(width=7)
lbl_search.place(x=250,y=10)
#btn
btn_register=Button(root,text="Register")
btn_register.configure(state=DISABLED)
btn_register.configure(width=16,height=1,font=30)
btn_register.bind("<Button-1>",onclickregister)
btn_register.place(x=50,y=175)
btn_search=Button(root,text="Search")
btn_search.bind("<Button-1>",onclicksearch)
btn_search.configure(width=7)
btn_search.place(x=250,y=10)
btn_delete=Button(root,text="Delete")
btn_delete.bind("<Button-1>",onclickdelete)
btn_delete.configure(width=16,height=1,font=30)
btn_delete.place(x=50,y=230)
#tbl
column=("c1","c2","c3","c4")
tbl=ttk.Treeview(root,column=column,show="headings")
tbl.heading(column[0],text="Name")
tbl.column(column[0],width=60)
tbl.heading(column[1],text="Family")
tbl.column(column[1],width=60)
tbl.heading(column[2],text="Age")
tbl.column(column[2],width=60)
tbl.heading(column[3],text="Gender")
tbl.column(column[3],width=60)

tbl.bind("<Button-1>",getselection)
tbl.place(x=250,y=40)

radiovar=IntVar()



radio1=ttk.Radiobutton(root,text="Male",value=1,variable=radiovar)
radio1.place(x=55,y=20)
radio2=ttk.Radiobutton(root,text="Female",value=2,variable=radiovar)
radio2.place(x=110,y=20)
radio3=ttk.Radiobutton(root,text="Private",value=3,variable=radiovar)
radio3.place(x=175,y=20)









root.mainloop()


