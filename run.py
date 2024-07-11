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
    """Retrieve list of counties from google sheet and print them."""
    available_counties = [worksheet.title for worksheet in SHEET]

    counties_text = (
        "Here is a list of the available counties:\n"
    )

    slow_print(counties_text)

    for county in available_counties:
        slow_print(f" - {county}")


def get_user_county():
    """Ask user to choose a County they want to go surfing in."""
    slow_print(
        "\nAbout which County would you like to know more?"
    )
    return input("Enter the County you would like to explore: \n").capitalize()


def show_spots(user_county):
    """Display the surf spots based on the chosen county by user."""
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
    else:
        slow_print(f"\nSorry, '{user_county}' is not a valid County.")
        get_counties()
        show_spots(get_user_county())


def get_user_surfspot(user_county):
    """Ask user to choose surfspot and display info."""
    slow_print(
        "\nAbout which spot would you like some more information?"
    )

    while True:
        selected_spot = input(
            "Enter the surfspot you would like to explore:\n"
        ).capitalize()

        # Retrieve the values from the selected sheet
        try:
            selected_sheet = GSPREAD_CLIENT.open(
                "surf_spot_finder"
            ).get_worksheet_by_id(
                next(
                    (worksheet.id for worksheet in SHEET if worksheet.title == user_county),
                    None
                )
            )
            surf_spot_names = selected_sheet.col_values(1)
        except gspread.exceptions.SpreadsheetNotFound:
            slow_print("Error: Spreadsheet 'surf_spot_finder' not found.")
            return
        except gspread.exceptions.WorksheetNotFound:
            slow_print(f"Error: Worksheet for '{user_county}' not found.")
            return

        if selected_spot in surf_spot_names:
            # Find the index of the selected surf spot
            spot_index = surf_spot_names.index(selected_spot)

            surf_spot_levels = selected_sheet.col_values(2)
            surf_spot_types = selected_sheet.col_values(3)
            surf_spot_crowds = selected_sheet.col_values(4)
            surf_spot_accessibility = selected_sheet.col_values(5)
            surf_spot_wind = selected_sheet.col_values(6)
            surf_spot_season = selected_sheet.col_values(7)

            # Display the row data in key-value pairs
            slow_print(f"\nHere are the details for {selected_spot}:\n")
            slow_print(f"Suitable for surf Level: {surf_spot_levels[spot_index]}")
            slow_print(f"Type of spot: {surf_spot_types[spot_index]} break")
            slow_print(f"Crowd Level: {surf_spot_crowds[spot_index]}")
            slow_print(f"Accessibility: {surf_spot_accessibility[spot_index]}")
            slow_print(f"Best wind direction: {surf_spot_wind[spot_index]}")
            slow_print(
                f"Best season for consistent "
                f"clean waves: {surf_spot_season[spot_index]}"
            )
            break

        else:
            slow_print(
                f"'{selected_spot}' is not a valid surfspot. "
                "Please enter one of the available options."
            )
            continue


def program_continue_options(user_county):
    """
    Ask user if they want to choose a different option.

    If Yes, the app restarts; if No, the app ends.
    """
    current_state = {
        'user_county': user_county
    }

    while True:
        restart = input(
            "\nWould you like to choose another spot in this County?\n\n"
            "- Enter Y for yes\n"
            "- N for no\n"
            "- C to choose a different County.\n"
        ).upper().strip()

        if restart == "Y":
            user_county = current_state['user_county']
            clear_terminal()
            # Restart from surf spots
            show_spots(user_county)
            get_user_surfspot(user_county)
            program_continue_options(user_county)
            break # exit the loop

        elif restart == "N":
            print("\nHave a great surf trip!\n")
            goodbye()
            break

        elif restart == "C":
            clear_terminal()
            # Restart from Counties
            get_counties()
            new_user_county = get_user_county()
            show_spots(new_user_county)
            get_user_surfspot(new_user_county)
            program_continue_options(new_user_county)
            break

        else:
            # Direct feedback without raising an exception
            print(f"Sorry, {restart} is an invalid input! Please enter Y, N or C.")
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


def main():
    """Run all program functions."""
    # Welcome message and banner
    welcome()

    # Display the list of available counties
    get_counties()

    # Ask user to select a county
    user_county = get_user_county()

    # Display surfspots for chosen County
    show_spots(user_county)

    # Ask user to select surfspot and display the spot info
    get_user_surfspot(user_county)

    # Ask user to choose different surf spot
    program_continue_options(user_county)


if __name__ == '__main__':
    main()
