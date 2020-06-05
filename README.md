
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

The features which users wish to access is always accessible by the side panel, the can access `home`, `teach`, `notes`, `profile`, `explore`, `logout`, `FAQ`. This sidebar makes it easy for them to access and have a farsight on the routes available on the website. 

On mobile responsive, the sizebar will turn into a hamburger dropdown.

The overall design of the website follows a white-dark purple theme color palette that is consistent with the brand colors throughout the interface. Every page communicates its purpose clearly and bears resemblance to a gig/freelance webpage. Every profile created can post teaching materials, buy consultations, and view purchased materials. The combination of both user groups simplifies the profile creation experience. People whom have used to `Carousell`, or similar buyer/seller account web applications such as `Shopee`, `Amazon`,`lazada`, would find resemblance to the user experience. A FAQ page is accessible for users to seek common questions such as `How to begin teaching`, `how to upload video materials` etc...

In the landing page, the user is greeted with a hero image that encapsulates the copy-write and slogan of the web application while capturing their attention to the search bar. This would be the first element users see within 1-2 seconds to understand that they can already get started. Upon searching for products in the database, going futher, certain actions (e.g. Checkout, View Cart, Add to Cart, teach) will thereafter prompt users to sign in or make account if they have not already done so yet.

Since performing certain actions (e.g. Checkout, View Cart, Add to Cart, Add to Wishlist) would require the user to login or register, users would be redirected to the login page and are prompted to login or register if they attempt to perform the actions without signing in.

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

#### Flow Chart
<img height="500" src="static\image\schematic.png"/>

#### Wireframe

##### Nav bar and sidebar layout
<img height="500" src="static\image\IMG_0379.PNG"/>

##### User experience for clicking on product detail to checkout
<img height="500" src="static\image\IMG_0380.PNG"/>

##### Home page layout
<img height="500" src="static\image\IMG_0381.PNG"/>


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
This web application has the following features:

#### 1. Side Bar

**• A collapsible side bar for a tab toggle experience.** 

Mobile responsive, turns into hamburger dropdown on smaller devices.

#### 2. Accounts:
**•	Login/Logout**

**•	Register**

**•	Password Reset**

**•	Profile**

**•	Order tracking**

Able to view unique order id and materials uploaded by tutor.

#### 3. Shop:
**•	View all products in the explore page**

Search by keyword or by category

**•	View individual product page with details and descriptions of the product**

**•	Add/Remove product to cart**

#### 4. Notes:
**•	upon successful purchase, once the tutor has uploaded the material, user can view the video and content material**

#### 5. Chat Room:
**•	Both teacher and student can enter a unique chat room for each material and share images and messages to dive deeper in consultation**

#### 6. Reviews:
**•	Student can share a review on their experience with the tutor after clicking resolved**

#### 7. Balance:
**•	Upon successful consultation, the amount earned will be reflected on teacher's account balance**

Once student has indicated that they are happy with the product, they will click on resolved and the amount will be appended into the teacher's bank account. 

#### 6. Checkout:
**•	Delivery and Payment Form**

**•	Payment Gateway that accepts all forms of credit card payment via Stripe**

### Features Left to Implement
- Add pagination to the explore, order and transaction history. 

- implement a transfer to bank account function. Which allow teachers to withdraw their earnings and deposit into their bank accounts. 

- implement 20% transaction fee. Modify the price students see. This will reflect a price of x1.20. Ie. We will earn 20% for each transaction made.

- implement report function for mischieveous use, ie tutor not providing proper materials, students can lodge a complaint and the money will be refunded into student's balance app.
  another case would be students mischief for abusing the report function, teachers will be able to leave a review on students and thus safeguard them from malicious students.

- implement a reject order function, teacher can opt to reject an order made by students if it is too difficult, unreasonable or due to the notoriety in reviews for student. 

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


## Credits
### Media
I do not own any of the photos used for the website and they were taken from various websites.

Icons are from the [Font Awesome CDN](https://fontawesome.com/v4.7.0/icons/)

### Acknowledgements

FAQ page credits to CodePen user [Baahubali](https://codepen.io/anupkumar92)

Add cart order details into session credits to fellow coursemate [elch93](https://github.com/elch93)

Sidebar javascript inspired by CodePen user [ouhiH](https://codepen.io/goodywebs/pen/ouhiH)

images in landing page credits to freepik user [pikisuperstar] 

- This is for educational use.