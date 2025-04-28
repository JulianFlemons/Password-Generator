#1 Create a dictionary called 'responses' with the key being something a user would say,
#  and the value being the response from the chatbot.

responses = {'I need help with something': "Hello what do you need help with?",
'I need help on deciding what career path I should go down': 'What career field are you interested in',
             'Tech': 'There are different fields in Tech. There is Software Engineering, Cyber Security, Data Science, Database Admin, Cloud Compunting'}
print(responses)

#2 Define a function 'get_response' that takes user input as an argument
# and returns the corresponding response from the 'responses' dictionary.
# for example, when I enter I need help with something, you should reply
# Hello, what do you need help with

def get_response(user_input: str) -> str:
  if user_input in responses: # So if the user input is in key of the dictionary I created the output should be one of the values that i created for the dictionary

    return responses[user_input]
  else: # If the users input is not in the keys of the dictionary created responed "I'm sorry what'd you say?"

    return "I'm sorry what'd you say?"


#a = get_response("wasssup")
print(get_response("Apple"))
print(get_response("I need help with something"))

#3 Define the main chatbot function.
#3 Define the main chatbot function named 'chatbot'. This function will handle the interaction
# between the user and the chatbot. Inside the function, display a welcome message to the user.
# Then, start a loop where the chatbot repeatedly prompts the user for input.
# If the user input is 'bye', display a farewell message and exit the loop.
# Otherwise, display the chatbot's response to the user input.
#I need to define the chatbot. The input should be "Welcome Message"
# The user output if they responed bye should give a goodbye mesaage
def chatbot ():
  print("Welcome to the Chatbot") # I created a welcome statement
  while True: # Allowing me to not have to keep pressing play (Lazy) It keeps running
    users = input ("Enter your Question?") # Then I asked the user a question I stored the users responses in a variable called 'users'
     #If a user types in bye I want the program to stop running
    if users == "bye": #I want the program to stop running
      print("Have a great day!!")
      break
    else: # If the users does not type bye it the program runs
      print(get_response(users))
#4 Run the chatbot.
chatbot()