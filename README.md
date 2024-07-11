# SURF SPOT FINDER

![Main Mockup](README-files/mockup-main.png)

[View Live Website here.](https://heroku)

[GitHub Repo](https://github.com/LemmenAid/surf-spot-finder)

*** 

## Project Description  

_Surf Spot Finder is a CLI application for my third portfolio project with [Code Institute](https://codeinstitute.net/ie/)._

The Surf Spot Finder is a CLI application that helps users find the best surf spots in different counties in Ireland. Users can choose from a list of available counties in Ireland to view the surf spots in that county. After selecting a county, the application will display a list of surf spots in that county.
Users can then choose a specific surf spot from the list to view more detailed information about that spot.

## Project Purpose

The Surf Spot Finder is a user-friendly command-line interface (CLI) application designed to help surf enthusiasts in Ireland discover the best surf spots. By providing a comprehensive database of surf spots across various counties, the application aims to enhance the surfing experience for both locals and visitors alike. With its intuitive features, the Surf Spot Finder simplifies the process of finding suitable surf spots, making it easier for users to plan their surfing adventures and make the most of Ireland's diverse coastal regions.

***

## Index – Table of Contents

* [User Experience (UX)](#user-experience)
* [Logic Flow](#logic-flow)
* [Design](#design)
* [Features](#features)
* [Libraries and Technologies Used](#libraries-and-technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

***

## User Experience (UX)

### User Stories

1. As a first time user, I want to easily understand the main purpose of the app. 
2. As a new user, I want to easily navigate the app. 
3. As a returning user I want to find information on different surfspots in Ireland.

***

## Logic Flow
Starting to design my project with a flowchart has been extremely helpful. It gave me an overview of the logic I needed to follow during the writing of the app. Creating this flowchart has helped me to break up the logic within functions, making the code more modular and easier to follow.

It also made it easier for me to navigate the debugging process more efficiently. The visual nature of the diagrams has enabled me to spot potential issues and trace the flow of execution more effectively, ultimately leading to a smoother development experience.

**There may be some differences because I drew the flowchart before I started my project.**

![Flow Chart](./readme-images/flowchart.png)

***

## Design

* ASCII art to make the welcome and good-bye screens a bit more interesting.
* The colour scheme of this app has not been changed, to keep it classic and simple.
* The type of script has also not been changed, the original one was well suited for this application.

***

## Features 

### ASCII Art

ASCII Art is used as a title for the app to improve the user experience and to get the user interested.

![ACSII Art](./readme-images/banner-surfspot.png)

### Slow Print

The text in the app are printed slowly to improve user experience and to make sure that the user is not overwhelmed by the text appearing on the screen.

### Welcome Message

* As soon as the page is loaded, the ASCII Art is displayed and a welcome message is gradually printed out. 
In the welcome message the purpuse of the app is explained. 

![Welcome](README-files/welcome.png)

### Counties

* After the welcome message a list of available Counties is displayed and the user is promted to choose a County where they want to go surfing and want to explore.

![Spot Details](README-files/counties.png)

### Surfspots

* After choosing a County a list of available surfspots for that County are displayed.

![Surfspots](README-files/surfspots.png)

### Surfspot Details

* After choosing a spot more detailed information is given about the chosen spot.

![Spot Details](README-files/spot-details.png)

### Program Continue Options

* After more detailed info is given about the chosen surfspot, the user can choose between 3 options on how to continue in the app. They can either choose another surfspot in the same County, choose a different County they want to explore or exit the program.

![Options](README-files/continue.png) 

### Goodbye Message

* At the end of the quiz the score is displayed and the user can choose between two option buttons:
play again or choose a different quiz. 

![Goodbye](README-files/goodbye.png)


### Future Implementations

* In the future, I could implement the user name usage and favorite surf spots tracking functionality.

*** 

## Libraries and Technologies Used

* [Github](https://github.com/) - Used for hosting the repository.
* [Heroku](https://heroku.com/) - Used for deploying the live project.n.
* [Gitpod](https://www.gitpod.io/#get-started) - Used for developing the application.
* [Python](https://www.python.org/) - Used for adding functionality to the application.
* [Lucidchart](https://lucid.co/) - Used for creating the app flowchart.
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validation python code.

### Python Libraries

* [Pyfiglet](https://pypi.org/project/pyfiglet/) - Used for the opening title and Goodbye message.
* [Time](https://docs.python.org/3/library/time.html) - Used for the slow print functionality and for delaying print statements.
* [Sys](https://docs.python.org/3/library/sys.html) - Used to provide access to some variables used or maintained by the interpreter.
* [Random](https://docs.python.org/3/library/random.html) - Used within the slow print functionality.
* [OS](https://docs.python.org/3/library/os.html) - Used to clear the screen in the terminal.

***

## Testing

The app has been tested by myself and several of my friends and family members for accessibility, functionality, responsiveness, performance and visual appeal.

### Python - PEP8 Testing

The [CI Python Linter](https://pep8ci.herokuapp.com/#) is used for validation python code. The run.py file was checked and no errors were reported:

![alt text](README-files/pep8.png)

### Input Testing

During testing I frequently checked if all the inputs were valid, namely if my validation functions were catching all errors and exceptions.

All of the above tests were completed in my local terminal and also in the Heroku terminal.

***

## Deployment to Heroku

### Project Deployment

I have taken this part from the README of https://github.com/lucia2007/towers-of-hanoi/ <br>

The application was deployed to Heroku. In order to deploy, the following steps were taken:

1. If you have an account, login to Heroku. Otherwise create a new account.
2. Once signed in, click the button "New" in the top right corner, below the header and choose "Create new app".
3. Choose a unique name for the application and select your region. When done, click "Create app".
4. This brings you to the "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars". In the KEY input field, enter "PORT" and in the VALUE input field, enter "8000". After that, click the "Add" button on the right.
5. Afterwards, scroll down to the "Buildpacks" section of the settings page and click the button "Add buildpack".
6. First add "Python" package and then "node.js". 
7. If you exchanged the order of the packages, just drag the Python package above.
8. Scroll back to the top of the page and choose the "Deploy" tab. Then choose "GitHub" as Deployment method.
9. Go to "Connect to GiHub" section, search for the repository and then click "Connect".
10. In the "Automatic Deploys" section, choose your preferred method for deployment. At first, I used the manual deployment option, and later I changed it to automatic deploys. Afterwards, click "Deploy Branch".

### Forking repo on GitHub

I have taken the following from the Sample README from Code Institute for this deployment section. <br>

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

***

## Credits

* I would like to thank Brian Macharia for his great mentor support and guidance - helping me through the process of building my first ever CLI application.
* My facilitator Amy from Code Institute for supporting us through our third project and giving us great tips and resources for learning tools, and her feedback during the weekly stand-ups.
* At last I would like to give thanks to my friends and family for taking the time to test the application and giving me great feedback.

### Content

I have taken information from the following websites for the Surf Spot Google Sheet:
* [Surf Forecast](https://www.surf-forecast.com/)
* [Discovering Cork](http://www.discoveringcork.ie/surfing/)
* [Surfer Today](https://www.surfertoday.com/surfing/the-best-surf-spots-in-ireland)
* [Surfline](https://www.surfline.com/travel/ireland-surfing-and-beaches/2963597)


### Code

The walkthrough project "Love Sandwiches" was a great way of understanding how to get started on an CLI application and it was therefor a good source of inspiration. 
I decided to make an app that can help users to find information on surfspots per County in Ireland. 
I have used various resources to help me with figuring out how to create the Surf Spot Finder app:

* [Stack overflow](https://stackoverflow.com/)
* [Pep Style Guide](https://peps.python.org/pep-0008/)
* [Real Python - for quick tutorials on several subjects](https://realpython.com/)
* [Real Python - Name-Main](https://realpython.com/if-name-main-python/)
* [Real Python - While loops](https://realpython.com/python-while-loop/)
* [Pypi - ASCII title banner](https://pypi.org/project/pyfiglet/)
* [Stack Overflow - Slow Printing](https://stackoverflow.com/questions/15375368/slow-word-by-word-terminal-printing-in-python)
* [Stack Overflow - clear terminal](https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)
* [W3Schools](https://www.w3schools.com/)
* [Tripleten - best practices](https://tripleten.com/blog/posts/python-best-practices)
* [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/style/)

* Code Institute Slack Channel


### Templates I have used for inspiration and creating my readme-file:

I have used several readme file as inspiration to write this readme:

* [Sample README Code Institute](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md?plain=1) - Copied the Deployment section and used for general guideline.
* [Towers of Hanoi - Lucia2007](https://github.com/lucia2007/towers-of-hanoi/) - For general inspiration and the Heroku Deployment section for this readme.
* [Weather Checker - mdurmus](https://github.com/mdurmus/weather-checker/) - Used for general guideline.
* [Read Me Template Code Institute](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md)
Used for general guideline.
* [Plant Factory - crypticCaroline](https://github.com/crypticCaroline/ms1-plantfactory/blob/master/README.md?plain=1) - Especially for the Technologies Used, Testing sections and design sections.
* [Visit Järbo - ClaudiaInSweden](https://github.com/ClaudiaInSweden/visit-jarbo/blob/main/README.md?plain=1) - General inspiration / guideline.
* [GitHub Docs](https://docs.github.com/en)