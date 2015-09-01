# WSDC_Task_2015-16
Design a user registration web app.
Django and angular is used to make a user registration system.

####Features :
People can register their self and login.You can see the user's username after login and right corner.
Setting and profile page is there ,showing the details only.


###Installation:
*'clone this repo.'
*'make virtualenv '
*'copy paste this repo folder inside that.'
*'activate env'
* 'pip install -r requirements.txt'
* 'npm install'
*  npm install -g bower
* 'bower install'
* 'python manage.py migrate'
* 'python manage.py runserver'

You can see the database using :
* 'python manage.py sqlmigrate <app_name> 0001'
       
here app name are : authentication , posts.

Go to python shell : 
$ python manage.py shell

and import the app databse models :

> from authentication.models import Account

Show all the current users

> print Account.objects.all()

[] # Returns an list of all registered user.

 Quit the Django shell.
> quit()




Note : 
* Best view in chrome.firfox may not work correctly in js part.
* If first time webpage is not working, be patient and refresh/reload your page 1-2 times with both browser.
* post part of the app is not completed.


Reference:
* 'code.tutsplus.com tutorial : django rest framework'
* 'thinkster.io tutorial : django-angular tutorial.'
* 'Django docs.'
* 'Djangular docs.'
* css from bootswatch.com free bootstrap stylesheet.



