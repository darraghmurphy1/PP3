# Battleship PP3 

![chrome_L6IUxkJtnP](https://user-images.githubusercontent.com/103134533/182044621-499146e0-fa9f-4bf3-872d-10501771f192.png)

Live Version - https://pp3battleship-3dbac7446df0.herokuapp.com/
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

- be entertained by the game 
- see rules clearly displayed at the beginning 
- beat the game
- be visually stimulated by the game 
- be able to use the game without any errors

On my second visit I would like to defeat the game if I was unsuccessful the first time.

If I was a repeat user I would like to see new features added to keep me stimulated. 

# Features 

## Greeting message 


![chrome_h6YngRPR0t](https://user-images.githubusercontent.com/103134533/182042266-1c54ed32-9065-4bd1-adc8-4585919882b8.png)

## Difficulty Levels

![chrome_amQThUAnuV](https://user-images.githubusercontent.com/103134533/182248270-77ef9481-d3f0-48d8-857c-3899125a3881.png)


## Random ship generation and placement.

## Hidden grid with ships on it and displayed empty grid for guessing


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

# Testing 

To test the input validation I deliberately entered invalid data. A successful result would be a prompt to the user to enter a valid option.

![chrome_3qbAkYZXDm](https://user-images.githubusercontent.com/103134533/182204606-591273d3-03da-4bf6-aa7e-e5eac27fe026.png)
![chrome_0Yb5fRBfgO](https://user-images.githubusercontent.com/103134533/182204632-3c3715b2-c70b-4c33-a119-3d3ad14af579.png)

This was a success. 

The project was tested in Heroku as can be seen in the features section.#

Also tested different difficulty levels successfully.


# Validator Testing

I used Pep8 online validator to test my python code. 

![chrome_EjQFuzO5xK](https://user-images.githubusercontent.com/103134533/182044352-d8d1b919-3cdf-485b-a676-4840b9c57102.png)

After fixing these errors I recieved a success message.

![chrome_BVwA1QjMeT](https://user-images.githubusercontent.com/103134533/182044372-482bc4c8-8132-47d7-b4c2-406ec5a501cf.png)




# Deployment

## As was required by this project I had to deploy my project to Heroku. I done this by following these steps: 

1. Commit and push final code to GitHub
2. Open Heroku
3. Open a new app in Heroku
4. Select a name for the app and select region as Europe
5. Add buildpacks to the app. Add Python and NodeJS in that order. Make sure Python is on top.
6. Add config vars. Fill in PORT as the key and 8000 as the value.
7. Go to Deploy tab 
8. Connect GitHub account and select repository
9. Manually deploy the main branch
10. Success


# Credits 

- My mentor Marcel Mulders 
- Heroku 
- GitHub
- GitPod
- Youtube. Specifically https://www.youtube.com/watch?v=tF1WRCrd_HQ
- Code Institute 
- Used random python import to select random integers
