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
 - [Lucidchart](https://lucid.co/product/lucidchart) - Lucidchart was used to create the [flowchart](#flowchart) of the project.
 - [Google Sheets](https://calendar.google.com/) - - The users input data creates and edits content on Google Sheets
 - [Google Cloud Platform](https://console.cloud.google.com/) - All data send and received with the help of the Google API, through the Google Cloud Platform

#### Third Party Libraries
- googleapiclient.discovery: needed to work with the Google API
- google.oauth2.service_account: So the application can access the account that the sheet are on with the credentials
- gspread: so the application can read Google Spreadsheets

[Back to Table of contents](#table-of-contents)