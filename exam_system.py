from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os


win = Tk()
win.title(' Exam system ')
win.geometry('1000x700+300+10')
win.config(bg='darkgrey')
win.iconbitmap('images/smile.ico')

#Style
s = ttk.Style()
print(s.theme_names(), s.theme_use('clam'))
s.configure('TEntry', foreground='saddlebrown')
s.configure('TButton', foreground='saddlebrown')


backfon = ImageTk.PhotoImage(Image.open('images/mit5.jpeg').resize((995,695), Image.BILINEAR))   #, Image.ANTIALIAS
Label(win, image=backfon).place(x=0, y=0)

# +++++++++++ frames +++++++++++
univ_name = Label(win, text='Examination system', font=('Times', 20, 'bold'), fg='Snow', bg='darkslategrey', bd=10, relief=GROOVE)
univ_name.pack(side=TOP, fill=X)

pic_frame = Frame(win, bg='darkslategrey')
pic_frame.place(x=160, y=60, width=110, height=110)

reg_frame = LabelFrame(win, text='Add',font=('Times', 16, 'bold'),  fg='saddlebrown', bg='aliceblue', bd=6, relief=GROOVE)
reg_frame.place(x=10, y=180, width=370, height=510)

inf_frame = LabelFrame(win, text='Information',font=('Times', 16),  fg='saddlebrown', bg='aliceblue', bd=6, relief=GROOVE)
inf_frame.place(x=390, y=60, width=600, height=260)

gallery_frame = Frame(win, bg='darkslategrey')
gallery_frame.place(x=440, y=330, width=505, height=355)

# +++++++++++ def +++++++++++
def total():
    e1 = int(one.get())
    e2 = int(two.get())
    e3 = int(three.get())
    e4 = int(final.get())

    total_ = round((e1*0.2)+(e2*0.2)+(e3*0.2)+(e4*0.4))
    if total_ > 100:
        print('Error')
    else:
        total_price.insert(0, str(total_))

def add():
    my_tree.insert(parent='', index='end', iid=count, text='', values=(combo_students.get(), combo_sub.get(), one.get(), two.get(), three.get(), final.get(), total_price.get()))

def delete():
    combo_students.delete(0, 'end')
    one.delete(0, 'end')
    two.delete(0, 'end')
    three.delete(0, 'end')
    final.delete(0, 'end')
    combo_sub.delete(0, 'end')
    total_price.delete(0, 'end')

# +++++++++++ picture def +++++++++++

def sel_student(e):
    global img_student
    student_index = combo_students.current()

    if os.path.exists(f'images/{photo[student_index]}'):
        img_student = ImageTk.PhotoImage(Image.open(f'images/{photo[student_index]}').resize((100,100), Image.BILINEAR))
    else:
        img_student = ImageTk.PhotoImage(Image.open(f'images/main.jpeg').resize((100,100), Image.BILINEAR))

    photo_stud.config(image = img_student)


subj = ('python_1', 'python_2', 'python_3')
stud_names = ('Arslan', 'Ahmet', 'Allanur', 'Agageldi')
photo = ('arslan.png', 'ahmet.png', 'allanur.png', 'agageldi.png')

phot_stud_main = ImageTk.PhotoImage(Image.open('images/main.jpeg').resize((100,100), Image.BILINEAR))
photo_stud = Label(pic_frame, image=phot_stud_main, bd=4, relief=RIDGE)
photo_stud.place(x=0, y=0)

# logo picture
logo = ImageTk.PhotoImage(Image.open('images/mit0.jpeg').resize((250,150), Image.BILINEAR))
lbl_img_logo = Label(reg_frame, image=logo, bd=7, relief=RIDGE, width=160, height=140)
lbl_img_logo.grid(row=9, column=0, columnspan=2)

# +++++++++++ labels +++++++++++
fullname = Label(reg_frame, text='Fullname', font=('Times', 16, 'bold'), fg='saddlebrown', bg='aliceblue', width=12)
exam1 = Label(reg_frame, text='Exam_1', font=('Times', 16, 'bold'), fg='saddlebrown', bg='aliceblue')
exam2 = Label(reg_frame, text='Exam_2', font=('Times', 16, 'bold'), fg='saddlebrown', bg='aliceblue')
exam3 = Label(reg_frame, text='Exam_3', font=('Times', 16, 'bold'), fg='saddlebrown', bg='aliceblue')
fexam = Label(reg_frame, text='Final exam', font=('Times', 16, 'bold'), fg='saddlebrown', bg='aliceblue')
subject = Label(reg_frame, text='Subject', font=('Times', 16, 'bold'), fg='saddlebrown', bg='aliceblue')
total = Button(reg_frame, text='Total', font=('Times', 16, 'bold'), fg='saddlebrown', bg='aliceblue', command=total)

# Entries
one = ttk.Entry(reg_frame, font=('Times', 16), width=16)
two = ttk.Entry(reg_frame, font=('Times', 16), width=16)
three = ttk.Entry(reg_frame, font=('Times', 16), width=16)
final = ttk.Entry(reg_frame, font=('Times', 16), width=16)
total_price = ttk.Entry(reg_frame, font=('Times', 16, 'bold'), width=16)

fullname.grid(row=0, column=0, padx=2, pady=4)
exam1.grid(row=1, column=0, pady=4)
one.grid(row=1, column=1, pady=4)
exam2.grid(row=2, column=0, pady=4)
two.grid(row=2, column=1, pady=4)
exam3.grid(row=3, column=0, pady=4)
three.grid(row=3, column=1, pady=4)
fexam.grid(row=4, column=0, pady=4)
final.grid(row=4, column=1, pady=4)
subject.grid(row=5, column=0, pady=4)
total.grid(row=6, column=0)
total_price.grid(row=6, column=1, pady=4)

# combobox
combo_students = ttk.Combobox(reg_frame, values=stud_names, font=('Times', 15), foreground='saddlebrown', background='white', width=16)
combo_students.current()
combo_students.bind('<<ComboboxSelected>>', sel_student)
combo_students.grid(row=0, column=1, padx=6, pady=4)

combo_sub = ttk.Combobox(reg_frame, values=subj, font=('Times', 15), foreground='saddlebrown', background='white', width=16)
combo_sub.current()
combo_sub.grid(row=5, column=1, padx=6, pady=4)


# +++++++++++ data_base text +++++++++++

# +++++++++++ create treeview +++++++++
tree_scroll_x = Scrollbar(inf_frame, orient=HORIZONTAL)
tree_scroll_y = Scrollbar(inf_frame, orient=VERTICAL)

my_tree = ttk.Treeview(inf_frame, xscrollcommand= tree_scroll_x.set, yscrollcommand=tree_scroll_y.set, selectmode=EXTENDED)

my_tree['columns'] = ('Fullname', 'Lesson', 'Exam1', 'Exam2', 'Exam3', 'FinalExam', 'TotalResult')

# +++++++++++ create columns +++++++++
my_tree.column('#0', width=0, stretch= NO)         # show='headings'

my_tree.column('Fullname', anchor= W, width=200)
my_tree.column('Lesson', anchor= W, width=100)
my_tree.column('Exam1', anchor= W, width=60)
my_tree.column('Exam2', anchor= W, width=60)
my_tree.column('Exam3', anchor= W, width=60)
my_tree.column('FinalExam', anchor= W, width=70)
my_tree.column('TotalResult', anchor= W, width=75)

# +++++++++++ create heading columns +++++++++
my_tree.heading('#0', text='', anchor=W)

my_tree.heading('Fullname', anchor= W, text='Fullname')
my_tree.heading('Lesson', anchor= W, text='Lesson')
my_tree.heading('Exam1', anchor= W, text='Exam1')
my_tree.heading('Exam2', anchor= W, text='Exam2')
my_tree.heading('Exam3', anchor= W, text='Exam3')
my_tree.heading('FinalExam', anchor= W, text='FinalExam')
my_tree.heading('TotalResult', anchor= W, text='TotalResult')

data = [
    ['Berdi Nuryyew', 'Python-3', 88, 99, 77, 90, 85],
    ['Mahri Nuryyewa', 'Python-3', 44, 55, 77, 66, 70],
    ['Aylar Nuryyew', 'Python-3', 65, 90, 88, 76, 65],
    ['Lachyn Ahmedowa', 'Python-3', 66, 49, 80, 59, 80],
    ['Nury Nuryyew', 'Python-3', 89, 50, 78, 90, 98],
    ['Berdi Nuryyew', 'Python-3', 88, 99, 77, 90, 85],
    ['Mahri Nuryyewa', 'Python-3', 44, 55, 77, 66, 70],
    ['Aylar Nuryyew', 'Python-3', 65, 90, 88, 76, 65],
    ['Lachyn Ahmedowa', 'Python-3', 66, 49, 80, 59, 80],
    ['Nury Nuryyew', 'Python-3', 89, 50, 78, 90, 98]
]

count = 0
for record in data:

    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
    count += 1

my_tree.pack()

tree_scroll_x.config(command=my_tree.xview)
tree_scroll_y.config(command=my_tree.yview)

tree_scroll_x.pack(side=BOTTOM, fill=X)
tree_scroll_y.pack(side=RIGHT, fill=Y)

# +++++++++++ buttons +++++++++++
btn_add = Button(reg_frame, text='Add', font=('Times', 16, 'bold'), command=add, fg='saddlebrown', bg='aliceblue', width=8)
btn_add.grid(row=7, column=0, padx=6, pady=4)
btn_del = Button(reg_frame, text='Delete', font=('Times', 16, 'bold'), command=delete, fg='saddlebrown', bg='aliceblue', width=8)
btn_del.grid(row=7, column=1, padx=2, pady=4)


# +++++++++++ Gallery +++++++++++

my_img1 = ImageTk.PhotoImage(Image.open('images/cambr8.jpeg').resize((500,320), Image.BILINEAR))
my_img2 = ImageTk.PhotoImage(Image.open('images/cambr12.jpeg').resize((500,320), Image.BILINEAR))
my_img3 = ImageTk.PhotoImage(Image.open('images/mit_lecture.jpeg').resize((500,320), Image.BILINEAR))
my_img4 = ImageTk.PhotoImage(Image.open('images/cambr10.jpeg').resize((500,320), Image.BILINEAR))
my_img5 = ImageTk.PhotoImage(Image.open('images/mit6.jpg').resize((500,320), Image.BILINEAR))
my_img6 = ImageTk.PhotoImage(Image.open('images/mit_stu.jpeg').resize((500,320), Image.BILINEAR))
my_img7 = ImageTk.PhotoImage(Image.open('images/cambr3.jpeg').resize((500,320), Image.BILINEAR))
my_img8 = ImageTk.PhotoImage(Image.open('images/exam2.webp').resize((500,320), Image.BILINEAR))
my_img9 = ImageTk.PhotoImage(Image.open('images/cambr7.jpeg').resize((500,320), Image.BILINEAR))

gallery_list =[my_img1, my_img2, my_img3, my_img4,
             my_img5, my_img6, my_img7, my_img8, my_img9]

my_label = Label(gallery_frame, image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

def forward(image_number):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    my_label = Label(gallery_frame, image = gallery_list[image_number - 1])
    btn_forward = Button(gallery_frame, text = "--->>>", command = lambda: forward(image_number + 1))
    btn_back = Button(gallery_frame, text = "<<<---", command = lambda: back(image_number - 1))

    if image_number == 9:
        btn_forward = Button(gallery_frame, text = "--->>>", state = DISABLED )
        
    
    my_label.grid(row =0, column = 0, columnspan = 3)
    btn_back.grid(row = 1, column = 0)
    btn_forward.grid(row = 1, column = 2)

def back(image_number):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    my_label = Label(gallery_frame, image = gallery_list[image_number - 1])
    btn_forward = Button(gallery_frame, text = "--->>>", command = lambda: forward(image_number + 1))
    btn_back = Button(gallery_frame, text = "<<<---", command = lambda: back(image_number - 1))

    if image_number == 1:
        btn_back =Button(gallery_frame, text = "<<<---", state = DISABLED)
    
    my_label.grid(row =0, column = 0, columnspan = 3)
    btn_back.grid(row = 1, column = 0)
    btn_forward.grid(row = 1, column = 2)

btn_back = Button(gallery_frame, text = "<<<---", command = back, state = DISABLED )
btn_exit = Button(gallery_frame, text = 'EXIT PROGRAMM', command = quit)
btn_forward = Button(gallery_frame, text = "--->>>", command = lambda:  forward(2))

btn_back.grid(row = 1, column = 0)
btn_exit.grid(row = 1, column = 1)
btn_forward.grid(row = 1, column = 2)

win.mainloop()