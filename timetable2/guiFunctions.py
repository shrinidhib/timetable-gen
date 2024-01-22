from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import xlsxRead as xlr

branch = ""
year = ""
academic_year = ""
sem = ""
global lab_subject_list
lab_subject_list = []

lab_data = {}

class_data = []
sete_theory ={}
extra_sub_se = ""

def lab_check(sub, n):
    if sub == "DSL":
        if n < 5:
            messagebox.showwarning(title="Error", message="Please allocate 5 or more labs")
            return False
    elif sub == "DEL":
        if n < 2:
            messagebox.showwarning(title="Error", message="Please allocate 2 or more labs")
            return False
    elif sub == "OOPCGL":
        if n < 10:
            messagebox.showwarning(title="Error", message="Please allocate 10 or more labs")
            return False
    elif sub == "LP1":
        if n < 6:
            messagebox.showwarning(title="Error", message="Please allocate 6 or more labs")
            return False
    elif sub == "DBMSL":
        if n < 6:
            messagebox.showwarning(title="Error", message="Please allocate 6 or more labs")
            return False
    elif sub == "CNSL":
        if n < 7:
            messagebox.showwarning(title="Error", message="Please allocate 7 or more labs")
            return False
    return True

def get_file():
    # global teacher_file
    teacher_file = fd.askopenfilename()
    if(teacher_file):
        messagebox.showinfo(title="File Upload", message="File : %s %sUploaded Succesfully"%(teacher_file, "\n"))
        xlr.read_file(teacher_file)
        global practical_data
        practical_data = xlr.practical
        print(practical_data)
        global theory_data
        theory_data = xlr.theory
        print("-----------------------------------------------------------------------------------------------------")
        print(theory_data) 
    else:
        messagebox.showinfo(title="File Upload", message="No File was Uploaded")

lab_list = ['A1209', 'A1216', 'A2303', 'A1010', 'A1314', 'A2302', 'A1204', 'A1302', 'A1306', 'A1203', 'A1310', 
            'A1302B', 'A1208', 'A1202', 'A2302', 'A1302A', 'A1107', 'A1307', 'A1301', 'A1303']


prof_list = ["swjadhav", "gvkale", "pakh adkikar" ,"adbundele", "mstakalikar", "psjoshi" ,"sngirme", "jsmahajan",
              "sshah", "pjjambhulkar", "yahandge", "rjadhav", "nykapadnis", "ptkohok", "psvidap", "vvbagade",
             "sssonawane", "prmakkar", "ddbhaiya", "aadeshpande", "uspawar", "rkulkarni", "kcwaghmare", "rrnavghare",
             "mrjansari", "rspaswan", "ssshentekar", "aachandorkar" ]

classroom_list = ['A1211', 'A1212', 'A1213', 'A1311', 'A1112', 'A1309', 'A1310']

extra_sub_list = lab_list + classroom_list
extra_sub_list.append(1)
extra_sub = {}

se_subject_sem1 = {'DM':3,'DELD':3,'CG':3,'FDS': 3,'OOP':3}
se_subject_sem2 = {'EM-3':3,'DSA':3,'SE':3,'MP': 3,'POPL':3}

def errormsg():
    messagebox.showwarning(title="Error", message="Please fill all required fields!!!")

te_subject_sem1 = {'DBMS':3,'TOC':3,'SPOS':3,'CNS':3}
te_subject_sem2 = {'DAA':3, 'SPOPS':3, 'ESIOT':3, 'SMD':3}

se_lab_subject_list_sem1 = ["DSL", "OOPCGL", "DEL", "BCSL"]
se_lab_subject_list_sem2 = ["DSA", "Microprocessor", "PBL-2"]

te_lab_subject_list_sem1 = ["DBMSL", "LP-1", "CNSL"]
te_lab_subject_list_sem2 = ["DSBAL", "WTL", "LP-2"]

be_lab_subject_list_sem1 = ["LP-3", "LP-4"]
be_lab_subject_list_sem2 = ["LP-5", "LP-6"]


