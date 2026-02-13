from flask import Flask, render_template, request, jsonify 
import requests

app = Flask(__name__)

#API Configuration:

API_KEY = ""
API_URL = ""
MODEL = "google/gemini-pro"

#keyword List:
greeting_key = ["hii", "hello", "hey"]
help_key = ["help", "support", "assist"]
bug_key = ["bug status", "check bug", "bug update"]

'''#Responses:

def handle_greeting(user_input):
    greetings = ["hi", "hello", "hey"]
    return any(word in user_input for word in greetings)

def handle_help(user_input):
    help = ["help", "support", "assist"]
    return any(word in user_input for word in help)

def handle_bug(user_input):
    bug = ["bug status", "check bug", "bug update"]
    return any(word in user_input for word in bug)'''

#API Functions:

def get_ai_response(user_message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type" : "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except:
        return "Sorry, I am unable to connect to AI service right now."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"].lower().strip()

    # greeting:
    if user_input in greeting_key:
        reply = "Hey There! How can I assist you Today?"
    
    elif user_input in help_key:
        reply = ("I can help you with the following:\n"
              "-> Greetings\n"
              "-> Check Bug Status\n"
              "-> General Questions using AI\n"
              "Just type your query!")
    
    elif user_input in bug_key:
        reply = ("Bug #1024 Status:\n"
              "Status: In Progress\n"
              "Assigned to: Development Team\n"
              "Expected Fix: 2 days")
        
    else:
        reply =  get_ai_response(user_input)
    
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
        

    