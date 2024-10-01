#IMPORT LIBRARY 
import json # load & save to json
from difflib import SequenceMatcher # for check similarity between 2 strings

# FUNCTION LOAD KNOWLEDGE FROM JSON
def load_knowledge():
    try:
        with open('knowledges.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"qa": []}

# FUNCTION SAVE KNOWLEDGE TO JSON 
def save_knowledge(knowledge):
    with open('knowledges.json', 'w') as file:
        json.dump(knowledge, file, indent=4)

# FUNCTION CHECK SIMILARITY BETWEEN 2 STRINGS
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# FUNCTION CHATBOT
def chatbot():
    # Initiation function load_knowledge() to knowledge variable
    knowledge = load_knowledge()
    
    # Print first chat if function chatbot first running 
    print("Chatbot: Hi! How can I help you?")
    
    # Loop 
    while True:
        # Initiation for user input
        user_input = input("You: ").lower()

        # Initiation found is false for check input from JSON
        found = False

        # Get from JSON qa
        for qa in knowledge.get("qa", []):
            # Initiation function similar add parameter user input & question from JSON
            similarity = similar(user_input, qa["question"])
            
            # Condition if simliar >= 60%
            if similarity >= 0.60:
                # Print answer from JSON not add new answer
                print(f"Chatbot: {qa['answer']}")
                # found answer from JSON
                found = True
                break

        # Condition if answer not found from JSON
        if not found:
            # print text chatbot
            print("Chatbot: Sorry, I don't know the answer to that.")
            # Initiation for get input option from user to add new answer or not
            add_question = input("Would you like to add this question and provide an answer? (yes/no): ").lower()

            # Condition if user input "yes"
            if add_question == "yes":
                # Initiation for get user input new answer
                answer = input("Please provide the correct answer: ")
                # Initiation for get new question and answer from user input
                new_qa = {"question": user_input, "answer": answer}
                # Add this new question and answer to JSON qa
                knowledge["qa"].append(new_qa)
                # Call function save_knowledge
                save_knowledge(knowledge)
                # Print text chatbot
                print("Chatbot: Thank you! I've saved the question and answer.")

# MAIN
if __name__ == "__main__":
    # Call function chatbot()
    chatbot()