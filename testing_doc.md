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

##### Checks I did for a logged out user

- User should only see HOME, BLOG and REGISTER/LOGIN links in nav: True
- I clicked each of these to make sure i was taken to the appropriate page.
- On register/login page user should see a tab for REGISTER and a tab for LOGIN: True
- I clicked these to make sure both login form and register forms are available
- I attempted to register with passwords that didnt match and i recived an error message
- I attempted to register with a username that was allready take and i recieved an error message
- I attempted to register with a unique username and a password and password confirmation and i was successfully registered
- I attempted to manually enter url address for pages i didnt have access to as a unregistered or logged out user
  - attempted to get to bugs page and was rdirected back to register/login
  - attempted to get to cart page and was rdirected back to register/login
  - attempted to get to checkout page and was rdirected back to register/login 

##### Checks I did for a logged in user

- User should see HOME, PROFILE, BUGS, FEATURES, BLOG, LOGOUT, CART in nav bar: True
- I clicked each of these to make sure i was taken to the appropriate page and that clicking logout logs me out of site.
- Profile page
  - My Feature section 
  - should contain a section with user avatar and name: True
  - Should contain 3 tabbed section one for My Features one for My Bugs one for Edit Profile
  - My Feactures tab section should be visible: True
  - When i click on others they should appear: True
    - My Feature section
      - My Features will show any suggested features i have suggested: True
      - If a Suggested Feature has not being paid for its status will be red and worded Owed: True
      - If a Suggested Feature has not being paid there will be no New Feature button available: True
      - If all Suggested Features are paid for a New Feature button will be available: True
      - If I click the New Feature button I will go to a page with a form to suggest a new feature: True
      - Each of my features is also a link that brings me to its details page and if i click them i go to the appropriate page:True
      - If a Feature has not being paid and i have clicked on its link in profile page when I arrive at details page it will show and Pay Now button: True
      - If I click Pay Now button I go directly to checkout page where I can pay: True
      - If I pay for the Feature link in profile changes status to Paid: True
      - If i click on its link i got to its details page where the Pay Now button is gone and an Add to Cart button shows: True
      - Allowing me to purchase it again if needs be
    - My Issue section
      - My Issues section will show any bugs i have reported: True
      - Each of my issues is also a link that brings me to its details page and if i click them i go to the appropriate page:True
      - There is a New Issue button available which I can click to bring me to a form to create a new issue: True
    -Edit Profile section
      - Here I can upload a suitable image to use for my avatar
      - If i choose a new image my previous avatar will be changed: True
      - If the file size of the image i try to use is to large it wont let me use it and a warning is given: True
      
- Bugs Page
  - I should see a list of all bugs all users have posted: True
  - There should be a New Issue button I can click to bring me to a form to fill in to create a new Issue: True
  - Clicking on New Issue button brings me to a page with a form to fill in: True
  - Each issue shown has a link to its details page: True
  - Clicking on the link brings me to its details page: True
  
- A bug details page
  - On bug details page I should see bug title and Id number, upvote count and a button to click for other users to upvote issue if they are also experiencing that issue.: True
  - On bug details page I should see a status button detailing if issue is OPEN DOING or CLOSED: True
  - On bug details page I should see initial comment explaining issue and user avatar: True
  - On bug details page I should see all others comments by user who created bug or by other users/admin/staff who commented on issue and their avatars: True
  - On bug details page I should see a comment area to fill in to create a comment: True
  - If user is Admin i should see a button in comment area to change the status of the issue from OPEN, DOING CLOSED: True
  - If commenting is closed I should not see the area for creating a comment: True
  - If a user upvotes a comment any further clicks should not upvote: True
  - If a user posts a comment it should append to the bottom of the other comments and display avatar of user: True

- Features page
  - On Feactures page a user should see a button to create a new feature: True
  - If user clicks this button they should be brought to a form to fill in to create a feature: True
  - On Feactures page a user should see a list of all available features: True
  - On Each feature a user should see how many of the feature were purchased: True
  - On Each feature there is a link a user can click that brings them to the feature details page: True
  - If a user clicks on link and goes to feature details page, user will see details of feature: True
    - Feature details including name of user who suggested the feature
  - A user should also see an Add to cart button: True
  - If a user clicks this button it should add to cart
    - Cart should update and display a new count of items: True
    - A user should also get a temporary message stating: added to cart: True
    - It should not let a user add to cart again if a user clicks button when item is in cart: True
    - Admin or Staff cannot add a feature to cart or see an add to cart button: True
  
- Blog page
  - On blog page a loggedin or logged out user should see short version of all blog posts: True
  - They should see a link to click which will bring the to a full blog post: True
  - They should see a view count showing how many times a blog post has being viewed: True
  - If they try to go to the create a blog route they should get redirected back to blog page: True
  - If user is Admin or Staff
    - Admin and Staff will see an edit button if the go to a full blog post: True
    - If they click this they go to the edit blog post page which contains a form with all blog details: True
      - A Staff user has only rights to view this page and if they edit it changes wont be saved: True
      - A Admin user can edit the blog post and any changes he makes will be saved: True
- Cart page
  - On cart page user should see any item that has being added to the cart: True
  - If an item is a suggested feature by that user and not paid for he should be able to see this in cart but not be able to remove it from cart: True
  - If an item is a suggested feature by him that is paid for or by another user It will have a red X beside it: True
  - If the X is clicked on the item will be removed from the cart and the total cost for items in cart adjusted down: True
  - User should see the cost of each item and a total cost of all items in cart: True
  - If a user adds another item to cart they should see the total cost go up: True
  - Users should see a checkout button: True
  - If checkout button is clicked they should be brought to the checkout page: True
- Checkout page
  -  Checkout page will show items being purchased and cost and a total price: True
  -  Checkout page will have form to fill in with personal and banking details: True
  -  Checkout page will have a submit payment button: True
  -  A user cannot Submit a payment with a blank field: True
  -  If a user fills in form but has no items to pay for and submits it justs redirects back: True
  -  If a user has an item showing to be purchased and fills in form correctly and submits a payment is made: True
  -  The cart is cleared on successful payement: True
- Logout
  - Logout should only appear to a logged in user: True
  - Clicking logout should logout user: True


### Visual checks

- I opend web site in Chrome and opened each page to make sure everything looked fine.
 - In Chrome dev tools I used the mobile setting to check each page in various mobile sizes
 - Dev tools showed how it would look in HTC, iPhone 6/7/8 ,iPhone 6/7/8 plus, iPhone x, iPad, iPad Pro, Galaxy S5 and it looked fine in all
- I also viewed it in Firefox with only one small issue wihch was a button label wrapping, so I adjusted styles to accomidate this
- I also viewed it in edge with only one issue which was a text not centreing, so I adjusted styles to accomidate this




