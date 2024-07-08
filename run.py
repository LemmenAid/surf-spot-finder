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


def show_spots(user_county): 
    """
    Display the surf spots for the chosen county.
    """
       # Find the sheet ID of the selected County
    selected_sheet_id = next((worksheet.id for worksheet in SHEET if worksheet.title == user_county), None)
     
    if selected_sheet_id:
        # Retrieve the values from the first column of the selected sheet
        selected_sheet = GSPREAD_CLIENT.open("surf_spot_finder").get_worksheet_by_id(selected_sheet_id)
        surf_spot_names = selected_sheet.col_values(1)

        surf_spot_levels = selected_sheet.col_values(2)
        surf_spot_types = selected_sheet.col_values(3)
        surf_spot_crowds = selected_sheet.col_values(4)
        surf_spot_accessibility = selected_sheet.col_values(5)


        # Print the values from the first column
        print(f"Here is a list of the available surf spots in County {user_county}:\n")
        for surfspot in surf_spot_names:
            print(f"- {surfspot}\n")
    else:
        print(f"Sorry, '{user_county}' is not a valid county.") 
        get_counties()
        show_spots(get_user_county())


def get_user_surfspot():
    """
    Prompt the user to choose a surfspot they want to explore.
    """
    print("Would you like to know more about one of these spots?")
    return input("Enter the surfspot you would like to explore: \n").capitalize()


def show_spot_info(user_surfspot):
    # Find the index of the selected surf spot
        spot_index = surf_spot_names.index(user_surfspot)

        # Display the row data in key-value pairs
        print(f"\nDetails for {selected_spot}:")
        print(f"Surf Level: {surf_spot_levels[spot_index]}")
        print(f"Type: {surf_spot_types[spot_index]}")
        print(f"Crowd Level: {surf_spot_crowds[spot_index]}")
        print(f"Accessibility: {surf_spot_accessibility[spot_index]}")



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
    user_county = get_user_county()
    # Display surfspots for chosen County
    #show_spots(user_county)
    show_spots(user_county)
    # Ask user to select surfspot for more info 
    user_surfspot = get_user_surfspot()
    # Print to check
    print(user_surfspot)

    #show_spot_info(user_surfspot)

    
   
  
if __name__ == '__main__':
    main()

