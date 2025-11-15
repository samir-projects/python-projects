import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Welcome1",
  database="bankapp"
)

mycursor=mydb.cursor()
sql1="select * from users"

def verify_users():
  mycursor.execute(sql1)
  for x in mycursor:
      y=list(x)
      return(y[1])

def verify_password():
  mycursor.execute(sql1)
  for x in mycursor:
      y=list(x)
      return(y[2])

def verify_balance():
  mycursor.execute(sql1)
  for x in mycursor:
      y=list(x)
      return(y[3])

def update_balance(username,balance):
  mycursor.execute("update users SET balance= %s where username =%s",(balance,username))
  mydb.commit()
 



