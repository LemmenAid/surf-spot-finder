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
SHEET = GSPREAD_CLIENT.open('surf_spot_finder')


def get_counties():
    """
    Retrieve the list of available counties from the first worksheet
    """
    counties_sheet = SHEET.get_worksheet(0)
    return counties_sheet.row_values(1)
    

def main():
    print("Welcome to the Irish Surf Spot Finder!\n")
    print("We want to help you find the best surfspots in Ireland.")
    print("First thing we need to know to help you on your way is in which County you would like to go surfing..\n")

    # Display the list of available counties
    counties = get_counties()
    print("Here is a list of the available counties:\n")
    for county in counties:
        print(f"- {county}\n")

    # Prompt the user to choose a county
    selected_county = input("Enter the County you want to explore: ")

  
if __name__ == '__main__':
    main()
