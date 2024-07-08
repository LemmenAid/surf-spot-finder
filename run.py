import gspread
from google.oauth2.service_account import Credentials


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
    and print them to the terminal.
    """
    available_counties = [worksheet.title for worksheet in SHEET]
    print("Here is a list of the available counties:\n")
    for county in available_counties:
        print(f"- {county}\n")


def get_user_county():
    """
    Prompt the user to choose a County they want to go surfing in.
    """
    return input("Enter the County you want to explore: \n").capitalize()


def show_spots(selected_county): 
    """
    Display the surf spots for the chosen county.
    """
       # Find the sheet ID of the selected County
    selected_sheet_id = next((worksheet.id for worksheet in SHEET if worksheet.title == selected_county), None)
     
    if selected_sheet_id:
        # Retrieve the values from the first column of the selected sheet
        selected_sheet = GSPREAD_CLIENT.open("surf_spot_finder").get_worksheet_by_id(selected_sheet_id)
        selected_county_surfspots = selected_sheet.col_values(1)

        # Print the values from the first column
        print(f"Here is a list of the available surf spots in County {selected_county}:\n")
        for surfspot in selected_county_surfspots:
            print(f"- {surfspot}\n")
    else:
        print(f"Sorry, '{selected_county}' is not a valid county.") 
        get_counties()
        show_spots(get_user_county())




def main():
    """
    Run all program functions
    """
    print("Welcome to the Irish Surf Spot Finder!\n")
    print("We want to help you find the best surf spots in Ireland.")
    print("First thing we need to know to help you on your way is in which County you would like to go surfing..\n")

    # Display the list of available counties
    get_counties()
    # Ask user to select a county 
    selected_county = get_user_county()
    # Display surfspots for chosen County
    show_spots(selected_county)
     

   
  
if __name__ == '__main__':
    main()

