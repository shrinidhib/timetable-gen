import mysql.connector
import random as r

mydb=mysql.connector.connect(host="localhost",
    username="root",
    password="Ayush_Chanekar23",
    database="ttproject",
    autocommit=True)
c=mydb.cursor()

days=['Monday','Tuesday','Wednesday','Thursday','Friday']

def lab_slot_allotment(class_year,ext,n,over_count):

    #overcount is 1 for se, 2 for te
    c.execute('''create table if not exists {}(
    day varchar(10) not null,
    slot1 varchar(20) default null,
    slot2 varchar(20) default null,
    slot3 varchar(20) default null)
    '''.format('templab'+class_year+ext))
    c.execute('select * from {}'.format('templab'+class_year+ext))
    p=c.fetchall()
    if len(p)==0:

        st="insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format('templab'+class_year+ext)
        c.execute(st)
    slots_alloted=0
    while slots_alloted<n:
        if ext=='4':
            for i in range(5):
                for j in range(1,4):
                    if slots_alloted<n:
                        c.execute("select {} from {} where day='{}'".format('slot'+str(j),'templab'+class_year+ext,str(days[i])))
                        slot_availability=c.fetchall()[0][0] 
                        st="select slot1,slot2,slot3 from {} where day='{}'".format('templab'+class_year+ext,days[i])
                        c.execute(st)
                        overburden_check=c.fetchall()[0] 
                        if (slot_availability==None) and (overburden_check.count(None)>1):
                            if class_year=='TE':
                                x=0
                                for i in overburden_check:
                                    if i!=None:
                                        if 'ELECTIVE' in i or 'HONOURS' in i:
                                            x+=1
                                if x>1:
                                    continue
                        c.execute("select {} from {} where day='{}'".format('slot'+str((j*2)-1),class_year+'1', days[i]))
                        s1=c.fetchall()[0][0]
                        c.execute("select {} from {} where day='{}'".format('slot'+str((j*2)-1),class_year+'2',days[i]))
                        s2=c.fetchall()[0][0]
                        c.execute("select {} from {} where day='{}'".format('slot'+str((j*2)-1),class_year+'3',days[i]))
                        s3=c.fetchall()[0][0]
                        c.execute("select {} from {} where day='{}'".format('slot'+str((j*2)-1),class_year+'4',days[i]))
                        s4=c.fetchall()[0][0]
                        l=[s1,s2,s3,s4]

                        if l.count(None)>over_count:
                            c.execute('select {} from {} where day="{}"'.format('slot'+str(j),'templab'+class_year+'1',days[i]))
                            c1=c.fetchall()[0][0]
                            c.execute('select {} from {} where day="{}"'.format('slot'+str(j),'templab'+class_year+'2',days[i]))
                            c2=c.fetchall()[0][0]
                            c.execute('select {} from {} where day="{}"'.format('slot'+str(j),'templab'+class_year+'3',days[i]))
                            c3=c.fetchall()[0][0]
                            tot=[c1,c2,c3]
                            if tot.count(None)==3:
                                c.execute("update {} set {}='y' where day='{}'".format('templab'+class_year+ext,'slot'+str(j), days[i]))
                                slots_alloted+=1
                                
        if slots_alloted!=n:
            while slots_alloted<n:
                day=r.randrange(0,5)
                slot=r.randrange(1,4)
                c.execute("select {} from {} where day='{}'".format('slot'+str(slot),'templab'+class_year+ext,str(days[day])))
                slot_availability=c.fetchall()[0][0] 
                st="select slot1,slot2,slot3 from {} where day='{}'".format('templab'+class_year+ext,days[day])
                c.execute(st)
                overburden_check=c.fetchall()[0] 
                if (slot_availability==None) and (overburden_check.count(None)>1):
                    if class_year=='te':
                        x=0
                        for i in overburden_check:
                            if i!=None:
                                if 'ELECTIVE' in i or 'HONOURS' in i:
                                    x+=1
                        if x>1:
                            continue
                    
                    c.execute("select {} from {} where day='{}'".format('slot'+str(slot),class_year+'1', days[day]))
                    s1=c.fetchall()[0][0]
                    c.execute("select {} from {} where day='{}'".format('slot'+str(slot),class_year+'2',days[day]))
                    s2=c.fetchall()[0][0]
                    c.execute("select {} from {} where day='{}'".format('slot'+str(slot),class_year+'3',days[day]))
                    s3=c.fetchall()[0][0]
                    c.execute("select {} from {} where day='{}'".format('slot'+str(slot),class_year+'4',days[day]))
                    s4=c.fetchall()[0][0]
                    l=[s1,s2,s3,s4]

                    if l.count(None)>over_count:
                        if class_year=='SE':
                            c.execute("select {} from {} where day='{}'".format('slot'+str(slot),'templabte1', days[day]))
                            s1=c.fetchall()[0][0]
                            c.execute("select {} from {} where day='{}'".format('slot'+str(slot),'templabte2',days[day]))
                            s2=c.fetchall()[0][0]
                            c.execute("select {} from {} where day='{}'".format('slot'+str(slot),'templabte3',days[day]))
                            s3=c.fetchall()[0][0]
                            c.execute("select {} from {} where day='{}'".format('slot'+str(slot),'templabte4',days[day]))
                            s4=c.fetchall()[0][0]
                            p=[s1,s2,s3,s4]

                            if p.count('y')>=3:
                                x=r.rand(1,3)
                                if x==2:
                                    continue
                        c.execute("update {} set {}='y' where day='{}'".format('templab'+class_year+ext,'slot'+str(slot), days[day]))
                        slots_alloted+=1

                    




def assignlab(class_div,batch,Lsubs,ext):
    for sub,n in Lsubs.items():
        no=n[-1]
        n1=0
        lis_rooms=n[:-1]
        room_count=1
        while n1<no:
            lab_name=sub+batch
            room=r.choice(lis_rooms)

            c.execute('''create table if not exists {}(
                day varchar(10) not null,
                slot1 varchar(20) default null,
                slot2 varchar(20) default null,
                slot3 varchar(20) default null,
                slot4 varchar(20) default null,
                slot5 varchar(20) default null,
                slot6 varchar(20) default null)'''.format(room)
            )
            c.execute('''select count(*) from {}'''.format(room))
            p=c.fetchall()[0][0]
            if p==0:
                c.fetchall()
                c.execute("insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(room))
        
            count=0
            x=0
            while n1<no:
                
                if x==1:
                    count=0
                    room_count+=1
                    room=r.choice(lis_rooms)

                    c.execute('''create table if not exists {}(
                        day varchar(10) not null,
                        slot1 varchar(20) default null,
                        slot2 varchar(20) default null,
                        slot3 varchar(20) default null,
                        slot4 varchar(20) default null,
                        slot5 varchar(20) default null,
                        slot6 varchar(20) default null)'''.format(room))
                    c.execute('''select count(*) from {}'''.format(room))
                    p=c.fetchall()[0][0]
                    if p==0:
                        c.fetchall()
                        c.execute("insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(room))
                    x=0

                if room_count>25:
                    return 0
                count+=1
                c.fetchall()
                c.execute("Select slot1,slot2,slot3 from {}".format('templab'+class_div))
                all_slots=c.fetchall()
                c.execute("select slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(room))
                lab_slots=c.fetchall()
                i=r.randrange(0,5)
                j=r.randrange(0,3)
                if all_slots[i][j]=='y' and lab_slots[i][2*j]==None and lab_slots[i][2*j+1]==None:
                    lab_name=sub+batch
                    c.execute("select day,{},{} from {} where day='{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),class_div,days[i]))
                    
                    empty_check=c.fetchall()[0]
                    if empty_check.count(None)==2 or empty_check.count('')==2 or empty_check.count(' ')==2:
                        c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),lab_name,'slot'+str(2*(j+1)),lab_name,days[i]))
                    elif empty_check.count(None)==1:
                        continue
                    elif batch in empty_check[-1] or batch in empty_check[-2]:
                        continue
                    else:
                        c.execute("select {},{} from {} where day='{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),class_div,days[i]))
                        s1,s2=c.fetchall()[0]
                        s1=remove_spaces(s1)
                        s2=remove_spaces(s2)
                        c.execute("update {} set {}=concat('{}','  ','{}'),{}=concat('{}','  ','{}') where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),s1,lab_name, 'slot'+str(2*(j+1)),s2,lab_name,days[i]))
                    c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)-1),sub+batch,'slot'+str(2*(j+1)),sub+batch,days[i]))
        
                    n1+=1
                if n1<no and count>15:
                        for i in range(5):
                            for j in range(3):
                                c.execute("select slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(room))
                                lab_slots=c.fetchall()
                                if (all_slots[i][j]=='y') and ((lab_slots[i][2*j]==None or lab_slots[i][2*j]==' ') and lab_slots[i][2*j+1]==None or lab_slots[i][2*j+1]==' '):
                                    
                                    c.execute("select day,{},{} from {} where day='{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),class_div,days[i]))
                                    empty_check=c.fetchall()[0]
                                    if empty_check.count(None)==2 or empty_check.count('')==2 or empty_check.count(' ')==2:
                                        c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),lab_name,'slot'+str(2*(j+1)),lab_name,days[i]))
                                    elif empty_check.count(None)==1:
                                        continue
                                    elif batch in empty_check[-1] or batch in empty_check[-2]:
                                        continue
                                    else:
                                        c.execute("select {},{} from {} where day='{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),class_div,days[i]))
                                        s1,s2=c.fetchall()[0]
                                        s1=remove_spaces(s1)
                                        s2=remove_spaces(s2)
                                        c.execute("update {} set {}=concat('{}','  ','{}'),{}=concat('{}','  ','{}') where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),s1,lab_name, 'slot'+str(2*(j+1)),s2,lab_name,days[i]))
                                    c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)-1),sub+batch,'slot'+str(2*(j+1)),sub+batch,days[i]))

                                    n1+=1
                                if n1==no:
                                    break         
                            if n1==no:
                                break
                        if n1!=no:
                            x=1
                            for i in range(5):
                                for j in range(3):
                                    c.execute("select slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(room))
                                    lab_slots=c.fetchall()
                                    c.execute("select {},{} from {} where day='{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),class_div,days[i]))
                                    x1,x2=c.fetchall()[0]
                                    if x1!=None and x2!=None:
                                        if lab_slots[i][2*j]==sub+batch and lab_name in x1 and lab_name in x2 :
                                            c.fetchall()
                                            c.execute("update {} set {}=NULL, {}=NULL where day='{}'".format(room,'slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),days[i]))
                                            c.fetchall()
                                            n1-=1                                                                
                                            c.execute("update {} set {}='{}', {}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),x1.replace(lab_name,''),'slot'+str(2*(j+1)),x2.replace(lab_name,''),days[i]))
                            continue


                    


def assign_extra(class_div,batch,E_subs,ext):
    for sub,n in E_subs.items():
        no=n[-1]
        n1=0
        c1=0      
        while n1<no:
            c1+=1
            if c1>50:
                return 0
            lis_rooms=n[:-1]
            room=r.choice(lis_rooms)
    

            c.execute('''create table if not exists {}(
                day varchar(10) not null,
                slot1 varchar(20) default null,
                slot2 varchar(20) default null,
                slot3 varchar(20) default null,
                slot4 varchar(20) default null,
                slot5 varchar(20) default null,
                slot6 varchar(20) default null)'''.format(room)
            )
            c.execute('''select count(*) from {}'''.format(room))
            p=c.fetchall()[0][0]
            if p==0:
                c.fetchall()
                c.execute("insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(room))
        
            count=0
            while n1<no:
              
                
                count+=1
                c.fetchall()
                c.execute("Select slot1,slot2,slot3 from {}".format('templab'+class_div))
                all_slots=c.fetchall()
        
                c.execute("select slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(room))
                lab_slots=c.fetchall()
                i=r.randrange(0,5)
                j=r.randrange(0,3)
                if all_slots[i][j]=='y' and (lab_slots[i][2*j]==None or lab_slots[i][2*j+1]==None):
                    lab_name=sub+batch
                    c.fetchall()
                    c.execute("select day,{},{} from {} where day='{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),class_div,days[i]))
                    empty_check=c.fetchall()[0]

                    x=0
                    if empty_check.count(None)==2:
                        if j==0:
                            x=2
                        elif j==2:
                            x=1
                        else:
                            x=r.randrange(1,3)
                        if x==1 and lab_slots[i][2*j]==None:
                            c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),lab_name,days[i]))
                            c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)-1),sub+batch,days[i]))
        
                        elif x==2 and lab_slots[i][2*j+1]==None:
                            c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)), lab_name,days[i]))
                            c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)),sub+batch,days[i]))        
                        else:
                            continue
                    elif  empty_check.count(None)==1:
                        if empty_check[1]==None and lab_slots[i][2*j]==None:
                            c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),lab_name,days[i]))
                            c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)-1),sub+batch,days[i]))
                        elif empty_check[2]==None and lab_slots[i][2*j+1]==None:
                            c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)),lab_name,days[i]))
                            c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)),sub+batch,days[i]))  
                        else:
                            continue      

                    elif batch in empty_check[-1] or batch in empty_check[-2]:
                        continue
                    else:
                        if j==0:
                            x=2
                        elif j==2:
                            x=1
                        else:
                            x=r.randrange(1,3)
                        if x==1:
                            if lab_slots[i][2*j]==None:

                                c.execute("update {} set {}=concat({},'  ','{}') where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1),lab_name,days[i]))
                                c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)-1),sub+batch,days[i]))
                            else:
                                continue
                        elif x==2:
                            if lab_slots[i][2*j+1]==None:
                                c.execute("update {} set {}=concat({},'  ','{}') where day='{}'".format(class_div,'slot'+str(2*(j+1)),'slot'+str(2*(j+1)),lab_name,days[i]))
                                c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)),sub+batch,days[i]))        
                            else:
                                continue
                    n1+=1
                if n1==no:
                    break
                if n1<no and count>15:
                    count2=0
                    while n1<no:
             
                        count2+=1
                        for i in range(5):
                            if n1==no:
                                break
                            for j in range(3):
                                if (all_slots[i][j]=='y') and ((lab_slots[i][2*j]==None or lab_slots[i][2*j+1] )):
                                    lab_name=sub+batch
                                    c.execute("select day,{},{} from {} where day='{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),class_div,days[i]))
                                    empty_check=c.fetchall()[0]
                                    if empty_check.count(None)==2:
                                        if j==0:
                                            x=2
                                        elif j==2:
                                            x=1
                                        else:
                                            x=r.randrange(1,3)
                           
                                        if x==1 and lab_slots[i][2*j]==None:
                                            c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),lab_name,days[i]))
                                            c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)-1),sub+batch,days[i]))
                        
                                        elif x==2 and lab_slots[i][2*j+1]==None:
                                            c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)), lab_name,days[i]))
                                            c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)),sub+batch,days[i]))        
                                        else:
                                            continue
                                    elif empty_check.count(None)==1:
                                        if empty_check[1]==None and lab_slots[i][2*j]==None:
                                            c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),lab_name,days[i]))
                                            c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)-1),sub+batch,days[i]))
                                        elif empty_check[2]==None and lab_slots[i][2*j+1]==None:
                                            c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(2*(j+1)),lab_name,days[i]))
                                            c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)),sub+batch,days[i])) 
                                        else:
                                            continue       

                                    elif batch in empty_check[-1] or batch in empty_check[-2] :
                                        continue
                                 
                                    else:
                                        if j==0:
                                            x=2
                                        elif j==2:
                                            x=1
                                        else:
                                            x=r.randrange(1,3)
                                        if x==1:
                                            if lab_slots[i][2*j]==None:

                                                c.execute("update {} set {}=concat({},'  ','{}') where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1),lab_name,days[i]))
                                                c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)-1),sub+batch,days[i]))
                                            else:
                                                continue
                                        elif x==2:
                                            if lab_slots[i][2*j+1]==None:
                                                c.execute("update {} set {}=concat({},'  ','{}') where day='{}'".format(class_div,'slot'+str(2*(j+1)),'slot'+str(2*(j+1)),lab_name,days[i]))
                                                c.execute("update {} set {}='{}' where day='{}'".format(room,'slot'+str(2*(j+1)),sub+batch,days[i]))        
                                            else:
                                                continue
                                    n1+=1


                                    if n1==no:
                                        break
                       
                        break
                    break
                


def assign_elective_slot():
    #class_div - TE3
    c.execute('''create table if not exists templabte1(
    day varchar(10) not null,
    slot1 varchar(20) default null,
    slot2 varchar(20) default null,
    slot3 varchar(20) default null,
    slot4 varchar(20) default null)
    ''')
    st="insert into templabte1(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')"
    c.execute(st)
    c.execute('''create table  if not exists templabte2(
    day varchar(10) not null,
    slot1 varchar(20) default null,
    slot2 varchar(20) default null,
    slot3 varchar(20) default null,
    slot4 varchar(20) default null)
    ''')
    st="insert into templabte2(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')"
    c.execute(st)
    c.execute('''create table  if not exists templabte3(
    day varchar(10) not null,
    slot1 varchar(20) default null,
    slot2 varchar(20) default null,
    slot3 varchar(20) default null,
    slot4 varchar(20) default null)
    ''')
    st="insert into templabte3(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')"
    c.execute(st)
    c.execute('''create table if not exists templabte4 (
    day varchar(10) not null,
    slot1 varchar(20) default null,
    slot2 varchar(20) default null,
    slot3 varchar(20) default null,
    slot4 varchar(20) default null)
    ''')
    st="insert into templabte4(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')"
    c.execute(st)
    
    c.execute('select * from templabte1')
    full=c.fetchall()
    e_alloted=0
    day=r.randrange(0,5)
    slot=3
    c.execute('update templabte1 set {}="E" where day="{}"'.format('slot'+str(slot), days[day]))
    c.execute('update templabte2 set {}="E" where day="{}"'.format('slot'+str(slot), days[day]))
    c.execute('update templabte3 set {}="E" where day="{}"'.format('slot'+str(slot), days[day]))
    c.execute('update templabte4 set {}="E" where day="{}"'.format('slot'+str(slot), days[day]))
    e_count=1
    while e_count<3:
        day=r.randrange(0,5)
        c.execute('select slot4 from templabte1 where day="{}"'.format( days[day]))
        val=c.fetchall()[0][0]
        if val==None:
            c.execute('update templabte1 set slot4="E" where day="{}"'.format(days[day]))
            c.execute('update templabte2 set slot4="E" where day="{}"'.format(days[day]))
            c.execute('update templabte3 set slot4="E" where day="{}"'.format(days[day]))
            c.execute('update templabte4 set slot4="E" where day="{}"'.format(days[day]))
            e_count+=1


def assign_elective(category,E_subs,classrooms):
    c.execute('select slot1,slot2,slot3,slot4 from templabte1')
    elective_slots=c.fetchall()
    for sub,batch in E_subs.items():
        k=0
        if category=='E':
            up=3
        else:
            up=2
        ds=100
        
        
        for i in range(5):
            if k==up:
                break
            for j in range(4):
                if k==up:
                    break
                if elective_slots[i][j]==category:
                    
                    cp=0
                    if batch>1:
                        no=0
                        while no<batch:
                            cp=1
                            clsroom=r.choice(classrooms)
                            c.execute('''create table if not exists {}(day varchar(10) not null,
                        slot1 varchar(100) default null,
                        slot2 varchar(100) default null,
                        slot3 varchar(100) default null,
                        slot4 varchar(100) default null,
                        slot5 varchar(100) default null,
                        slot6 varchar(100) default null,
                        slot7 varchar (100) default null)'''.format(clsroom))
                            c.execute('select * from {}'.format(clsroom))
                            p=c.fetchall()
                            if len(p)==0:
                                st="insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(clsroom)
                                c.execute(st)
                            if j==3:
                                c.fetchall()
                                c.execute('select slot1,slot2,slot3,slot4,slot5,slot6,slot7 from te1')
                                all_slots=c.fetchall()
                                if all_slots[i][6]==None:
                                    c.execute('select slot7 from {} where day="{}"'.format(clsroom,days[i]))
                                    result=c.fetchall()[0][0]
                                    if result==(None):
                                            c.execute("update TE1 set slot7='{}' where day = '{}'".format('ELECTIVE '+sub+'('+clsroom+')', days[i]))
                                            c.execute("update {} set slot7='{}' where day='{}'".format(clsroom, sub,days[i]))
                                            c.execute("update TE2 set slot7='{}' where day = '{}'".format('ELECTIVE '+sub+'('+clsroom+')', days[i]))
                                            c.execute("update TE3 set slot7='{}' where day = '{}'".format('ELECTIVE '+sub+'('+clsroom+')', days[i]))
                                            c.execute("update TE4 set slot7='{}' where day = '{}'".format('ELECTIVE '+sub+'('+clsroom+')', days[i]))
                                            no+=1

                                        
                                else: 
                                    if sub in all_slots[i][6]:
                                        c.execute('select slot7 from {} where day="{}"'.format(clsroom,days[i]))
                                        result=c.fetchall()[0][0]
                                        if result==(None):
                                            c.execute("update TE1 set slot7=concat(slot7,'{}') where day = '{}'".format('('+clsroom+')', days[i]))
                                            c.execute("update {} set slot7='{}' where day='{}'".format(clsroom, sub,days[i]))
                                            c.execute("update TE2 set slot7=concat(slot7,'{}') where day = '{}'".format('('+clsroom+')', days[i]))
                                            c.execute("update TE3 set slot7=concat(slot7,'{}') where day = '{}'".format('('+clsroom+')', days[i]))
                                            c.execute("update TE4 set slot7=concat(slot7,'{}') where day = '{}'".format('('+clsroom+')', days[i]))
                                            no+=1
                                        

                                
                            else:
                                c.fetchall()
                                c.execute('select slot1,slot2,slot3,slot4,slot5,slot6,slot7 from te1')
                                all_slots=c.fetchall()
                                if all_slots[i][2*j]==None:
                                    c.execute('select {},{} from {} where day="{}"'.format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),clsroom,days[i]))
                                    result=c.fetchall()[0]
                                    if result==(None,None):
                                        c.execute("update TE1 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1),'ELECTIVE '+ sub+'('+clsroom+')','slot'+str(2*(j+1)), 'ELECTIVE '+sub+'('+clsroom+')',days[i]))
                                        c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(clsroom, 'slot'+str(2*(j+1)-1), sub,'slot'+str(2*(j+1)),sub,days[i]))
                                        c.execute("update TE2 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), 'ELECTIVE '+sub+'('+clsroom+')','slot'+str(2*(j+1)),'ELECTIVE '+ sub+'('+clsroom+')',days[i]))
                                        c.execute("update TE3 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), 'ELECTIVE '+sub+'('+clsroom+')','slot'+str(2*(j+1)), 'ELECTIVE '+sub+'('+clsroom+')',days[i]))
                                        c.execute("update TE4 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), 'ELECTIVE '+sub+'('+clsroom+')','slot'+str(2*(j+1)),'ELECTIVE '+ sub+'('+clsroom+')',days[i]))
                                        no+=1
                                        

                                else:
                                    if sub in all_slots[i][2*j]:
                                        c.execute('select {},{} from {} where day="{}"'.format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),clsroom,days[i]))
                                        result=c.fetchall()[0]
                                        if result==(None,None):
                                            c.execute("update TE1 set {}=concat({},'{}'), {}=concat({},' ','{}') where day = '{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), '('+clsroom+')','slot'+str(2*(j+1)),'slot'+str(2*(j+1)), '('+clsroom+')',days[i]))
                                            c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(clsroom, 'slot'+str(2*(j+1)-1), sub,'slot'+str(2*(j+1)),sub,days[i]))
                                            c.execute("update TE2 set {}=concat({},'{}'), {}=concat({},' ','{}') where day = '{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), '('+clsroom+')','slot'+str(2*(j+1)),'slot'+str(2*(j+1)), '('+clsroom+')',days[i]))
                                            c.execute("update TE3 set {}=concat({},'{}'), {}=concat({},' ','{}') where day = '{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), '('+clsroom+')','slot'+str(2*(j+1)),'slot'+str(2*(j+1)), '('+clsroom+')',days[i]))
                                            c.execute("update TE4 set {}=concat({},'{}'), {}=concat({},' ','{}') where day = '{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), '('+clsroom+')','slot'+str(2*(j+1)),'slot'+str(2*(j+1)), '('+clsroom+')',days[i]))
                                            no+=1
                                            



                    if cp==1:
                        k+=1
                    else:
                        while True: 
                            clsroom=r.choice(classrooms)
                            c.execute('''create table if not exists {}(day varchar(10) not null,
                        slot1 varchar(100) default null,
                        slot2 varchar(100) default null,
                        slot3 varchar(100) default null,
                        slot4 varchar(100) default null,
                        slot5 varchar(100) default null,
                        slot6 varchar(100) default null,
                        slot7 varchar (100) default null)'''.format(clsroom))
                            c.execute('select * from {}'.format(clsroom))
                            p=c.fetchall()
                            if len(p)==0:
                                st="insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(clsroom)
                                c.execute(st)
                            if j==3:
                                c.fetchall()
                                c.execute('select slot1,slot2,slot3,slot4,slot5,slot6,slot7 from te1')
                                all_slots=c.fetchall()
                                if all_slots[i][6]==None:
                                    c.execute('select slot7 from {} where day="{}"'.format(clsroom,days[i]))
                                    result=c.fetchall()[0][0]
                                    if result==(None):
                                        if category=='H':
                                            c.execute("update TE1 set slot7='{}' where day = '{}'".format('HONOURS '+sub+' ('+clsroom+')', days[i]))
                                            c.execute("update {} set slot7='{}' where day='{}'".format(clsroom, sub,days[i]))
                                            c.execute("update TE2 set slot7='{}' where day = '{}'".format('HONOURS '+sub+' ('+clsroom+')', days[i]))
                                            c.execute("update TE3 set slot7='{}' where day = '{}'".format('HONOURS '+sub+' ('+clsroom+')', days[i]))
                                            c.execute("update TE4 set slot7='{}' where day = '{}'".format('HONOURS '+sub+' ('+clsroom+')', days[i]))
                                            k+=1


                                            break
                                        else:

                                            c.execute("update TE1 set slot7='{}' where day = '{}'".format(" "+sub+'('+clsroom+')', days[i]))
                                            c.execute("update {} set slot7='{}' where day='{}'".format(clsroom, sub,days[i]))
                                            c.execute("update TE2 set slot7='{}' where day = '{}'".format(' '+sub+'('+clsroom+')', days[i]))
                                            c.execute("update TE3 set slot7='{}' where day = '{}'".format(' '+sub+'('+clsroom+')', days[i]))
                                            c.execute("update TE4 set slot7='{}' where day = '{}'".format(' '+sub+'('+clsroom+')', days[i]))
                                            k+=1


                                            break
                                else: 
                                    if sub+' ' not in all_slots[i][6]:
                                        c.execute('select slot7 from {} where day="{}"'.format(clsroom,days[i]))
                                        result=c.fetchall()[0][0]
                                        if result==(None):
                                            c.execute("update TE1 set slot7=concat(slot7,' ','{}') where day = '{}'".format(' '+sub+'('+clsroom+')', days[i]))
                                            c.execute("update {} set slot7='{}' where day='{}'".format(clsroom, sub,days[i]))
                                            c.execute("update TE2 set slot7=concat(slot7,' ','{}') where day = '{}'".format(' '+sub+'('+clsroom+')', days[i]))
                                            c.execute("update TE3 set slot7=concat(slot7,' ','{}') where day = '{}'".format(' '+sub+'('+clsroom+')', days[i]))
                                            c.execute("update TE4 set slot7=concat(slot7,' ','{}') where day = '{}'".format(' '+sub+'('+clsroom+')', days[i]))
                                            k+=1
                                            break

                                
                            else:
                                c.fetchall()
                                c.execute('select slot1,slot2,slot3,slot4,slot5,slot6,slot7 from te1')
                                all_slots=c.fetchall()
                                if all_slots[i][2*j]==None:
                                    c.execute('select {},{} from {} where day="{}"'.format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),clsroom,days[i]))
                                    result=c.fetchall()[0]
                                    if result==(None,None):
                                        if category=='H':
                                            c.execute("update TE1 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1),'HONOURS ' +sub+'('+clsroom+')','slot'+str(2*(j+1)), 'HONOURS '+sub+'('+clsroom+')',days[i]))
                                            c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(clsroom, 'slot'+str(2*(j+1)-1), sub,'slot'+str(2*(j+1)),sub,days[i]))
                                            c.execute("update TE2 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), 'HONOURS '+sub+'('+clsroom+')','slot'+str(2*(j+1)), 'HONOURS '+sub+'('+clsroom+')',days[i]))
                                            c.execute("update TE3 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), 'HONOURS '+sub+'('+clsroom+')','slot'+str(2*(j+1)), 'HONOURS '+sub+'('+clsroom+')',days[i]))
                                            c.execute("update TE4 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), 'HONOURS '+sub+'('+clsroom+')','slot'+str(2*(j+1)), 'HONOURS '+sub+'('+clsroom+')',days[i]))
                                            k+=1
                                            break
                                        else:
                                            c.execute("update TE1 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), ' '+sub+'('+clsroom+')','slot'+str(2*(j+1)), ' '+sub+'('+clsroom+')',days[i]))
                                            c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(clsroom, 'slot'+str(2*(j+1)-1), sub,'slot'+str(2*(j+1)),sub,days[i]))
                                            c.execute("update TE2 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), ' '+sub+'('+clsroom+')','slot'+str(2*(j+1)), ' '+sub+'('+clsroom+')',days[i]))
                                            c.execute("update TE3 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), ' '+sub+'('+clsroom+')','slot'+str(2*(j+1)),' '+ sub+'('+clsroom+')',days[i]))
                                            c.execute("update TE4 set {}='{}', {}='{}' where day = '{}'".format('slot'+str(2*(j+1)-1), ' '+sub+'('+clsroom+')','slot'+str(2*(j+1)), ' '+sub+'('+clsroom+')',days[i]))
                                            k+=1
                                            break

                                else:
                                    name=' '+sub
                                    if name not in all_slots[i][2*j]:
                                        c.execute('select {},{} from {} where day="{}"'.format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),clsroom,days[i]))
                                        result=c.fetchall()[0]
                                        if result==(None,None):
                                            c.execute("update TE1 set {}=concat({},' ','{}'), {}=concat({},' ','{}') where day = '{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), sub+'('+clsroom+')','slot'+str(2*(j+1)),'slot'+str(2*(j+1)), sub+'('+clsroom+')',days[i]))
                                            c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(clsroom, 'slot'+str(2*(j+1)-1), sub,'slot'+str(2*(j+1)),sub,days[i]))
                                            c.execute("update TE2 set {}=concat({},' ','{}'), {}=concat({},' ','{}') where day = '{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), sub+'('+clsroom+')','slot'+str(2*(j+1)),'slot'+str(2*(j+1)), sub+'('+clsroom+')',days[i]))
                                            c.execute("update TE3 set {}=concat({},' ','{}'), {}=concat({},' ','{}') where day = '{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), sub+'('+clsroom+')','slot'+str(2*(j+1)),'slot'+str(2*(j+1)), sub+'('+clsroom+')',days[i]))
                                            c.execute("update TE4 set {}=concat({},' ','{}'), {}=concat({},' ','{}') where day = '{}'".format('slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), sub+'('+clsroom+')','slot'+str(2*(j+1)),'slot'+str(2*(j+1)), sub+'('+clsroom+')',days[i]))
                                            k+=1
                                            break



                
def assign_honor_slot():
    c.execute('select * from templabte1')
    full=c.fetchall()
    e_alloted=0
    while e_alloted<2:
        day=r.randrange(0,5)
        c.execute('select slot3 from templabte1 where day="{}"'.format( days[day]))
        val=c.fetchall()[0][0]
        if val==None:
            c.execute('update templabte1 set slot3="H" where day="{}"'.format(days[day]))
            c.execute('update templabte2 set slot3="H" where day="{}"'.format(days[day]))
            c.execute('update templabte3 set slot3="H" where day="{}"'.format(days[day]))
            c.execute('update templabte4 set slot3="H" where day="{}"'.format(days[day]))
            e_alloted+=1




def remove_spaces(st):
    c=0
    st1=''
    for i in st:
        if i==' ':
            if c!=0:
                if st1[-1]==' ':
                    continue
            c+=1
        st1+=i
    return st1

        
