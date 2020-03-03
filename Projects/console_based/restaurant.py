                                                                        #### CUSTOMER LOGIN ####
'''
import re
import csv
users = []

def loadData():
    with open('data.txt','r') as data:
        for line in data:
            user = makeUser(line)
            users.append(user)
    return True

def saveData():
    with open('data.txt','w') as data:
        for user in users:
            print(user['name']+'|'+user['surname']+'|'+user['username']+'|'+user['password'],file = data)

def makeUser(line):
    name, surname, username, password = line.split('|')
    if password[-1:] == '\n':
        password = password[:-1]
    return {'name':name, 
            'surname':surname,
            'username':username,
            'password':password
            }

def register():
    name = input('Name:')
    surname = input('Surname:')
    while True:
        username = input('Username:')
        if checkLen(username):
            break

    while True:
        password = input('Password:')
        if checkLen(password):
            break
    users.append({'name':name,'surname':surname,'username':username,'password':password})

def checkLen(info):
    if len(info) > 0:
        return True
    else:
        print('Can\'t be blank!')

def login(state):
    while state:
        username = input('Username:')
        password = input('Password:')
        for user in users:
            if user['username'] == username and user['password'] == password:
                print('You are logged in.')
                state = False
                break
        else:
            print('Wrong input.')

'''

                                                                    ####### CUSTOMER DATA MAIN CLASS #########


class Hotel():
    def __init__ (self,total=0):
        
        self.fname=input("Enter Your first Name: ")
        self.lname=input("Enter Your last Name: ")
        self.email=input("Enter Your Email ID: ")
        self.identityproof=input("What you are going to provide as Identity Proof ? :")
        self.checkin=input("Enter your checkin date: ")
        self.members=(input("Enter how many members to stay: "))
        

    def WriteToFile(self):
        f=open("C:\\itvedant\\python\\project\\console_based\\restaurant.csv", 'w+')
        
        writeString=self.fname+", "+self.lname+", "+self.email+", "+self.checkin+", "+self.members+", "+self.identityproof+", "+"\n"
        f.write(writeString)
        f.close
        
    def RoomRent(self):
        print("""Room detials are:
              Choice 1. 3500 rs for upto 4 people
              Choice 2. 5500 rs for upto 6 people
              choice 3. 7500 rs for upto 8 people
              choice 4. Enquiry""")

        choice=int(input("Enter your Choice: "))
        days=int(input("Enter how many days to stay: "))

        if (choice==1):
            print(" ")
            self.total=3500*days

        elif(choice==2):
            print(" ")
            self.total=5500*days

        elif(choice==3):
            print(" ")
            self.total=7500*days

        elif(choice==4):
            print("Put Enquiry we will get back to you.")
            
        else:
            print("Invalid Choice")

        print("Your Room Rent is: ",self.total)
        


##    def Display(self):
##        f=open("restaurant.csv")
##        read=f.readlines()
##        print("Customer first Name: ",self.fname)
##        print("Customer last Name: ",self.lname)
##        print("Customer Email ID: ",self.email)
##        print("Customer Identity proof: ",self.identityproof)
##        print("Customer Checkin Date: ",self.checkin)
##        print("Customer Rent: ",self.total)
##
##
    def EditData(self):
        line_count = 0
        marked_item = int(input("Enter the item number:"))
        with open("restaurant.csv", 'r') as f:
            reader = csv.reader(f, delimiter=',')
            title = next(reader)
            print(title)
            print(title[3])
            lines = []
            for line in reader:
                if title[3] == 'a':
                    line_count += 1
                    if marked_item == line_count:
                        title[3] = 'b'
                lines.append(line)
        with open("restaurant.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(title)
            writer.writerows(lines)

####    def EditData(self):
####        r=csv.reader(open("restaurant.csv"))
####        lines=list(r)
####        lines[0][5]=="AdharCard"
####        writer=csv.writer(open("restaurant.csv"))
####        writer.writerows(lines)
####        r.close()
##                

    
def main():
    ''' state = loadData()

        print('1) Login')
        print('2) Register')
        print('x - Exit')
        choice = input('>')

        while choice not in ['1','2','x']:
            choice = input('>')

        if choice == '1':
            login(state)
        elif choice == '2':
            register()
            main()
        elif choice == 'x':
            saveData()
            quit()
    '''
    h=Hotel()
    h.WriteToFile()
    h.RoomRent()
##    h.Display()
    h.EditData()



if __name__ == '__main__':
    main()
