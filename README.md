## **Swoosh Source - Trainer Selling Website**

### Milestone Project 4 - Full Stack Frameworks with Django

* Swoosh Source is a online platform to sell popular Nike Trainers to members. 
* This website has been designed using Django full-stack framework and uses a Relational Database. Technologies used include HTML, CSS, Javascript, Python, Google Maps API and Stripe payments and is my submission for Milestone Project 4

## Live Project

[View the live project here](https://swoosh-source-caf22a2ccbfa.herokuapp.com/)

## Contents



# **User Experience**

## Background

* Swoosh Source is an innovative online store project dedicated to providing a seamless and enjoyable shopping experience for trainers enthusiasts. Swoosh Source aims to offer a comprehensive platform where users can easily browse, search, and purchase their favorite trainers. Users can also leave feedback on their purchase.


## User stories

| User Story ID | As a/an | I want to be able to... | So that I can... |
| --- | ----------- | ----------- | ----------- |
 | Viewing and Navigation | 
 | 1 | Customer | View a list of products | Add them to my bag to purchase  | 
 | 2 | Customer | View individual products details | Find out the price of the item, details of the product | 
 | 3 | Customer | Be able to add and remove products from my favourites | View them at a later date |
 | 4 | Customer | Be able to view my the total cost of my items at any time | Know my spending at all times | 
 | Registration and User Accounts | 
 | 5 | Site User | Easily register for an account | Have a personal account and be able to see my profile | 
 | 6 | Site User | Easily login or logout | Access my personal info | 
 | 7 | Site User | Easily access my user profile | Access my account quickly | 
 | 8 | Site User | Have a personalised user profile | With my personal order history and be able to update my default billing address | 
 | 9 | Site User | Be able to make an account after checkout | To be able to see my order if I haven't made one before | 
 | 10 | Site User | Make an account to leave ratings and reviews | Give site owners feedback on my experiecne | 
 | Sorting and Searching | 
 | 11 | Customer | Sort/ Filter products by all, price and category.  | Easily identify products that I like and fit my price range | 
 | 12 | Customer | Be able to edit my filters. | To make it quicker and easier to apply filters | 
 | 13 | Customer | Search for a product by name, description or key feature | Find a specific product I am looking for | 
 | 14 | Customer | Easily see what I've searched for and the number of results | Be able to see which options match my search | 
 | 15 | Customer | See if there are no search results | Quickly see there is nothing that matches my search | 
 | Purchasing and Checkout | 
 | 16 | Customer | Select the size of the product I am purchasing | Make sure I dont purchase the wrong size | 
 | 17 | Customer | View the items that I have added to my bag | View the total amount that I will be charged for my purchase | 
 | 18 | Customer | Adjust the quantity of items in my bag | Make sure I dont order the wrong amount | 
 | 19 | Customer | Easily enter my payment information | Quickly checkout | 
 | 20 | Customer | Feel my personal and payment information is safe and secure | Confidentially provide my payment information and make a purchase | 
 | 21 | Customer | View an order confirmation after checkout | Review my order and make sure I have made no mistakes | 
 | Landing Page | 
 | 22 | Store Owner | Showcase random listings | Give website visitors a quick peak at random products available to possibly try something new | 
 | Admin and Product Management | 
 | 23 | Store Owner | Add a product | Add new products to my store | 
 | 24 | Store Owner | Edit a product | Update or correct details shown to user about a product | 
 | 25 | Store Owner | Add a product | Remove a product from my store |


# **Design**

## Colour

* There is only 1 colour used on my site which is present on the landing page. This is a blue to white gradient behind the heading text and shop now button, as I am displaying a wide range of colours via my products on the home page and also the products page I didn't want to cause any colour clashes that may effect accessibility.



## Typography

I have chosen the Bebas Neue Font. This is provided by Google Fonts and [can be found here.](https://fonts.google.com/specimen/Bebas+Neue) This font is used for all my headings and sub headings and also my navigation bar and text.

I have opted to use Sans-Serif as my main font for regular text throughout the site.



## Images Used

The images I have used are for the products only. I have not added any background images even on my homepage as I am displaying a wide range of colours and didn't want to cause any colour clashes that may effect accessibility. All images used have been gathered from [Sole Supplier](https://thesolesupplier.co.uk/)

## Icons

I have used fontawesome icons which are present all throughout my site.


# **Structure**

## **Wireframes**

Here are all of the wireframes designed for this page broken down into device level. I desgined these wireframes with mobile first in mind and due to the nature of the site and the size of the content there was no changes needed to be made in terms of content displayed so I have combined my mobile and tablet wireframes into one.

  [Homepage Wireframes](/media/readme/Swoosh-Source-Home.png)

  [Sign Up Wireframes](/media/readme/Swoosh-Source-Sign-Up.png)

  [Sign In Wireframes](/media/readme/Swoosh-Source-Sign-In.png)

  [My Profile Wireframes](/media/readme/Swoosh-Source-Profile.png)

  [Products Wireframes](/media/readme/Swoosh-Source-Products.png)

  [Product Details Wireframes](/media/readme/Swoosh-Source-details.png)

  [Bag Wireframes](/media/readme/Swoosh-Source-Bag.png)

  [Checkout Wireframes](/media/readme/Swoosh-Source-Checkout.png)

  [Order Confirmation Wireframes](/media/readme/Swoosh-Source-Order-Thanks.png)

  [Feedback Wireframes](/media/readme/Swoosh-Source-Feedback.png)

  [Feedback Thanks Wireframes](/media/readme/Swoosh-Source-Feedback-Thanks.png)

  [Add Product Wireframes](/media/readme/Swoosh-Source-Add-product.png)

  [Edit Product Wireframes](/media/readme/Swoosh-Source-Edit.png)

  [All Wireframes](/media/readme/all-wireframes.pdf)

## Website Layout

The website has been desinged using Django, Python, ElephantSQL & PostgreSQL Javascript, HTML, CSS and Bootstrap 4. It has been desinged using a mobile first approach.
The website has a landing homepage that details the main purpose of the site and has a promintent get started button which takes the user to the products page.

There is also a responsive Navigation Bar which is present on all pages.

Each feature that is mentioned on pages are covered fully in the features section of this Readme

### Base.html page:
Although this page is not shown to the user it is one of the most important pages of my site when it comes to the design. This is where the Navbar is held. The Base templated is also stored where the includes such as Mobile Nav Bar and Toasts are held which will be covered more in the features section.

### Landing page (index.html):
This is the page the user is shown upon first time access to the website. The responsive navbar is at the top of the screen and some welcome text informing the customer the purpose of the website. There is a shop now button which will direct the user to the All Products section of the site. Under this there are 3 cards that show random Trainers to the user. Tempting them to try something new or a trainer they may never have considered before. The user is able to click product details to be taken straight to that Trainers details page.

![Homepage](/media/readme/Responsive-home.png)

### Signup page: 
This is the page where the user will create an account it is a simple form that requires the user to enter the following information.
  * Email Address
  * Email Address Confirmation
  * Username
  * Password
  * Password Confirmation

* This is a Django app called All-Auth which allows site owners to quickly add an accounts based system to their websites.
* All of the fields are requiured to be completed by the user to sign up if a user presses sign up without completing all of them a warning alert will prompt the user to fill in the field.

![Sign Up](/media/readme/Responsive-signup.png)

### Signin page: 
This is the page where the user will create an account it is a simple form that requires the user to enter the following information.
  * Username
  * Password

* This is a Django app called All-Auth which allows site owners to quickly add an accounts based system to their websites.
* The username and password must correctly match what the user used to create their account to sign in.
* Users can choose to Reminder this information.

![Sign In](/media/readme/Responsive-signin.png)

### My Profile Page:
The My profile page requires the user to be signed in. It is split into 2 main sections. Firstly there is the Default Delivery Information section, A user can fill out this information so that when they go to make a payment the delivery address is already held. The second section shows the user all their previous orders which can be clicked on to show the full order confirmation.

![My Profile](/media/readme/Responsive-profile.png)

### Products Page:
This page shows the user all of the trainers currently for sale on the website. The user is able to use the Sort selector to arrange items by price, name or category. The user to able to click on a trainer they like and be shown the full trainer details.

* The user can also reach this page by searching for a specific trainer in the search bar.
* If a site admin is logged in, under each product will be a link to either let the admin edit the product of remove it entirely.

![Products](/media/readme/Responsive-products.png)

### Product Details Page:
When a user clicks on a trainer they are then shown the full details of that trainer. This includes the full name, the category, the price, an image of the trainer and a brief description. The user is also presented with a number of options:

  * Select a quantity of pairs if they wish to order.
  * Select a size.
  * Add the item to thier bag.
  * Add the item to thier favourites.
  * Remove the item to thier favourites.

* Once a user has selected thier size and quantity then adds the item to thier bag, the bag will be updated and the user will be shown a popup of their current bag. 
* If a user selects add to favourites they will be shown a message saying they have done so
* If a user selects remove to favourites they will be shown a message saying they have done so

![Product Details](/media/readme/Responsive-details.png)

### Bag Page:
Users can view the page page to review their order before confirming they wish to purchase. They are shown all of the trainers they have added to their bag and can also update the quantity of items directly through the bag. They are shown the total cost of their spending and once happy can checkout their order.

![Bag](/media/readme/Responsive-bag.png)

### Checkout Page:
Once users are happy to checkout they are taken to the order checkout page. Where they are shown a breif summary of the items in their bag and there is then a crispyforms orderform for them to complete. This is a secure checkout page which is linked up with the stripe payments system The user needs to fill in the following before checking out:

  * Name
  * Email
  * Delivery Details
  * Payment Information

* Users can choose to save their delivery information they have entered to their profile which will update the my profile page.
* There is a button to adjust bag if users need to change thier order.
* The complete order button will attempt to purchase the item for the user, using the stripe payment system.

![Checkout](/media/readme/Responsive-checkout.png)

### Order Confirmation Page

Once users have successfully checked out their trainers, they will be shown the order confirmation page. Also they will be shown a success toast letting them know their order number. The order confirmation shows the user all of the order info including.

  * Order Number
  * Order Date
  * Order Details
  * Delivery Details
  * Billing Info

* At the bottom is a button for users to leave feedback or a button to return home.

![Order Confirmation](/media/readme/Responsive-order.png)

### Feedback Page
If a user selects to leave feedback they are shown the feedback page. It asks the user 2 things, First to rate their experience out of 5 stars. The other is a comments box where they can leave personalised comments.

![Feedback](/media/readme/Responsive-feedback-form.png)

### Feedback Thanks Page
If a user leaves feedback they are then shown a page which thanks them for doing so and then gives them an option to return home.

![Feedback Thanks](/media/readme/Responsive-feedback-thanks.png)

### Add Product Page
This is a page that is only accesible to admins of the site. It allows them to add new trainers to the website. Their is a crispy form to fill in that requires the following:

  * Product Name
  * Product Price
  * Product Category
  * Product Image
  * Product Description

Once complete the admin can press Add Product and the trainers will then be added to the websites product database.

![Add Product](/media/readme/Responsive-product-add.png)

### Edit Product Page
This is a page that is only accesible to admins of the site. It allows them to edit trainer information on trainers already in the database and update them. Their is a crispy form to fill in that requires the following:

  * Product Name
  * Product Price
  * Product Category
  * Product Image
  * Product Description

The form is already prefilled with the information that is held.
Once complete the admin can press Edit Product and the database will be updated.

![Edit Product](/media/readme/Responsive-product-edit.png)


## Features

My Navbar has been desgined to be responsive in a number of ways. It responds to the device in which it is being used and also the options displayed to the user are different if they are logged in or out.

MY navbar also contains a search bar which lets users search for trainers they are looking for.

__Desktop logged out Nav bar__

![Desktop Logged Out](/media/readme/nav-desktop-signout.png)

__Desktop logged in Nav bar__

![Desktop Logged In](/media/readme/nav-desktop.png)

__Mobile Nav bar__

![Mobile Nav ba](/media/readme/nav-mobile.png)

__Mobile Nav Search__

![Mobile Nav ba](/media/readme/nav-mobile-search.png)

__Mobile Expanded Nav bar Signed Out__

![Mobile Expanded Nav bar Signed Out](/media/readme/nav-mobile-expanded-signout.png)

__Mobile Expanded Nav bar Signed In__

![Mobile Expanded Nav bar Signed In](/media/readme/nav-mobile-expanded.png)

### User Accounts 
Users are able to sign up for an account they will need to complete a signup form. Users need to input the following:
  * Email Address
  * Email Address Confirmation
  * Username
  * Password
  * Password Confirmation

Once a user has registered an account they will be able to view previous orders they have made and update their saved delivery information for faster checkout.

### All Auth

Swoosh Source uses Django Allauth for robust user authentication and management.

### Features

- **User Registration and Login**: Easy setup for user sign-up and sign-in, supporting email verification.
- **Social Authentication**: Seamless integration with popular social login providers (e.g., Google, Facebook).
- **Password Management**: Built-in functionality for password reset and change.
- **Email Address Management**: Allows users to manage multiple email addresses with verification.

### Security

- **Secure Password Handling**: Uses Django's built-in password hashing.
- **SSL/TLS**: Ensures encrypted data transmission.
- **Customizable**: Easily configurable to meet specific security requirements.

For more details, refer to the [Django Allauth documentation](https://django-allauth.readthedocs.io/en/latest/).

__Sign Up Form__

![Sign up form](/media/readme/signup-form.png)

__Sign In Form__

![Mobile Expanded Nav bar Signed In](/media/readme/sign-in.png)

__My Profile Page__

![Mobile Expanded Nav bar Signed In](/media/readme/my-profile.png)


### Product Cards

Throughout my site I have product trainer cards. They are first shown on the homepage where 3 random pairs of trainers are displayed to the user. When clicked on the user will be directed to that products details.

The product cards are also used on the all products page.

__Random Product Cards on Homepage__

![Product Home](/media/readme/random-product-cards.png)

__Random Product Cards on Products Page__

![Product Page](/media/readme/product-page-cards.png)

### Sort Selector

When displaying products users can use the selector to sort products in order of Price, Name and Category.

__Sort Selector__

![Sort Selector](/media/readme/sort-selector.png)

__Sort Selector Expanded__

![Sort Expanded](/media/readme/sort-selector-expanded.png)


### Product Details
When a user clicks on a specific trainer they are shown the full details of that product. Which includes the Name, Price, Image and description.

Users are then able to select a size and quantity of trainer before adding to bag.

Users can also add and remove products from thier favourites.

__Product Details__

![Product Page](/media/readme/product-details.png)

__Size and Quantity Selector__

![Product Page](/media/readme/size-qty.png)

__Add and Remove from Favourites buttons__

![Product Page](/media/readme/favourites.png)


### Bag Preview
When a user add an item to their bag they are shown a preview of the bag under the icon in the navbar.
Users are able to view all the items in their bag at this point and view their total amount of spending.
There is a button that when pressed takes the user to thier full bag to look at before checking out.

__Bag Preview__

![Preview](/media/readme/bag-preview.png)

### Bag Page

The bag page is where the user can see their full order. They can update the quantity of their items using the selector or remove them fully.

Once a user has reviewed their bag they can the proceed to checkout.


__Bag__

![Bag](/media/readme/bag-page.png)

__Quantity Selector__

![Quantity](/media/readme/qty.png)

__Checkout Button__

![Checkout Button](/media/readme/checkout.png)


### Checkout Page

The checkout page has 2 main sections. 

A form that the user needs to fill in including:
 * Name
 * Email
 * Address Info
 * Payment Info

A summary of the users order

Once the checkout form is complete the user can press complete order and the stripe payment system will attempt to take a payment and the user will be informed if the purchase was successful. They will be then redirected to a page confirming their order.

__Checkout Form__

![Checkout Form](/media/readme/checkout-details.png)

__Order Summary__

![Order Summary](/media/readme/order-summary.png)

__Complete Order Button__

![Complete Order Button](/media/readme/complete-order.png)


### Order Confirmation Box

The order confirmation page generates an order number for the user and displays the following

  * Order Number
  * Order Date
  * Order Details
  * Delivery Details
  * Billing Info

* At the bottom is a button for users to leave feedback or a button to return home.

__Confirmation Form Button__

![Confirmation](/media/readme/order-confirmation.png)


### Feedback Form
Users can chose to leave feedback and rate their experience on the site. They can chose to rate their expeience out of 5 and also leave a comment for the site owner.

__Feedback Form__

![Feedback Form](/media/readme/feedback-form.png)


## Admin Features
### Add Product Form
Admins of the site are able to add new products using the product management link on the navbar. They will need to add:

  * Product Name
  * Product Price
  * Product Category
  * Product Image
  * Product Description

Once all information has been input and selects add product it will be added to the site database and shown on the relevant pages.

__Add Product Form__

![Add Form](/media/readme/add-form.png)

### Edit Product Form
Admins of the site are able to edit existing products using the product management link on the navbar.
The form will be pre populated with existing data on the product.

__Edit Product Form__

![Edit Form](/media/readme/Edit-form.png)

### Edit and Delete Product Button
Logged in admins when viewing the product page will be shown 2 buttons not visible to non admins. They are to edit and delete products.

__Edit and delete buttons__

![Edit Form](/media/readme/edit-delete.png)

## Toasts

Depending on what action the user is performing on the site they will be shown toasts to assist them.

They can be shown the following toasts.
  
  * Success
  * Info
  * Error

The toast will also contain a small message providing information to the customer.

__Toast Success__

![Toast Succes](/media/readme/toast-success.png)

__Toast Info__

![Toast Succes](/media/readme/toast-info.png)

__Toast Error__

![Toast Succes](/media/readme/toast-error.png)


# Data Model

I have used dbdiagram.io to design these database models. I have used the following data models:
  * User - Contains user sign in information, order history and default delivery details.
  * Favourites - Contains trainers users have favourited.
  * Order Feedback - Contains the rating and comments users have left on orders.
  * Category - Contains category ID names and type.
  * Products - Contains Product category, details, price and images.
  * Basket - Contains products users have added to thier basket.
  * Checkout order - Contains order details, user details, payment details.

![Data Models](/media/dbmodel.png)


# Deployment & Local Development

## Deployment

The project is deployed using Heroku. Follow these steps to deploy the project:

### Live Database Setup

For local development, you can use SQLite, but for live deployment, we will use an external database. Here, we will use ElephantSQL.

1. Go to the [ElephantSQL](https://www.elephantsql.com/) dashboard and click the 'New Instance' button.
2. Name your plan, select the Tiny Turtle plan (free plan), choose the region closest to you, and then click the review button.
3. Confirm the details and click 'Create Instance' at the bottom right.
4. In the dashboard, select the newly created database.
5. Copy the provided URL.

### Heroku Setup

1. Go to the [Heroku dashboard](https://dashboard.heroku.com/), click the 'New' button in the top right corner, and select 'Create New App'.
2. Name your app, select the region closest to you, and click the 'Create App' button at the bottom left.
3. Open the 'Settings' tab and create a new config var called `DATABASE_URL`, pasting the database URL from ElephantSQL into the value.

### Actions in the IDE

1. Install necessary packages:

    ```sh
    pip3 install dj_database_url==0.5.0 psycopg2
    ```

2. Freeze the requirements:

    ```sh
    pip3 freeze > requirements.txt
    ```

3. In `settings.py`, add the following:

    ```python
    import dj_database_url
    ```

4. Update the `DATABASES` setting:

    ```python
    DATABASES = { 'default': dj_database_url.parse('elephantsql-db-url-here') }
    ```

5. Check and apply migrations:

    ```sh
    python manage.py showmigrations
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a superuser for the new database:

    ```sh
    python manage.py createsuperuser
    ```

7. Update your `DATABASES` setting to:

    ```python
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
            }
        }
    ```

8. Install Gunicorn:

    ```sh
    pip3 install gunicorn
    pip3 freeze > requirements.txt
    ```

9. Create a `Procfile` in the root directory with the following line:

    ```sh
    web: gunicorn app_name.wsgi:application
    ```

10. Ensure your `ALLOWED_HOSTS` in `settings.py` includes both your Heroku URL and `localhost`:

    ```python
    ALLOWED_HOSTS = ['your-heroku-app.herokuapp.com', 'localhost']
    ```

11. Save, commit, and push all changes to GitHub.

## Amazon Web Services (AWS) for Static Files

1. Access your AWS account at [AWS](https://aws.amazon.com). Sign up or log in, then navigate to the S3 service.
2. Create a storage bucket:
   - Name the bucket after your project.
   - Choose your nearest region.
   - Enable "ACLs enabled" and select "Bucket owner preferred".
   - Uncheck "Block Public Access" and acknowledge to make the bucket public.
   - Click "Create bucket".

3. Enable static web hosting in the bucket properties.
4. Configure bucket permissions:
   - Copy the bucket's ARN.
   - Create a bucket policy allowing public read access.
   - Paste the generated policy into the Bucket Policy Editor and add `/*` to the end of the resource value.
   - Save the policy.

5. Configure CORS (Cross-Origin Resource Sharing):

    ```json
    [
        {
            "AllowedHeaders": ["Authorization"],
            "AllowedMethods": ["GET"],
            "AllowedOrigins": ["*"],
            "ExposeHeaders": []
        }
    ]
    ```

6. Edit the ACL section to enable public access for listing.

## Creating AWS Groups, Policies, and Users

1. Access IAM on the AWS Console.
2. Create a user group and name it (e.g., "manage-megabytes").
3. Create an S3 access policy:
   - Import the `AmazonS3FullAccess` managed policy.
   - Replace `*` with your bucket's ARN, adding `/*` to the end.
   - Name and create the policy.

4. Attach the policy to your user group.
5. Create a user with programmatic access and add it to the group.
6. Download the CSV with the user's access keys.

## Connecting Django to Your S3 Bucket

1. Install required packages:

    ```sh
    pip3 install boto3 django-storages
    pip3 freeze > requirements.txt
    ```

2. Add `storages` to `INSTALLED_APPS` in `settings.py`.

3. Configure Django settings for AWS:

    ```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }
        AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
        AWS_S3_REGION_NAME = 'your-region'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```

4. Add AWS keys to Heroku config vars using the values from your CSV file:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `USE_AWS` = `True`

5. Create `custom_storages.py` in the project root:

    ```python
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage

    class StaticStorage(S3Boto3Storage):
        location = 'static'

    class MediaStorage(S3Boto3Storage):
        location = 'media'
    ```

6. Update `settings.py`:

    ```python
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    ```

7. Deploy and verify that static files are collected.
8. In your S3 bucket, create a new folder named 'media'.

## Setting up Stripe

1. Obtain your Stripe keys from the [Stripe Dashboard](https://dashboard.stripe.com/):
   - Publishable key
   - Secret key

2. Add these keys to Heroku config vars:
   - `STRIPE_PUBLIC_KEY`
   - `STRIPE_SECRET_KEY`

3. Set up a webhook in Stripe:
   - Go to "Developers" -> "Webhooks" -> "Add endpoint".
   - Provide your deployed site's webhook URL (e.g., `https://your-site.herokuapp.com/webhook/`).
   - Select "Receive all events".
   - Create the endpoint and retrieve the webhook signing secret.

4. Add the webhook secret to Heroku:
   - `STRIPE_WH_SECRET`

5. Update `settings.py`:

    ```python
    import os

    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```

Make sure to replace placeholder values with your actual keys and URLs.

## Local Development

### How to Fork

To fork the Swoosh Source repository:

1. Log in to your GitHub account or sign up if you don't have one.
2. Visit the repository at Jordan094/Swoosh-Source.
3. Click the "Fork" button located at the top right corner.

### How to Clone

To clone the Swoosh Source repository:

1. Log in to your GitHub account or sign up if you don't have one..
2. Go to the repository for this project, Jordan094/Swoosh-Source.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

# **Accessibility**

I wanted to ensure that the website was fully accessible. I have done this by doing the following:

* Providing Alternative Text (Alt Text)
  * I've made sure to add descriptive alternative text (alt text) to all images on the website. Alt text adds context to images, enabling users who rely on screen readers to understand the visual content even if they can't see it.
* Ensuring Color Contrast
  * I've chosen color combinations that maintain accessible contrast ratios, ensuring that text remains readable against different background colors. This benefits users with visual impairments or color blindness.
* Responsive Design
  * The site is designed to adapt to various devices and screen sizes. This caters to users who rely on different devices or have specific accessibility requirements.

# Testing

I performed manual testing all through the creation of my website. I would test to ensure full functionaility is present across all devices before committing any changes.

Below is an overview of my testing and tests were carried out on the following devices:

* Samsung Galaxy S22 Ultra
* iPhone 14
* Samsung Galaxy Tab
* ASUS Chromebook with 15.3" Screen
* Windows 11 desktop computer with a 27" Monitor

## Site Wide Testing

### Accounts Testing

#### Scenario - User Account

Expectation: Users to be able to sign up for an account. Once logged into the account they should be able to complete the following:

  * Edit their default delivery address so the information is pre-populated when placing an order.
  * Add and remove items from their favourites.
  * Leave feedback on thier orders.
  * View their order history.

Result: Passed all tests.

#### Scenario - Admin Account

Expectation: If a site administrator is logged in they should be able to complete the following:

 * Add new trainers to the website.
 * Edit information of trainers already on the website.
 * Delete trainers from the website.

Result: Passed all tests.


### Navigation Testing

Expectation: Navigation mar needs to be able to complete the following:

  * Contain the website title that directs the users home
  * Contain a responsive bag icon that shows a preview when pressed
  * Contain a profile icon that gives further options when pressed
  * Contain a search bar that allows users to search for a specific trainer
  * Contain quick access links for searching for a specific trainer category, name or price
  * Turn into a respond to the device being displayed on.

Result: Passed all tests.


### Trainer Cards

Expectation: Trainer cards to be visible on the homepage showing the name, price and a button to view the full product.

Result: Passed all tests.


### User forms

Expectation: A number of forms requiring the user to complete and progress further through the site. The forms are as follows:

 * User Registration
 * Sign In
 * My Profile
 * Checkout Details
 * Feedback Form

Result: Passed all tests.

## Page Testing

__Home Page (index.html)__

Expectation: 
 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Have a shop now button under the header text saying shop now, shop now button to take the user to the all products section of the website.
 * 3 product cards to be shown to the user tempting them to try a new trainer that they may not have considered.
 * Product cards to be shown in random order.

Result: Passed all tests.

__Signup Page (signup.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Users should be able to complete all forms to create thier own unique account.
 * Once account has been created it should be added to the accounts database.
 * If users already have an account they should be prompted to head to the log in page with a clickable link.

Result: Passed all tests.

__Signin Page (signin.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Users should be able to complete all forms to login to their own unique account.
 * Once logged in the user should be redirected to the index landing page.
 * If users have not signed up they should be prompted to create an account using clickable link.

 Result: Passed all tests.

__Profile Page (profile.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Page should be split into 2 sections, order history and default billing info.
 * All previous orders should be shown to the user in the order history section.
 * Clicking on that order should show them a confirmation of that previous order.
 * Users should be shown a form containing either their blank shipping address if not completed or saved before, or if saved be shown the saved info.
 * Users should be able to update this form and update thier default saved address.
 * Once complete, when users head to the checkout page. Their default shipping info should be pre-populated.

 Result: Passed all tests.

__Products Page (products.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Products to be displayed depending on how the links are accessed.
 * Products that match search terms be shown if user submits a search
 * When users click on their respective links (e.g. Air max 95 category) they should only be shown that category.
 * Users should be able to sort products by the following: Name, Price, Category
 * When a product is clicked on they should be taken to the full product details page for that specific product.
 * When admins are logged in they should see options to edit and delete products.

 Result: Passed all tests.


__Product Details Page (products/details.html)__

Expectation:

* Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
* Users to be shown the full information of the product including: Name, Price, Category, Description and image.
* Product size selector.
* Product quantity selector.
* Add to bag button present that when pressed adds the product to bag.
* Toast to show product has been added to bag and a bag preview shown to user.
* Button to add product from favourites.
* Button to remove product from favourites.
* Toast to show if favourites adjusted.

Result: Passed all tests.


__Bag Page (bag.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Show users all items in thier bag.
 * Show users the Name, price, size and quantity selected of each item.
 * Allow users to quickly adjust the quantity of the items.
 * Show users a total.
 * Show users their delivery fee.
 * Show users their grand total.
 * Show users a button to return to shopping if they have not finished or a checkout now button that should direct them to the checkout page.

Result: Passed all tests.


__Checkout Page (checkout.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Show the users a summary of their order with all items and a grand total.
 * Provide a form for users to complete to purchase their items.
 * Require users to provide a name and email address on every purchase.
 * If users have saved billing info, pre populate this section of the form.
 * Require user to input payment details into form that will be handled by the stripe payment system.
 * Show a confirm order button once users order happy to continue which will attempt to purchase the item.
 * If successful the user should be directed to the order confirmation page.

Result: Passed all tests.


__Order Confirmation Page (checkout/order.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Show the users a summary a confirmation of thier order.
 * Give the user an order ID number incase they require it for support.
 * Show the user their order info (order number, date of purchase)
 * Show the user their order details (products, size, quantity)
 * Show the user therr delivery details (Address)
 * Show the user their Billing info (Total, delivery, grand total)
 * Give the user an option to leave feedback which will direct the to the feedback page.
 * Give the user the option to return home which will direct them to the landing page.

Result: Passed all tests.

__Feedback Page (feedback.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Allow the user to rate thier experience.
 * Show 5 star icons to rate their order out of 5.
 * Show a comments box for user to comment on their order.
 * Button for users to leave feedback which will add feedback to database and redirect users to feedback thanks page.

Result: Passed all tests.


__Feedback Thanks Page (feedback_thanks.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Show a breif message thanking users for leaving feedback on thier order.
 * Showing the user a button that will return them to the landing page.

Result: Passed all tests.

__ADMIN ONLY - Add products Page (products/add.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Only be accessible to site admins.
 * Show the admin a blank form to complete to add a new prodcut to the website.
 * Require the following categories to be completed (Name, Price, Category, Description, Image)
 * Once complete and submitted product should be then displayed on the website.

Result: Passed all tests.

__ADMIN ONLY - Edit products Page (products/edit.html)__

Expectation:

 * Responsive to the device in which it is being displayed on, contain the navbar at the top with responsive icons.
 * Only be accessible to site admins.
 * Show the admin a pre-filled out form of the product they have chosen to edit.
 * Require the following categories to be completed (Name, Price, Category, Description, Image)
 * Once complete and submitted product should be then updated on the website.

Result: Passed all tests.


## Testing User stories

| Test ID | As a/an | I want to be able to... | Result? |
| --- | ----------- | ----------- | ----------- |
 | Viewing and Navigation | 
 | 1 | Customer | View a list of products | Passed Test.  | 
 | 2 | Customer | View individual products details | Passed Test. | 
 | 3 | Customer | Be able to add and remove products from my favourites | Passed Test. |
 | 4 | Customer | Be able to view my the total cost of my items at any time | Passed Test. | 
 | Registration and User Accounts | 
 | 5 | Site User | Easily register for an account | Passed Test. | 
 | 6 | Site User | Easily login or logout | Passed Test. | 
 | 7 | Site User | Easily access my user profile | Passed Test. | 
 | 8 | Site User | Have a personalised user profile | Passed Test. | 
 | 9 | Site User | Be able to make an account after checkout | Passed Test. | 
 | 10 | Site User | Make an account to leave ratings and reviews | Passed Test. | 
 | 11 | Customer | Sort/ Filter products by all, price and category.  | Passed Test. | 
 | 12 | Customer | Be able to edit my filters. | Passed Test. | 
 | 13 | Customer | Search for a product by name, description or key feature | Passed Test. | 
 | 14 | Customer | Easily see what I've searched for and the number of results | Passed Test. | 
 | 15 | Customer | See if there are no search results | Passed Test. | 
 | 16 | Customer | Select the size of the product I am purchasing | Passed Test. | 
 | 17 | Customer | View the items that I have added to my bag | Passed Test. | 
 | 18 | Customer | Adjust the quantity of items in my bag | Passed Test. | 
 | 19 | Customer | Easily enter my payment information | Passed Test. | 
 | 20 | Customer | Feel my personal and payment information is safe and secure | Passed Test. | 
 | 21 | Customer | View an order confirmation after checkout | Passed Test. | 
 | Landing Page | 
 | 22 | Store Owner | Showcase random listings | Passed Test. | 
 | Admin and Product Management | 
 | 23 | Store Owner | Add a product | Passed Test. | 
 | 24 | Store Owner | Edit a product | Passed Test. | 
 | 25 | Store Owner | Add a product | Passed Test. |



# **Future Developments**

There are a number of features I would like to add in the future to my website, the features are as follows:

  * Page for admins to view user feedback
  * Page for users to view favourites
  * Email authentication


# **Technologies Used**
* [Django](https://www.djangoproject.com/)
  * This website is built using Django, a high-level Python web framework.
* [HTML5](https://www.w3schools.com/html/html_intro.asp)
  * HTML was used to create my website
* [Python](https://www.python.org/)
  * Used for my websites core functionality
* [Heroku](https://id.heroku.com/login)
  * Heroku is the deployment source I used for this project.
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
  * Templating Language
* [MaterialiseCSS](https://materializecss.com/)
  * UI component library that is created with HTML, CSS, and Javascript
* [ElephantSQL](https://www.elephantsql.com/)
  * ElephantSQL installs and manages PostgreSQL databases
* [CSS3](https://www.w3schools.com/css/css_intro.asp)
  * CSS was used to style my website
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
  * Javascript was used to add functionality to my website
* [GitHub](https://github.com/)
  * I used github to create my repository and store my projects code.
* [Code Anywhere](https://app.codeanywhere.com/)
  * I used Code Anywhere as my IDE
* [Chrome](https://www.google.com/intl/en_uk/chrome/)
  * I tested my website and responsiveness throught creation using chrome developer tools.
* [Balsamiq](https://balsamiq.com/)
  * Balsamiq was used to create the wireframes during the design process.
* [Google Fonts](https://fonts.google.com/)
  * I used the font Outfit which is a Google font, with a fallback font of Sans-Serif thoughout my whole project.
* [Am I Responsive?](https://ui.dev/amiresponsive)
  * This was used to test the responsiveness on all devices once the pages were complete.
* [W3 Schools HTML Validation Service](https://validator.w3.org/)
  * This was used to check for any HTML errors in the code.
* [W3 Schools CSS Validation Service](https://jigsaw.w3.org/css-validator/)
  * This was used to check for any HTML errors in the code.

## Validation and Tools

### W3C Validation Tools

Once my pages were complete I used [W3C Markup Validation Service](https://validator.w3.org/) to ensure my code had no errors.

No errors are present throughout the whole site.

I also used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to ensure my code has no CSS errors. This came back as a pass, However there are a number of errors with the fontawesome and materialise which are unavoidable.

Lastly I used [JSHint](https://jshint.com/) to validate my JavaScript.

There were no errors found. There was 1 warning to say I had an unused variable but this will be used in future interations of this site.

### Responsiveness Testing

I used [Am I Responsive?](https://ui.dev/amiresponsive) to ensure my page displayed correctly on all devices. The screenshots are above each pages section

# Credits

## Code

* [Code Institute's Level 5 in Web Application Development course](https://codeinstitute.net/) for providing me lessons and source code which has helped to create my website.

* [MaterializeCSS](https://materializecss.com/) for providing templates to build my site with ease.

* [Heroku](https://id.heroku.com/login) Heroku is the deployment source I used for this project.
  
* [Flask](https://flask.palletsprojects.com/en/2.2.x/) Templating Language.

* [ElephantSQL](https://www.elephantsql.com/) for providing me with database hosting and management.

* [W3Schools](https://www.w3schools.com/) for providing examples of code for further customisation of my site and quick help for HTML elements.

* [Fontawesome](https://fontawesome.com/) for providing me with icons which I have used ony my footer.

* [Mozilla MDN Javascript Developer Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript) for guidance with my Javascript Age Validation.

## Imagery


# Acknowledgements

* Thank you to [Code Institute](https://codeinstitute.net/) staff for providing me lessons.
  
* Thank you to [City of Bristol College](https://www.cityofbristol.ac.uk/) for facilitating my learning.

* Thank you to Pasquale Fasulo for my tutoring sessions and [Manuel Perez Romero](https://github.com/Manuperezro) for my one to one sessions.

* Thank you to Thomas Farrell for providing invaluable in depth user testing feedback as a qualified software tester.

* Thank you to [Daniel Matthews](https://github.com/Dan-Matthews-23) for support offered and also for testing.

* Thank you to Levi Webb for providing android testing and laptop testing.