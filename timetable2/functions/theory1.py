import mysql.connector
from random import *
from string import *
#from test_1 import *
from math import *
db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Ayush_Chanekar23",
    database="ttproject",
    autocommit=True)
mycursor=db.cursor()
days=['Monday','Tuesday','Wednesday','Thursday','Friday']
#LINKING TEACHERS WITH THE LABS AND THEORY THEY TEACH
def theory_assign(dict,year,subjects_slots):
    teachers_theory={}
    teachers_theory_1={}
    list_ts=list(dict.items())
    for name,subj in list_ts:
        for i in subj:
            if i not in teachers_theory.keys():
                teachers_theory[i]=[name]
            else:
                teachers_theory[i]+=[name]
        for j in subj:
            if j not in teachers_theory_1.keys():
                teachers_theory_1[j]=[{name:[]}]
            else:
                teachers_theory_1[j]+=[{name:[]}]

    for theory,slots in subjects_slots:
        c=0
        l1=['1','2','3','4']
        while len(l1)!=0:
            x=[]
            #print(len(x))
            sub=theory
            #print(theory) 
            r=choice(teachers_theory[theory])
            ind=0
            leng=len(teachers_theory[theory])
            if leng<4:
                theory_per_teacher=ceil(4/leng)
            else:
                theory_per_teacher=1
            for m in range(leng):
                if teachers_theory[theory][m]==r:
                    ind=m
                    break
            mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(year+l1[0]))
            all_slots=mycursor.fetchall()
            #print(all_slots)
            mycursor.execute('''CREATE TABLE IF NOT EXISTS {} 
                            (days VARCHAR(45) NOT NULL,
                            slot1 VARCHAR(45) DEFAULT NULL,
                            slot2 VARCHAR(45) DEFAULT NULL,
                            slot3 VARCHAR(45) DEFAULT NULL,
                            slot4 VARCHAR(45) DEFAULT NULL,
                            slot5 VARCHAR(45) DEFAULT NULL,
                            slot6 VARCHAR(45) DEFAULT NULL)'''.format(r))
            mycursor.execute('''select count(*) from {}'''.format(r))
            p=mycursor.fetchall()[0][0]
            if p==0:
                mycursor.fetchall()
                mycursor.execute("insert into {}(days) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(r))

            mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(r))
            t_slots=mycursor.fetchall()
            for i in range(5):
                for j in range(6):
                    #print(all_slots[i][j])
                    if sub in all_slots[i][j] and len(all_slots[i][j])<12 :
                        #print(1)
                        if j==0 or j==2 or j==4:
                            if (t_slots[i][j]==None and t_slots[i][j+1]==None):
                                x.append([i,j])
                        elif j==1 or j==3 or j==5:
                            if (t_slots[i][j]==None and t_slots[i][j-1]==None):
                                x.append([i,j])
            # print(len(x))
            # print(x)
            # print(r)
            #min=one_least(theory,r,ind)
            number=len(teachers_theory_1[theory][ind][r])
            c+=1
            if c>50:
                return 0
            #cv=avail(r)
            #h=dict[r][-1]
            if len(x)==slots and number<theory_per_teacher: #and cv>(30-h):
                for n in x:
                    mycursor.execute("UPDATE {} SET slot{}='{}' WHERE days='{}'".format(r,(n[-1]+1),(all_slots[n[0]][n[-1]]+"_div"+l1[0]),days[n[0]]))
                teachers_theory_1[theory][ind][r].append(l1[0])
                del l1[0]
            else:
                continue


"""def  one_least(sname,tname,ind):
    c=0
    for n in teachers_theory_1[sname]:
        if len(n[ind][tname])==0:
            c+=1
    return c
for subj,hours in subjects:
    d1=-1
    l1=['1','2','3','4']
    leng=len(teachers_theory[subj])
    for names in teachers_theory[subj]:
        d1+=1
        sub=subj
        #subjo=subj+"div_"+l1[0]
        mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6 from tt{}".format(l1[0]))
        all_slots=mycursor.fetchall()
        print(all_slots)
        mycursor.execute('''CREATE TABLE IF NOT EXISTS {} 
                                    (days VARCHAR(45) PRIMARY KEY,
                                    slot1 VARCHAR(45) DEFAULT NULL,
                                    slot2 VARCHAR(45) DEFAULT NULL,
                                    slot3 VARCHAR(45) DEFAULT NULL,
                                    slot4 VARCHAR(45) DEFAULT NULL,
                                    slot5 VARCHAR(45) DEFAULT NULL,
                                    slot6 VARCHAR(45) DEFAULT NULL)'''.format(names))
        mycursor.execute("INSERT IGNORE INTO {} (days) VALUES ('mon'),('tues'),('wed'),('thurs'),('fri')".format(names))
        mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(names))
        t_slots=mycursor.fetchall()
        print(t_slots)
        for i in range(5):
            for j in range(6):
                if sub in all_slots[i][j] and len(all_slots[i][j])<=12 :
                    if j==0 or j==2 or j==4:
                        if (t_slots[i][j]==None and t_slots[i][j+1]==None):
                            mycursor.execute("UPDATE {} SET slot{}='{}' WHERE days='{}'".format(names,(j+1),(all_slots[i][j]+"_div"+l1[0]),days[i]))
                    elif j==1 or j==3 or j==5:
                        if (t_slots[i][j]==None and t_slots[i][j-1]==None):
                            mycursor.execute("UPDATE {} SET slot{}='{}' WHERE days='{}'".format(names,(j+1),(all_slots[i][j]+"_div"+l1[0]),days[i]))
        del l1[0]"""