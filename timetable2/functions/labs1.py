import mysql.connector
from random import *
from string import *
from math import *
db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Ayush_Chanekar23",
    database="ttproject",
    autocommit=True)
mycursor=db.cursor()
days=["Monday","Tuesday","Wednesday","Thursday","Friday"]
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
def lab_assign(dict,year,labs):
    teach={}
    teach_1={}
    all_teachers=[]
    list_ts=list(dict.items())
    for name,subj in list_ts:
        all_teachers.append(name)
    for name,subj in list_ts:
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
    #print(teach)

    for labname,slots in labs:
        c=0
        l_l1=["e1","f1","g1","h1","e2","f2","g2","h2","e3","f3","g3","h3","e4","f4","g4","h4"]
        while len(l_l1)!=0:
            x=[]
            #print(len(x))
            sub=labname
            #print(labname)
            r=choice(teach[labname])
            ind=0
            leng=len(teach[labname])
            if leng<16:
                labs_per_teacher=ceil(16/leng)
            else:
                labs_per_teacher=1
            for m in range(leng):
                if teach[labname][m]==r:
                    ind=m
                    break
            mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(year+l_l1[0][-1]))
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
            # print(l_l1[0])
            number=len(teach_1[labname][ind][r])
            c+=1
            if c>50:
                return 0
            #cv=avail(r)
            #h=dict[r][-1]

            if len(x)==slots and number<=labs_per_teacher : #and cv>(30-h):
                for n in x:
                    mycursor.execute("UPDATE {} SET slot{}='{}',slot{}='{}' WHERE days='{}'".format(r,(n[-1]+1),(sub+l_l1[0]),(n[-1]+2),(sub+l_l1[0]),days[n[0]]))
                teach_1[labname][ind][r].append(l_l1[0])
                del l_l1[0]
            else:
                continue
        

    hss={}
    l_l2=["e1","f1","g1","h1","e2","f2","g2","h2","e3","f3","g3","h3","e4","f4","g4","h4"]
    while len(l_l2)!=0:
        rn=choice(all_teachers)
        if rn not in hss.keys():
            hss.update({rn:[]})
        sub="HSS"+l_l2[0]
        mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(year+l_l2[0][-1]))
        all_slots=mycursor.fetchall()
        #print(all_slots)
        mycursor.execute('''CREATE TABLE IF NOT EXISTS {} 
                            (days VARCHAR(45) NOT NULL,
                            slot1 VARCHAR(45) DEFAULT NULL,
                            slot2 VARCHAR(45) DEFAULT NULL,
                            slot3 VARCHAR(45) DEFAULT NULL,
                            slot4 VARCHAR(45) DEFAULT NULL,
                            slot5 VARCHAR(45) DEFAULT NULL,
                            slot6 VARCHAR(45) DEFAULT NULL)'''.format(rn))
        mycursor.execute('select * from {}'.format(rn))
        p=mycursor.fetchall()
        if len(p)==0:
            mycursor.execute("INSERT INTO {}(days) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(rn))
   
        mycursor.execute("SELECT slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(rn))
        t_slots=mycursor.fetchall()
        
        number=len(hss[rn])
        cv=avail(r)
        h=dict[r][-1]
        for i in range(5):
                for j in range(6):
                    if sub in all_slots[i][j]:
                        if j==0 or j==2 or j==4:
        
                            if t_slots[i][j]==None and t_slots[i][j+1]==None and number<3:#and cv>(30-h):
                                mycursor.execute("UPDATE {} SET slot{}='{}' WHERE days='{}'".format(rn,(j+1),sub,days[i]))
                                del l_l2[0]
                        elif j==1 or j==3 or j==5:
     
                            if t_slots[i][j]==None and t_slots[i][j-1]==None and number<3: #and cv>(30-h):
                                mycursor.execute("UPDATE {} SET slot{}='{}' WHERE days='{}'".format(rn,(j+1),sub,days[i]))
                                del l_l2[0]