[![Build Status](https://travis-ci.com/JohnL3/milestone-project-five.svg?branch=master)](https://travis-ci.com/JohnL3/milestone-project-five)

# Milestone Project 5
Project hosted at: [BUGS & FEATURES](https://bugs-features.herokuapp.com/) 


### For use during testing

Staff user details  
username: Ems_1  
password: generic22staff  

I have supplied a user with staff credentials for visiting pages an ordinary user cannot.
This user can be used to see the form for creating a blog post and the form for editing a blog post.
They cannot though, create or edit a post.


## UX

The idea for this website is that imaginary users who previously got websites from me now have a website available to them
where they can 

- Report any bug issues they have on their website
  - Track whether the issues is being dealt with
  - And see when the issue is sorted and closed
- Suggest features 
  - Also suggest features that they find they now require on their site for their users and that I can create and incorprate into their website
- A Profile area
  - A profile area where they have access to all there information with regards to bug issues and feature suggestions 
- A cart and checkout area
  - Cart and checkout area giving them the ability to purchase the features they suggest or others have suggested 
- A Blog
  - A blog section where they can read post about various topics



## Features

- A accounts app:  
  - For signup, login, logout
  - Profile page for user to see bug issues they have submitted, suggested features they have submitted, and adding a user avatar.
- A Bugs app:
  - For showing all bug issues and for showing single bug issues and form to submit bug issues.
- A Features app:
  - For showing all features and for showing single features and a from to submit features. 
- A Blog app:
  - For writing blog posts and forms for creating blog posts and editing blog posts. 
- A Cart app:
  - For showing what items are stroed in cart that user intends to purchase.
- A Checkout app:
  - For purchaseing features and form to fill out for purchases.
- A database
  - Used for storing all user details, bug issues details and feature details


## Technologies Used

- cloud9
  - Recommended by course
  - ['Cloud9'](https://ide.c9.io/)
- jQuery
  - Used as it simplifies Dom manipulation
  - ['jQuery'](https://api.jquery.com/)
- Stripe
  - Used for payments
  - ['Stripe'](https://stripe.com/ie)
- AWS
  - Used for storing static files
  - ['AWS'](https://aws.amazon.com/)
- Heroku
  - Used for hosting web site and the database was a addon supplied by heroku
  - [Heroku](https://www.heroku.com/products)



## Testing

Write up for testing is done here: ['Testing documentation'](./testing_doc.md)  

## TO RUN LOCALLY ON CLOUD9

- Set up a virtual env: Type the following into terminal.  
  - wget -q https://git.io/v77xs -O /tmp/setup-workspace.sh && source /tmp/setup-workspace.sh

- Install all the packages from the requirements.txt file: 
  - pip3 install -r requirements.txt


When you clone this repo to cloud9 you will need to create a env.py file. If you are going to be saving your work
to github make sure to add the env.py file to the .gitignore

You will need to add the following to the env.py file  

```python
    import os
    
    os.environ.setdefault('STRIPE_PUBLISHABLE', "")
    os.environ.setdefault('STRIPE_SECRET', "")
    os.environ.setdefault('SECRET_KEY', '')
    os.environ.setdefault('DATABASE_URL', '')
    os.environ.setdefault('AWS_ACCESS_KEY_ID', '')
    os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '')
```

You will need to create a SECRET_KEY and fill it in above.  
You will need to add your AWS keys and Stripe keys.  
Until you have a database set up (you can use Postgres for database on Heroku) you can comment out  
os.environ.setdefault('DATABASE_URL', '') in your env.py file.  

In your terminal you will need to type in: python3 ./manage.py makemigrations  
In your terminal you will need to type in: python3 ./manage.py migrate  
In your terminal you will need to type in: python3 ./manage.py createsuperuser  
and follow on screen instructions

In your terminal you will need to type in: python3 manage.py collectstatic  
This will transfer all static files to your AWS storage

To run server type in terminal the following:
python3 manage.py runserver $IP:$C9_PORT 

### DEPLOYMENT

#### Create an app on heroku

- To create an app on heroku for your project
  - log into heroku and go to the personal tab and click the link for create new. 
  - You will then need to name your app and choose a region to host it.
  - When this is done click the deploy link and at the bottom of the page you will see all you need to do is
  - in your cloud9 terminal type the following: heroku git:remote -a \<name of your app\> 
  - This will link your cloud9 to your heroku app

#### Add the database

- Adding the database
  - When you have created your app on heroku you can click on the resources tab.  
  - Scroll down to Add-ons and type in Postgres and this will show you a link to click on to provision this for your app.
  - Go then an click on the settings tab and click on the: reveal config vars.    
  - You will see DATABASE_URL with address on the right ... copy this to put in the eny.py file.     
  - Add all the keys from the env.py file to heroku config vars section.


#### PRE DEPLOYMENT CHECKS

- On heroku in the reveal config vars section, make sure you have filled in
  - STRIPE_PUBLISHABLE key, STRIPE_SECRET key, SECRET_KEY key, AWS_ACCESS_KEY_ID key and AWS_SECRET_ACCESS_KEY key
  - Add one final key: DISABLE_COLLECTSTATIC set it to 1
- On cloud9 go to settings.py and comment out import env ... as this is not being pushed to Heroku
- On cloud9 go to settings.py and set: DEBUG = False
- On cloud9 go to eny.py and uncomment out os.environ.setdefault('DATABASE_URL', '') if you previously had it commented out
- On cloud9 run the following: to be able to use your Postgres database
  - python3 ./manage.py makemigrations
  - python3 ./manage.py migrate
  - python3 ./manage.py createsuperuser 
  - follow the instructions to create superuser
- On cloud9 do: git add . then do a git commit and a git push
- You can now push to heroku with the following:
  - git push heroku master
  

