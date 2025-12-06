import random

subjects = [
  "Shahrukh",
  "Messi",
  "Dhoni",
  "Rahul",
  "Shofik",
  "Modi Ji",
  "Lover Boy"
]
actions = [
  "launches",
  "cancels",
  "dances with",
  "eats",
  "declares war on ",
  "orders",
  "celebrates"
]
places_or_things =[
  "Red Fort",
  " Siliguri ",
  "a plate of biryani",
  "at Bangladesh",
  " during cricket match",
  "at Goa",
  "inside parliament"
]

#start of the loop
while True:
   subject = random.choice(subjects)
   action = random.choice(actions)
   place_or_thing = random.choice(places_or_things)
  
   headline = f"BREAKING NEWS : {subject} {action} {place_or_thing}" 
   print("\n"+ headline)

   user_input = input("\n Do you want another headline ? (yes or no)").strip().lower()

   if user_input == "no":
    break
   

#print goodbye message 
print("Thank you for using fake news headline generator. Have a good day !!")   