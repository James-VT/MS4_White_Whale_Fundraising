# White Whale Fundraising

This website serves as the main online presence of a charitable fundraising organisation dedicated to the conservation of whales and other sea creatures. Visitors to the site can become members of the organisation for a rolling monthly or annual donation, make one-off donations, and sponsor fundraising activities. Donations for membership are at a fixed amount, while one-off donations and sponsorships can be for any amount. Users can leave public messages for fundraisers whom they have sponsored. The owner(s) of the site will be using it to drive membership subscriptions, generate donations, and raise awareness of fundraising activities.

---

# Table of contents

# UX
This site is built to serve as a full-stack ecommerce site for a charitable organisation. It utilises Stripe to allow users to make donations via secure transactions, and is built using the Django framework. Users are able to register an account with the site, with which they can then become paying members if they wish, or make one-off donations or sponsor fundraisers and leave comments of encouragement.

## User stories
### A visitor to the site will want to:
1. Learn about the charity, its goals and its work.
2. Donate money to the charity.
3. Register an account on the site.
4. Become a member of the charity by subscribing with a monthly or annual donation.
5. Have their bank details used only in a secure way, such as that provided by the use of Stripe.
6. Learn about fundraisers and fundraising activities on the blog.
7. Leave comments for fundraisers and fundraising activities, such as messages of encouragement.
8. Edit or delete their own comments.

### A site owner will want to:
9. Explain to users who they are, what they do and how they can help as soon as a user lands on the home page.
10. Generate revenue via donations.
11. Grow their member base by encouraging users to become new members.
12. Raise awareness of upcoming fundraising events.
13. Host a blog.
14. Encourage interaction with users by allowing registered users to leave a comment.
15. Add upcoming fundraising events to the site for users to see.

---

# Features

## Donation form

The donation form allows users to donate a sum of money to the charity.

![Image of top half of donation form](assets/features/donationformtophalf.png)

![Image of bottom half of donation form](assets/features/donationformbottomhalf.png)

* Users can:
    * Choose from a selection of pre-set donation amounts.
    * Choose whether to Gift Aid their donations.
    * Fill in their details so that the charity can apply to have the donation value augmented with Gift Aid. For this reason, all required fields are for data required by HMRC for Gift Aid to be applied.
    * Have their details auto-fill from those in their profile, if they are logged in and have completed same. Likewise, if users are logged in but have not submitted default details, a checkbox allows users to choose whether details they enter onto the form are saved to their profiles.
    * Users do not need to be logged in to donate.

---

# Deployment

Below I include instructions on how to deploy, contribute to and clone this project.

## How to deploy a static project to GitHub pages:

1. You'll need a GitHub account, if you don't already have one. Head to their site https://github.com and you'll see the sign-up links straightaway on the home page. Google Chrome is the recommended browser for GitHub.
2. Once you're signed-up, this'll be your landing page.
3. Click on the user icon in the top right corner of the screen. This opens a dropdown menu. Click "Your repositories."
4. You'll then see a list of your repositories.
5. In the list of repositories, click the repository you want - in this case, Halo Pizza.
6. Then, from the bar along the top (not the nav bar - lower, under the repo name) click Settings.
7. On the Settings page, click "Pages" from the left-hand menu.
8. In the Pages options, before you've deployed, your "Branch" under "Source" will have a default value of none. Click this, then set it to Main or Master depending on the version you're using. Mine, having been already deployed, says Master and yours will too when deployed, but ignore that discrepancy for now.
9. Click Save.
10. The page will refresh, and you'll see it change to say "Your site is ready to be deployed at "https://username.github.io/repository-name/"
11. Be aware this deployed site will take a few minutes to deploy, usually about ten. Be patient and don't click while it's building as that can slow it down.
12. Click the link to make sure it works after a suitable wait. Et voila, you've deployed the site!

### Forking the repository for your own use

This creates a copy of the repository for editing or viewing without affecting my (original) version. If you want to do it, do this:

1. You'll need a GitHub account. Go to https://github.com to make one.
2. Locate the repository (this one). At the top right of the page, beneath my pink and white avatar, you'll see the Fork button. Click it.
3. This should add a version for you to use in your own repository. Have fun with it!

### Cloning the repository

Another way of getting your own local version to work on is to clone the repository. Below are the steps.

1. You'll need a GitHub account. Go to https://github.com to make one.
2. Locate the repository (this one).
3. Click Code, the button just to the left of the green GitPod button.
4. Click HTTPS to make sure you're in it, then copy the link you see there.
5. Head into GitPod or your IDE of choice, and open Git Bash.
6. The current working directory needs to be changed to the location you want the cloned one to be.
7. In the CLI, type "git clone" and then the URL you copied earlier.
8. Press enter. Result!

In my own workspace I am using my own secret keys and environment variables; you will need to sort out your own. Also, remember to consult requirements.txt for the project requirements.

## Deploying to Heroku:

Heroku allows us to host Python projects, instead of solely static sites which are all GitHub allows.

### Creating your Heroku app

1. Make an account with Heroku, if you don't already have one, here: https://www.heroku.com/
2. After setting your password and/or logging in, you'll find yourself looking at the Heroku dashboard.
3. You can click your chosen development language for some helpful tips and tutorials about how to use it with Heroku, if that'd help you.
4. From the dashboard, click "Create new app."
5. Enter a name for your app. It must be unique, and contain only letters, numbers and hyphens.
6. Choose a region. In our case, Europe.
7. Click "Create app."
8. From Heroku Resources you'll need Postgres. The free plan will work fine for this.

### Connect your Git repository to Heroku

1. You now want to find the "deploy" tab at the top of the screen.
2. You want to find "Deployment method" and "GitHub" from in there.
3. In the search bar, find your GitHub repo.
4. On the correct repo, click "Connect." DO NOT click to "Enable Automatic Deployment" at this stage. Tried it once. Can't recommend.

TO BE FINISHED

---

# Credits

## Technologies used

* Languages:
    * [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
    * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
    * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
    * [Python](https://www.python.org/) was used for the back end programming of the site.

* [Django](https://www.djangoproject.com/)
    * Django was used as the framework for the site's back-end development.

* [Pip](https://pip.pypa.io/en/stable/)
    * Pip is the package installer for Python, allowing us to install the packages we need for this site.

* [Jinja](https://www.palletsprojects.com/p/jinja/)
    * Jinja is a templating engine for Python, used to write Flask and other templating services.

* [GitHub](https://github.com/)
    * GitHub is where we host our site.

* [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    * Lighthouse assesses our pages for accessibility, performance and other things.

* [Jigsaw](https://jigsaw.w3.org/css-validator/)
    * Jigsaw validates our CSS for best practices.

* [JSHint](jshint.com)
    * JSHint assesses our Javascript for being practices, bugs, and syntax errors.

* [PEP8 Online](http://pep8online.com/)
    * PEP8 Online checks for errors in out Python code.

* [Am I Responsive?](http://ami.responsivedesign.is/#)
    * This is where we created the header image for this README.

* [favicon](favicon.io)
    * Favicon was used to create the site's favicon.

* [Heroku](https://devcenter.heroku.com/)
    * Heroku is where we deploy this live site. Throughout, we have ensured the version being deployed to Heroku matches our development version by checking features and screen layouts on both versions.

* [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes for this project. 

* [Git](https://git-scm.com/)
    * Git was used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.

* [Chrome](https://www.google.com/intl/en_uk/chrome/)
    * This project was created in the Google Chrome browser, and as such Chrome was used as the default testing browser.

* [Google Fonts](https://fonts.google.com/)
    * The fonts for the site were imported from Google Fonts. This site uses Roboto and Just Me Again Down Here throughout.

* [FontAwesome](https://fontawesome.com/)
    * The icons for social media links were taken from FontAwesome.

* [Coolors](https://coolors.co/)
    * The colour palette for this site was chosen using Coolors.

* [Stripe](https://stripe.com/gb)
    * The payment handling for this site was built using Stripe.

## Tutorials

Tutorials that assisted me with this project include Code Institute's Boutique Ado and Hello Django. I also leaned heavily on Django's own documentation for 3.2, and on [this video from Youtuber Dennis Ivy for the donation app.](https://www.youtube.com/watch?v=oZwyA9lUwRk)

Youtube channel Codemy.com also helped me create this project. Specifically, [this video](https://www.youtube.com/watch?v=CVEKe39VFu8&t=251s)

Others which provided code or inspiration:
https://www.youtube.com/watch?v=AZs4zggS7kA

This one from JustDjango helped with the membership, particularly the views and models:
https://www.youtube.com/watch?v=zu2PBUHMEew

This page also helped with the above, mentioned in memeberships/models.py:
https://levelup.gitconnected.com/building-a-membership-system-in-django-under-5-mins-5efd7e03627d

This video by Youtuber Code With Stein helped with the blog app:
https://www.youtube.com/watch?v=m3hhLE1KR5Q&t=565s

## Websites

Several websites with similar features were helpful to understand what sort of information might be seen on a typical charity website, for example form fields, membership types, etc. In particular, the websites of the Royal Armouries, the National Funding Scheme, and the National Trust influenced my decisions on layouts, styling and orders. Credit inevitably also goes to StackOverflow and to Code Institute's Slack for a constant resource of information and answers.

## Images

whalelighthousebanner.jpg is an open source image taken from Wikimedia Commons. Attribution: Gillfoto, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons

whitewhaleicon.jpg is is an open source image taken from Wikimedia Commons. Attribution: Tris T7, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons