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
# dict={"gvkale":["dm"],"swjadhav":["fds","dsl"],"pakhadkikar":["oop","oopcgl"],"adbundele":["deld","del","bcsl"],
#       "mstakalikar":["cg","oopcgl"],"psjoshi":["dsl","fds"],"sngirme":["dsl"],"jsmahajan":["dsl","dm"],"sshah":["oopcgl","cg","bcsl"],
#       "pjjambhulkar":["oopcgl","bcsl","oop"],"yahandge":["oopcgl","oop"],"rjadhav":["del","deld"],"nykapadnis":["del","deld"],
#       "ptkohok":["del","deld"],"psvidap":["bcsl"],"vvbagade":["bcsl"],"sssonawane":["dm","dsl"],"prmakkar":["fds","dsl","bcsl"],
#       "ddbhaiya":["cg","bcsl","oopcgl"],"aadeshpande":["dsl","dm"],"uspawar":["oopcgl"],"rkulkarni":["oopcgl","cg"],"kcwaghmare":["dsl","fds"],
#       "rrnavghare":["bcsl"],"mrjansari":["bcsl"],"rspaswan":["oop","oopcgl"],"ssshevtekar":["bcsl"],"aachandorkar":["bcsl"]}


# dict_2={"basonkamble":["dbms"],"spshintre":["toc","lp1"],"aachandorkar":["spos","lp1"],"prpatil":["cns","cnsl"],"sngirme":["electiveds"],"ssshevtekar":["electiveds","lp1"],
#         "mvmane":["electiveds","lp1"],"uspawar":["electivehci"],"mswakode":["electiveiot","lp1"],"prmakkar":["honorsdsv"],"vsgaikwad":["honorscs","dbmsl","dbms"],"pajain":["honorsics","cnsl","cns"],
#         "kurane":["dbmsl"],"ppjoshi":["dbmsl","dbms"],"vvbagade":["dbmsl"],"rrnavghare":["lp1","toc"],"psvidap":["lp1","spos"],"mrjansari":["lp1","spos"],"mschavan":["cnsl","cns"],"bpmasram":["cnsl","cns","lp1"],
#         "agphakatkar":["dbms","dbmsl"],"ptkohok":["dbmsl"],"vkandekar":["dbmsl"],"rakulkarni":["lp1","spos"],"gppotdar":["toc"],"kgangrade":["spos"],"rjadhav":["dbmsl"],"yahandge":["dbmsl"],
#         "nykapadnis":["dbmsl"]}

def get_sy_teachers(teach_dict):
    teach_dict_1=list(teach_dict.items())
    names=[]
    for name ,subj in teach_dict_1:
        if len(subj)==1 and "BCSL" in subj:
            continue
        names.append(name)
    return names
# sy_teachers=get_sy_teachers(dict)
# print(sy_teachers)

def avail(name):
    mycursor.execute("SELECT * from {}".format(name))
    var=mycursor.fetchall()
    #print(var)
    count=0
    for g in var:
        for l in g:
            if l==None:
                count+=1
    #print(count)
    return count
#labs_per_teacher={"oopcgl":2,"dsl":2,"bcsl":2,"del":4}

def te_lab_assign(dict,dict_2,year,labs):
    l_l1=["k1","l1","m1","n1","k2","l2","m2","n2","k3","l3","m3","n3","k4","l4","m4","n4"]
    list_ts=list(dict.items())
    list_ts1=list(dict_2.items())
    # print(list_ts)
    teach={}
    teach_1={}
    all_teachers=[]
    for name,subj in list_ts1:
        all_teachers.append(name)
    for name,subj in list_ts1:
        # print(name)
        # print(subj)
        for i in subj:
            if i not in teach.keys():
                teach[i]=[name]
            else:
                teach[i]+=[name]
        for j in subj:
            if j not in teach_1.keys():
                teach_1[j]=[{name:[]}]
            else:
                teach_1[j]+=[{name:[]}]
    # print(teach)
    # labs=[("cnsl",1),("lp1",2),("dbmsl",2)]
    sy_teachers=get_sy_teachers(dict)
    for labname,slots in labs:
        c=0
        l_l1=["k1","l1","m1","n1","k2","l2","m2","n2","k3","l3","m3","n3","k4","l4","m4","n4"]
        while len(l_l1)!=0:
            x=[]
            # print(len(x))
            sub=labname
            # print(labname)
            r=choice(teach[labname])
            ind=0
            leng=len(teach[labname])
            if leng<16:
                labs_per_teacher=ceil(16/leng)
                if r in sy_teachers:
                    labs_per_teacher-=1
            else:
                labs_per_teacher=1
            for m in range(leng):
                if teach[labname][m]==r:
                    ind=m
                    break
            mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6,slot7 from {}".format(year+l_l1[0][-1]))
            all_slots=mycursor.fetchall()
            # print(all_slots)
            mycursor.execute('''CREATE TABLE IF NOT EXISTS {} 
                            (days VARCHAR(45) NOT NULL,
                            slot1 VARCHAR(45) DEFAULT NULL,
                            slot2 VARCHAR(45) DEFAULT NULL,
                            slot3 VARCHAR(45) DEFAULT NULL,
                            slot4 VARCHAR(45) DEFAULT NULL,
                            slot5 VARCHAR(45) DEFAULT NULL,
                            slot6 VARCHAR(45) DEFAULT NULL,
                            slot7 VARCHAR(45) DEFAULT NULL)'''.format(r))
            mycursor.execute('select * from {}'.format(r))
            p=mycursor.fetchall()
            if len(p)==0:
                mycursor.execute("INSERT INTO {}(days) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(r))
            mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(r))
            t_slots=mycursor.fetchall()
            for i in range(5):
                for j in range(5):
                    if j==0 or j==2 or j==4:
                        if sub+l_l1[0] in all_slots[i][j]:#and len(all_slots[i][j])>12:
                            if t_slots[i][j]==None and t_slots[i][j+1]==None:
                                x.append([i,j])
            # print(len(x))
            # print(x)
            # print(r)
            number=len(teach_1[labname][ind][r])
            #cv=avail(r)
            #h=dict[r][-1]
            c+=1
            if c>=50:
                return 0
            if r not in sy_teachers:
                if len(x)==slots and number<=labs_per_teacher : #and cv>(30-h):
                    for n in x:
                        mycursor.execute("UPDATE {} SET slot{}='{}',slot{}='{}' WHERE days='{}'".format(r,(n[-1]+1),(sub+l_l1[0]),(n[-1]+2),(sub+l_l1[0]),days[n[0]]))
                    teach_1[labname][ind][r].append(l_l1[0])
                    del l_l1[0]
                else:
                    continue
            else:
                if len(x)==slots and number<labs_per_teacher : #and cv>(30-h):
                    for n in x:
                        mycursor.execute("UPDATE {} SET slot{}='{}',slot{}='{}' WHERE days='{}'".format(r,(n[-1]+1),(sub+l_l1[0]),(n[-1]+2),(sub+l_l1[0]),days[n[0]]))
                    teach_1[labname][ind][r].append(l_l1[0])
                    del l_l1[0]
                else:
                    continue