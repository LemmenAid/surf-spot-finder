import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import time
import sys
import random
import os

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


def title_banner():
    """Display the title with ascii art."""
    title_text = 'Surf Spot Finder!'
    title_art = pyfiglet.figlet_format(
        title_text,
        font='larry3d',
        justify='center')
    print(title_art)


def slow_print(text: str):
    """Print text letter by letter. Speed of the print can be adjusted."""
    for word in text + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()  # defeat buffering
        time.sleep(random.random() * 0.05)


def welcome():
    """
    Welcome the user and explain the purpuse of the app.

    Text is printed slowly, letter by letter.
    """
    title_banner()

    welcome_text = (
        "Welcome to the Surf Spot Finder!\n\n"
        "We want to help you find the best surf spots in Ireland.\n\n"
        "We just need to know in which County you would like to go surfing..\n"
    )

    slow_print(welcome_text)


def get_counties():
    """
    Retrieve list of counties from google sheet and print them.
    returns available_counties.
    """
    available_counties = [worksheet.title for worksheet in SHEET]
    return available_counties


def get_user_county(available_counties):
    """
    Ask user to choose a County they want to go surfing in.
    returns user_county
    """
    
    counties_text = (
        "Here is a list of the available counties:\n"
    )
    slow_print(counties_text)

    for county in available_counties:
        slow_print(f" - {county}")

    """Prompt the user to choose a county and validate the input."""
    while True:
        user_county = input("\nEnter the County you want to explore: ").capitalize().strip()
        if user_county in available_counties:
            return user_county
        else:
            slow_print(f"Sorry, '{user_county}' is not a valid county.")
            continue


def show_spots(user_county):
    """
    Display the surf spots based on the chosen county by user.
    returns surf_spots.
    """
    # retrieve the sheet ID of the selected County
    selected_sheet_id = (
        next(
            (worksheet.id for worksheet in
             SHEET if worksheet.title == user_county), None
            )
    )

    if selected_sheet_id:
        # Retrieve the values from the the selected sheet
        selected_sheet = GSPREAD_CLIENT.open(
            "surf_spot_finder").get_worksheet_by_id(
            selected_sheet_id
        )
        # Exclude the first row
        surf_spot_names = selected_sheet.col_values(1)[1:]

        # clear the terminal for better overview
        clear_terminal()

        # Print the values from the first column
        slow_print(
            f"\nHere's a list of the available surf spots "
            f"in County {user_county}:\n"
        )
        for surfspot in surf_spot_names:
            slow_print(f" - {surfspot}")
        # Return the list of surf spots
        return surf_spot_names

    else:
        #slow_print(f"\nSorry, '{user_county}' is not a valid County.")
        get_counties()
        show_spots(get_user_county())
        # return show_spots(get_user_county())


def get_user_surfspot(user_county, surf_spots):
    """Ask user to choose surfspot and display info."""
    # Retrieve the values from the selected sheet
    selected_sheet = GSPREAD_CLIENT.open(
           "surf_spot_finder"
        ).get_worksheet_by_id(
            next(
                (worksheet.id for worksheet in SHEET
                 if worksheet.title == user_county),
                None
                )
        )

    while True:
        selected_spot = input(
            "\nEnter the surfspot you would like to explore or press 'E' to exit the program:\n"
        ).capitalize().strip()

        if selected_spot in surf_spots:
            # Find the index of the selected surf spot
            spot_index = surf_spots.index(selected_spot)

            surf_spot_levels = selected_sheet.col_values(2)[1:]
            surf_spot_types = selected_sheet.col_values(3)[1:]
            surf_spot_crowds = selected_sheet.col_values(4)[1:]
            surf_spot_accessibility = selected_sheet.col_values(5)[1:]
            surf_spot_wind = selected_sheet.col_values(6)[1:]
            surf_spot_season = selected_sheet.col_values(7)[1:]

            # Display the row data in key-value pairs
            slow_print(f"\nHere are the details for "
                       f"{selected_spot}:\n")
            slow_print(f"Surf Level: {surf_spot_levels[spot_index]}")
            slow_print(f"Type of spot: {surf_spot_types[spot_index]} break")
            slow_print(f"Crowd Level: {surf_spot_crowds[spot_index]}")
            slow_print(f"Accessibility: {surf_spot_accessibility[spot_index]}")
            slow_print(f"Best wind direction: {surf_spot_wind[spot_index]}")
            slow_print(
                f"Best season for consistent "
                f"clean waves: {surf_spot_season[spot_index]}")
            break
        elif selected_spot == 'E':
            clear_terminal()
            break
        else:
            slow_print(
                f"'{selected_spot}' is not a valid surfspot. "
                "Please enter one of the available options."
            )
            continue


def program_continue_options(user_county, available_counties, surf_spots):
    """
    Ask user how they want to continue in program.
    """
    current_state = {
        'user_county': user_county
    }

    while True:
        restart = input(
            "\nWould you like to choose another spot in this County?\n\n"
            "- Enter 'Y' for yes\n"
            "- Enter 'E' to exit the program\n"
            "- Enter 'C' to explore a different County.\n"
        ).upper().strip()

        if restart == "Y":
            user_county = current_state['user_county']
            clear_terminal()
            # Restart from surf spots
            show_spots(user_county)
            get_user_surfspot(user_county, surf_spots)
            program_continue_options(user_county, available_counties, surf_spots)
            break

        elif restart == "E":
            clear_terminal()
            print("\nHave a great surf trip!\n")
            goodbye()
            break

        elif restart == "C":
            clear_terminal()
            # Restart from Counties
            main(show_welcome_message=False)
            break

        else:
            # Direct feedback without raising an exception
            print(f"{restart} is an invalid input! Please enter Y, N or C.")
            continue


def clear_terminal():
    """Clear the terminal."""
    # from: stackoverflow.com/questions/2084508
    os.system('cls' if os.name == 'nt' else 'clear')


def goodbye():
    """Display the title with ascii art."""
    title_text = "Surf is Up!"
    title_art = pyfiglet.figlet_format(
        title_text,
        font='larry3d',
        justify='center')
    print(title_art)


def main(show_welcome_message=True):
    """
    Run all program functions.
    Program restarts without welcome message.
    """
    if show_welcome_message:
        # Welcome message and banner
        welcome()

        # Display the list of available counties
        get_counties()
        available_counties = get_counties()

        # Ask user to select a county
        user_county = get_user_county(available_counties)

        # Display surfspots for chosen County
        surf_spots = show_spots(user_county)

        # Ask user to select surfspot and display the spot info
        get_user_surfspot(user_county, surf_spots)

        # Ask user to choose different surf spot
        program_continue_options(user_county, available_counties, surf_spots)
    else:
        # Restart from Counties
        get_counties()
        available_counties = get_counties()
        user_county = get_user_county(available_counties)
        surf_spots = show_spots(user_county)
        get_user_surfspot(user_county, surf_spots)
        program_continue_options(user_county, available_counties, surf_spots)

if __name__ == '__main__':
    main()
