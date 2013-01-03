#-*- coding: utf-8 -*-

import os, sys

### Get path of JSON file
if len(sys.argv) != 2:
  sys.exit("expected json file")

json_file = sys.argv[1]

### SQL
from sqlobject import *

#~ mysql://user:password@host/database
#~ postgres://user@host/database

#~ sqlite:///full/path/to/database
sqlite_path = os.getcwd()
sqlite_file = "kamoulox.db"
sqlhub.processConnection = connectionForURI('sqlite://%s' %os.path.join(sqlite_path, sqlite_file))

# Schema
class Dbrpbelge(SQLObject):
     pub_date = DateCol()
     authors  = StringCol()
     source   = StringCol()
     url      = StringCol()
     title    = StringCol()
     content  = StringCol()

# Let's create
Dbrpbelge.createTable(ifNotExists=True)

### Parse and insert
import json, time

json_data=open(json_file)
data = json.load(json_data)
json_data.close()

for idx, article in enumerate(data):
    auteur = article['AUTHORS'].encode("utf-8")
    title  = article['TITLE'].encode("utf-8")
    text   = article['CONTENT'].encode("utf-8")

    url    = article['URL']
    source = article['SOURCE']

    year   = article['YEAR']
    date   = article['DATE']

    if date:
        try:
            date = time.strptime(date, "%d/%m/%Y")
            date = time.strftime("%Y-%m-%d", date)
        except ValueError:
            print '[ERROR] JSON : date value invalid : #%s : "%s" - "%s"' %(idx, date, title.decode("utf-8"))
            date = None
    else:
        date = None

    print '#%s - %s' %(idx, title)
    Dbrpbelge(pub_date=date, authors=auteur, source=source, url=url, title=title, content=text)
