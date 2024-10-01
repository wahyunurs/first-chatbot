# first-chatbot

This project is a simple chatbot that runs in the terminal. The chatbot can answer user questions based on knowledge stored in a JSON file. If the chatbot doesn't know the answer to a question, the user can add new questions and answers, and the knowledge will be saved for future interactions.

INSTALLATION

1. Clone the repository:
   git clone https://github.com/username/chatbot-terminal.git
   cd chatbot-terminal
2. System Requirements:
   Python 3.x
   The json and difflib Python modules (both come pre-installed with Python)
3. Run the Program:
   python main.py

HOW TO USE
Start the Chatbot: When run, the chatbot will greet the user and wait for input.
Ask Questions: The user can type a question, and the chatbot will look for the most similar question in its knowledges.json file.
Add New Questions: If the chatbot doesn't find a match, the user can add the question and answer through the terminal. The new knowledge will be saved for future use.
