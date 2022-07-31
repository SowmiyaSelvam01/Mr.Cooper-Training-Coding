import datetime
users={1:"User (Owner)", 2: "User (Tenant)",3:"Admin", 4:"Approver"}
houses_available=[]
requests=[]
main_history=[]
class HouseRental:
    def __init__(self):
        print("WELCOME TO ONLINE HOUSE RENTING PORTAL\n")
    
    def available_houses(self,owner_id=None):
        print()
        if len(houses_available)==0:
            print("No house available!")
            return False
        for index,house in enumerate(houses_available):
            if owner_id==None:
                print("House No:{0} Details:{1}".format(index,house))
            else:
                if house["Owner id"]==owner_id:
                    print("House No:{0} Details:{1}".format(index,house))                    
        return True
    
class History():
    history={}
    
    def add_history(self,user_id,msg):
        curr_time=datetime.datetime.now()
        if user_id not in self.history:
            self.history[user_id]=["{0} at {1}".format(msg,curr_time)]
        else:
            self.history[user_id].append("{0} at {1}".format(msg,curr_time))
        main_history.append("User-{0} {1} at {2}".format(user_id,msg,curr_time))
            
    def show_history(self,option,user_id):
        print("History: (from recent to past)")
        for elem in self.history[user_id][-1::-1]:
            print(elem)
        self.add_history(user_id,"Viewed their history")
        self.user_options(option,user_id)
        
class Owner(History):  
    def post_house(self,user_id):
        house={}
        house["Locality"]=input("\nEnter Locality:")
        house["City"]=input("Enter City:")
        house["Sqft"]=input("Enter Square Feet:")
        house["Type"]=input("Enter Type:")
        house["Rent"]=input("Enter Rent:")
        house["Owner id"]=input("Enter Owner Id:")
        houses_available.append(house)
        self.add_history(user_id,"Added a house") 
        print("\nHouse Added Successfully!!")
        self.user_options(1,user_id)
        
    def remove_house(self,user_id):
        print("\nAvailable houses:")
        if self.available_houses(user_id):
            house_no=int(input("Enter house number to remove: "))
            if house_no>=len(houses_available):
                print("\nWrong House Number!!")
                self.add_history(user_id,"Tried removing a house")
            else:
                houses_available.pop(house_no)
                print("\nHouse Removed Successfully!!")
                self.add_history(user_id,"Removed a house")
        self.user_options(1,user_id)
        
    def view_requests(self,user_id):
        print("\nRental Requests:")
        if len(requests)==0:
            print("No Requests available")
        else:
            flag=False
            for index,request in enumerate(requests):
                if request["House Owner ID"]==user_id:
                    flag=True
                    print("Request No: {0} Request: {1}".format(index,request))
            if not flag:
                print("No Requests available")
                
        self.add_history(user_id,"Viewed Requests")
        self.user_options(1,user_id)



class Tenant:   
    def rent_request(self,user_id):
        request={}
        request["Name"]=input("\nEnter Name: ")
        request["House No"]=input("Enter House No: ")
        request["Tenant User ID"]=input("Enter Tenant User ID: ")
        request["House Owner ID"]=input("Enter House Owner ID: ")
        request["Approval status"]="Pending"
        requests.append(request)
        print("\nRequest Submitted Successfully!!")
        self.add_history(user_id,"Requested a house for rent")
        self.user_options(2,user_id)
        
    def view_available_houses(self,user_id):        
        self.available_houses()
        self.add_history(user_id,"Viewed available houses")
        self.user_options(2,user_id)
        
class Admin:
    def view_all_requests(self,user_id):
        if len(requests)==0:
            print("No Requests available")
        else:
            print("\n All Requests")
            for index,request in enumerate(requests):
                print("Request No: {0} Request: {1}".format(index,request))
        self.add_history(user_id,"Viewed all requests")
        if user_id==3:
            self.user_options(3,user_id)  
        else:
            return 
        
    def view_user_activities(self,user_id):
        if len(main_history)==0:
            print("No user activities")
        else:
            print("\nAll User Activities:")
            for row in main_history[-1::-1]:
                print(row)
        self.add_history(user_id,"Viewed all user activities")
        self.user_options(3,user_id)
        
    def view_all_available_houses(self,user_id):        
        self.available_houses()
        self.add_history(user_id,"Viewed all available houses")
        self.user_options(3,user_id)
        
class Approver:
    def update_approval(self,user_id):
        self.view_all_requests(user_id)
        update_request_num=int(input("Enter request number to update"))
        for request_num,request in enumerate(requests):
            if request_num==update_request_num:
                request["Approval status"]=input("Enter yes/no:")
            print("Approval status updated!!")
            print(request)
            self.add_history(user_id,"Updated the approval status of House {0}".format(request_num))
        self.user_options(4,user_id)
                

class userType(HouseRental,Owner,Tenant,Admin,Approver,History):
    houses=[]
    user_id=None
    def options(self):
        for key,val in users.items():
            print("{0}. {1}".format(key,val))
        user_type=int(input("Enter user-type(1-4):"))
        print("\nWelcome {0}".format(users[user_type]))
        self.user_options(user_type,False)
        
    def relogin(self,user_id):
        self.add_history(user_id,"Logged Out")
        print("\nLogged Out successfully!!")
        print("USE PORTAL AGAIN??")
        login=input("Enter y/n: ")
        if login=="y":
            self.options()
        else:
            print("Thank you for using the Online House Renting Portal!!")
        
    def user_options(self,user_type,user_id):
        if user_type==1:
            if not user_id:
                user_id=input("Enter your id:")
                self.add_history(user_id,"Logged In")
            print("\nUser (owner) Options:")
            print("1. Post a house for rental")
            print("2. Remove house from rental")
            print("3. View requests")
            print("4. Show History")
            print("5: Logout")
            option=int(input("\nEnter option number:"))
            if option==1:
                self.post_house(user_id)
            elif option==2:
                self.remove_house(user_id)
            elif option==3:
                self.view_requests(user_id)
            elif option==4:
                self.show_history(1,user_id)
            else:
                self.relogin(user_id)
            
            
        elif user_type==2:
            if not user_id:
                user_id=input("Enter your id:")
                self.add_history(user_id,"Logged In")
            print("\nUser (Tenant) Options:")
            print("1. Request to rent a house")
            print("2. View available houses")
            print("3. Show History")
            print("4. Quit")
            option=int(input("Enter option: "))
            if option==1:
                self.rent_request(user_id)
            elif option==2:
                self.view_available_houses(user_id)
            elif option==3:
                self.show_history(2,user_id)
            else:
                self.relogin(user_id)
        elif user_type==3:
            if not user_id:
                user_id="Admin"
                self.add_history(user_id,"Logged In")
            print("\nAdmin Options:")
            print("1. View requests")
            print("2. View available house data")
            print("3. View user activities")
            print("4. Logout")
            option=int(input("Enter option number:"))
            if option==1:
                self.view_all_requests(user_id)
            elif option==2:
                self.view_all_available_houses(user_id)
            elif option==3:
                self.view_user_activities(user_id)
            else:
                self.relogin(user_id)
        
        elif user_type==4:
            if not user_id:
                user_id="Approver"
                self.add_history(user_id,"Logged In")
            print("\nApprover Options:")
            print("1. View and Approve Requests")
            print("2. Show History")
            print("3. Logout")
            option=int(input("Enter option number:"))
            if option==1:
                self.update_approval(user_id)
            elif option==2:
                self.show_history(4,user_id)
            else:
                self.relogin(user_id)

                       
if __name__=="__main__":
    x=userType()
    x.options()
    
