#!C:\ProgramData\Anaconda3\python.exe

import cgi
params = cgi.FieldStorage()

print('')
print (params.getvalue('firstname'))
print (params.getvalue('status'))
print (params.getvalue('Email'))
print (params.getvalue('smjer'))
print (params.getvalue('Napomene'))