
<img src="static\image\webimg.png"/>

# TeachSenpai - An on-demand E-Learning platform web application, allowing people to earn money by helping others overcome their learning hurdles.

This e-commerce platform is an e-learning platform which allow users to teach or learn from other users around the world. It shares features similar to Fiveer and Carousell, where users can `simulatenously be a teacher or a student upon registration, browse the database for content, compare prices of products, view details of the product,make an order, add/remove from cart, checkout, make payment, track their order, view the material they bought and chat with their teacher, leave a review,and earn money.`

The website aims to act as a platform that encourages people to share their knowledge and help people with their work, studies or even hobbies, all while being able to earn money. 

## Project Purpose
> “Once you have learned to ask questions—relevant and appropriate and substantial questions—you have learned how to learn and no one can keep you from learning whatever you need to know.”  –Neil Postman and Charles Weingartner (1969)

As a University student, I came to realize how important it was to have teaching assistants(TA) readily available for us to seek help from and the impact it accumulatively had on my studies. There were many times where I found myself stuck on a problem and the guidance from my TA and lecturers were key factors to helping me understand those concepts. 

However, not all students have access to readily available teaching assistants. Some may be self-learners, part-time students, or may simply just have no one to seek help from. This hinders their learning progress and makes it difficult for them to learn new, difficult concepts. While many online materials may be available on Udemy, coursera or youtube, pre-made learning courses do not directly address the specific questions or misconceptions a student may have. Thus despite the many materials and thousands of open tabs a student went through on their google chrome page, they may still find themselves scratching their heads over the content, hoping someone could enlighten them on where they went wrong.

My motivation for this project is to bridge the gap between University students and self-learners, so that even self-learners would have access to the same level of support and guidance a university student may have. And ultimately, become the go-to platform for on-demand consultations and learning.

## Demo

A live demo can be found [here](https://teachsenpai.herokuapp.com/).

link: https://teachsenpai.herokuapp.com/
##### Please use the provided test account to view the website
- username: `miso`
- password: `rotiprata123` 

## UX

My goal is to allow users to easily search for topics posted by teachers by entering keywords, or search for their content by category. Starting with a search engine placed at the hero image section, this allows users to understand that they have direct access to type in a topic that they have in mind to see if there are any available on the server. 

The features which users wish to access is always accessible by the side panel,

- Users can either directly search from the home page and be redirected to show events page, or alternatively they can click on the [Nav] search icon to be brought to the see all events page.
- On the show programmes page, users can create a new event by clicking on the [+] button next to the search button. 
- Users can also filter their search by clicking on key categories or level of difficulty.

The overall design of the website follows a purple-pink colour palette that is consistent throughout the interface. Every page communicates its purpose clearly and does not stray too far from the generic e-shop layout which users - who frequently do online shopping, may find easy to use.

In the landing page, the user is greeted with an interactive hero image that encapsulates the title and slogan of the e-shop while capturing their attention as they move their cursor. They can then choose to access the shop via the call-to-action button and browse the products.

If the user attempts to perform an action, a notification would pop-up which informs the user that the action they are trying to complete is successful/unsuccessful.

Since performing certain actions (e.g. Checkout, View Cart, Add to Cart, Add to Wishlist) would require the user to login or register, users would be redirected to the login page and are prompted to login or register if they attempt to perform the actions without signing in.

Illustrations can also be found on majority of the pages as they are visual representations of expressing messages. They also help to elevate the website's aesthetics and improve the overall interface as a whole.

The website also takes on a mobile-first approach and is optimized for mobile viewing.

## User Stories

These are the user stories that highlights the requirements of each feature from an end-user perspective, for development purposes.

Users refer to teachers and students. As a user...

`I want to browse the products by category, so that I can view a list of products filtered according to my selection.`

`I want the website to be mobile responsive, so I can view the website conveniently from my smartphone or tablet.`

`I would like to click on the product description, so I  can know more about the product and make a purchase.`

`I want to add/remove a product to my cart, so I can continue shopping and collating my order before checking out.`

`I want to ensure that the payment function is secure so that my sensitive information (e.g. passwords, credit card details) will not be vulnerable to cyber threats.`

`I would like to check my order location, so that I can access my learning material`

`I would like to enter a chat page on my order, so that I can communicate with my tutor`

`I would like to review my tutor, so that I can share my experience with others`

`I would like to view my profile, so that I can see how my page looks like to others`

Every user can be a teacher or a student. There is no requirement for them to specify, as such...

`As a teacher, I want to be able to create, read, update and delete information to the website's database, so that I can add my topics I am willing to teach.`

`As a teacher, I would like to have a control panel, so that I can view resolved, or new orders.`

`As a teacher, I would like to be able to create, read, update learning materials for each order.`

`As a teacher, I would like to know how to upload teaching materials.`

`As a teacher, I would like to know how TeachSenpai's business model works and how much I can earn.`

`As a teacher, I would like to communicate with my students.`

### Wireframe mockup
<img height="500" src="static\image\schematic.png"/>


## Technologies
1.	HTML
2.	CSS
3.	[Bootstrap version 4.4](https://getbootstrap.com/)
4.	Python (3.6)
5.	Jinja2 (2.10.3)
6.	UploadCare
7.	Stripe
8.	Font Awesome (4.7.0)
9.	Google Fonts API
10. Django python
11. Javascript
12. SQLite to PostGRES
13. Heroku Deployment

## Features
The web application achieves these four basic functions of a database, namely CRUD –  an acronym for the four basic types of SQL commands: Create , Read , Update , Delete.
<img src="static\images\Annotation 2020-05-20 231601.png"/>

These functions allows users to perform the following features:
#### 1.	Create
a)	Add a new event with the following detail: 

- Event image
- Title
- Host Name
- Date/Time of event
- Estimated Duration of event
- Location
- Difficulty
- Category
- Description

b) Create a comment on each individual event

#### 2.	Read
Find events that matches the queries such as having a searchbox for event titles, alternatively clicking on keyword tags that allows the user to filter their searches via categories or level of difficulty.
Clicking on event card opens up more information which allows users to read comments left by the public.

#### 3.	Update
Edit the event details in the database

#### 4.	Delete
Delete the event

### Features Left to Implement
- Introduce functionality of likes/im going so that will have a +1 increment each time a user clicks on it.
- Allow users to upload image files to the website, instead of having to upload the image URL or convert their image to a URL
- Validate search query by preventing users to type in "[]" in search bar.

## Testing
#### 1. Create:
**•	Add a new event archive to the database**

All the form input boxes are able to fetch data to the database when the user fills up the form and press the submit button. There is also a javascript validator in date/time, event name, duration, location to prevent the user from submitting an empty field.

Selecting the category is optional if host is not sure. Image is also optional and a default image will be added.

**•	Create a comment on each individual event**

The comment form is successful in fetching input data to the database with both the commenter’s name and comment. Every single comment entry made on each individual event is added to the database as an object in an array called ‘reviews’, under the specific object ID given for each event. Once the user has submitted the comment, the comments will show up after the page has automatically refreshed.

#### 2. Read:
**•	Searchbox for event titles**

The search function is able to perform its function by filtering out the results according to the search query input using the regular expression, which would ignore any case sensitivity and parse in the search query as a string.

However, there is a limitation I found during testing that adding in "[]" would cause an error. This will be looked into. 

**•	Keywords to filter the queries**

In addition to the search function, the user has the ability to narrow down their searches by filtering out the results based on the each category/difficulty that the event has been assigned to. 

#### 3. Update:
**•	Edit the details of the existing event**

The default details of the existing events from the database will reflect in the input form. This is to ensure that the user is aware of the changes they are making to the event archive. Once the form is submitted, the data of the event archive will be updated to the database.

## Mobile Responsiveness and testing
To ensure compatibility and responsiveness, the site was tested across multiple browsers such as Chrome, Safari and Internet Explorer and on iOS devices - iPhone Xs Max, iPad and iPad Pro.

All links have been tested to ensure correct re-direction to desired destination.

## Deployment
This site is hosted using Heroku, deployed directly from the master branch and Github. The deployed site will update automatically upon new commits to the master branch.

To clone this project:

    Download/clone the master branch of this respository.
    Ensure that PIP, Visual Studio Code(or other code editors), Python and Git are in your system.
    Install required extensions/modules from requirements.txt by typing "pip -r requirements.txt" in the terminal.

Heroku:

    Create a new app and a Procfile that will allow the app to be deployed on Heroku.
    Input .env secret key values inside app settings. Set IP: 0.0.0.0 and Port:5000.
    Install Heroku CLI on Windows and login.
    To push to Heroku from VSC, enter 'git push heroku master'.

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/kwokcheong/Project3_12Run.git` into your terminal.

## Credits
### Media
I do not own any of the photos used for the website and they were taken from various websites.

Icons are from the [Font Awesome CDN](https://fontawesome.com/v4.7.0/icons/)

### Acknowledgements

Responsive navbar tutorial by Youtuber [Dev Ed](https://www.youtube.com/watch?v=gXkqy0b4M5g&t=127s)

Parallax effect on cursor credits to CodePen user [GreenSock](https://codepen.io/GreenSock/pen/OeqgrZ)

Gradient background tutorial by Youtuber [DarkCode](https://www.youtube.com/watch?v=NnrBempao2M&t=169s)

Account form layout credits to CodePen user [Tirth Patel](https://codepen.io/T-P/pen/bpWqrr)

Shop cart layout inspired by Dribble user [Olia Gozha's design](https://dribbble.com/shots/5039057-Shopping-cart-V2)

Image hover effect credits to CodePen user [Naoya](https://codepen.io/nxworld/pen/ZYNOBZ) 

- This is for educational use.