#!C:\ProgramData\Anaconda3\python.exe

import cgi
params = cgi.FieldStorage()

firstname = params.getvalue('firstname')
status = params.getvalue('status')
name = params.getvalue('email')
smjer = params.getvalue('smjer')

print  ("""
<!DOCTYPE html>
<html>
<body>
<h2>Unesite podatke:</h2>
<form action="data.py" method="post">
  Napomene:
  <textarea type="text" name="Napomene" value=""></textarea>
  <br><br>""")
print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer") + '">')
print ('<input type="hidden" name="firstname" value="' + params.getvalue("firstname") + '">' )
print ('<input type="hidden" name="Email" value="' + params.getvalue("Email") + '">')
print ('<input type="hidden" name="status" value="' + params.getvalue("status") + '">' )
print("""<br><br>
  <input type="submit" value="Submit">
</form> 


</body>
</html>
""")