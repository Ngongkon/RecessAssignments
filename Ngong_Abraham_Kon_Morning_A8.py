#exception handling in python
try:
    x = 20/0
except ZeroDivisionError:
    print("Invalid")
finally:
    print("it is trials")
#Dict is a dictionary{}
#EXECISE BELOW 
feeling = {
    'happy': "that's good to be happy",
    'sad': "that's bad to be sad",
    'angry': "that's really bad to be angry",
    'fearful': "it is not good to be fearful",
}
##prompt the user to enter their names

user_feeling = input("how are you feeling today?")
user_feeling = user_feeling.lower()
if user_feeling in feeling:
    print(feeling[user_feeling])
else:
    print("i'm sorry because i'm unable to identify your feeling")
    
#BELOW IS ANOTHER ALTERNATIVE WAY TO GET THE FEELING FROM THE USER
# Prompt the user to enter their feelings
feelings = input("How are you feeling today? ")

# Analyze the user's feelings and provide a response
if feelings.lower() == "happy":
    print("That's great to hear! Enjoy your day!")
elif feelings.lower() == "sad":
    print("I'm sorry to hear that. Things will get better!")
elif feelings.lower() == "angry":
    print("Take a deep breath. It's important to stay calm.")
else:
    print("I see. Remember to take care of yourself.")

