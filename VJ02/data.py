#!C:\ProgramData\Anaconda3\python.exe

import cgi
form_data = cgi.FieldStorage()

print('')
print (form_data.getvalue('firstname'))
print (form_data.getvalue('lastname'))
print (form_data.getvalue('status'))
print (form_data.getvalue('email'))
print (form_data.getvalue('smjer'))