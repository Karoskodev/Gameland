# Gameland

![am I responsive screenshot](static/images/responsive.png)

# An Events Registration Website.
> An events registration website showcasing upcoming events. This site empowers users to register on the website and participate in upcoming events.


## **[Live site](https://gameland-b306d6404761.herokuapp.com/)**

---

## **[Repository](https://github.com/Karoskodev/Gameland)**

---

## Table of contents
<a name="contents">Back to Top</a>
 1. [ UX ](#ux)
 2. [Agile Development](#agile)
 3. [ Features ](#features)  
 4. [ Features Left to Implement ](#left)  
 5. [ Technology used ](#tech) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#bugs)  
 8. [ Deployment](#deployment)
 9. [ Credits](#credits)
 10. [ Content](#content)  
 11. [ Acknowledgements](#acknowledgements)

 ## UX

<a name="ux"></a>
#### Pre-project Planning

> Database Structure

![Lucid Diagram](static/images/lucid.png)

- When I decided on my initial concept of Gameland I knew I needed to understand what type of data I would need to store and the relationships between them.
- I created the above diagram on lucidchart to help guide me.

### Database Schema
#### Event Model

| id | Field |
|--|--|
| name |CharField  |
| slug |SlugField|
|date|DateTimeField|
|image|CloudinaryField|
|excerpt|TextField|
|status|IntegerField|

---

#### Entry Model

| id | Field |
|--|--|
| event |ForeignKey|
|user|ForeignKey|
|nickname|Charfield|
|clan|Charfield|
|created_on|DateTimeField|
|approved|BooleanField|

---

# UX design

## Overview

Gameland is your go-to for immersive events.  
The main goal of the website is to allow users to view Events, user can create an account and use it to entry Event.

### Design
Once the name was chosen I decided that I wanted this website to be modern, minimalistic in it's appearance to use colors of blue and White where possible.

### Site User

 - Someone looking to attend Esport events
 - Someone who would prefer to make bookings digitally rather than speaking with others

###  Goals for the website

- Easily check out Events beforehand.
- Quickly book your spot in Events and store entries in a neat place for staff to accept / decline in an easy manner depending on occupancy.

## Wireframes

###  Wireframes

My goal for this project was to create a simple sleek website that allowed the admin create, change, filter or delete an Events and the users register to the website and create, edit,delete entry for Events

> index.html

![Index page](static/images/index.png)

![Index page](static/images/index111.jpg)

> event_detail.html

![event page](static/images/event.png)

![event page](static/images/event111.png)


## Agile Development

<a name="agile"></a>

### Agile Overview

This project was started alongside a GitHub Projects Page to track and manage the expected workload ahead.
The aim was to set out my expected workload, list the user stories and ultimately finish the site in good time.

To see Kanban please click [here](https://github.com/users/Karoskodev/projects/9).

At the initial stages I decided on 2 epics and 10 user stories. When I started working on user stories and epics I moved them from todo to in progress, when I finished them I moved them from in progress to done

#### User stories

#####  Completed User Stories

To view any of the expanded details of the user stories please click on a user story below to be taken to the Kanban project.
If the specific user story does not auto pop up then please click on it from the project page and you will see the details and comments.

 1. [USER STORY: Early Deployment #1](https://github.com/Karoskodev/Gameland/issues/1)
 2. [USER STORY: Account registration #2](https://github.com/Karoskodev/Gameland/issues/2)
 3. [USER STORY: View Events List #3](https://github.com/Karoskodev/Gameland/issues/3)
 4. [USER STORY: Open an Event #4](https://github.com/Karoskodev/Gameland/issues/4)
 5. [USER STORY: Join an Event #5](https://github.com/Karoskodev/Gameland/issues/5)
 6. [USER STORY: Change Event Registration #6](https://github.com/Karoskodev/Gameland/issues/6)
 7. [USER STORY: Remove Event registration #7](https://github.com/Karoskodev/Gameland/issues/7)
 8. [USER STORY: List of Players #8](https://github.com/Karoskodev/Gameland/issues/8)
 9. [USER STORY: Manage Events #9](https://github.com/Karoskodev/Gameland/issues/9)
 10. [USER STORY: Approve Registrations #10](https://github.com/Karoskodev/Gameland/issues/10)


## Features

<a name="features"></a>

#### User based Features Implemented:

 - **Users can** create an account (**Create**)
 - **Users can** log into their account
 - **Users can** log out of their account
 - **Users can** view list of Events (**Read**)
 - **Users can** make a registration for an event **(Create)**
 - **Users can** add their nick name and clan for each entry (**Create**)
 - **Users can** view entries for specific event (**Read**)
 - **Users can** edit their nickname and clan for existing entry (**Update**)
 - **Users can** delete entry at any stage of the process (**Delete**)

#### Account restrictions:
 - **Users cannot** access event details without being logged in
 - **Users cannot** edit entry without being logged in
 - **Users cannot** create multiple entries for one event
 - **Users cannot** access the admin panel of the website unless they have admin status

#### Website features:

##### Dynamic Events listings

 - The website displays events that are updated on the back end and shown on the front-end.
 - If the event is updated by the business owner then this change will reflect on the front end.
 - This allows the business owner to make easy changes.


##### Events registration System

 - Once a user has created an account they can view events details and create registration requests for event.
 - Once a user is registered in an event he can edit or delete his entry.

##### Website registration System

 - The user can register on the website
 - The user can log in to the website
 - The user can log out of the website

### index.html

> Navbar

![Navbar](static/images/navbar.png)

 - navbar consists of Logo, Home, Register, Login links.
 - If the user is logged in they have access to logout and the username is displayed on the right side of navbar.

 ![Navbar](static/images/navbar2.png)
---

> Events

![Events](static/images/eventsLogin.jpg)

- list of events with start dates and with message asking users to log in if they want to enter event
- If the user is logged in they can enter event.

![Events](static/images/events.jpg)

---

> Footer

![Footer](static/images/footer.png)


- footer with social links.

---

### event_detail.html

> Event info

![Event info](static/images/eventInfo.png)

 - event info with event image

---

> Entries

![Entries](static/images/entries.png)

 - list of entries for opened event with dates, users, nicknames, clans

---

> Event register form

![event register form](static/images/register.png)

 - event register form with nickname and clan fields

---

> Approval message

![Aproval message](static/images/approval.png)

 - awaiting approval message after event registration submition

---

> Edit entry

![Edit entry](static/images/edit.png)

 - user can edit nickname and clan

---

> Delete entry

![Delete entry](static/images/delete.png)

 - user can delete entry

---

> Messages

![Messages](static/images/message1.png)
![Messages](static/images/message2.png)

 - messages after entry edit or deletion

---

<a name="left"></a>
## Features left to Implement 


 - Add ability for users to open pofile page and add profile picture
 - Add ability for users to open a list of all their entries
 - Add ability for users to create Events
 - Add ability for users to reset or change the password
 - Allow users to sign up with social media
 - Add gallery with photos from events

 ---

 <a name="tech"></a>
##  Technology Used

### Html

 - Used to structure my webpages and the base templating language

### CSS

 - Custom CSS to make it as close to the wireframes as I felt it needed to be.

### JavaScript

 -  Used to add timeout function for messages as well as to enable the menu on index.html

### Python

 -  Used for the logic in this project.

### Django

 -  Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.

### Font Awesome

 -  Icon library used for the profile and admin panel section.

### Bootstrap 5
 - Used as the base front end framework to work alongside Django

### GitHub
 - Used to store the code for this project & for the projects Kanban board used to complete it.

### Heroku
- Used to host and deploy this project

### Heroku PostgreSQL
-Heroku PostgreSQL was used as the database for this project during development and in production.

### Cloudinary
- Used to host the static files for this project including user profile images.

---

<a name="testing"></a>
## Testing


### Testing Phase

#### Manual Testing

> Each user story was manually tested in line with intended functionality on both desktop & mobile.
> As this project was driven by my own User Stories I felt manual testing was applicable on all logic code.


>If the intended outcome completes then this will be flagged as pass. If it does not then this is a fail.

#### Account Registration Tests
| Test |Result  |
|--|--|
| User can create account | Pass |
| User can log into account| Pass|
|User can log out of account|Pass|

---

#### User Navigation Tests

| Test |Result  |
|--|--|
|User can navigate to Events | Pass |
|User can access Events details| Pass|
|SuperUser can access admin panel|Pass|

---

#### Account Security Tests

| Test |Result  |
|--|--|
|Non logged in user cannot access Events details | Pass |
|Non logged in user cannot register in to Event| Pass|
|Non superuser cannot access admin panel|Pass|

---

#### Admin Tests

| Test |Result  |
|--|--|
|Admin can add Events |Pass|
|Admin can edit events|Pass|
|Admin can delete events|Pass|
|Events they display correctly on front-end when updated / added|Pass|
|Admin can approve Events entries |Pass|

#### Events Entries Tests

| Test |Result  |
|--|--|
|User can register in to event |Pass|
|User can edit events registrations|Pass|
|User can delete events registrations|Pass|

---

## Google Lighthouse Testing

> index.html


![Google Lighthouse Index](static/images/test1.png)

> event_detail.html


![Google Lighthouse Event](static/images/score2.png)


## HTML W3 Validation

### index.html


![W3 Validation checker](static/images/htmlcheck.png)
### Result: Multiple Errors Related to Django Templates, These errors can be safely ignored, as they are specifically tied to the Django templating system.

### CSS Validation


![w3 Jigsaw CSS checker](static/images/css.png)
#### Result: Pass - No Errors

---

<a name="bugs"></a>
## **Bugs**

#### W3 Validation
![W3 Validation checker](static/images/error.png)

- When I ran my code through the w3 html validator I got Multiple Errors Related to Django Templates, These errors can be safely ignored, as they are specifically tied to the Django templating system.

---

<a name="deployment"></a>

## Deployment

> I have broken up the deployment into two sections as it is quite extensive and can be hard to follow.

To deploy the project through Heroku I followed these steps:

- Sign up / Log in to  [Heroku](https://www.heroku.com/)
- From the main Heroku Dashboard page select 'New' and then 'Create New App'
- Give the project a name
- After this you select select create app. 
- The name for the app must be unique or you will not be able to continue.
- Heroku will create the app and bring you to the deploy tab. 
- From the submenu at the top, navigate to the resources tab.
- Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
- Click on the setting tab
- Open the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
- Inside the Django app repository create a new file called env.py
- within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. 
- The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
-   Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
-   Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
-   In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
-   insert the line if os.path.isfile("env.py"): import env
-   remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
-   replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
-   In the terminal migrate the models over to the new database connection
---
-   Navigate in a browser to cloudinary, log in, or create an account and log in.
-   From the dashboard - copy the CLOUDINARY_URL to the clipboard
-   In the env.py file - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
-   In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
-   Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
-   this key value pair must be removed prior to final deployment
-   Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
-   in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
-   Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
-   Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
-   Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
-   In your code editor, create three new top level folders, media, static, templates
-   Create a new file on the top level directory - Procfile
-   Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
-   In the terminal, add the changed files, commit and push to GitHub
-   In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
-   Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository

By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository.
You can do this by: 
-  Logging into GitHub or create an account. 
- Locate the repository at  [here](https://github.com/Karoskodev/Gameland)  . 
-  At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
-  A copy of the repository should now be created in your own repository.

#### [](https://github.com/Karoskodev/Gameland)Create a clone of this repository

Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally: This can be done by:

-   Navigate to  [https://github.com/Karoskodev/Gameland](https://github.com/Karoskodev/Gameland)
-   click on the arrow on the green code button at the top of the list of files
-   select the clone by https option and copy the URL it provides to the clipboard
-   navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
-   type 'git clone' and paste the https link you copied from github
-   press enter and git will clone the repository to your local machine
