import gspread
from google.oauth2.service_account import Credentials
import time

# Set up Google Sheets API credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheet and get the worksheets
SHEET = GSPREAD_CLIENT.open('surf_spot_finder').worksheets()


def get_counties():
    """
    Retrieve a list of available counties from the surf_spot_finder google sheet
    """
    available_counties = [worksheet.title for worksheet in SHEET]
    
    print("Here is a list of the available counties:\n")
    for county in available_counties:
        print(f"- {county}\n")
   





def main():
    """
    Run all program functions
    """
    print("Welcome to the Irish Surf Spot Finder!\n")
    print("We want to help you find the best surf spots in Ireland.")
    print("First thing we need to know to help you on your way is in which County you would like to go surfing..\n")

    # Display the list of available counties
    get_counties()
    # Ask to select a county and display surfspots
    select_county()
     

   
  
if __name__ == '__main__':
    main()

