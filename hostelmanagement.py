# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:16:28 2020

@author: Ayushi
"""

class hostelfarecal:


    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):

        print ("\n\n*****WELCOME TO  kota HOSTEL*****\n")


        self.rt=rt


        self.r=r


        self.t=t



        self.s=s

        self.a=a

        self.name=name

        self.address=address

        self.cindate=cindate

        self.coutdate=coutdate

        self.rno=rno

    def inputdata(self):

        self.name=input("\nEnter your name:")

        self.address=input("\nEnter your address:")

        self.cindate=input("\nEnter your check in date:")

        self.coutdate=input("\nEnter your checkout date:")

        print("Your room no.:",self.rno,"\n")

        
    def roomrent(self):

        print ("We have the following rooms for you:-")


        print ("1.  type A---->rs 6500 PN\-")


        print ("2.  type B---->rs 5500 PN\-")


        print ("3.  type C---->rs 4500 PN\-")


        print ("4.  type D---->rs 3500 PN\-")


        x=int(input("Enter Your Choice Please->"))


        n=int(input("For How Many Months Did You Stay:"))


        if(x==1):


            print ("you have opted room type A")


            self.s=6500*n


        elif (x==2):


            print ("you have opted room type B")


            self.s=5500*n


        elif (x==3):


            print ("you have opted room type C")


            self.s=4500*n


        elif (x==4):

            print ("you have opted room type D")


            self.s=3500*n


        else:


            print ("please choose a room")


        print ("your room rent is =",self.s,"\n")


    def restaurentbill(self):


        print("MESS MENU")


        print("1.water----->Rs20","2.tea----->Rs10","3.breakfast combo--->Rs90","4.lunch---->Rs110","5.dinner--->Rs150","6.Exit")



        while (1):


            c=int(input("Enter your choice:"))



            if (c==1):

                d=int(input("Enter the quantity:"))

                self.r=self.r+20*d


            elif (c==2):

                 d=int(input("Enter the quantity:"))

                 self.r=self.r+10*d


            elif (c==3):

                 d=int(input("Enter the quantity:"))

                 self.r=self.r+90*d


            elif (c==4):

                 d=int(input("Enter the quantity:"))

                 self.r=self.r+110*d


            elif (c==5):

                 d=int(input("Enter the quantity:"))

                 self.r=self.r+150*d


            elif (c==6):

                break;

            else:

                print("Invalid option")


        print ("Total food Cost=Rs",self.r,"\n")


    def laundrybill(self):

        print ("LAUNDRY MENU")


        print ("1.Shorts----->Rs3","2.Trousers----->Rs4","3.Shirt--->Rs5","4.Jeans---->Rs6","5.Girlsuit--->Rs8","6.Exit")


        while (1):
            


            e=int(input("Enter your choice:"))


            if (e==1):

                f=int(input("Enter the quantity:"))

                self.t=self.t+3*f


            elif (e==2):

                f=int(input("Enter the quantity:"))

                self.t=self.t+4*f


            elif (e==3):

                f=int(input("Enter the quantity:"))

                self.t=self.t+5*f


            elif (e==4):

                f=int(input("Enter the quantity:"))

                self.t=self.t+6*f


            elif (e==5):

                f=int(input("Enter the quantity:"))

                self.t=self.t+8*f

            elif (e==6):

                break;

            else:


                print ("Invalid option")



        print ("Total Laundary Cost=Rs",self.t,"\n")


    

    def display(self):

        print ("******HOSTEL BILL******")

        print ("Customer details:")

        print ("Customer name:",self.name)

        print ("Customer address:",self.address)

        print ("Check in date:",self.cindate)

        print ("Check out date",self.coutdate)

        print ("Room no.",self.rno)

        print ("Your Room rent is:",self.s)

        print ("Your Food bill is:",self.r)

        print ("Your laundary bill is:",self.t)


        self.rt=self.s+self.t+self.r


        print ("Your sub total bill is:",self.rt)

        print ("Additional Service Charges is",self.a)

        print ("Your grandtotal bill is:",self.rt+self.a,"\n")

        self.rno+=1


            

        

        

def main():


    a=hostelfarecal()

    

    while (1):
        print("1.Enter Customer Data")

        
        print("2.Calculate rommrent")


        print("3.Calculate mess bill")


        print("4.Calculate laundry bill")


        print("5.Show total cost")


        print("6.EXIT")




        b=int(input("\nEnter your choice:"))

        if (b==1):

            a.inputdata()


        if (b==2):


            a.roomrent()


        if (b==3):


            a.restaurentbill()


        if (b==4):


            a.laundrybill()


        if (b==5):


            a.display()


        if (b==6):


            quit()




main()

