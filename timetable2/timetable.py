import mysql.connector
import random as r
import functions.lab_functions as lab
import functions.theory_functions as theory
import functions.classroom as clsroom
import guiFunctions as guiF 
# import gui.xlsxRead as xlr
import guiCalendar5v2 as cal_gui
from functions.theory1 import *
from functions.labs1  import *
from functions.te_tt_lab import *
from functions.te_tt_theory import *



mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Ayush_Chanekar23",
    database="ttproject",
    autocommit=True)


c=mydb.cursor()

#static variables declaration for testing purposes
year='SE'
no_of_divs=4

c.execute("drop database if exists ttproject")
c.execute("create database ttproject")
c.execute("use ttproject")


days=['Monday','Tuesday','Wednesday','Thursday','Friday']


###------------------------------------------------------------------###

#lab, extra and theory subjects static declaration

cal_gui.cal_ui("SE")
Lsubs={"DEL":['A1202','A1203',1],"DSL":['A1204','A1208','A1209','A1107','A1303',2],'OOPCGL':['A1216','A1314','A1302A','A1202','A1204','A1302B','A2303','A1307','A2302','A1303',2],"BCSL":['A1107','A1202','A1203','A1204','A1208','A1209','A1216','A1302A','A1302B','A1303','A1306','A1307','A1314','A2302','A2303',1]}
Esubs={"HSS":['A1107','A1311','A1309','A1310','A1010','A1211','A1212','A1213','A1202','A1203','A1204','A1208','A1209','A1216','A1302A','A1302B','A1303','A1306','A1307','A1314','A2302','A2303',1]}
t_subs={'DM':3,'DELD':3,'CG':3,'FDS': 3,'OOP':3}
se_class=['A1211','A1212','A1213']
Lsubs.update(guiF.lab_data)
t_subs.update(guiF.sete_theory)
Esubs.update(guiF.extra_sub)
print(Esubs)
se_class = guiF.class_data
guiF.extra_sub_list.remove(1)

# cal_gui.cal_ui("TE")
L_subs_te={'LP1':['A1306','A2302','A1307','A1107','A2303',2],'DBMSL':['A1204','A1302B','A1302A','A1303','A2303','A1216',2],'CNSL':['A1302A','A1216','A1314','A1107','A1203','A1306',1]}
t_subs_te={'DBMS':3,'TOC':3,'SPOS':3,'CNS':3}
te_class=['A1309','A1310','A1311']
# L_subs_te.update(guiF.lab_data)
# t_subs.update(guiF.sete_theory)
# te_class = guiF.class_data

H_subs={'ICS':1,'DSV':1,'CS':1}
H_class=['A1309','A1310','A1311']
Elective={'DS':3,'IOT':1,'HCI':1}
elective_rooms=['A1212','A1213','A1311','A1309','A1310']

n_lab_se=0
n_lab_te=0
labs_se=Lsubs.copy()
labs_se.update(Esubs)
for i in labs_se.values():
    n_lab_se+=i[-1]
    print(n_lab_se)

for i in L_subs_te.values():
    n_lab_te+=i[-1]

print(n_lab_se, n_lab_te)
se_theory={'cls': se_class}
te_theory={'cls': te_class}
common=[]
se_sep=[]
se,te=[],[]
full=Lsubs.copy()
full.update(Esubs)
full.update(se_theory)
for i in full.values():
    for j in i:
        if j not in se:
            se.append(j)

te_full=L_subs_te.copy()
te_full.update(te_theory)
for i in te_full.values():
    for j in i:
        if j not in te:
            te.append(j)

for i in se:
    if i in te:
        common.append(i)
    else:
        se_sep.append(i)


d={"swjadhav":["FDS","DSL"],"gvkale":["DM"],"pakhadkikar":["OOP","OOPCGL"],"adbundele":["DELD","DEL","BCSL"],
        "mstakalikar":["CG","OOPCGL"],"psjoshi":["DSL","FDS"],"sngirme":["DSL"],"jsmahajan":["DSL","DM"],"sshah":["OOPCGL","CG","BCSL"],
        "pjjambhulkar":["OOPCGL","BCSL","OOP"],"yahandge":["OOPCGL","OOP"],"rjadhav":["DEL","DELD"],"nykapadnis":["DEL","DELD"],
        "ptkohok":["DEL","DELD"],"psvidap":["BCSL"],"vvbagade":["BCSL"],"sssonawane":["DM","DSL"],"prmakkar":["FDS","DSL","BCSL"],
        "ddbhaiya":["CG","BCSL","OOPCGL"],"aadeshpande":["DSL","DM"],"uspawar":["OOPCGL"],"rkulkarni":["OOPCGL","CG"],"kcwaghmare":["DSL","FDS"],
        "rrnavghare":["BCSL"],"mrjansari":["BCSL"],"rspaswan":["OOP","OOPCGL"],"ssshentekar":["BCSL"],"aachandorkar":["BCSL"]}



dict_2={"basonkamble":["DBMS"],"spshintre":["TOC","LP1"],"aachandorkar":["SPOS","LP1"],"prpatil":["CNS","CNSL"],"sngirme":["ELECTIVEDS"],"ssshevtekar":["ELECTIVEDS","LP1"],
        "mvmane":["ELECTIVEDS","LP1"],"uspawar":["ELECTIVEHCI"],"mswakode":["ELECTIVEIOT","lp1"],"prmakkar":["HONOURSDSV"],"vsgaikwad":["HONOURSCS","DBMSL","DBMS"],"pajain":["HONOURSICS","CNSL","CNS"],
        "kurane":["DBMSL"],"ppjoshi":["DBMSL","DBMS"],"vvbagade":["DBMSL"],"rrnavghare":["LP1","TOC"],"psvidap":["LP1","SPOS"],"mrjansari":["LP1","SPOS"],"mschavan":["CNSL","CNS"],"bpmasram":["CNSL","CNS","LP1"],
        "agphakatkar":["DBMS","DBMSL"],"ptkohok":["DBMSL"],"vkandekar":["DBMSL"],"rakulkarni":["LP1","SPOS"],"gppotdar":["TOC"],"kgangrade":["SPOS"],"rjadhav":["DBMSL"],"yahandge":["DBMSL"],
        "nykapadnis":["DBMSL"]}



labs1=[("CNSL",1),("LP1",2),("DBMSL",2)]
subjects1=[("DBMS",3),("TOC",3),("CNS",3),("SPOS",3)]
labs=[("DSL",2),("OOPCGL",2),("DEL",1),("BCSL",1)]
subjects=[('FDS',3),('OOP',3),('CG',3),('DM',3),('DELD',3)]

se_lab_subs=[]
for i in labs:
    se_lab_subs.append(i[0])
se_theory_subs=[]
for i in subjects:
    se_theory_subs.append(i[0])

se_subs=se_lab_subs+se_theory_subs



tables=d.keys()
tables2=dict_2.keys()

print()
subs=list(Lsubs.keys())+list(Esubs.keys())+list(t_subs.keys())


clear_count=0
def clear_se():
    c.execute('show tables')
    p=c.fetchall()

    tables=[]
    for i in p:
        tables.append(i[0])
    c.execute('drop table se1,se2,se3,se4')
    for i in se_sep:
        c.execute('drop table if exists {}'.format(i))
    for j in common:
        if j in tables:
            c.execute("select slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(j))
            all_slots=c.fetchall()
            for k in range(5):
                for m in range(6):
                    if all_slots[k][m]:
                        for n in subs:
                            if n in all_slots[k][m]:
                                c.execute("update {} set {}=NULL where day='{}'".format(j,'slot'+str(m+1),days[k]))
                                break
    c.execute('show tables')
    p=c.fetchall()
    tables=[]
    for i in p:
        tables.append(i[0])
    for j in ['A1212','A1213','A1211']:
        if j in tables:
            c.execute("select slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(j))
            all_slots=c.fetchall()
            for k in range(5):
                for m in range(6):
                    if all_slots[k][m]:
                            if all_slots[k][m] in ['se1','se2','se3','se4']:
                                c.execute("update {} set {}=NULL where day='{}'".format(j,'slot'+str(m+1),days[k]))




    for i in range(no_of_divs):
        name=year+str(i+1)
        c.execute('''create table if not exists {}(
        day varchar(10) not null,
        slot1 varchar(100) default null,
        slot2 varchar(100) default null,
        slot3 varchar(100) default null,
        slot4 varchar(100) default null,
        slot5 varchar(100) default null,
        slot6 varchar(100) default null)
        '''.format(name))
        c.execute('''insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')'''.format(name))




def full_lab(class_div,Lsubs):
    div=class_div[-1]
    for i in ['e','f','g','h']:
        a=lab.assignlab(class_div,i+div,Lsubs,div)
        if a==0:
            return 0
    print('lab subs ',class_div)

def full_extra(class_div,Esubs,ext):

    div=class_div[-1]
    for i in ['e','f','g','h']:
        a=lab.assign_extra(class_div,i+div,Esubs,div)
        if a==0:
            return 0
        
    print("extra ", class_div," done")





# -----------------------------------
for i in range(no_of_divs):
            name='TE'+str(i+1)
            c.execute('''create table {}(
            day varchar(10) not null,
            slot1 varchar(120) default null,
            slot2 varchar(120) default null,
            slot3 varchar(120) default null,
            slot4 varchar(120) default null,
            slot5 varchar(120) default null,
            slot6 varchar(120) default null,
            slot7 varchar(120) default null)
            '''.format(name))
            c.execute('''insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')'''.format(name))


for i in range(no_of_divs):
        name=year+str(i+1)
        c.execute('''create table if not exists {}(
        day varchar(10) not null,
        slot1 varchar(100) default null,
        slot2 varchar(100) default null,
        slot3 varchar(100) default null,
        slot4 varchar(100) default null,
        slot5 varchar(100) default null,
        slot6 varchar(100) default null)
        '''.format(name))
        c.execute('''insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')'''.format(name))

def clear_te_lab():
    for i in range(1,5):
        c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format('te'+str(i)))
        all_slots=c.fetchall()
        for j in range(5):
            for k in range(6):
                if all_slots[j][k]:
                    for sub in L_subs_te.keys():
                        if sub in all_slots[j][k]:
                            c.execute('update {} set {}=NULL where day="{}"'.format('te'+str(i),'slot'+str(k+1),days[j]))

    c.execute('show tables')
    p=c.fetchall()
    tables=[]
    for i in p:
        tables.append(i[0])
    rooms=[]
    for i in L_subs_te.values():
        rooms+=i
    rooms=set(rooms)
    for i in rooms:
        if i in tables:
            c.execute('drop table {}'.format(i))

def clear_se_lab():
    subs=list(Lsubs.keys())+list(Esubs.keys())
    full=Lsubs.copy()
    full.update(Esubs)
    for i in range(1,5):
        c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format('se'+str(i)))
        all_slots=c.fetchall()
        for j in range(5):
            for k in range(6):
                if all_slots[j][k]:
                    for s in subs:
                        if s in all_slots[j][k] and '(' not in all_slots[j][k]:
                            c.execute('update {} set {}=NULL where day = "{}"'.format('se'+str(i),'slot'+str(k+1),days[j]))
    c.execute('show tables')
    p=c.fetchall()
    tables=[]
    for i in p:
        tables.append(i[0])
    rooms=[]
    for i in full.values():
        rooms+=i
    rooms=set(rooms)
    for i in rooms:
        if i in tables:
            c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format(i))
            lab_slots=c.fetchall()
            for j in range(5):
                for k in range(6):
                    if lab_slots[j][k]:
                        for s in subs:
                            if s in lab_slots[j][k]:
                                c.execute('update {} set {}=NULL where day = "{}"'.format(i,'slot'+str(k+1),days[j]))



def clear_se_teachers():
    c.execute('show tables')
    p=c.fetchall()
    all_tables=[]
    for i in p:
        all_tables.append(i[0])
    for i in tables:
        if i not in tables2:
            c.execute('drop table if exists {}'.format(i))
    
    for i in tables2:
        if i in tables:
            if i in all_tables:
                c.execute('select * from {} '.format(i))
                teacher=c.fetchall()
                day=-1
                for m in teacher:
                    day+=1
                    slot=-1
                    for j in m:
                        slot+=1
                        if j!=None:
                            for k in se_subs:
                                if k in j:
                                    c.execute('update {} set {}=NULL where days="{}"'.format(i,'slot'+str(slot),days[day]))





while True:
    p=1
    check=0
    te_lab_block=0
    te_clear_count=0
    while True:
        if p==1:
            print('clearing te')
            c.execute("drop database if exists ttproject")
            c.execute("create database ttproject")
            c.execute("use ttproject")
            for i in range(no_of_divs):
                name='TE'+str(i+1)
                c.execute('''create table {}(
                day varchar(10) not null,
                slot1 varchar(120) default null,
                slot2 varchar(120) default null,
                slot3 varchar(120) default null,
                slot4 varchar(120) default null,
                slot5 varchar(120) default null,
                slot6 varchar(120) default null,
                slot7 varchar(120) default null)
                '''.format(name))
                c.execute('''insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')'''.format(name))

            
            p=0
        if te_lab_block==1:
            te_clear_count+=1
            if te_clear_count==4:
                te_clear_count=0
                p=1
                te_lab_block=0
                continue
            te_lab_block=0
            clear_te_lab()
        else:
            lab.assign_elective_slot()
            lab.assign_elective('E',Elective,elective_rooms)
            lab.assign_honor_slot()
            
            lab.assign_elective('H',H_subs,H_class)
            lab.lab_slot_allotment('te','1',n_lab_te,2)
            lab.lab_slot_allotment('te','2',n_lab_te,3)
            lab.lab_slot_allotment('te','3',n_lab_te,2)
            lab.lab_slot_allotment('te','4',n_lab_te,3)

            

            for i in ['1','2','3','4']:
                theory.theory_slot('TE'+i)
                theory.assign_theory_te('TE'+i,t_subs_te)
                clsroom.assign_remedial_te('TE'+i)
                c1=clsroom.assign_classroom('TE'+i,te_class,t_subs_te)
                if c1==0:
                    break
            if c1==0:
                p=1
                continue
        


        for i in ['1','2','3','4']:
            for j in ['k','l','m','n']:
                t=lab.assignlab('TE'+i,j+i,L_subs_te,i)
                if t==0:
                    te_lab_block=1
                    break
        
        if te_lab_block==1:
            continue
     

        print('TE done')
        p=1
        break

    x=0


   

    for i in tables:
        c.execute('drop table if exists {}'.format(i))
    for j in tables2:
        c.execute('drop table if exists {}'.format(j))
    
    counter=0
    m=0
    while True:
        if x==1:
            if counter==10:
                m=1
                break
            for i in tables:
                c.execute('drop table if exists {}'.format(i))
            for j in tables2:
                c.execute('drop table if exists {}'.format(j))
            x=0
        c1=te_theory_assign(d,dict_2,"TE",subjects1)
        if c1==0:
            x=1
            counter+=1
            continue
        print("Theory TE")
        a=te_lab_assign(d,dict_2,"TE",labs1)
        if a==0:
            x=1
            counter+=1
            continue
        print("Labs TE")
        break

    if m==1:
        continue




    for i in range(no_of_divs):
        name=year+str(i+1)
        c.execute('''create table if not exists {}(
        day varchar(10) not null,
        slot1 varchar(100) default null,
        slot2 varchar(100) default null,
        slot3 varchar(100) default null,
        slot4 varchar(100) default null,
        slot5 varchar(100) default null,
        slot6 varchar(100) default null)
        '''.format(name))
        
        c.execute('''insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')'''.format(name))


    c.execute('drop table if exists templabse1,templabse2,templabse3,templabse4')
    m=0
    lab_clear=0
    lab_clear_count=0
    x=0
    while True:
        if x==1:
            if m>=6:
                break
            print('clearing se')
            clear_se()  
            x=0
        if lab_clear==1:
            lab_clear_count+=1
            if lab_clear_count>=4 or lab_clear_count<0:
                m+=1
                lab_clear_count=0
                lab_clear=0
                x=1
                continue
            lab_clear=0
            clear_se_lab()

        else:
            c.execute('drop table if exists templabse1,templabse2,templabse3,templabse4')
            lab.lab_slot_allotment('se','1',n_lab_se,1)
            lab.lab_slot_allotment('se','2',n_lab_se,1)
            lab.lab_slot_allotment('se','3',n_lab_se,1)
            lab.lab_slot_allotment('se','4',n_lab_se,1)

            for i in ['1','2','3','4']:
                theory.theory_slot('SE'+i)
                theory.assign_theory('SE'+i,t_subs)
                a=clsroom.assign_classroom('SE'+i,se_class,t_subs)
                clsroom.assign_remedial('SE'+i)
                if a==0:
                    break
            
            if a==0:
                x=1
                continue
            
            print('classrooms done')

        

        
        print()
        for i in ('se1','se2','se3','se4'):
            b=full_lab(i,Lsubs)
            if b==0:
                lab_clear=1
                break
        if lab_clear==1:
            continue
        
        c1=full_extra('se1',Esubs,'1')
        if c1==0:
            lab_clear=1
            lab_clear_count-=1
            continue
        c2=full_extra('se2',Esubs,'2')
        if c2==0:
            lab_clear=1
            continue
        c3=full_extra('se3',Esubs,'3')
        if c3==0:
            lab_clear=1
            lab_clear_count-=1
            continue
        c4=full_extra('se4',Esubs,'4')
        if c4==0:
            lab_clear=1
            m-=1
            lab_clear_count-=2
            continue
            


        

        
        m=0
        counter=0
        x=0
        while True:
            if x==1:
                if counter==20:
                    break
                clear_se_teachers()

            d1=theory_assign(d,"SE",subjects)
            if d1==0:
                x=1
                print()
                counter+=1
                continue
            print("Theory SE")
            b=lab_assign(d,"SE",labs)
            if b==0:
                x=1
                print()
                counter+=1
                continue
            print("Labs SE")
            print("Lab teacher assigned")
            break
        
        if counter==20:
            x=1
            m=0
            lab_clear_count=0
            continue
        break

    if m>=6:
        continue
    break
print('YAYYY')



print("YAYYY")
