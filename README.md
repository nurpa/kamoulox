## To-do

* replace `\u0022``"` with `\u00ab``«` and `\u00bb``»`;
* replace `\u0027``'` with `\u2019``’`;
* convert unicode entities to utf-8 ;
* authors homogenization (extend; make lower/uppercase) ;
* add a "LANGUAGE" field ;

## json_to_db

Dependencies:
* python2-sqlobject

How to use:
* python2 json_to_db.py /path/to/file.json

Configure:
* Choose DB :

~~~
connectionForURI('sqlite://%s' %os.path.join(sqlite_path, sqlite_file))
connectionForURI('mysql://user:password@host/database')
connectionForURI('postgres://user@host/database')
~~~
