TableMasher
===========

It's for mashing your tables. Or your newsroom's tables.

Quick start:

    # preferably all this in a virtualenv
    
    $ git clone git://github.com/homicidewatch/table-masher.git
    $ cd table-masher
    $ pip install -r requirements.txt
    $ cd tablemasher
    $ python manage.py validate
    $ python manage.py syncdb
    $ python manage.py loaddata tables.json # it's in the tables app
    $ python manage.py runserver # or run_gunicorn
    
Load some tables via the admin (http://localhost:8000/admin/).

Comparing tables (not implemented just yet):
--------------------------------------------

From the home view, hit the "compare" link next to any table. You'll see a list of other tables to compare it to. Choose a column from each. You'll see a chart showing how they match up. Tell your friends. Or go write a story.