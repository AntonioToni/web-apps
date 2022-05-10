#! python.exe

import os
import cgi
import session
import subjects
params = cgi.FieldStorage()


if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

def start_html():
    print('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python PR04</title>
        <style>
            table{
                margin: 10px;
                min-width: 600px;
                text-align: center;
            }
            table, tr, th, td{
                border: 1px solid black;
            }
            td{
                padding: 3px
            }
            button{
                width: 80px;
                margin: 10px;
            }
        </style>
    </head>
    <body>
    <form action="" method="post">
    <input type='submit' name='botun' value='1st Year'>
    <input type='submit' name='botun' value='2nd Year'>
    <input type='submit' name='botun' value='3rd Year'> 
    <br><br>
    ''')


def end_html():
    print('''
    <br>
    <input type='submit' name='botun' value='List all'> 
    </form>
    </body>
    </html>
    ''')



#    <a href="lista.py">List all</a>
# <button type="submit" formaction="lista.py">List all</button>

def print_subjects(yr, session_data):
    print('''<table><tr><th>''')
    print(params.getvalue('botun'))
    print('''</th><th>''')
    print('Ects')
    print('''</th><th>''')
    print('Status') 
    print('''</th></tr>''')
    for key_subject, value_subject in subjects.subjects.items():
        if value_subject['year']==yr:
            print('''<tr><td>''')
            print(value_subject['name'])
            print('''</td><td>''')
            print(value_subject['ects'])
            print('''</td><td>''')
            for key_radio, value_radio in subjects.status_names.items():
                if (session_data.get(key_subject) == key_radio ):
                    print( value_radio + '''<input type="radio" name="''' + key_subject + '''" value="''' + key_radio + '''" checked>''' )
                else:
                    print(value_radio + '<input type="radio" name="' + key_subject + '" value="' + key_radio + '">')

            print('''</td></tr>''')
    print('''</table>''')

""" 
if dict[key_subject]==key_radio or params.getvalue(key_subject):
    print( value_radio + '''<input type="radio" name="''' + key_subject + '''" value="''' + key_radio + '''" checked>''' )
else:
    print(value_radio + '<input type="radio" name="' + key_subject + '" value="' + key_radio + '">') 
"""
    

def year_value(session_data):
    if params.getvalue("botun") == "1st Year":
        print_subjects(1, session_data)
    elif params.getvalue("botun") == "2nd Year":
        print_subjects(2, session_data)
    elif params.getvalue("botun") == "3rd Year":
        print_subjects(3, session_data)
    elif params.getvalue("botun") == None:
        print_subjects(1, session_data)
    elif params.getvalue("botun") == "List all":
        print_list(session_data)


def zbroj(session_data):
    zbroj=0
    for key, value in subjects.subjects.items():
        if session_data.get(key) =='pass' or session_data.get(key)=='enr':
            zbroj+=int(value['ects'])
    return zbroj

def pretvori(status):
        for k, v in subjects.status_names.items():
            if k==status:
                return v

def print_list(session_data):
    print('''<table><tr><th>''')
    print('Subjects')
    print('''</th><th>''')
    print('Ects')
    print('''</th><th>''')
    print('Status') 
    print('''</th></tr>''')
    for key_subject, value_subject in subjects.subjects.items():
        print('''<tr><td>''')
        print(value_subject['name']) 
        print('''</td><td>''')
        print(value_subject['ects'])
        print('''</td><td>''')
        if session_data.get(key_subject):
            print(pretvori(session_data.get(key_subject)))
        print('''</td>''')
    print('''<tr><th>''')
    print('Ukupno')
    print('''<th>''')
    print(zbroj(session_data))
    print('''</th></th><th></th></tr></table>''')

""" start_html()
year_value()
end_html() """

#print(session_data)
#print(os.environ)