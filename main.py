from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from db import Database
from tkinter import messagebox

db = Database("Employees.db")

root = Tk()
root.title("Employees Management System")
root.geometry("1412x700+0+0")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# StringVar nesnelerini root oluşturulduktan sonra tanımlayın
name = StringVar()
age = StringVar()
job = StringVar()
email = StringVar()
gender = StringVar()
mobile = StringVar()

original_logo = Image.open("logo.png")
resized_logo = original_logo.resize((350, 300))  # Adjust the size as needed
logo = ImageTk.PhotoImage(resized_logo)

# Create the logo label
lbl_logo = Label(root, image=logo, bg="#2c3e50")
lbl_logo.place(x=0, y=615 - 155)

# ======= [entries_frame]  ========
entries_frame = Frame(root, bg="#2c3e50")
entries_frame.place(x=0, y=0, width=360, height=500)

title = Label(entries_frame, text="Employees Company", font=("Calibri", 18, "bold"), bg="#2c3e50", fg="#FFFFFF")
title.place(x=10, y=1)

lblName = Label(entries_frame, text="Name", font=("Calibri", 18), bg="#2c3e50", fg="#FFFFFF")
lblName.place(x=10, y=50)
txtName = Entry(entries_frame, textvariable=name, width=20, font=("Calibri", 18))
txtName.place(x=120, y=50)

lblJob = Label(entries_frame, text="Job", font=("Calibri", 18), bg="#2c3e50", fg="#FFFFFF")
lblJob.place(x=10, y=90)
txtJob = Entry(entries_frame, textvariable=job, width=20, font=("Calibri", 18))
txtJob.place(x=120, y=90)

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 18), bg="#2c3e50", fg="#FFFFFF")
lblGender.place(x=10, y=130)
comboGender = ttk.Combobox(entries_frame, textvariable=gender, state="readonly", font=("Calibri", 18), width=19)
comboGender["values"] = ("Female", "Male")
comboGender.place(x=120, y=130)

lblAge = Label(entries_frame, text="Age", font=("Calibri", 18), bg="#2c3e50", fg="#FFFFFF")
lblAge.place(x=10, y=170)
txtAge = Entry(entries_frame, textvariable=age, width=20, font=("Calibri", 18))
txtAge.place(x=120, y=170)

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 18), bg="#2c3e50", fg="#FFFFFF")
lblEmail.place(x=10, y=210)
txtEmail = Entry(entries_frame, textvariable=email,  width=20, font=("Calibri", 18))
txtEmail.place(x=120, y=210)

lblContact = Label(entries_frame, text="Contact", font=("Calibri", 18), bg="#2c3e50", fg="#FFFFFF")
lblContact.place(x=10, y=250)
txtContact = Entry(entries_frame, textvariable=mobile,  width=20, font=("Calibri", 18))
txtContact.place(x=120, y=250)

lblAddress = Label(entries_frame, text="Address :", font=("Calibri", 18), bg="#2c3e50", fg="#FFFFFF")
lblAddress.place(x=10, y=290)
txtAddress = Text(entries_frame, width=30, height=3, font=("Calibri", 18))
txtAddress.place(x=10, y=330)

btn_frame = Frame(entries_frame, bg="#2c3e50", bd=1, relief="flat")
btn_frame.place(x=10, y=380, width=341, height=106)


# ======= [Define]  ========

def get_data():
    selected_rows = tv.focus()
    data = tv.item(selected_rows)
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])
    return row  # Bu satır ile 'row' değerini geri döndürüyoruz


def hide():
    root.geometry("360x500")


def show():
    root.geometry("1412x700+0+0")


btn_hide = Button(entries_frame, text="HIDE", command=hide, relief="flat", font=("Calibri", 12), cursor="hand")
btn_hide.place(x=285, y=10)

btn_show = Button(entries_frame, text="SHOW", command=show, relief="flat", font=("Calibri", 12), cursor="hand")
btn_show.place(x=215, y=10)


def display_all():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert('', 'end', values=row)


def clear():
    name.set("")
    age.set("")
    job.set("")
    email.set("")
    gender.set("")
    mobile.set("")
    txtAddress.delete(1.0, END)


def delete():
    row = get_data()  # 'get_data' fonksiyonundan 'row' değerini alıyoruz
    if row:  # Eğer row boş değilse devam et
        db.remove(row[0])
        clear()
        display_all()
    else:
        messagebox.showerror("Error", "No record selected")


def add_employee():
    if (txtName.get() == "" or txtAge.get() == "" or txtJob.get() == "" or txtEmail.get() == "" or
            comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END) == ""):
        messagebox.showerror("Error", "Please fill all the Entry")
        return
    db.insert(txtName.get(),
              txtAge.get(),
              txtJob.get(),
              txtEmail.get(),
              comboGender.get(),
              txtContact.get(),
              txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Added new employees")
    clear()
    display_all()


# =========[Button Frame] =========

btnAdd = Button(
    btn_frame,
    text="Add Details",
    width=11,
    height=1,
    font=("Calibri", 16),
    bg="#16a085",
    bd=0,
    command=add_employee,
    highlightbackground="#16a085",
    highlightthickness=10
)
btnAdd.place(x=4, y=5)

btnEdit = Button(btn_frame,
                 text="Update Details",
                 width=11,
                 height=1,
                 font=("Calibri", 16),
                 bg="#2980b9",
                 bd=0,
                 highlightbackground="#2980b9",
                 highlightthickness=10
                 )
btnEdit.place(x=4, y=54)

btnDelete = Button(btn_frame,
                   text="Delete Details",
                   width=11,
                   height=1,
                   font=("Calibri", 16),
                   bg="#c0392b",
                   bd=0,
                   command=delete,
                   highlightbackground="#c0392b",
                   highlightthickness=10
                   )
btnDelete.place(x=170, y=5)

btnClear = Button(btn_frame,
                  text="Clear Details",
                  width=11,
                  height=1,
                  font=("Calibri", 16),
                  bg="#f39c12",
                  bd=0,
                  highlightbackground="#f39c12",
                  highlightthickness=10
                  )
btnClear.place(x=170, y=54)


# =========[Table Frame] =========

tree_frame = Frame(root, bg="white")
tree_frame.place(x=380, y=1, width=1100, height=700)
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 13), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=("Calibri", 13))

tv = ttk.Treeview(tree_frame, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"), style="mystyle.Treeview")

tv.heading("#1", text="ID")
tv.column("#1", width=50)

tv.heading("#2", text="FullName")
tv.column("#2", width=160)

tv.heading("#3", text="Age")
tv.column("#3", width=60)

tv.heading("#4", text="Job")
tv.column("#4", width=140)

tv.heading("#5", text="Email")
tv.column("#5", width=230)

tv.heading("#6", text="Gender")
tv.column("#6", width=90)

tv.heading("#7", text="Contact")
tv.column("#7", width=170)

tv.heading("#8", text="Address")
tv.column("#8", width=200)

tv["show"] = "headings"
tv.bind("<ButtonRelease-1>", get_data)
tv.pack()

display_all()
root.mainloop()
