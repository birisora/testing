#Database(db) Introduction

Note I'm downloading [sqlite browser]('http://sqlitebrowser.org/')

###Relational Databases:
- model data by storing rows and columns in tables
- ability to retrieve data from tables and relationship between other tables in query

####Terms
- Database: contains many tables
- table (Relation): contains attributes and tuples
- Tuple (row): set of field that represents an object and info about object
- Attribute (column): one or more elements of data corresponding to object represented by row
- Object: pysical object or concepts
- Relation: set of tuples that have same attributes
	- aka table, organized into rows and columns
![image from sfdcloud](https://developer.salesforce.com/docs/resources/img/en-us/192.0?doc_id=dev_guides%2Fappx_dev%2Fimages%2Fadg_db_positions.jpg&folder=fundamentals)

###SQL
- Structured Query Language: language used to issues commands to db
	- create table, retrieve data, insert, delete ...
	- This is CRUD (Create, Retrieve, Update, Delete)

###Database Model
- db model/schema is structure or format of a db.
	- application of data model when used with db management system
- Three Major DB Management Systems:
	- Oracle: large, enterprise scale, commercial
	- MySql: Simpler, fast and scalable, commercial open source
		- There's a MariaDB
	- SqlServer: nice from Microsoft
	- Others are SQLite, Postgress and more
		- SQLite is an embedded DB
			- part of a software, built in

```SQL
/* Single Table example */
CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
)

```

######SQL Insert
- insert statment inserts a row into a table
```SQL
INSERT INTO Users(name,email) VALUES ('danny', 'danny@gmail.com')
```

######SQL Delete
- Deletes a row in a table based on selection criteria
```SQL
DELETE FROM Users WHERE email='danny@gmail.com'
```

######SQL Update
- Allow updates to a field with a where clause
```SQL
UPDATE Users SET name="John" WHERE email='yolo@gmail.com'
```

######SQL Retrieving Records
- Select statment retrieves group of records
	- with WHERE, you can retrieve all or subset of records
```SQL
SELECT*FROM Users WHERE email='yolo@gmail.com'
```
######Sorting with ORDER BY
- You can add an ORDER BY clause to SELECT statements to get results sorted (asc or desc)
```SQL
SELECT*FROM Users ORDER BY name
```

###Data Models
- It's a good idea to plan out how you're going to make your db. For example, let's use the idea of songs/tracks
- Generally a good idea to make your table from outside in
- primary key: a way to refer to a particular row
	- we'll put insert the title, which will get a number
	- then use number in a column to point to a different table
- logical key: the unique thing we use to look up this row from the outside world. 
- foreign key: one of the columns that we add to starting point of the arrows.
	- primary key is end of the arrow, while foreign is start
- tracks contains:
	- id, title, rating, len, count, album_id, genre_id
	- Belongs-to genre
		- contains: id, name
	- Belongs-to album
		- contains: id, title, artist_id
		- belongs to artist
			- contains: id, name
	
sample of making a table
```SQL
CREATE TABLE Track(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
	title TEXT,
	album_id INTEGER,
	genre_id Integer,
	len INTEGER, rating INTEGER, count INTEGER
)
```

###Relational Power
- web: removing replicated data and substitue with references to single copy of each bit of data
	- data comes from number of tables linked by foreign keys
	- can read through quickly
- linking tables by What we want to see, the tables that hold data, and then how the tables are linked
```SQL
select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
```

if you get rid of the on Album.artist_id = Artist.id,
it then does things by all combinations, which can become really messy for bigger dbs

There's a pattern

```SQL
select Track.title, Artist.name, Album.title, Genre.name
from Track join Genre join Album join Artist
on Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id
```

###Many to Many
- occurs when you need to add a 'connection' table with 2 foreign keys (they point outwards)
	- usually no separate primary keys
		- both numbers, so duplication allowed
	- create a composite key, both of these two things are the primary key for the table
	- eg. 1 game can have many producers and 1 producer can have many games
		- so we have to build a table between them (junction table)

###Multistep Data Analysis
- Data Source -Gather-> Database -> Clean/Process -> Clean db -> Visualize or analyze data
	- Gatherisng process needs to be careful, since things could blow up in between so we store in a database and continue wherever last gathered

####Geocoding
- Google geodata -where.data->geoload.py-> geodata.sqlite -> geodump.py ->where.js -> what we see
	- where.data is a bunch of location data
	- data stored in sqlite file (gets cached)
	- then file to process and shows you results from data

####Search Engine Architecture
- Web crawling 
	- a program that scours the WWW in an automated manner to create a copy of visited pages for later processing of a search enginer for other purposes.
- index building
- searching

####Gmane
- crawl archive of mailing list
- do some analysis/cleanup
- visualize data as word cloud and lines
