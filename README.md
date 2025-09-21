# Workout Tracker script in Python<br>
A simple workout tracker script in Python using Sheety and Nutritionix APIs to get information about users' exercises put on Google Sheet Spreadsheet.<br>

## To get started you need to:
+ Create account on [Nutritionix](https://developer.nutritionix.com/) and obtain your APP ID and APP Key
+ Create a new spreadsheet in Google Sheets and allow to modify the spreadsheet for everyone with the link
+ Connect Google Sheets with [Sheety](https://sheety.co/), create new project [from Google Sheets] and turn on get and post methods
+ Navigate to your Sheety project -> Authentication and click on Basic type of authentication to obtain your Authorization Header

## Example Usage
The scripts will open in terminal where you should provide an exercise you did (e.g. `I ran 3 miles and did 20 minutes of yoga`).<br>
Afterwards, you should see columns such as `Date`, `Time`, `Exercise`, `Duration` and `Calories` to be put on your Google Sheets spreadsheet. 
