import pymysql
import random
import datetime
from msvcrt import getch
class railway():
    
    def connection(self):
        
        self.con=pymysql.connect('localhost','root','','project')
        self.cursor=self.con.cursor()
    def enter(self):
        print('PRESS ENTER TO GO TO MAIN MENU')
        key=ord(getch())
        if key==13:
            self.index()

    def admin_login(self):
        
        self.connection()
        user=(input('ENTER USERNAME\n'))
        pas=(input('ENTER PASSWORD\n'))

        query='''select password from admin where username=(%s);'''
        check=(user)
        self.cursor.execute(query,check)
        result=self.cursor.fetchall()
        u='''select username from admin'''
        self.cursor.execute(u)
        a=[]
        username=self.cursor.fetchall()
        for i in username:
            a.append(i[0])
        if user in a:
            if pas==result[0][0]:
                print('LOGIN SUCCESSFULL\n')
                self.index()
                
            else:
                print('WRONG PASSWORD \n')
                self.admin_login()
        else:
            print('USER NOT EXIST\n')
            self.admin_login()

            self.con.close()

    def insert_tdetail(self):
        #self.admin_login()
        add='y'
        while add=='y' or add=='Y':
            try:
                tname=input('ENTER NAME OF THE TRAIN :')
                print('\n')
                tno=int(input('ENTER TRAIN NUMBER :'))
                print('\n')
                ac_1class=int(input('ENTER NUMBER OF AC FIRST CLASS SEAT RESERVED ARE :'))
                print('\n')
                ac_2class=int(input('ENTER NUMBER OF AC SECOND CLASS SEAT RESERVED ARE :'))
                print('\n')
                ac_3class=int(input('ENTER NUMBER OF AC THIRD CLASS SEAT RESERVED ARE :'))
                print('\n')
                sleep=int(input('ENTER NUMBER OF SLEEPER CLASS SEAT RESERVED ARE :'))
                print('\n')
                s_point=input('ENTER STARTING POINT :')
                print('\n')
                e_point=input('ENTER DESTINATION POINT :')
                print('\n')

                self.connection()
                q='''insert into train values('{}','{}',{},{},{},{},'{}','{}')'''.format(tname,tno,ac_1class,ac_2class,ac_3class,sleep,s_point,e_point)
                #v=(tname,tno,ac_1class,ac_2class,ac_3class,sleep,s_point,e_point)
                self.cursor.execute(q)
                
                
                self.con.commit()
                print('INSERTED SUCCESSFULLY')
                
                
                add=input('DO YOU WANT TON ADD MORE TRAIN DETAILS?\n\t\tY/N')
            except:
                print('TRAIN NUMBER ALREADY EXIST')
                self.con.close()
        else:
            self.enter()


    def train(self):
        self.connection()
        t=int(input('ENTER TRAIN NUMBER'))
        q='select * from train where tno=%s '
        qu=(t)
        result=self.cursor.execute(q,qu)
        
       
        if result>0:  
            ans=self.cursor.fetchall()
            print('NAME OF THE TRAIN IS :\t',ans[0][0])
            print('TRAIN NUMBER         :\t',ans[0][1])
            print('STARTING POINT       :\t',ans[0][6])
            print('DESTINATION POINT    :\t',ans[0][7])
            d='select source,destination,km from distance where tno=%s order by source'
            query=(t)
            self.cursor.execute(d,query)
            ans=self.cursor.fetchall()
            print('\nSOURCE\t\t\tDESTINATION\n')
            
            a=0           
            for i in ans:      
                print(ans[a][0],'\t\t',ans[a][1])
                a+=1                     
        else:
            print('TRAIN NOT FOUND')
        
        
    def update_tdetail(self):
        
        
        update='y'
        while update=='y' or update=='Y':
            try:
           
            
                self.connection()
                i=int(input('ENTER TRAIN NUMBER YOU WNAT TO UPDATE'))
                q='''select * from train where tno=(%s)'''
                q1=(i)
                s=self.cursor.execute(q,q1)
                result=self.cursor.fetchall()
##                print(result[0][6])
                print('NAME OF THE TRAIN IS:',result[0][0])
               
                print('NUMBER OF AC FIRST CLASS SEAT RESERVED ARE :',result[0][2])
                print('NUMBER OF AC SECOND CLASS SEAT RESERVED ARE :',result[0][3])
                print('NUMBER OF AC THIRD CLASS SEAT RESERVED ARE :',result[0][4])
                print('NUMBER OF SLEEPER CLASS SEAT RESERVED ARE :',result[0][5])
                print('STARTING POINT  :',result[0][6])
                print('DESTINATION POINT :',result[0][7])

                print('1.NAME OF THE TRAIN :')
                
                print('2.NUMBER OF AC FIRST CLASS SEAT RESERVED  :')
                print('3.NUMBER OF AC SECOND CLASS SEAT RESERVED :')
                print('4.NUMBER OF AC THIRD CLASS SEAT RESERVED  :')
                print('5.NUMBER OF SLEEPER CLASS SEAT RESERVED  :')
                print('6.STARTING POINT :')
                print('7.DESTINATION POINT :')
                choice=int('ENTER YOUR CHOICE WHAT YOU WANT TO UPDATE')
                while c=='y' or c=='Y':
                    if choice==1:
                          
                        tname=input('ENTER NAME OF THE TRAIN :')
                        print('\n')
                    elif choice==2:
                        ac_1class=int(input('ENTER NUMBER OF AC FIRST CLASS SEAT RESERVED  :'))
                        print('\n')
                    elif choice==3:
                        ac_2class=int(input('ENTER NUMBER OF AC SECOND CLASS SEAT RESERVED  :'))
                        print('\n')
                    elif choice==4:
                        ac_3class=int(input('ENTER NUMBER OF AC THIRD CLASS SEAT RESERVED :'))
                        print('\n')
                    elif choice==5:
                        sleep=int(input('ENTER NUMBER OF SLEEPER CLASS SEAT RESERVED:'))
                        print('\n')
                    elif choice==6:
                        s_point=input('ENTER STARTING POINT :')
                        print('\n')
                    elif choice==7:
                        e_point=input('ENTER DESTINATION POINT :')
                        print('\n')
                    else:
                          print('INVALID CHOICE')
                          c=input('DO YOU WANT TO UPDATE?\nY/N?')
##
##                    
##                print('connection success')
                self.connection()
                q="""Update train set tname=%s,ac_1class=%s,ac_2class=%s,ac_3class=%s,sleeper_class=%s,s_point=%s,e_point=%s where tno=%s;"""
##                q="""Update train set tname=%s where tno=%s;"""
##                
                v=(tname,ac_1class,ac_2class,ac_3class,sleep,s_point,e_point,i)
##                #.format(tname,tno,ac_1class,ac_2class,ac_3class,sleep,s_point,e_point)
##                v=(tname,i)
##                
##                #v=(i)
                self.cursor.execute(q,v)
##                print('query executed')
                #self.cursor.close()
##                
                self.con.commit()
                print('UPDATED SUCCESSFULLY!!!')
##                
                self.con.close()
                update=input('DO YOU WANT TO UPDATE TRAIN DETAIL?\t\t\nY/N')
                
            except:
                print('SOME ERROR OCCURE')
        else:
            
            self.enter()
    def reserv(self):
            self.connection()
            d=datetime.datetime.now()
            tn=input('ENTER TRAIN NUMBER:')
            q=('''select tname from train where tno=%s''')
            t=(tn)
            r=self.cursor.execute(q,tn)
            if r>0:
                tname=self.cursor.fetchall()
                
                tname=tname[0][0]
               
                print('TRAIN NAME IS',tname)                

                ts='select ac_1class,ac_2class,ac_3class,sleeper_class from train where tno=%s'
                t=(tn)
                s=self.cursor.execute(ts,t)
                ans=self.cursor.fetchall() 
                print('AC FIRST CLASS SEAT AVAILABLE ARE ',ans[0][0])
                print('AC SECOND CLASS SEAT AVAILABLE ARE ',ans[0][1])
                print('AC THIRD CLASS SEAT AVAILABLE ARE ',ans[0][2])
                print('SLEEPER CLASS SEAT AVAILABLE ARE ',ans[0][3])

                r=input('DO YOU WANT TO BOOK A TICKET???Y/N')
                while r=='y' or r=='Y':
                        self.connection()
                        try:
                            
##                   try:
                    
                            name=input('ENTER PASSANGER NAME')
                            age=int(input('ENTER PASSANGER AGE'))
                    
                            source=input('ENTER START/SOURCE STATION')                        
                            des=input('ENTER DESTINATION/END STATION')
                            s='select km from distance where source=%s and destination=%s or source=%s and destination=%s '
                            t=(source,des,des,source)
                            an=self.cursor.execute(s,t)
                            print(an)
                            if an>0:
                                    
                                
                                km=self.cursor.fetchall()
                                print(km)
                                km=km[0][0]
                                print('----------------SELECT OPTION------------------')
                                print('1. AC FIRST CLASS')
                                print('2. AC SECOND CLASS')
                                print('3. AC THIRD CLASS')
                                print('4. SLEEPER CLASS')
                                choice=int(input(''))

                            

                                if(choice==1):
                                    clas='ac_1class'
                                    i=int(input('ENTER NUMBER OF AC FIRST CLASS SEAT TO BE RESERVED'))
                                    xx='select ac_1class from train where tno=%s'
                                    amount=(km*3)*i
                                    
                                    a1=ans[0][0]-i
                                    a2=ans[0][1]
                                    a3=ans[0][2]
                                    a4=ans[0][3]
                                    print(ans[0][0]-i)
                                    
                                    
##                                   
                                elif(choice==2):
                                    clas='ac_2class'
                                    i=int(input('ENTER NUMBER OF AC SECOND CLASS SEAT TO BE RESERVED'))
                                    xx='select ac_2class from train where tno=%s'
                                    amount=round(km*2.5)*i
                                    a1=ans[0][0]
                                    a2=ans[0][1]-i
                                    a3=ans[0][2]
                                    a4=ans[0][3]
                                    print(ans[0][1]-i)
####                                    
                                        
                                elif choice==3:
                                    clas='ac_3class'
                                    i=int(input('ENTER NUMBER OF AC THIRD CLASS SEAT TO BE RESERVED'))
                                    xx='select ac_3class from train where tno=%s'
                                    amount=(km*2)*i
                                    a1=ans[0][0]
                                    a2=ans[0][1]
                                    a3=ans[0][2]-i
                                    a4=ans[0][3]
                                    print(ans[0][2]-i)
##                                                              
                                elif choice==4:
                                    clas='sleeper_class'
                                    i=int(input('ENTER NUMBER OF SLEEPER CLASS SEAT TO BE RESERVED'))
                                    xx='select sleeper_class from train where tno=%s'
                                    amount=round(km*1.5)*i
                                    a1=ans[0][0]
                                    a2=ans[0][1]
                                    a3=ans[0][2]
                                    a4=ans[0][3]-i
                                    print(ans[0][3]-i)
##                                    
                                else:
                                    print('INVALID CHOICE!!!')
                                    break
                                print('Processing......')
                                print('TOTAL AMOUNT TO BE PAID\t: ',amount,'Rs.')
                                pnr=0

                                q='update train set ac_1class=%s,ac_2class=%s,ac_3class=%s,sleeper_class=%s where tno=%s'
                                qu=(a1,a2,a3,a4,tn)
                                s=self.cursor.execute(q,qu)

                                ts='select ac_1class,ac_2class,ac_3class,sleeper_class from train where tno=%s'
                                t=(tn)
                                s=self.cursor.execute(ts,t)
                                ans=self.cursor.fetchall()
                                
                                print('AC FIRST CLASS SEAT AVAILABLE ARE ',ans[0][0])
                                print('AC SECOND CLASS SEAT AVAILABLE ARE ',ans[0][1])
                                print('AC THIRD CLASS SEAT AVAILABLE ARE ',ans[0][2])
                                print('SLEEPER CLASS SEAT AVAILABLE ARE ',ans[0][3])
                                self.con.commit()

                                t=(tn)
                                ans=self.cursor.execute(xx,t)
                                a=self.cursor.fetchall()
##                                print('class of the selected ',a)
                                x=a[0][0]
                                print('total number of seat available',a[0][0])
                                if x<=0:
                                    s='Waiting List'
                                    print('Status WL\  ',s)
##                                    q='select ticket from reserv where pnr=%s'
##                                    query=(pnr)
##                                    self.cursor.execute()
                                    a=i
                                    i=0
                                    
                                else :
                                    s='Confirmed'
                                    print('Status  ',s)
                                    i=i
                                    a=0
                                    


                                
                                ts="insert into reserv values('{}','{}',{},'{}',{},'{}',{},{},'{}','{}',{},'{}',{})".format(tname,clas,i,s,age,name,tn,pnr,source,des,amount,d,a)
                                   
                                query=self.cursor.execute(ts)
                                self.con.commit()
                                print('TICKET BOOKED SUCCESSFULLY')

                                    
                                ts='select ac_1class,ac_2class,ac_3class,sleeper_class from train where tno=%s'
                                t=(tn)
                                s=self.cursor.execute(ts,t)
                                ans=self.cursor.fetchall()
                                
                                print('AC FIRST CLASS SEAT AVAILABLE ARE ',ans[0][0])
                                print('AC SECOND CLASS SEAT AVAILABLE ARE ',ans[0][1])
                                print('AC THIRD CLASS SEAT AVAILABLE ARE ',ans[0][2])
                                print('SLEEPER CLASS SEAT AVAILABLE ARE ',ans[0][3])
                                self.con.commit()
                                self.con.close()
                                r=input('DO YOU WANT TO BOOK A MORE TICKETS')
                            else:
                                 print('SOURSE OR DESTINATION STATION NOT FOUND')
                                 self.enter()

                        except:

                            print('BOOKING CANCELLED!!!')
                            self.enter()
                else:
                    self.enter()
            

            else:
                print('INVALID TRAIN NUMBER!!!')
                self.enter()
                 
##                    self.index()



    def cancel(self):
##        pass
        self.connection()
        pnr=int(input('ENTER PNR NUMBER'))

        tr='delete from reserv where pnr=%s'
        t=(pnr)
        c=self.cursor.execute(tr,t)
             
        if c>0:
            print('TICKET CANCELLED SUCCESSFULLY!')
        else:
            print('INVALID PNR NUMBER!!!')
            self.index()
                
            
          
                  
            
    def pnr(self):
        self.connection()
        pnr=int(input('ENTER PNR NUMBER'))
        
        s='select status from reserv where pnr_no=%s'
        pn=(pnr)
        q=self.cursor.execute(s,pn)
        if q>0:
            result=self.cursor.fetchall()
            print(result[0][0])

        else:
            print("PNR NUMBER NOT FOUND!!!")

            
            
                
##              
    def index(self):
        print("----------WELCOME TO NAYAN'S RAILWAY RESERVATION SYSTEM----------\n")
        print('\t\t1. ADD TRAIN DETAILS.\n')
        print('\t\t2. UPDATE TRAIN DETAILS.\n')
        print('\t\t3. TRAIN DETAILS.\n')
        print('\t\t4. RESERVATION OF TICKETS.\n')
        print('\t\t5. CANCELLATION OF TICKETS.\n')
        print('\t\t6. DISPLAY PNR STATUS.\n')
        print('\t\t7. QUIT.')
        print('** - OFFICE USE.........\n')

        print('\t\tENTER YOUR CHOICE :')
        choice=int(input(''))
        if choice==1:
            self.insert_tdetail()
        elif choice==2:
            self.update_tdetail()
        elif choice==3:
            self.train()
        elif choice==4:
            self.reserv()
        elif choice==5:
            self.cancel()
        elif choice==6:
            self.pnr()
        elif choice==7:
            exit()
            
        else:
            print('Invalid Choice')
            self.enter() 
        
    def main_page(self):
        self.admin_login()
       
            


       
def main():
    
    s=railway()
    #s.admin_login()
    #s.insert_tdetail()
    s.main_page()

if __name__=='__main__':
    main()
