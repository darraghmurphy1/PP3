# How to Play

Battleship is a classic game traditionally played as a board game. This is a slightly manipulated version of the classic rules.

The player will see a blank grid or gameboard with the x and y axis labeled A-E and 1-5. The player will enter the coordinated they think an enemy ship is located and drop a bomb on that location. The user will have 15 attempts to take out 5 enemy battleships. If the user locates an enemy ship it will show up as "X" on the grid. If the user takes a shot and misses all enemy ships a "O" will be displayed on the grid. 

If the user takes out 5 enemy ships in less than 15 attempts then they are victorious. If the user runs out of bombs before taking out 5 ships they will lose.

# Project Goals 

The goal of this project is to create an entertaining and challenging game with a decent amount of replayability and to display the creator's understanding of python essentials. 

User Goals:
First Time Goals

On my first visit to the game I want to 

-be entertained by the game 
-see rules clearly displayed at the beginning 
-beat the game
-be visually stimulated by the game 
-be able to use the game without any errors

On my second visit I would like to defeat the game if I was unsuccessful the first time.

If I was a repeat user I would like to see new features added to keep me stimulated. 

Features 

Random ship generation and placement.

Hidden grid with ships on it and displayed empty grid for guessing 

Valiadation for input for coordinates 

A counter to tell you how many ships are left 

A counter to tell the user how many bombs are left 

A success message 

A defeat message 

ASCII art 


Deployment

As was required by this project I had to deploy my project to Heroku. I done this by following these steps: 

Push all code to GitHub
Open Heroku
Select new in the top right corner.
Create new app.
Enter the app name and select Europe as the region.
Connect to GitHub.
Search for repo-name.
Select connect to the relevant repo you want to deploy.
Select the settings tab.
Add buildpack
Select Python, then save changes.
Select Nodejs, then save changes.
Make sure Heroku/Python is at the top of the list, followed by Heroku/Nodejs
Navigate to the deploy tab
Scroll down to Manual Deploy and select deploy branch.
Success

