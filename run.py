  
import gspread
from google.oauth2.service_account import Credentials

from client import *

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('personal-trainer-tool')

clients_worksheet = SHEET.worksheet('clients-data')


def initial_screen():
    """
    The personal trainer professional is greeted with this welcome screen,
    from here user can either choose the patient or staff section.
    """
    welcome_greeting = '\nWelcome to the Personal Trainer Tool\n'
    print(welcome_greeting.upper())
    print('Made for use by Personal Trainer Professional\n')
    print('To use this app, hit enter after each choice.\n')

    while True:
        nclient_or_eclient = input(
            'Hit "n" to add new client or "e" for existing client:\n\n'
        )
        nclient_or_eclient = nclient_or_eclient.lower()

        if nclient_or_eclient == "n":
            new_client()
            return False

        if nclient_or_eclient == "e":
            existing_client()
            return False

        print('\nInvalid entry, please try again\n')

def new_client():
    """
    Function to let user continue with add new client or go back,
    for example if a user entered the wrong input
    """
    print("\nLet's add a new client...\n")
    print('Client data will be saved to our database upon confirmation.\n\n')
    new_or_back = input(
        'Hit "1" to continue or any other key to go back.\n\n'
        )
    if new_or_back == "1":
        #  Initiate the adding process if user chooses to continue
        process_client_details()

    else:
        initial_screen()

def existing_client():
    print("existing client function")

def process_client_details():
    
    print("\nLet's get client personal data...\n")
    new_client = Client(validate_name(),validate_l_name(), validate_gender(), validate_height(), validate_weight(), validate_age(), activite_level())
    print("\n\nProcessing New Client data...\n\n ")
    print(new_client.description())
    print("Client succesfully created!\n")
   
    """
    Passing Client input values into variables, making this possible to interact with them.
    """
    name = new_client.name
    last_name = new_client.last_name
    gender = new_client.gender
    height = new_client.height
    weight = new_client.weight
    age = new_client.age
    act_level = float(new_client.act_level)
    
    # update_worksheet()
    # print("Saving client to our database...\n")
    # print("Client succesfully saved!")
    bmi = check_bmi(name, weight, height)
    bmr = check_bmr(name, gender, weight, height, age)
    
    diet_process = create_diet(bmr, act_level)
    
def check_bmi(name, weight, height):
    print("-------------------------\n")
    print("Let's calculate their (BMI)")
    print("BMI (body mass index) is a measure of whether you're a healthy weight for your height\n")
    bmi_check = weight / (height/100)**2
    bmi = round(bmi_check,1)
    print(f"{name} BMI is: {bmi}\n")

    if bmi <= 18.4:
        print(f"{name} is underweight.")
    elif bmi <= 24.9:
        print(f"{name} is healthy.")
    elif bmi <= 29.9:
        print(f"{name} is over weight.")
    elif bmi <= 34.9:
        print(f"{name} is severely over weight.")
    elif bmi <= 39.9:
        print(f"{name} is obese.")
    else:
        print(f"{name} is severely obese.")
    

def check_bmr(name, gender, weight, height, age):
    print("-------------------------\n")
    print("Let's calculate their (BMR)")
    print("BMR (Basal metabolic rate) is the amount of energy expended per day at rest.")
    print("This is fundamental to decide either if it is needed to consume more or less KCAL per day, depending on the client objective\n")

    """
    Calculating BMR formula
    Male
    10 x weight (kg) + 6.25 x height (cm) – 5 x age (y) + 5
    Female
    10 x weight (kg) + 6.25 x height (cm) – 5 x age (y) – 161
    """
    if gender == "m":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    print(f"{name} BMR is: {bmr}\n")
    return bmr
    
def create_diet(bmr, act_level):
    print("-------------------------\n")
    print("Let's create a daily KCAL diet")
    if act_level == 1.2:
        real_bmr = bmr * 1.2
    elif act_level == 1.375:
        real_bmr = bmr * 1.375
    elif act_level == 1.55:
        real_bmr = bmr * 1.55
    elif act_level == 1.725:
        real_bmr = bmr * 1.725
    else:
        real_bmr = bmr * 1.9
    
    return real_bmr
    
    #mantain = real_bmr 
    #gain = real_bmr * 1.15
    #loss = real_bmr * 0.85
 
initial_screen()
# bmi = check_bmi("Arthur", 75, 180)
# print(bmi)

#bmr = check_bmr("f", 74, 176, 21)

# creat_diet(1740, 1.2)