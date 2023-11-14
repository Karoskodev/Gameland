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

