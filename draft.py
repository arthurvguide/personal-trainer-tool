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
        print ("\nInvalid input! All characters should be alphabet letters (a-z)")

def validate_l_name():
    while True:
        last_name = input("Client last name?\n\n").lower()
        
        if last_name.isalpha():
            return last_name
            break
        print ("\nInvalid input! All characters should be alphabet letters (a-z)")

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
        height = input("Client height (KG) ? It MUST be in Centimeters!!\n\n")
        
        if height.isnumeric():
            return int(height)
            break
        print ("\nInvalid input! All characters should be numbers (1-10)")

def validate_weight():
    while True:
        weight = input("Client weight (kg) ? It MUST be in Kilogram!!\n\n")
        
        if weight.isnumeric():
            return int(weight)
            break
        print ("\nInvalid input! All characters should be numbers (1-10)")

def validate_age():
    while True:
        age = input("Client Age?\n")
        
        if age.isnumeric():
            return int(age)
            break
        print ("\nInvalid input! All characters should be numbers (1-10)")

def act_level():
    print("Client Activite Level? Digit one of the following options\n")
    print(" `1.2` for sedentary (little or no exercise)")
    print(" `1.375` for lightly active (light exercise/sports 1-3 days/week)")
    print(" `1.55` for moderately active (moderate exercise/sports 3-5 days/week")
    print(" `1.725` for very active (hard exercise/sports 6-7 days a week)")
    print(" `1.9` for extra active (very hard exercise/sports & physical job or 2x training)")
    
    while True:
        activite = input()

        if activite == "1.2":
            return float(activite)
            break
        elif activite == "1.375":
            return float(activite)
            break
        elif activite == "1.55":
            return float(activite)
            break
        elif activite == "1.725":
            return float(activite)
            break
        elif activite == "1.9":
            return float(activite)
            break
        else:
            print("Invalid input!")

act_level()
# example = Client(validate_name(), validate_l_name())
# print(example.name)
 
 