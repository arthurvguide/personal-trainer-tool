  
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
            'Hit "n" to new client or "e" for existing client:\n\n'
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
    print("new client function")

def existing_client():
    print("existing client function")

initial_screen()
