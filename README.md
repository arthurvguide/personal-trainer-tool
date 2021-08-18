# [Personal Trainer Tool](https://personal-trainer-tool.herokuapp.com/)

 ![](/docs/images/project-img.JPG)

 Personal Trainer Tool is an app created for professional who works at the health environment, can it being a personal trainer, nutritionist, whoever. 

 This app analyzes client's health and creates diets for them, according to their goals.
 
 [Click here](https://personal-trainer-tool.herokuapp.com/) to visit the deployed site.

 [Here](https://docs.google.com/spreadsheets/d/1xkOIW6pDstDv1EDaznGfMbKba8Nzhc8cX9CcQQYTlNw/edit?usp=sharing) is the link to the Google Spreadsheet, to see the updates made.

---

# Table of contents
1. [Project Goals](#project-goals)
2. [User Goals](#user-goals)
3. [Structure](#structure)
    1. [Initial Screen](#inital-screen)
    2. [New Client](#new-client)
    3. [Existing Client](#existing-client)
4. [Technical Design](#technical-design)
    1. [Flow Chart](#flow-chart)
    2. [Data Models](#data-models)
5. [Features](#features)
    1. [Feature 1: The New Client](#feature-1-new-client)
    2. [Feature 2: The Existing Client](#feature-2-existing-client)
    3. [Features to be implemented](#features-to-be-implemented)
6. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Applications and Platforms](#applications-and-platforms)       
7. [Validation](#validation)
8. [Testing of New Client User stories](#testing-of-new-client-user-stories)
9. [Testing of Existing Client User stories](#testing-of-existing-client-user-stories)
10. [Bugs](#bugs)
11. [Deployment](#deployment)
    1. [Forking the GitHub Repository](#forking-the-github-repository)
    2. [Making a Local Clone](#making-a-local-clone)
    3. [Heroku](#heroku)
    4. [Google API](#google-api)
12. [Credits](#credits)

## Project Goals
 The project goals are:
  - Create an app for health professionals to check client health and weight status
  - Create an app for health professionals to track their clients and help them to achieve their goals
  - Create an app that calculates BMI ( Body Mass Index), BMR (Basal Metabolic Rate)
  - Create an app that creates diets for specific objective (maintain, loss or gain weight)
  - Create and update a worksheet for the professionals to track their clients easily
  - Automate calculations

## User Goals
 The user goals are:
  - Input client details and get their BMI ( Body Mass Index), BMR (Basal Metabolic Rate)
  - Creat diets for their clients 
  - Save client details into a worksheet
  - Update client details and get new diets
  - Check client health and weight status
  - Track their clients
 
 [Back to Table of contents](#table-of-contents)

## Technologies Used

### Languages
 - [Python 3](https://www.python.org/) - Was used solely to create this project.
### Applications and Platforms
 - [Git](https://git-scm.com/) - Version control system used to commit and push to Github via Gitpod.
 - [Github](https://github.com/) - The projects repository and all its branches were commited, pushed and deployed to Github.
 - [Gitpod](https://gitpod.com/) - All code was written and tested using the Gitpod web-based IDE.
 - [Heroku](https://www.heroku.com) - Used to deploy the application.
 - [Lucidchart](https://lucid.co/product/lucidchart) - Lucidchart was used to create the flowchart of the project.
 - [Google Sheets](https://calendar.google.com/) - The users input data creates and edits content on Google Sheets
 - [Google Cloud Platform](https://console.cloud.google.com/) - All data send and received with the help of the Google API, through the Google Cloud Platform

#### Third Party Libraries
- googleapiclient.discovery: needed to work with the Google API
- google.oauth2.service_account: So the application can access the account that the sheet are on with the credentials
- gspread: so the application can read Google Spreadsheets

[Back to Table of contents](#table-of-contents)

## Validation
 All Python files passed the [PEP8](http://pep8online.com/) tests with 0 errors.
 Click [here]() to view them.


## Deployment
 ### Heroku
 This application has been deployed from Github using Heroku. Here's how:
 1. Create an account at [heroku.com](https://.heroku.com/)
 2. Create a new app, add app name and your region
 3. Click on create app
 4. Go to "Settings"
 5. Under Config Vars, add your sensitive data (creds.json for example)
 6. For this project, I set buildpacks to <Python> and <NodeJS> in that order.
 7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
 8. Enter your repository name and click on it when it shows below
 9. Choose the branch you want to buid your app from
 10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository
 11. All done!

 ### Google API
 Here's how you can set up your own API:
 1. Login or create a Google account and navigate to https://console.cloud.google.com/
 2. Create a new Project by clicking on the New Project icon
 3. Add Project name and details
 4. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets)
 5. IF the API requires, create a credential (service account in this case) for your project
 6. Download the credential and upload it to your workspace as creds.json file
 7. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets)
 8. Add them to your code.

 [Back to Table of contents](#table-of-contents)

