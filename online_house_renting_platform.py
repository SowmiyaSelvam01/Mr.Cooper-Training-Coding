
users={1:"User (Owner)", 2: "User (Tenant)",3:"Admin", 4:"Approver"}
houses_available=[]
requests=[]
class HouseRental:
    def __init__(self):
        print("WELCOME TO ONLINE HOUSE RENTING PORTAL\n")
    
    def available_houses(self):
        print()
        if len(houses_available)==0:
            print("No house available!")
            return False
        for index,house in enumerate(houses_available):
            print("House No:{0} Details:{1}".format(index,house))
        return True
    
        
class Owner(userType):
    
    def post_house(self):
        house={}
        house["Locality"]=input("\nEnter Locality:")
        house["City"]=input("Enter City:")
        house["Sqft"]=input("Enter Square Feet:")
        house["Type"]=input("Enter Type:")
        house["Rent"]=input("Enter Rent:")
        house["Owner id"]=input("Enter Owner Id:")
        houses_available.append(house)
        print("\nHouse Added Successfully!!")
        self.user_options(1)
        
    def remove_house(self):
        print("\nAvailable houses:")
        if self.available_houses():
            house_no=int(input("Enter house number to remove: "))
            houses_available.pop(house_no)
            print("\nHouse Removed Successfully!!")
        self.user_options(1)
        
    def view_requests(self):
        print("\nRental Requests:")
        if len(requests)==0:
            print("No Requests available")
        else:
            for index,request in enumerate(requests):
                print("Request No: {0} Request: {1}".format(index,request))
        self.user_options(1)



class Tenant(userType):
    
    def rent_request(self):
        self.available_houses()
        request={}
        request["Name"]=input("\nEnter Name: ")
        request["House No"]=input("Enter House No: ")
        request["Tenant User ID"]=input("Enter Tenant User ID: ")
        request["House Owner ID"]=input("Enter House Owner ID: ")
        requests.append(request)
        print("\nRequest Submitted Successfully!!")
        self.relogin()

class userType(HouseRental,Owner,Tenant):
    houses=[]
    def options(self):
        for key,val in users.items():
            print("{0}. {1}".format(key,val))
        user_type=int(input("Enter user-type(1-4):"))
        print("\nWelcome {0}".format(users[user_type]))
        self.user_options(user_type)
        
    def relogin(self):
        print("\nLogged Out successfully!!")
        print("USE PORTAL AGAIN??")
        login=input("Enter y/n: ")
        if login=="y":
            self.options()
        
    def user_options(self,user_type):
        if user_type==1:
            print("\nUser (owner) Options:")
            print("1. Post a house for rental")
            print("2. Remove house from rental")
            print("3. View requests")
            print("4: Logout")
            option=int(input("\nEnter option number:"))
            if option==1:
                self.post_house()
            elif option==2:
                self.remove_house()
            elif option==3:
                self.view_requests()
            else:
                self.relogin()
            
            
        elif user_type==2:
            print("\nUser (Tenant) Options:")
            print("1. Request to rent a house")
            print("2. Quit")
            option=int(input("Enter option: "))
            if option==1:
                self.rent_request()
            else:
                self.options()
        elif user_type==3:
            print("\nAdmin Options:")
            print("1. View reports")
            print("2. Make advertisements")
            option=int(input("Enter option number:"))
        
        elif user_type==4:
            print("\nApprover Options:")
            print("View Requests")   

                       
if __name__=="__main__":
    x=userType()
    x.options()
    