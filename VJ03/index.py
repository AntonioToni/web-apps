#!E:\Programs\New folder\python.exe
import subjects

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
    <button onclick="year1()">1st Year</button>
    <button>2nd Year</button>
    <button>3rd Year</button>
    """)


def end_html():
    print("""</body>
    </html>
    """)  

def year1():
    print("""
        <table>
        <tr>
            <th>1st Year</th>
            <th>Ects</th>
            <th>Status</th>
        </tr>
    """)
    for i, j in subjects.subjects.items():
        if j.get("year")==1:
            print("<tr>")
            for x,y in j.items():
                if (x != "year"):
                    print("<td>")
                    print(y)
                    print("</td>")
            print("""<td>Not selected<input name="dmt" value="not" type="radio"> Enrolled<input name="dmt" value="enr" type="radio"> Passed<input name="dmt" value="pass" type="radio"></td>""")
            print("</tr>")

def year2():
    print("""
        <table>
        <tr>
            <th>2nd Year</th>
            <th>Ects</th>
            <th>Status</th>
        </tr>
    """)
    for i, j in subjects.subjects.items():
        if j.get("year")==2:
            print("<tr>")
            for x,y in j.items():
                if (x != "year"):
                    print("<td>")
                    print(y)
                    print("</td>")
            print("""<td>Not selected<input name="dmt" value="not" type="radio"> Enrolled<input name="dmt" value="enr" type="radio"> Passed<input name="dmt" value="pass" type="radio"></td>""")
            print("</tr>")

def year3():
    print("""
        <table>
        <tr>
            <th>3rd Year</th>
            <th>Ects</th>
            <th>Status</th>
        </tr>
    """)
    for i, j in subjects.subjects.items():
        if j.get("year")==3:
            print("<tr>")
            for x,y in j.items():
                if (x != "year"):
                    print("<td>")
                    print(y)
                    print("</td>")
            print("""<td>Not selected<input name="dmt" value="not" type="radio"> Enrolled<input name="dmt" value="enr" type="radio"> Passed<input name="dmt" value="pass" type="radio"></td>""")
            print("</tr>")

start_html()
body()
end_html()
