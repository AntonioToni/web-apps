#!python.exe

import os
import cgi
import base
import session
import db

params=cgi.FieldStorage()


if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)


session_id = session.get_or_create_session_id()
_,session_data = db.get_session(session_id)

print()
base.start_html() 

    
if(params.getvalue("botun") == "List all"):
     base.print_list(session_data)
else:
     base.year_value(session_data)
base.end_html()
