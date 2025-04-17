import sys

speed_limit = int(sys.stdin.readline().strip())
real_speed = int(sys.stdin.readline().strip())

x = real_speed-speed_limit

if 1<= x <= 20:
   print("You are speeding and your fine is $100.")
elif 21<= x <= 30:
   print("You are speeding and your fine is $270.")
elif 31<= x :
   print("You are speeding and your fine is $500.")
else:
   print("Congratulations, you are within the speed limit!")