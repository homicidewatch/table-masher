Mashing up data for fun and reporting 
=====================================

The challenge here is to build a tool (or set of tools) to help reporters make
sense of large data sets and find stories that might otherwise be missed.
Knowing that Excel, Google Refine, ManyEyes and other such tools exist means
there's no point trying to reinvent what they do.

TableMasher is a tool for quickly sorting, filtering and visualizing data from
spreadsheets and comparing it with other data.

A common workflow might be something like this:

 1. Get some data 
 2. Clean it up in Google Refine 
 3. Filter, sort and compare it to other data in TableMasher 
 4. Go write a story

How it should work:

A reporter finds a data set that may or may not be interesting. It's sometimes
hard to tell, and starting with data but no story tends to lead to boring
stories.

So let's assume our reporter is working on a story about health problems in
(possibly soon-to-be-independent) southern Sudan. [This one][1], let's say.

 [1]: http://www.pbs.org/newshour/bb/health/jan-june11/sudan_01-03.html

Using [TableFu][2], a quick count of series names shows there are 1,636
unique types of data. The spreadsheet contains 76,324 rows.

 [2]: https://github.com/eyeseast/python-tablefu