class Client:
    def __init__(self, name, last_name, gender, height, weight, age, act_level):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.act_level = act_level

    def description(self):
        """
        Describes the instance of the new Client
        """
        print(f"Name: {self.name}, Last Name: {self.last_name}, Gender: {self.gender}")
        print(f"Height: {self.height}, Weight: {self.weight}, Age: {self.age}, Activite Level: {self.act_level}")

def validate_name():
    """
    Function to get the name input and validate.
    """
    while True:
        name = input("Client name?\n\n").lower()
        
        if name.isalpha():
            return name
            break
        print ("\nInvalid input! All characters should be alphabet letters (a-z)")

def validate_l_name():
    """
    Function to get the last name input and validate.
    """
    while True:
        last_name = input("Client last name?\n\n").lower()
        
        if last_name.isalpha():
            return last_name
            break
        print ("\nInvalid input! All characters should be alphabet letters (a-z)")

def validate_gender():
    """
    Function to get the gender input and validate
    """
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
    """
    Function to get the height input and validate.
    """
    while True:
        height = input("Client height (CM) ? It MUST be in Centimeters!!\n\n")
        
        if height.isnumeric():
            return int(height)
            break
        print ("\nInvalid input! All characters should be numbers (1-10)")

def validate_weight():
    """
    Function to get the weight input and validate.
    """
    while True:
        weight = input("Client weight (kg) ? It MUST be in Kilogram!!\n\n")
        
        if weight.isnumeric():
            return int(weight)
            break
        print ("\nInvalid input! All characters should be numbers (1-10)")

def validate_age():
    """
    Function to get the age input and validate.
    """
    while True:
        age = input("Client Age?\n\n")
        
        if age.isnumeric():
            return int(age)
            break
        print ("\nInvalid input! All characters should be numbers (1-10)")

def activite_level():
    """
    Function to get the activite level input and validate.
    """
    print("Client Activite Level? Digit one of the following options:\n")
    print(" '1.2' for sedentary (little or no exercise)")
    print(" '1.375' for lightly active (light exercise/sports 1-3 days/week)")
    print(" '1.55' for moderately active (moderate exercise/sports 3-5 days/week")
    print(" '1.725' for very active (hard exercise/sports 6-7 days a week)")
    print(" '1.9' for extra active (very hard exercise/sports & physical job)")
    
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