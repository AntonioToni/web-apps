#!E:\Programs\New folder\python.exe
import imp
import subjects
import cgi
import os
params = cgi.FieldStorage()
from http import cookies

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

def make_cookies(params):
    for key in subjects.subjects:
        if params.getvalue(key):
            cookie = cookies.SimpleCookie()
            cookie[key] = params.getvalue(key)
            print(cookie.output())

def get_cookies(cookies):
    dictionary = {}
    for key in subjects.subjects:
        if cookies.get(key):
            dictionary[key] = cookies.get(key).value
    return dictionary

dicti = get_cookies(all_cookies_object)

def year(yr):
    yr= int(yr)
    print("""
        <table>
        <tr>
            <th>""")
    for y,r in subjects.year_names.items():
        if (yr == y):
            print(r) 
            print("""</th>
            <th>Ects</th>
            <th>Status</th>
        </tr>
    """)
    for i, j in subjects.subjects.items():
        if j.get("year")==yr:
            print("<tr>")
            for x,y in j.items():
                if (x != "year"):
                    print("<td>")
                    print(y)
                    print("</td>")
            print("<td>")
            for s,vel in subjects.status_names.items():
                if(vel in dicti):
                    print('''<input type="radio" name ="'''+i+'''" + value ="'''+s+'''"> ''' + vel +'checked="checked"')
                else:
                    print('''<input type="radio" name ="'''+i+'''" + value ="'''+s+'''"> ''' + vel)
            print("</tr>")


def start_html():
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python PR03</title>
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
    """)

def body():
    print("""
    <form method="post">
    <button type="submit" name="yr" value=1>1st Year</button>
    <button name="yr" value="2">2nd Year</button>
    <button name="yr" value="3">3rd Year</button>
    """)
    yr = params.getvalue("yr")
    if (yr!="None"):
        year(yr)


def end_html():
    print("""</body>
    </html>
    """)


make_cookies(params)

start_html()
body()
end_html()
