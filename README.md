Website for guys to help them with girls using python django framework with postgresql backend.

How to set up.

PREREQ:
Have python/django framework installed as well postgresql. Have a database called pocket_wingman (you can change this in the settings.py file later)


1) cd to the directory you want. To put this repo in type: "git clone https://github.com/mrpoor/pocketwingman"

2) vi first_python_project/setting.py edit USER: and PASSWORD: to the password and username you created on the postgresql db.

3) cd to your base directory type: "python manage.py syncdb"

4) type: "python manage.py runserver"

5) Go to http://localhost:8000/pocketwingman/
