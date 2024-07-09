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
        print(f"- {county}")


def get_user_county():
    """
    Prompt the user to choose a County they want to go surfing in.
    """
    return input("\nEnter the County you would like to explore: \n").capitalize()


def show_spots(user_county): 
    """
    Display the surf spots based on the chosen county by user.
    """
    # retrieve the sheet ID of the selected County
    selected_sheet_id = next((worksheet.id for worksheet in SHEET if worksheet.title == user_county), None)
     
    if selected_sheet_id:
        # Retrieve the values from the the selected sheet
        selected_sheet = GSPREAD_CLIENT.open("surf_spot_finder").get_worksheet_by_id(selected_sheet_id)
        surf_spot_names = selected_sheet.col_values(1)

        # Print the values from the first column
        print(f"\nHere is a list of the available surf spots in County {user_county}:\n")
        for surfspot in surf_spot_names:
            print(f"- {surfspot}")
    else:
        print(f"\nSorry, '{user_county}' is not a valid county.") 
        get_counties()
        show_spots(get_user_county())


def get_user_surfspot(user_county):
    """
    Prompt the user to choose a surfspot they want to explore and display the spot info.
    """
    print("\nWould you like to know more about one of these spots?")
    selected_spot = input("Enter the surfspot you would like to explore: \n").capitalize()

    if selected_spot:
        # Retrieve the sheet ID of the selected County
        selected_sheet_id = next((worksheet.id for worksheet in SHEET if worksheet.title == user_county), None)
     
        # Retrieve the values from the the selected sheet
        selected_sheet = GSPREAD_CLIENT.open("surf_spot_finder").get_worksheet_by_id(selected_sheet_id)
        surf_spot_names = selected_sheet.col_values(1)
        surf_spot_levels = selected_sheet.col_values(2)
        surf_spot_types = selected_sheet.col_values(3)
        surf_spot_crowds = selected_sheet.col_values(4)
        surf_spot_accessibility = selected_sheet.col_values(5)
            
        # Find the index of the selected surf spot
        spot_index = surf_spot_names.index(selected_spot)

        # Display the row data in key-value pairs
        print(f"\nHere are the details for {selected_spot}:\n")
        print(f"Required surf Level: {surf_spot_levels[spot_index]}")
        print(f"Type of spot: {surf_spot_types[spot_index]} break")
        print(f"Crowd Level: {surf_spot_crowds[spot_index]}")
        print(f"Accessibility: {surf_spot_accessibility[spot_index]}")
    
    else:
        print(f"Sorry, '{selected_spot}' is not a valid surfspot. Please enter one of the available options") 
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
    user_county = get_user_county()
    
    # Display surfspots for chosen County
    show_spots(user_county)

    # Ask user to select surfspot and display the spot info 
    get_user_surfspot(user_county)

  
if __name__ == '__main__':
    main()

