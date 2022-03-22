#!E:\Programs\New folder\python.exe

import cgi
params = cgi.FieldStorage()

pw1 = params.getvalue('password1')
pw2 = params.getvalue('password2')

def validate(pw1 , pw2):
    if (pw1 != pw2):
        Location: form1.py

print  ("""
<!DOCTYPE html>
<html>
<body>
<h2>Unesite podatke:</h2>
<form action="form3.py" method="post">
  Status:
  Redovan: <input type="radio" name="status" value="Redovan"> Izvanredan: <input type="radio" name="status" value="Izvanredan">
  <br><br>
  Email:
  <input type="email" name="Email" value="">
  <br><br>
  Smjer:
  <select name="smjer">
    <option value="programiranje">programiranje</option>
    <option value="baze_podataka">baze podataka</option>
    <option value="mreze">mreze</option>
    <option value="informacijski_sustavi">informacijski sustavi</option>
  </select>
  <br><br>
  <input type="submit" value="Submit">
</form> 


</body>
</html>
""")