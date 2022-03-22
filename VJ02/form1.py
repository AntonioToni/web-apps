#!E:\Programs\New folder\python.exe
import cgi
params = cgi.FieldStorage()

print  ("""
<!DOCTYPE html>
<html>
<head>
  Location: form1.py
</head>
<body>
<h2>Unesite podatke:</h2>
<form action="form2.py" method="post">
  Ime:
  <input type="text" name="firstname" value="">
  <br><br>
  Lozinka:
  <input type="password" name="password1" value="">
  <br><br>
  Ponovi lozinku:
  <input type="password" name="password2" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 
</body>
</html>
""")


    
