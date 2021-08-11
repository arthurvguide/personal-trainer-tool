class Client:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


def validate_name():
    while True:
        name = input("Client name?\n\n").lower()
        
        if name.isalpha():
            return name
            break
        print ("Invalid input! All characters should be alphabet letters (a-z)")

def validate_l_name():
    while True:
        last_name = input("Client last name?\n\n").lower()
        
        if last_name.isalpha():
            return last_name
            break
        print ("Invalid input! All characters should be alphabet letters (a-z)")

def validate_gender():
    while True:
        gender = input("Client gender?  hit 'f' for female or 'm' for male\n\n")

        if gender == "f":
            return gender
            break
        elif gender == "m":
            return gender
            break
        else:
            print("Invalid input!")

def validate_height():
    while True:
        height = input("Client height (KG) ? It MUST be in KG\n\n")
        
        if height.isnumeric():
            return int(height)
            break
        print ("Invalid input! All characters should be numbers (1-10)")


validate_height()
# example = Client(validate_name(), validate_l_name())
# print(example.name)

 