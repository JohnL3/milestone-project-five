# ALL ABOUT TESTING WILL BE COVERED HERE. 

### AUTOMATED TESTING

For automated testing I first did: pip3 install coverage    
For each app I did: coverage run --source=<name of app> manage.py test  
I ran: coverage html 
This created an index file that I could open and check what test were required to be done and showed a precentage of test covered.  

- For accounts app
  - I did tests for [forms.py](./accounts/test_forms.py) and [views.py](./accounts/test_views.py)
  - Coverage: 90%
- For blog app
  - I did tests for [models.py](./blog/test_models.py) and [views.py](./blog/test_views.py)
  - Coverage: 98%
- For bugs app
  - I did tests for [models.py](./bugs/test_models.py) and [views.py](./bugs/test_views.py)
  - Coverage: 99%
- For cart app
  - I did tests for [views.py](./cart/test_views.py)
  - Coverage: 85%
- For checkout app
  - I did tests for [views.py](./checkout/test_views.py)
  - Coverage: 70%
- For features app
  - I did tests for [models.py](./features/test_models.py) and [views.py](./features/test_views.py)
  - Coverage: 98%
  

### MANUAL TESTING

##### Checks did for a logged out user

- User should only see HOME, BLOG and REGISTER/LOGIN links in nav: True
- I clicked each of these to make sure i was take to the appropriate page.
- On register/login page user should see a tab for REGISTER and a tab for LOGIN: True
- I clicked these to make sure both login form and register forms are available
- I attempted to register with passwords that didnt match and i recived an error message
- I attempted to register with a username that was allready take and i recieved an error message
- I attempted to register with a unique username and a password and password confirmation and i was successfully registered
- I attempted to manually enter url address for pages i didnt have access to as a unregistered or logged out user
  - attempted to get to bugs page and was rdirected back to register/login
  - attempted to get to cart page and was rdirected back to register/login
  - attempted to get to checkout page and was rdirected back to register/login 

##### Checks did for a logged in user

