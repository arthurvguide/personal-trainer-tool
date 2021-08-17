import gspread
from google.oauth2.service_account import Credentials

import string
from random import choice

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

worksheet = SHEET.worksheet('clients-data')


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
    """
    Function to let user decide if wants to consult an
    existing client or go back to the initial screen
    """
    print("\nHit one of the following options")
    print("\n1 - Consult client details")
    print("2 - Exit\n")
    option = input()
    while True:
        if option == "1":
            consult_client()
            return False
        if option == "2":
            print("\nThank you!")
            return False
        print('\nInvalid entry, please try again\n')


def process_client_details():
    """
    Function to get all input deitails from the new client already validated,
    process all necessary calculations (calling other functions), and at
    the end save all data into the worksheet.
    """
    print("\nLet's get client personal data...\n")
    new_client = Client(validate_name(), validate_l_name(), validate_gender(), validate_height(), validate_weight(), validate_age(), activite_level())
    print("\n\nProcessing New Client data...\n\n ")
    print(new_client.description())
    next()

    # Passing Client input values into separate variables, making this possible
    # to interact with them.
    name = new_client.name
    last_name = new_client.last_name
    gender = new_client.gender
    height = new_client.height
    weight = new_client.weight
    age = new_client.age
    act_level = float(new_client.act_level)

    # Call the create id function and pass this to the new client
    id = int(create_id())

    # Calculate the bmi calling its function and pass to the new client
    bmi = check_bmi(name, weight, height)
    next()

    # Calculate the bmr calling its function and pass to the new client
    bmr = check_bmr(name, gender, weight, height, age)
    next()

    # Calculate the diet calling its function and display the result at the end
    diet_process = create_diet(name, bmr, act_level)
    loss = int(diet_process * 0.85)  # less 15% KCAL daily to loss weight
    mantain = int(diet_process)
    gain = int(diet_process * 1.15)  # more 15% KCAL daily to gain weight

    print(f"For WEIGHT LOSS it's recommended: {loss} KCAL daily.")
    print(f"For MANTAIN WEIGHT it's recommended: {mantain} KCAL daily.")
    print(f"For WEIGHT GAIN it's recommended: {gain} KCAL daily.")

    # save all data into the worksheet calling its function
    save_to_worksheet(id, name, last_name, gender, height, weight, age, act_level, bmi, bmr, loss, mantain, gain)


def check_bmi(name, weight, height):
    """
    Function to calculate the client BMI (body mass index)
    """
    print("-------------------------\n")
    print("Let's calculate their (BMI)")
    print("BMI (body mass index) is a measure of whether")
    print("you're a healthy weight for your height\n")

    # Calculate the BMI and show up to the user
    bmi_check = weight / (height/100)**2
    bmi = round(bmi_check, 1)  # only 1 decimal
    print(f"{name} BMI is: {bmi}\n")

    # Condition to check if client is helthy or not
    # comparing its bmi result
    if bmi <= 18.4:
        print(f"{name} is underweight.\n")
    elif bmi <= 24.9:
        print(f"{name} is healthy.\n")
    elif bmi <= 29.9:
        print(f"{name} is over weight.\n")
    elif bmi <= 34.9:
        print(f"{name} is severely over weight.\n")
    elif bmi <= 39.9:
        print(f"{name} is obese.\n")
    else:
        print(f"{name} is severely obese.\n")
    return bmi


def check_bmr(name, gender, weight, height, age):
    """
    Function to calculate the client BMR (Basal metabolic rate)
    """
    print("-------------------------\n")
    print("Let's calculate their (BMR)")
    print("BMR (Basal metabolic rate) is the amount of")
    print("energy expended per day at rest.")
    print("This is fundamental to decide either if it is needed to consume")
    print("more or less KCAL per day, depending on the client objective\n")

    # Calculating BMR formula
    # Male
    # 10 x weight (kg) + 6.25 x height (cm) – 5 x age (y) + 5
    # Female
    # 10 x weight (kg) + 6.25 x height (cm) – 5 x age (y) – 161

    if gender == "m":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    print(f"{name} BMR is: {bmr}\n")
    return bmr


def create_diet(name, bmr, act_level):
    """
    Function to calculate the real KCAL consume of client
    depending on activite level.
    """
    print("-------------------------\n")
    print("Let's create a daily KCAL diet")

    # real_bmr is the BMR multiplied by activite level

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

    print(f"Processing {name} diet...\n\n")
    return real_bmr


def save_to_worksheet(id, name, last_name, gender, height, weight, age, act_level, bmi, bmr, loss, mantain, gain):
    """
    Function to save all client data into the worksheet
    """
    print("\nSaving client to our database...\n\n")

    # Pass all client data into a list and then insert into the worksheet
    client_data = [id, name, last_name, gender, height, weight, age, act_level, bmi, bmr, loss, mantain, gain]
    worksheet.append_row(client_data)

    print("Client succesfully saved!\n")
    print("Thank You!")


def next():
    """
    Function just to make the app more interactable.
    """
    while True:
        next = input(
            'Hit "n" to next\n\n'
        )
        next.lower()

        if next == "n":
            return False
        print('\nInvalid entry, please try again\n')


def create_id():
    """
    Function to creat a unique ID for each client ( 6  numbers)
    ps: I havent checked if the ID created is already been used
    for other clients, because it can happen 1 time in 1.000.000
    0,0001 % probability
    very unlikely to happen in a proportion of the number of clients
    that ONE personal trainer has.
    """
    chars = string.digits
    random = ''.join(choice(chars) for _ in range(6))
    id = random
    return id


def consult_client():
    """
    Function to consult existing client by its ID, and
    if requested, update the client details, or return
    to inital screen.
    """
    id = input("\nPlease, what is the client ID?\n\n")

    # "r" is the row of the worksheet where is based the existing client
    # details, comparing the ID inserted I can find out the row number.

    r = 1
    while worksheet.cell(r, 1).value != id:
        r += 1

    find_client = worksheet.row_values(r)

    # Passing Client Existing data into separate variables, making this
    #  possible to interact with them easily

    name = find_client[1]
    last_name = find_client[2]
    gender = find_client[3]
    height = find_client[4]
    weight = find_client[5]
    age = find_client[6]
    act_level = find_client[7]
    bmi = find_client[8]
    bmr = find_client[9]
    loss = find_client[10]
    mantain = find_client[11]
    gain = find_client[12]

    # Show up informations of the client selected
    print(f"The currently deatails we have from {name} are:\n\n")
    print(f"Name: {name}, Last Name: {last_name}, Gender: {gender}")
    print(f"Height: {height}, Weight: {weight}, Age: {age}")
    print(f"Activite Level: {act_level}")
    print(f"BMI: {bmi}, BMR: {bmr}\n\n")
    print(f"For WEIGHT LOSS it's recommended: {loss} KCAL daily.")
    print(f"For MANTAIN WEIGHT it's recommended: {mantain} KCAL daily.")
    print(f"For WEIGHT GAIN it's recommended: {gain} KCAL daily.")

    # User decide if wants to edit/ update currently informations,
    # or leave the app.

    update_or_exit(name, height, weight, age, act_level, gender, r)


def update_client(name, height, weight, age, act_level, gender, r):
    """
    Function to get and update the new inputs from the user, and then insert
    these data into the worksheet.
    Calculate the BMI, BMR and DIET with the updated data.
    """
    print(f"\n\nLets update {name}'s details\n")
    # Collect the variabels the could have changed

    height = validate_height()
    weight = validate_weight()
    age = validate_age()
    act_level = activite_level()

    # Calculating the new BMI, BMR and DIET using the updated data

    bmi = check_bmi(name, weight, height)
    next()
    bmr = check_bmr(name, gender, weight, height, age)
    next()
    diet_process = create_diet(name, bmr, act_level)

    loss = int(diet_process * 0.85)   # less 15% KCAL daily to loss weight
    mantain = int(diet_process)
    gain = int(diet_process * 1.15)   # more 15% KCAL daily to loss weight

    # Show up the updated diet
    print(f"The new diet for {name} is:\n\n")
    print(f"For WEIGHT LOSS it's recommended: {loss} KCAL daily.")
    print(f"For MANTAIN WEIGHT it's recommended: {mantain} KCAL daily.")
    print(f"For WEIGHT GAIN it's recommended: {gain} KCAL daily.\n\n")
    # Update worksheet with all new informations collected

    worksheet.update_cell(r, 5, height)
    worksheet.update_cell(r, 6, weight)
    worksheet.update_cell(r, 7, age)
    worksheet.update_cell(r, 8, act_level)
    worksheet.update_cell(r, 9, bmi)
    worksheet.update_cell(r, 10, bmr)
    worksheet.update_cell(r, 11, loss)
    worksheet.update_cell(r, 12, mantain)
    worksheet.update_cell(r, 13, gain)

    print(f"{name} was successfully updated")
    print("Thank You!")


def update_or_exit(name, height, weight, age, act_level, gender, r):
    """
    Function to user decide either update cliente details, or
    exit the app.
    """
    print("\nHit one of the following options")
    print("\n1 - Update client details")
    print("2 - Exit\n")
    option = input()

    while True:
        if option == "1":
            update_client(name, height, weight, age, act_level, gender, r)
            return False
        if option == "2":
            print("\nThank you!")
            return False
        print('\nInvalid entry, please try again\n')


initial_screen()
