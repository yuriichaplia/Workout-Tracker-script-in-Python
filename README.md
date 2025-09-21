# Workout Tracker script in Python<br>
A simple workout tracker script in Python using Sheety and Nutritionix APIs to get information about users' exercises put on Google Sheet Spreadsheet.<br>
Example: the script opens in terminal which allows users to provide information about their exercises, such as `I ran 3 miles`. Afterwards, columns like `Date`, `Time`, `Exercises`, `Duration` and `Calories` will be put on Google Sheet Spreadsheet with information about the user's provided exercises. 

## To get started you need to:
+ Create account on [Nutritionix](https://developer.nutritionix.com/)
+ Obtain [Nutritionix](https://developer.nutritionix.com/) APP ID and APP Key
+ Create a new spreadsheet in Google Sheets and allow to modify the spreadsheet for everyone with the link
+ Connect Google Sheets with [Sheety](https://sheety.co/)
+ On [Sheety](https://sheety.co/) create new project from Google Sheets and turn on get and post methods
+ Go to your Sheety project -> Authentication and click on Basic type of authentication to obtain your Authorization Header
