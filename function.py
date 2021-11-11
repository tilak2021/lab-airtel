def fallback():
  print("Hello from a fallback function")
  
  
def config():
  print("Hello from a confign function")


def xyz():
  print("Hello from a xyz function")

print("""
for fallback press 1
for config press 2
for xyz press 3
""")

input1 = input("Enter what you need to do today")

if input1 == "1":
	fallback()
    
elif input1 == "2":
	config()
