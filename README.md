## To-do

* replace `\u0022``"` with `\u00ab``«` and `\u00bb``»`;
* replace `\u0027``'` with `\u2019``’`;
* convert unicode entities to utf-8 ;
* [Done] authors homogenization (extend; make lower/uppercase) ;
* add a "LANGUAGE" field ;

## parse_and_fix
Fix some fields in JSON.

`python2 parse_and_fix.py /path/to/kamoulox.json` (will overwrite kamoulox.json)

## json_to_db
Insert JSON data in DB. Can configure type of DB (SQLITE is default)

`python2 json_to_db.py /path/to/kamoulox.json` (will generate kamoulox.db)

Python dependencies:
* python2-sqlobject

Configure DB:

```python
connectionForURI('sqlite://%s' %os.path.join(sqlite_path, sqlite_file))
connectionForURI('mysql://user:password@host/database')
connectionForURI('postgres://user@host/database')
```
