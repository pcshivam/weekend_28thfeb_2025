login = {'username':"user",'password':"user123"}
while True:
  username = input("Enter a username:")
  password = input("Enter a password:")
  if username == login['username'] and password == login['password']:
    print(f"{username} is logged in successfully")
    break
  else:
    print("Invalid username or password")
print("Now. User can perform operations")

def leap_year(year):
  if ((year%100!= 0 and year%4 == 0) or year%400 == 0):
    print(f"{year} is Leap year")
  else:
    print(f"{year} is not a Leap year")
leap_year(2024)