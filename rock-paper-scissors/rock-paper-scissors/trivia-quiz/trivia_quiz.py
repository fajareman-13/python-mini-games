# A trivia quiz 
questions_bank = {
    "what is the capital of France ?" : "paris",
    "How plant make their food ?" : "photosynthesis",
    "What is the capital of China ? " : "Beijing" ,
    "Which planet is known as the red planet ?" : "mars" ,
    "which language is this ?" : "python"
} # using a dictionary
def ask_question(question,answer): #defining a function
    user = input(f"{question}").strip().lower()
    return user == answer
score = 0
for q , a in questions_bank.items(): #using a loop 
    if ask_question(q,a):
        print("Correct answer! 🎉")
        score+=1
    else:
        print("Incorrect answer! 😣")
print(f"Your final score is {score}.")
