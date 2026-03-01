login = {'username':"user",'password':"user123"}
while True:
  username = input("Enter a username:")
  password = input("Enter a password:")
  if username == login['username'] and password == login['password']:
    print(f"{username} is logged in successfully")
    break
  else:
    print("Invalid username or password")