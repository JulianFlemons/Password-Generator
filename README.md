# Simple Python Chatbot

## Project Overview
This project is a **basic rule-based chatbot** built using Python. It simulates a simple conversation by matching user inputs to pre-defined responses stored in a dictionary. If the chatbot recognizes the user's message, it responds accordingly; if not, it prompts the user for clarification. The conversation continues in a loop until the user says "bye."

## Features
- Dictionary of pre-defined user inputs and chatbot responses
- A `get_response` function to map user input to responses
- A `chatbot` function that:
  - Welcomes the user
  - Takes continuous input in a loop
  - Ends the conversation politely when the user types "bye"

## Technologies Used
- **Programming Language**: Python 3

## How It Works
1. **User Input**: The user types a message.
2. **Response Lookup**: The program checks if the input exists in the predefined dictionary:
   - If found, it returns the corresponding response.
   - If not found, it replies: `"I'm sorry, what'd you say?"`
3. **Exit Condition**: If the user types `"bye"`, the chatbot ends the conversation with a farewell message.

## Sample Interaction
