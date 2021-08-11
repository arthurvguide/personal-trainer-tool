  
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('personal-trainer-tool')

clients_data = SHEET.worksheet('clients-data')

data = clients_data.get_all_values()



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
        get_client_details()

    else:
        initial_screen()

def existing_client():
    print("existing client function")

def get_client_details():
    print("\nLet's get client informations...\n")
    # Criar uma class pra geral


def validate_name():
    while True:
        name = input("What is the client name?\n\n").lower()
        
        if name.isalpha():
            return name
            break
        print ("Invalid input! All characters should be alphabet letters (a-z)")

def validate_l_name():
    while True:
        last_name = input("What is the client last name?\n\n").lower()
        
        if last_name.isalpha():
            return last_name
            break
        print ("Invalid input! All characters should be alphabet letters (a-z)")
      

initial_screen()
