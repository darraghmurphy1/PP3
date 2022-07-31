# How to Play

Battleship is a classic game traditionally played as a board game. This is a slightly manipulated version of the classic rules.

The player will see a blank grid or gameboard with the x and y axis labeled A-E and 1-5. The player will enter the coordinated they think an enemy ship is located and drop a bomb on that location. The user will have 15 attempts to take out 5 enemy battleships. If the user locates an enemy ship it will show up as "X" on the grid. If the user takes a shot and misses all enemy ships a "O" will be displayed on the grid. 

If the user takes out 5 enemy ships in less than 15 attempts then they are victorious. If the user runs out of bombs before taking out 5 ships they will lose.

# Flowchart

![bQ9gWuWCDJ](https://user-images.githubusercontent.com/103134533/182043570-150a0117-16ab-4663-abab-66974f167056.png)

# Project Goals 

The goal of this project is to create an entertaining and challenging game with a decent amount of replayability and to display the creator's understanding of python essentials. 

# User Goals:
First Time Goals

On my first visit to the game I want to 

-be entertained by the game 
-see rules clearly displayed at the beginning 
-beat the game
-be visually stimulated by the game 
-be able to use the game without any errors

On my second visit I would like to defeat the game if I was unsuccessful the first time.

If I was a repeat user I would like to see new features added to keep me stimulated. 

# Features 

## Greeting message 


![chrome_h6YngRPR0t](https://user-images.githubusercontent.com/103134533/182042266-1c54ed32-9065-4bd1-adc8-4585919882b8.png)

## Random ship generation and placement.

## Hidden grid with ships on it and displayed empty grid for guessingf 


![chrome_5qvcerms2Z](https://user-images.githubusercontent.com/103134533/182042270-38a2d89a-8728-4c80-be62-6137ad3234e7.png)

## Valiadation for input for coordinates 


![chrome_3qbAkYZXDm](https://user-images.githubusercontent.com/103134533/182042252-873dd6a7-002b-4dc1-a573-edd8109a5c84.png)
![chrome_0Yb5fRBfgO](https://user-images.githubusercontent.com/103134533/182042257-dac69631-26c2-4b38-b820-fa2d6bef38df.png)

## A counter to tell the user how many bombs are left 


![chrome_3uN34tKVT9](https://user-images.githubusercontent.com/103134533/182042247-ca31efc6-7b9e-4648-bf4a-dee646ad7255.png)

## A success message 


![chrome_8fe29FjfcS](https://user-images.githubusercontent.com/103134533/182042220-c4c917c0-cfb3-4a86-b688-99ef171d73af.png)


## A defeat message 


![chrome_pNO6RDVCak](https://user-images.githubusercontent.com/103134533/182042224-526a2918-775a-485b-80ce-29e42d658054.png)

## ASCII art 


![chrome_6AqSDGJKfq](https://user-images.githubusercontent.com/103134533/182042226-fefe8c75-772e-45b4-9b84-ee80c883e47f.png)

# Deployment

As was required by this project I had to deploy my project to Heroku. I done this by following these steps: 

### Push all code to GitHub
### Open Heroku
### Select new in the top right corner.
### Create new app.
### Enter the app name and select Europe as the region.
### Connect to GitHub.
### Search for repo-name.
### Select connect to the relevant repo you want to deploy.
### Select the settings tab.
### Add buildpack
### Select Python, then save changes.
### Select Nodejs, then save changes.
### Make sure Heroku/Python is at the top of the list, followed by Heroku/Nodejs
### Add config vars. Fill in PORT as the key and 8000 as the value.
### Navigate to the deploy tab
### Scroll down to Manual Deploy and select deploy branch.
### Success

