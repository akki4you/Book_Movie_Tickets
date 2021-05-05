# import pickle
class Cinema:
    purchased_ticket = 0
    total_seat = 100
    current_income = 0
    total_income = 1000
    booked_data = {"Name":[],"Gender":[],"Age":[],"Num":[]}
    def showseats(self,rows,columns):
        self.rows = rows
        self.columns =columns
        for i in range(1,rows+1):
            for j in range(1,columns+1):
                if j<=i:
                    print('S',end= ' ')
                else:
                    print('S',end= ' ')
            print()
    def buy_ticket(self,ticket_price):
        self.r11 = input("Type the row number:")
        self.cl12 = input("Type the column num:")
        self.ticket_price = ticket_price
        print('ticker price is',self.ticket_price)
        do_process = input('10 $ cost is for evrey seats so do you want to process then press y or press n:')
        if do_process == 'y':
            self.name = input("Enter your Name:")
            self.gender =  input("Enter your Gender:")
            self.age = input("Enter your Age:")
            self.num = input("Enter your Phone Num:")
            Cinema.booked_data["Name"].append(self.name),Cinema.booked_data["Gender"].append(self.gender),Cinema.booked_data["Age"].append(self.age),Cinema.booked_data["Num"].append(self.num)
            print(Cinema.booked_data)
            Cinema.purchased_ticket = Cinema.purchased_ticket +1
            print("Your Ticket is successFully booked")
        elif do_process == 'n':
            print("You can book another time,have a nice movie next Time")   
    def statistic(self):
        print("Number of purchased tickets:",Cinema.purchased_ticket)
        self.percenta = (Cinema.total_seat*Cinema.purchased_ticket)/100
        print("Percentage:",self.percenta,"%")
        Cinema.current_income = Cinema.current_income+self.ticket_price
        print("Current income:",Cinema.current_income)
        print("Total income:",Cinema.total_income)
    def Show_booked_Ticket_User_Info(self):
        self.ro1 = input("Enter row number:")
        self.col1 = input("Enter column number:")
        if (self.ro1 == self.r11) and (self.col1 == self.cl12):
            print("Name:",self.name)
            print("Gender:",self.gender)
            print("Age:",self.age)
            print("Phone no:",self.num)
        else:
            print("Please Book FIrst then Come for your informartion")

        
            
c = Cinema()
while(True):
    welcomemsg = '''\n------Welcome to the MoviesMaina-------
    1.Show the Seats
    2.Buy a Ticket
    3.Statsics
    4.Show Booked Ticket User Info
    '''
    print(welcomemsg)
    a = int(input("Enter a choice: "))
    if a == 1:
        c.showseats(10,10)
    elif a == 2:
        c.buy_ticket(10)
    elif a == 3:
        c.statistic()
    elif a == 4:
        c.Show_booked_Ticket_User_Info()
        exit()
    else:
        print("Invalid Choice!")