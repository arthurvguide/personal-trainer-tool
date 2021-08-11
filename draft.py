class Client:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


def validate_name():
    while True:
        name = input("What is the client name?\n\n").lower()
        
        if name.isalpha():
            return name
            break
        print ("Invalid input! All characters should be alphabet letters (a-z)")

def validate_l_name():
    while True:
        name = input("What is the client last name?\n\n").lower()
        
        if name.isalpha():
            return last_name
            break
        print ("Invalid input! All characters should be alphabet letters (a-z)")
    
Client(validate_name(), validate_l_name())
print(Client)

