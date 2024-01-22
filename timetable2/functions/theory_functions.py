import mysql.connector
import random as r

mydb=mysql.connector.connect(host="localhost",
    username="root",
    password="Ayush_Chanekar23",
    database="ttproject",
    autocommit=True)
c=mydb.cursor()

days=['Monday','Tuesday','Wednesday','Thursday','Friday']



def assign_theory(class_div,t_subs):
    for sub,n in t_subs.items():
        no=0
        count=0
        while no<n:
            count+=1
            i=r.randrange(0,5)
            j=r.randrange(1,6)
            c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format(class_div))
            all_slots=c.fetchall()
            if all_slots[i][j-1]=='T':
                if sub in all_slots[i]:
                    continue
                else:
                    c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(j),sub,days[i]))
                    no+=1
            
            if (no<n and count>20):
                count1=0
                x=1
                for i in range(5):
                    if x==0:
                        break
                    for j in range(1,7):
                        c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format(class_div))
                        all_slots=c.fetchall()  
                        if all_slots[i][j-1]=='T':
                            count1+=1
                            if sub in all_slots[i]:
                                continue
                            else:
                                c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(j),sub,days[i]))
                                no+=1
                        if no>=n:
                            x=0
                        if x==0:
                            break
                if no!=n:
                    x=1
                    for i in range(5):
                        if x==0:
                            break
                        for j in range(1,7):
                            c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format(class_div))
                            all_slots=c.fetchall()  
                            if all_slots[i][j-1]=='T':
                                c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(j),sub,days[i]))
                                no+=1
                            if no>=n:
                                x=0
                            if x==0:
                                break

                break           
              
def assign_theory_te(class_div,t_subs):
    for sub,n in t_subs.items():
        no=0
        count=0
        while no<n:
            count+=1
            i=r.randrange(0,5)
            j=r.randrange(2,7)
            c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format(class_div))
            all_slots=c.fetchall()
            if all_slots[i][j-1]=='T':
                if sub in all_slots[i]:
                    continue
                else:
                    c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(j),sub,days[i]))
                    no+=1
            
            if (no<n and count>20):
                count1=0
                x=1
                for i in range(5):
                    if x==0:
                        break
                    for j in range(2,7):
                        c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format(class_div))
                        all_slots=c.fetchall()  
                        if all_slots[i][j-1]=='T':
                            count1+=1
                            if sub in all_slots[i]:
                                continue
                            else:
                                c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(j),sub,days[i]))
                                no+=1
                        if no>=n:
                            x=0
                        if x==0:
                            break
                if no!=n:
                    x=1
                    for i in range(5):
                        if x==0:
                            break
                        for j in range(1,7):
                            c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format(class_div))
                            all_slots=c.fetchall()  
                            if all_slots[i][j-1]=='T':
                                c.execute("update {} set {}='{}' where day='{}'".format(class_div,'slot'+str(j),sub,days[i]))
                                no+=1
                            if no>=n:
                                x=0
                            if x==0:
                                break

                break 


def theory_slot(class_div):
    c.execute('select slot1,slot2,slot3 from {}'.format('templab'+class_div))
    temp_slots=c.fetchall()
    c.execute('select slot1,slot2,slot3,slot4,slot5,slot6 from {}'.format(class_div))
    all_slots=c.fetchall()
    for i in range(5):
        for j in range(3):
            if temp_slots[i][j]==None:
                c.execute("update {} set {}='T',{}='T' where day='{}'".format(class_div,'slot'+str(2*(j+1)-1),'slot'+str(2*(j+1)),days[i]))
