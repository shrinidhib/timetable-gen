import mysql.connector
import random as r

mydb=mysql.connector.connect(host="localhost",
    username="root",
    password="Ayush_Chanekar23",
    database="ttproject",
    autocommit=True)
c=mydb.cursor()

days=['Monday','Tuesday','Wednesday','Thursday','Friday']

def assign_classroom(class_div,lis_class, t_subs):
    c.execute("select slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(class_div))
    all_slots=c.fetchall()
    
    for i in range(0,5):
        for j in range(0,3):
            x=r.choice(lis_class)
            c.execute('''create table if not exists {}(
            day varchar(10) not null,
            slot1 varchar(20) default null,
            slot2 varchar(20) default null,
            slot3 varchar(20) default null,
            slot4 varchar(20) default null,
            slot5 varchar(20) default null,
            slot6 varchar(20) default null)'''.format(x))
            c.execute('''select count(*) from {}'''.format(x))
            p=c.fetchall()[0][0]
            if p==0:
                c.fetchall()
                c.execute("insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(x))

            if all_slots[i][2*j] in t_subs and all_slots[i][2*j + 1] in t_subs:
                c.execute("select {},{} from {} where day='{}'".format('slot'+str(2*(j+1)-1), 'slot'+str(2*(j+1)), x, days[i]))
                p=c.fetchall()[0]
                if p.count(None)==2:
                    c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(x,'slot'+str(2*(j+1)-1), class_div, 'slot'+str(2*(j+1)),class_div,days[i]))
                    c.execute("update {} set {}=concat({},'({})') , {}=concat({},'({})') where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), x, 'slot'+str(2*(j+1)),'slot'+str(2*(j+1)),x,days[i]))
                else:
                    count=0
                    while True:
                            count+=1
                            x=r.choice(lis_class)
                            c.execute('''create table if not exists {}(
                            day varchar(10) not null,
                            slot1 varchar(20) default null,
                            slot2 varchar(20) default null,
                            slot3 varchar(20) default null,
                            slot4 varchar(20) default null,
                            slot5 varchar(20) default null,
                            slot6 varchar(20) default null)'''.format(x))
                            c.execute('''select count(*) from {}'''.format(x))
                            p=c.fetchall()[0][0]
                            if p==0:
                                c.fetchall()
                                c.execute("insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(x))

                            c.execute("select {},{} from {} where day='{}'".format('slot'+str(2*(j+1)-1), 'slot'+str(2*(j+1)), x, days[i]))
                            p=c.fetchall()[0]
                            if p.count(None)==2:
                                c.execute("update {} set {}='{}',{}='{}' where day='{}'".format(x,'slot'+str(2*(j+1)-1), class_div, 'slot'+str(2*(j+1)),class_div,days[i]))
                                c.execute("update {} set {}=concat({},'({})') , {}=concat({},'({})') where day='{}'".format(class_div,'slot'+str(2*(j+1)-1), 'slot'+str(2*(j+1)-1),x, 'slot'+str(2*(j+1)), 'slot'+str(2*(j+1)),x,days[i]))
                                break
                            if count>8:
                                return 0
                                

            elif  all_slots[i][2*j] in t_subs:
                
                    c.execute("select {} from {} where day='{}'".format('slot'+str(2*(j+1)-1), x, days[i]))
                    p=c.fetchall()[0][0]
                    if p==None:
                        c.execute("update {} set {}='{}' where day='{}'".format(x,'slot'+str(2*(j+1)-1), class_div, days[i]))
                        c.execute("update {} set {}=concat({},'({})') where day='{}'".format(class_div,'slot'+str(2*(j+1)-1), 'slot'+str(2*(j+1)-1),x,days[i]))

                    else:
                        count=0
                        while True:
                            count+=1
                            x=r.choice(lis_class)
                            c.execute('''create table if not exists {}(
                            day varchar(10) not null,
                            slot1 varchar(20) default null,
                            slot2 varchar(20) default null,
                            slot3 varchar(20) default null,
                            slot4 varchar(20) default null,
                            slot5 varchar(20) default null,
                            slot6 varchar(20) default null)'''.format(x))
                            c.execute('''select count(*) from {}'''.format(x))
                            p=c.fetchall()[0][0]
                            if p==0:
                                c.fetchall()
                                c.execute("insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(x))

                            c.execute("select {} from {} where day='{}'".format('slot'+str(2*(j+1)-1), x, days[i]))
                            p=c.fetchall()[0][0]
                            if p==None:
                                c.execute("update {} set {}='{}' where day='{}'".format(x,'slot'+str(2*(j+1)-1), class_div, days[i]))
                                c.execute("update {} set {}=concat({},'({})')  where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)-1), x,days[i]))
                                break
                            if count>8:
                                return 0

            elif all_slots[i][2*j+1] in t_subs:
                    c.execute("select {} from {} where day='{}'".format('slot'+str(2*(j+1)), x, days[i]))
                    p=c.fetchall()[0][0]
                    if p==None:
                        c.execute("update {} set {}='{}' where day='{}'".format(x,'slot'+str(2*(j+1)),class_div,days[i]))
                        c.execute("update {} set {}=concat({},'({})') where day='{}'".format(class_div, 'slot'+str(2*(j+1)),'slot'+str(2*(j+1)),x,days[i]))

                    else:
                        count=0
                        while True:
                            count+=1
                            x=r.choice(lis_class)
                            c.execute('''create table if not exists {}(
                            day varchar(10) not null,
                            slot1 varchar(20) default null,
                            slot2 varchar(20) default null,
                            slot3 varchar(20) default null,
                            slot4 varchar(20) default null,
                            slot5 varchar(20) default null,
                            slot6 varchar(20) default null)'''.format(x))
                            c.execute('''select count(*) from {}'''.format(x))
                            p=c.fetchall()[0][0]
                            if p==0:
                                c.fetchall()
                                c.execute("insert into {}(day) values ('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday')".format(x))

                            c.execute("select {} from {} where day='{}'".format('slot'+str(2*(j+1)), x, days[i]))
                            p=c.fetchall()[0][0]
                            if p==None:
                                c.execute("update {} set {}='{}' where day='{}'".format(x,'slot'+str(2*(j+1)), class_div, days[i]))
                                c.execute("update {} set {}=concat({},'({})') where day='{}'".format(class_div,'slot'+str(2*(j+1)),'slot'+str(2*(j+1)), x,days[i]))
                                break
                            if count>8:
                                return 0

      
      
def assign_remedial(class_div):
    c.execute("select slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(class_div))
    all_slots=c.fetchall()
    x=[]
    for i in range(5):
        for j in range(6):
            if all_slots[i][j]=='T':
                x=[i,j]
                break

        if len(x)>0:
            break

    c.execute("update {} set {}='{}' where day='{}'".format(class_div, 'slot'+str(j+1),'REMEDIAL', days[i]))


def assign_remedial_te(class_div):
    c.execute("select slot1,slot2,slot3,slot4,slot5,slot6 from {}".format(class_div))
    all_slots=c.fetchall()
    x=0
    c1=0
    for i in range(5):
        for j in range(6):
            if all_slots[i][j]=='T':
                c1+=1
                c.execute("update {} set {}='{}' where day='{}'".format(class_div, 'slot'+str(j+1),'REMEDIAL', days[i]))
                if c1==2:
                    break
        if c1==2:
            break
                
