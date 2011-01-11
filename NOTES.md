Mashing up data for fun and reporting 
=====================================

The challenge here is to build a tool (or set of tools) to help reporters make sense of large data sets and find stories that might otherwise be missed. Knowing that Excel, Google Refine, ManyEyes and other such tools exist means there's no point trying to reinvent what they do.

TableMasher is a tool for quickly sorting, filtering and visualizing data from spreadsheets and comparing it with other data.

A common workflow might be something like this:

 1. Get some data 
 2. Clean it up in Google Refine 
 3. Filter, sort and compare it to other data in TableMasher 
 4. Go write a story

How it should work:

A reporter finds a data set that may or may not be interesting. It's sometimes hard to tell, and starting with data but no story tends to lead to boring stories.

So let's assume our reporter is working on a story about health problems in (possibly soon-to-be-independent) southern Sudan. [This one][1], let's say.

 [1]: http://www.pbs.org/newshour/bb/health/jan-june11/sudan_01-03.html

Part of the difficulty with this data set is the number of data types. Using [TableFu][2], a quick count of series names shows there are 1,636 unique types of data. The spreadsheet contains 76,324 rows. The data is/are in pretty good shape, though not terribly well organized. It's probably more than should really be in one spreadsheet.

 [2]: https://github.com/eyeseast/python-tablefu

TableFu alone will get us a slightly more useful set of data. We can facet the table by country or by series. Splitting it up by country gives us 57 new files.

Next step is re-arranging the data into something more usable. I added a transpose method to TableFu. I want column names to be year, country name, country code, then data types, with each year of data in rows.

As soon as this is cleaned up I'm going to shove it in a database (probably Mongo) and run actual queries.

Database structure
------------------

 - app
   - Model
     - field

 - tables
   - Table
     - title
     - created (datetime)
     - updated (datetime)
     - tags (list)
     - public (bool)
     - columns (list)
     - rows (json)

Rows are basically JSON (really, a list of dictionaries). We could stash this in a Django JSON field, but that means rows stop acting like rows. 

Using MongoDB has its drawbacks. Most Django apps are built for the standard ORM and some flavor of SQL. MongoEngine is the closest to a viable alternative, with an auth backend and session engine included. It doesn't play well with Piston out of the box due to lack of native serializers. The project (at least in its main repo) hasn't had a commit since mid-October when it reached v0.4. I have a fork that incorporates multidb support (a must if only for testing purposes), plus a JSON serializer. If it ends up being too painful it shouldn't be hard to convert back to plain Django. There's really only one core model.

(I'm suddenly wishing I had a better handle on CouchDB.)

Another alternative: TableSetter (which TableFu was originally built for) has no real concept of persistence. Metadata is stored in YAML files and data is parsed into TableFu objects every time. We could just swap YAML for a (simplified) database model and use Redis to store blobs of data, with storage/retrieval methods on the Django model. Or CSVs could stay in the filesystem (or on the web) with data lazy-loaded when called for.

Where I'm going with this (while something else is installing):

I want a reporter to be able to upload a cleaned/refined data set and quickly compare values in another set. Over time, reporters will add new tables and find new comparisons. So, if I had a bunch of population and health records in different spreadsheets. I could copy columns between Excel projects or keep a master Google Doc. Or I could upload each sheet as I get it to TableMasher, and compare it with spreadsheets another reporter has uploaded.

Wild-eyed alternative: What I'd really like is a command-line-like interface on the web, where data is filtered and transformed live, with results displayed below. A [CouchApp](http://couchapp.org) might be the way to do this, with a [CoffeeScript](http://coffeescript.org) DSL for filtering. Not something I'm likely to get done in a week, though.

Ahem, anyway, past all that.

I'm well down the path of doing this with traditional Django (ORM, templates, etc). This definitely has fewer pain points. Tables are slow to load, but I think that's on the rendering end, so I need some pagination or something. That shouldn't be too hard. It's fast enough in the shell.

Updated Database structure
------------------

 - app
   - Model
     - field

 - tables
   - Table
     - title
     - created (datetime)
     - updated (datetime)
     - tags (taggit)
     - public (bool)
     - columns (csv)
     
     data: lazy load a TableFu instance

URLs
-----

 - /
 table list
 
 - /<id>/
 table detail
 
 - /<id>/compare/
 list other tables to compare this table to
 
 - /<id>/compare/<id>
