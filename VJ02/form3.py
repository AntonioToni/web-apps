#!E:\Programs\New folder\python.exe

import cgi
params = cgi.FieldStorage()
print  ("""
<!DOCTYPE html>
<html>
<body>
<h2>Unesite podatke:</h2>
<form action="data.py" method="post">
  Napomene:
  <textarea type="text" name="Napomene" value=""></textarea>
  <br><br>
  <input type="submit" value="Submit">
</form> 


</body>
</html>
""")