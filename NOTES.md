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

Right now, TableFu doesn't have a transpose function, so adding that is on the agenda. Data by year should really be in rows, not columns. Country name is good to have somewhere but isn't what we're really looking for. Since I'm short on time, [tablib][3] will do the trick for now.

 [3]: https://github.com/kennethreitz/tablib/

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

