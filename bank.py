
#customer text file
file= "./customer.txt"
 

#staff details read from json object file system using json(dictionary) file system of python
def readstaff(files):
    import json
    with open(files,'r') as staffdetails:
        json_data = json.load(staffdetails)
        return json_data

staff= readstaff('./staff.txt')


#login user
def login_success():
    print('welcome today, \n  select an option, select 1, 2 or 3\n (1)  Create new bank account\n (2) Check Account Details\n(3) Logout')
    option= int(input('selection__  '))
    if option == 1:
        CreateAcct(file)
    if option == 2:
        Check_Account_Details(file)
    if option ==3:
        sesssions.clear_sessions()
        print('logged out, bye')
        home()# calling home function after log in success

class sesssions():
    def create_session():
        from datetime import datetime
        sessions=open("session.txt",'w')
        now = datetime.now()
        sessions.write(f'sussion time {now}')
        sessions.close()

    def check_sessions():
        import os
        from pathlib import Path
        sessions= Path('./session.txt')
        if sessions.is_file():
            return True 
        else:
            return False
            
    def clear_sessions():
        import os
        os.remove('session.txt')
        







    



#user validaation function
def loginstaff(staff):
    
    authorization = False
    print('login--')
    while authorization == False:
        
        stafflogin = input('Username: ')
        staffpassword = input('Password: ')
        for obj in staff:
            if obj.get('username')==stafflogin and obj.get('password')==staffpassword:
               authorization = True
               user=obj['full name']
               print(f'success, logged in as {user}')
               sesssions.create_session()#create sessions after succesfull login
               sesssions.check_sessions() #create user sessions on log in
               login_success() # calling home function
        if authorization == False:
            print('authorization failed try again wrong login details')



#account create function
def CreateAcct(file):
    import json
    import random
    print('welcome to new account creation ssection')
    Account_name= input('Account name. ')
    Opening_Balance=input('Opening Balance ')
    Account_Type= input('Account Type ')
    Account_Type= input('Account_email ')
    user_data={}
    user_data[' Account name']= Account_name
    user_data[' Opening Balance']= Opening_Balance
    user_data[' Account Type']= Account_Type
    user_data['Account Type']= Account_Type
    #customer_list.append(user_data)
    values="1234567890"
    acct=''
    acct_no_size=10
    while len(acct)<acct_no_size:
        acct+=random.choice(values)
    acct_no=int(acct)
    print(f'hurray!, set up success , new account number for { Account_name } is {acct_no} ')
    user_data['account number'] =acct_no
    with open(file,'r') as CustomerData:
        json_data = json.load(CustomerData)
        json_data.append(user_data)     
    with open(file,'w') as CustomerData:
        json.dump(json_data,CustomerData)
    login_success() #calling login _success function after creating account success
        
        #json.dump(json_data,CustomerData)

#check account
def Check_Account_Details(file):
    import json
    Account_number= input('Account number ?. ')
    with open(file,'r') as CustomerData:
        json_data = json.load(CustomerData)
        for customer_details in json_data:
            if customer_details.get("account number") == int(Account_number):
                print('customer details found')
                print(customer_details)
                login_success() # calling login success function
        if customer_details.get("account number") != int(Account_number):
             print(f"customer with account no {Account_number} not found in database")
             Check_Account_Details(file)


       



def home():
    if sesssions.check_sessions():
        print('user already logged in sesions')
        login_success()
    else:
        print('welcome today, \n  select an option, select 1 or 2\n (1) login\n (2) close app')
        option= int(input('selection__  '))
        if option == 1:
            loginstaff(staff)
        if option == 2:
            print('have a nice day')
            pass
        else:
            print('please selesct a valid option and try again')
            home() #looping if the user slect a wrong number



#call the home function which is the entry point(function) of the banking system app
# print(sesssions.check_sessions())
home()







            
            


       
           
           
        
      
     
            


           
            


