from tkinter import *
from tkinter import ttk 
import guiFunctions as gif



def cal_ui(prompt):
    def get_lab_data():
            lab_room_data = []
            labSub = lab_subject.get()
            slots = int(lab_slots.get())
            for i in lab_room.curselection():
                lab_room_data.append(gif.lab_list[i])
            if(gif.lab_check(labSub, len(lab_room_data))):
                p2_LAT.insert("", "end", values=(labSub, slots, lab_room_data))
            lab_room_data.append(slots)
            gif.lab_data.update({labSub:lab_room_data})
            print(gif.lab_data)



    def get_class_data():
        class_room_data = []
        for i in class_room.curselection():
            class_room_data.append(gif.classroom_list[i])
        gif.class_data = class_room_data
        print(gif.class_data)


    def get_class_data_extra():   
        extra_sub_room = []
        for j in select_esub_room.curselection():
            extra_sub_room.append(gif.extra_sub_list[j])
        extra_sub_room.append(1)
        gif.extra_sub.update({gif.extra_sub_se :extra_sub_room})
        if(extra_sub_room == [] or extra_sub_room == [1]):
            gif.extra_sub.update({gif.extra_sub_se : gif.extra_sub_list})


    def subject_select_toggle(sub, sem):
        # print(sub, sem)
        if sub =="SE" and sem == 1:
            lab_subject['values'] = gif.se_lab_subject_list_sem1
            gif.sete_theory = gif.se_subject_sem1
            gif.extra_sub_se = "HSS"
            extra_sub_label['text'] = "Allocate Rooms for HSS"

        elif sub == "SE" and sem == 2:
            lab_subject['values'] = gif.se_lab_subject_list_sem2 
            gif.sete_theory = gif.se_subject_sem2
            gif.extra_sub_se = "COC"
            extra_sub_label['text'] = "Allocate Rooms for COC"

        elif sub == "TE" and sem == 1:
            lab_subject['values'] = gif.te_lab_subject_list_sem1
            gif.sete_theory = gif.te_subject_sem1

        elif sub == "TE" and sem == 2:
            lab_subject['values'] = gif.te_lab_subject_list_sem2
            gif.sete_theory = gif.te_subject_sem2
            
        elif sub == "BE" and sem == 1:
            lab_subject['values'] = gif.be_lab_subject_list_sem1
        elif sub == "BE" and sem == 2:
            lab_subject['values'] = gif.be_lab_subject_list_sem2
        else:
            print("Error!")





    def show_frame(frame):
        frame.tkraise()

    
    root = Tk()
    root.title("Calendar Generator")
    root.resizable(False, False)
    frame1 = ttk.Frame(root)
    frame2 = ttk.Frame(root)
    frame3 = ttk.Frame(root)
    # frame4 = ttk.Frame(root)
    for frame in (frame1, frame2, frame3):
        frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)


    # Page 1
    filepath = "IMG_1450.png"
    p1_bg = PhotoImage(file=filepath)
    p1_img_label = ttk.Label(frame1, image=p1_bg)
    p1_img_label.grid(row=0,column=0, padx=10, pady=10, rowspan=10, columnspan=4, sticky="nsew")


    p1_frame1 = ttk.Labelframe(frame1) 
    p1_frame1.grid(row=0,column=5, rowspan=10, columnspan=6, padx=10, pady=10, sticky="nsew")


    label1 = Label(p1_frame1, text="Welcome to %s Timetable Generator"%(prompt), font=("Sans Serif", 18, "bold")) 
    label1.grid(row=0,column=0, columnspan=2, padx=50, pady=50)


    # Content of Page 1

    branch_label = ttk.Label(p1_frame1, text="Branch")
    branch = ttk.Combobox(p1_frame1, values=["CE", "IT", "EnTC"], width=20)
    branch_label.grid(row=3, column=0)
    branch.grid(row=4, column=0)


    academic_year_label = ttk.Label(p1_frame1, text="Academic - Year")
    academic_year = ttk.Entry(p1_frame1, width=30)
    academic_year_label.grid(row=3, column=1)
    academic_year.grid(row=4, column=1, pady=10)


    year_label = ttk.Label(p1_frame1, text="Year")
    year = ttk.Label(p1_frame1, text=prompt)
    year_label.grid(row=5, column=0)
    year.grid(row=6, column=0)


    sem_label = ttk.Label(p1_frame1, text="Semester")
    sem = ttk.Combobox(p1_frame1, values=[1, 2], width=20)
    sem_label.grid(row=5, column=1)
    sem.grid(row=6, column=1)


    for widget in p1_frame1.winfo_children():
        if isinstance(widget, ttk.Label):
            widget['font'] = ("Times New Roman", 12)
            widget.grid_configure(padx=30, pady=10)
        
        elif isinstance(widget, ttk.Combobox):
            widget['width'] = 20
            widget['font'] = ("Times New Roman", 12)
            widget.grid_configure(padx=30, pady=10)
        else:
            widget.grid_configure(padx=50)


    #Next Button

    next_button1 = ttk.Button(frame1, text="Next", command=lambda: get_fields(frame2))
    next_button1.grid(row=11, column=10, padx=10, pady=20, columnspan=2)


    # Page 2

    p2_LAT = ttk.Treeview(frame2, show="headings", height=19)
    p2_LAT["columns"] = ("LabSub", "Slots", "LabRooms")
    treeScroll = ttk.Scrollbar(frame2, orient="horizontal", command=p2_LAT.xview)
    p2_LAT.configure(xscrollcommand=treeScroll.set)
    treeScroll.grid(row=10, column=0, columnspan=4, sticky="ew")

    p2_LAT.heading("LabSub", text="Lab\nSubjects")
    p2_LAT.column("LabSub", width=55)

    p2_LAT.heading("LabRooms", text="Lab Rooms Selected")
    p2_LAT.column("LabRooms", width=195)

    p2_LAT.heading("Slots", text="Weekly\nSlots")
    p2_LAT.column("Slots", width=50)
    p2_LAT.grid(row=0,column=0, padx=10, pady=10, rowspan=10, columnspan=4, sticky="nsew")    

    p2_frame2 = ttk.Labelframe(frame2) 
    p2_frame2.grid(row=0,column=5, rowspan=10, columnspan=6, padx=30, pady=15, sticky="nsew")


    label1 = Label(p2_frame2, text="Enter Lab Details", font=("Sans Serif", 18)) 
    label1.grid(row=0,column=0, columnspan=2, padx=50, pady=30)



    # Content of Page 2

    lab_room_label = ttk.Label(p2_frame2, text="Select Labs for Subject")
    lab_room = Listbox(p2_frame2, width=25, selectmode=MULTIPLE)

    for i in range(len(gif.lab_list)):
        lab_room.insert((i+1), gif.lab_list[i])
    lab_room_label.grid(row=1, column=2, sticky="e")
    lab_room.grid(row=2, column=2, sticky="ns", rowspan=5, columnspan=2)

    listScroll = ttk.Scrollbar(p2_frame2, orient="vertical", command=lab_room.yview)
    lab_room.configure(yscrollcommand=listScroll.set)
    listScroll.grid(row=2, column=2, sticky="nse", rowspan=5)


    lab_subject_label = ttk.Label(p2_frame2, text="Lab Subject")
    lab_subject = ttk.Combobox(p2_frame2, values=gif.lab_subject_list)
    lab_subject_label.grid(row=1, column=0)
    lab_subject.grid(row=2, column=0, sticky="n")


    lab_slots_label = ttk.Label(p2_frame2, text="Number of Slots per week \n (Each Slot is of 2 hours)")
    lab_slots = ttk.Spinbox(p2_frame2, from_=0, to=20, width=27)
    lab_slots_label.grid(row=4, column=0)
    lab_slots.grid(row=5, column=0, sticky="ns")

    submit_lab = ttk.Button(p2_frame2, text="Confirm", command=get_lab_data)
    submit_lab.grid(row=12, column=0, columnspan=3 , pady=25)


    for widget in p2_frame2.winfo_children():

        if isinstance(widget, ttk.Label):
            widget['font'] = ("Times New Roman", 12)
            widget.grid_configure(padx=30)
        
        elif isinstance(widget, ttk.Combobox):
            widget['width'] = 20
            widget['font'] = ("Times New Roman", 12)
            widget.grid_configure(padx=30, pady=5)

        

    next_button2 = ttk.Button(frame2, text="Next", command=lambda: get_fields(frame3))
    next_button2.grid(row=10, column=10, padx=25, pady=20, columnspan=2)

    back_button = ttk.Button(frame2, text="Back", command= lambda: show_frame(frame1))
    back_button.grid(row=10, column=8, padx=0, pady=20, columnspan=2)

    # Page 3

    p3_frame3 = ttk.Labelframe(frame3) 
    p3_frame3.grid(row=0,column=5, rowspan=10, columnspan=6, padx=20, pady=25, sticky="nsew")

    p3_frame4 = LabelFrame(frame3)
    p3_frame4.grid(row=0, column=0, rowspan=10, columnspan=5, sticky="nsew", padx=20, pady=25)

    label1 = ttk.Label(p3_frame3, text="Enter Classroom Details", font=("Sans Serif", 18)) 
    label1.grid(row=0,column=0, columnspan=2, padx=50, pady=30)

    extra_sub_label = ttk.Label(p3_frame3, text="Allocate Rooms for SUB")
    extra_sub_label.grid(row=1, column=2, padx=30)

    select_esub_room = Listbox(p3_frame3, selectmode=MULTIPLE)
    select_esub_room.grid(row=2, column=2, padx=30, rowspan=5, columnspan=2) 
    for i in range(len(gif.extra_sub_list)):
        select_esub_room.insert((i+1), gif.extra_sub_list[i])
    listScroll = ttk.Scrollbar(p3_frame3, orient="vertical", command=select_esub_room.yview)
    select_esub_room.configure(yscrollcommand=listScroll.set)
    listScroll.grid(row=2, column=2, sticky="nse", rowspan=5) 

    # Content of Page 3

    class_room_label = ttk.Label(p3_frame3, text="Select Classrooms for Theory")
    class_room = Listbox(p3_frame3, width=25, selectmode=MULTIPLE)

    for i in range(len(gif.classroom_list)):
        class_room.insert((i+1), gif.classroom_list[i])

    class_room_label.grid(row=1, column=0, sticky="e")
    class_room.grid(row=2, column=0, sticky="ns", rowspan=5, columnspan=2)

    listScroll = ttk.Scrollbar(p3_frame3, orient="vertical", command=class_room.yview)
    class_room.configure(yscrollcommand=listScroll.set)
    listScroll.grid(row=2, column=0, sticky="nse", rowspan=5)

    submit_class= ttk.Button(p3_frame3, text="Confirm Classrooms", command=get_class_data)
    submit_class.grid(row=12, column=0, columnspan=2 , pady=25)

    submit_class= ttk.Button(p3_frame3, text="Confirm Extra\nSubject Rooms", command=get_class_data_extra)
    submit_class.grid(row=12, column=2, columnspan=2 , pady=25)

    filebtn1_label = ttk.Label(p3_frame4, text="Upload the Faculty Subject List", font=("Sans Serif", 16, "bold"))
    filebtn1 = ttk.Button(p3_frame4, text="Upload File", command=gif.get_file, width=20)
    filebtn1_label.grid(row=3, column=0 ,padx=30, pady=30)
    filebtn1.grid(row=4, column=0, pady=25)


    for widget in p3_frame3.winfo_children():

        if isinstance(widget, ttk.Label):
            widget['font'] = ("Times New Roman", 12)
            widget.grid_configure(padx=20)
        
        elif isinstance(widget, ttk.Combobox):
            widget['width'] = 20
            widget['font'] = ("Times New Roman", 12)
            widget.grid_configure(padx=20, pady=5)


    next_button2 = ttk.Button(frame3, text="Exit", command=lambda: get_fields(0))
    next_button2.grid(row=11, column=10, padx=20, pady=20, columnspan=2)
    back_button = ttk.Button(frame3, text="Back", command= lambda: show_frame(frame2))
    back_button.grid(row=11, column=8, padx=20, pady=20, columnspan=2)

    def get_fields(frame):
        if frame == frame2:
            if branch.get() and academic_year.get() and sem.get():
                gif.branch = branch.get()
                gif.academic_year = academic_year.get()
                gif.year = prompt
                gif.sem = int(sem.get())
                subject_select_toggle(gif.year, gif.sem)
                show_frame(frame2)
            else:
                gif.errormsg()

        elif frame == frame3:
            if gif.lab_data:
                show_frame(frame3)
            else:
                gif.errormsg()
        elif frame == 0:
            get_class_data_extra()
            if gif.class_data:
                gif.messagebox.showinfo(title="Thank You!", message="Your Responses have been submitted")
                root.destroy()
            else:
                gif.errormsg()
        else:
            print("Oops! Something went wrong \nPlease restart Calendar Generator.")
  

    show_frame(frame1)
    root.mainloop()

# cal_ui("SE")
