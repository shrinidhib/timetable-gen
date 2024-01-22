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

def te_theory_assign(dict,dict_2,year,subjects):
    list_ts=list(dict.items())
    list_ts1=list(dict_2.items())
    honors_list=[]
    elective_list=[]
    teacher_honors_index={}
    teachers_elective_index={}
    for name,subj in list_ts1:
        for i in subj:
            if "HONOURS" in i:
                honors_list.append(name)
            if "ELECTIVE" in i:
                elective_list.append(name)
    for name,subj in list_ts1:
        for i in range(len(subj)):
            if "HONOURS" in subj[i]:
                teacher_honors_index[name]=i
            if "ELECTIVE" in subj[i]:
                teachers_elective_index[name]=i
    # print(honors_list)
    # print(elective_list)
    # print(teacher_honors_index)
    # print(teachers_elective_index)

    def get_sy_teachers(teach_dict):
        teach_dict_1=list(teach_dict.items())
        names=[]
        for name ,subj in teach_dict_1:
            if len(subj)==1 and "BCSL" in subj:
                continue
            names.append(name)
        return names
    sy_teachers=get_sy_teachers(dict)
    # print(sy_teachers)
    teachers_theory={}
    teachers_theory_1={}

    
    for name,subj in list_ts1:
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
    # print(teachers_theory)

    class_no_list={}
    while len(honors_list)!=0:
        r=choice(honors_list)
        # print(r)
        mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6,slot7 from {}".format(year+"2"))
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
            for j in range(7):
                if all_slots[i][j]!=None:
                    if "HONOURS" in all_slots[i][j]:
                        s1=all_slots[i][j].split()
                        for m in range(1,len(s1)):
                            s1[m]+=" "   
                        for k in range(1,len(s1)):
                            ind=s1[k].find("(")
                            subj=s1[k][:ind]
                            if subj not in class_no_list.keys():
                                class_no_list[subj]=[]
                            while(s1[k]!=" "):
                                ind1=s1[k].find("(")
                                ind2=s1[k].find(")")
                                class_no=s1[k][ind1+1:ind2]
                                class_no_list[subj]+=[class_no]
                                s1[k]=s1[k][ind2+1:]
        

        # print(class_no_list)
        for i in range(5):
            for j in range(7):
                if all_slots[i][j]!=None:
                    if "HONOURS" in all_slots[i][j]:
                        content=dict_2[r][teacher_honors_index[r]]
                        class_no=dict_2[r][teacher_honors_index[r]][len("HONOURS"):]
                        mycursor.execute("UPDATE {} SET slot{}='{}' WHERE days='{}'".format(r,(j+1),content+" ("+class_no_list[class_no][0]+")",days[i])) 
        del class_no_list[class_no][0]
        honors_list.remove(r)
    class_no_list={}
    while len(elective_list)!=0:
        r=choice(elective_list)
        # print(r)
        mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6,slot7 from {}".format(year+"2"))
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
        mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6,slot7 from {}".format(r))
        t_slots=mycursor.fetchall()
        for i in range(5):
            for j in range(7):
                if all_slots[i][j]!=None:
                    if "ELECTIVE" in all_slots[i][j]:
                        s1=all_slots[i][j].split()
                        for m in range(1,len(s1)):
                            s1[m]+=" "   
                        for k in range(1,len(s1)):
                            ind=s1[k].find("(")
                            subj=s1[k][:ind]
                            if subj not in class_no_list.keys():
                                class_no_list[subj]=[]
                            while(s1[k]!=" "):
                                ind1=s1[k].find("(")
                                ind2=s1[k].find(")")
                                class_no=s1[k][ind1+1:ind2]
                                class_no_list[subj]+=[class_no]
                                s1[k]=s1[k][ind2+1:]      
        # print(class_no_list)  
        for i in range(5):
            for j in range(7):
                if all_slots[i][j]!=None:
                    if "ELECTIVE" in all_slots[i][j]:
                        content=dict_2[r][teachers_elective_index[r]]
                        class_no=dict_2[r][teachers_elective_index[r]][len("ELECTIVE"):]
                        mycursor.execute("UPDATE {} SET slot{}='{}' WHERE days='{}'".format(r,(j+1),content+" ("+class_no_list[class_no][0]+")",days[i]))
        del class_no_list[class_no][0]
        elective_list.remove(r)


    # subjects=[("dbms",3),("toc",3),("cns",3),("spos",3)]
    for theory,slots in subjects:
        c=0
        l1=['1','2','3','4']
        while len(l1)!=0:
            x=[]
            # print(len(x))
            sub=theory
            # print(theory)
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
            mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6,slot7 from {}".format(year+l1[0]))
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
            mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6,slot7 from {}".format(r))
            t_slots=mycursor.fetchall()

            if theory_per_teacher>1:
                for i in range(5):
                    for j in range(7):
                        if all_slots[i][j]!=None:
                            if sub in all_slots[i][j] and len(all_slots[i][j])<=12:
                                if t_slots[i][j]==None:
                                    x.append([i,j])
            else:
                for i in range(5):
                    for j in range(7):
                        if all_slots[i][j]!=None:
                            if sub in all_slots[i][j] and len(all_slots[i][j])<=12 :
                                if j==0 or j==2 or j==4 :
                                    if (t_slots[i][j]==None and t_slots[i][j+1]==None):
                                        x.append([i,j])
                                elif j==1 or j==3 or j==6:
                                    if (t_slots[i][j]==None and t_slots[i][j-1]==None):
                                        x.append([i,j])
                                elif  j==5 :
                                    if (t_slots[i][j]==None and t_slots[i][j-1]==None and t_slots[i][j+1]==None):
                                        x.append([i,j])
            # print(len(x))
            # print(x)
            # print(r)
            #min=one_least(theory,r,ind)
            number=len(teachers_theory_1[theory][ind][r])
            c+=1
            if c>10:
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