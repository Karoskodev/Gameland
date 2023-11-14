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