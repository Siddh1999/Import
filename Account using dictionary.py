i=0
m=0
dict={12345:"Siddhant",
      12346:"Samer",
      12347:"Suyog",
      12348:"Saurabh",
      "Statement":[]}
while(i==m):
 Ac_number=int(input("Enter your Account Number"))
 x=dict.get(Ac_number)
 if Ac_number in dict :
   print("Your Name is",x)  
   Amount=int(input("Please enter opening balance"))
   print("1.View Bal\n2.Deposite\n3.Withdrawl\n4.Transfer\n5.Statement")
   c=int(input())
   if c==1: 
        print("Your account balance is=",Amount)
        print("Enter 5 to know statement or Press any key to move further")
        c=int(input())
        if c==5:
          dict["Statement"].append("One View")
          b=dict.get("Statement")
          print(b)
   elif c==2:
          Deposite=int(input("Enter amount to be deposite"))
          Now=Deposite+Amount
          print("Your Account is credited for Rs=",Deposite,"Now your Balance is Rs=",Now)
          print("Enter 5 to know statement or Press any key to move further")
          c=int(input())
          if c==5:
            dict["Statement"].append("One Deposite")
            b=dict.get("Statement")
            print(b)
   elif c==3:
        Withdrawl=int(input("Enter a Amount to be withdrawl"))
        if Withdrawl<=Amount:
         Amount=Amount-Withdrawl
         print("You have withdrawl Rs=",Withdrawl,"Now your balance is=",Amount)
         print("Enter 5 to know statement or Press any key to move further")
         c=int(input())
         if c==5:
           dict["Statement"].append("One Withdrawl")  
           b=dict.get("Statement")
           print(b)
        else:
            print("Insufficiant Balance")
   elif c==4:
        print("Name is account holder is",x)
        Ac_number=int(input("Enter benificery Account Number"))
        x=dict.get(Ac_number)
        if Ac_number in dict :
          print("Name of benificery is",x)
          Tra=int(input("Amount to be tranfer"))
          if Tra<=Amount:
              Tra=Amount-Tra
              print("Money transfer successful")
              print("Available balance is",Tra)
          elif Tra>Amount:
              print("Insufficent balance to transfer")
          print("Enter 5 to know statement or Press any key to move further")
          c=int(input())
          if c==5:
            dict["Statement"].append("One Transfer")  
            b=dict.get("Statement")
            print(b)       
        else:
         print("Wrong Account Number")
         print("Do you want to continue? press 1 for yes or 2 for no")
         d=int(input())
         if d==1:
           m=m+1
         elif d==2:
           m=1
           print("exit")
   
       
   elif c==5:
    
       print("0 transaction ")
       print("Do you want to continue? press 1 for yes or 2 for no")
       d=int(input())
   if d==1:
       m=m+1
       i=m
   elif d==2:
     m=1
     print("exit")
        
 else:
     print("Wrong Account Number")
     print("Do you want to continue? press 1 for yes or 2 for no")
     d=int(input())
     if d==1:
         m=m+1
     elif d==2:
        m=1
        print("exit")
