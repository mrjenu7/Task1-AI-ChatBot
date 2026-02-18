from flask import Flask, render_template, request, jsonify 
import requests


app = Flask(__name__)

#API Configuration:
api_key=""
API_URL = ""
MODEL = "openai/gpt-4o-mini"

users = {
    "Alex": [],
    "Max": [],
    "Lily": []
}

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
        "Authorization": f"Bearer {api_key}",
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

# -------- Routes -------- #
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data:
        return jsonify({"response": "Invalid request"}), 400

    user_name = data.get("user")
    message = data.get("message")

    if not user_name or not message:
        return jsonify({"response": "Missing user or message"}), 400

    if "@ai" in message.lower():

        clean_message = message.replace("@AI", "").replace("@ai", "").strip()

        reply = get_ai_response(clean_message)

        return jsonify({"response": reply})

    return jsonify({"response": None})

'''def chat():
    data = request.get_json()
    print("Incoming Data:", data)

    if not data:
        return jsonify({"response": "Invalid request"}), 400

    user_name = data.get("user")
    message = data.get("message")

    if not user_name or not message:
        return jsonify({"response": "Missing user or message"}), 400

    # Check if message contains @AI
    if "@ai" in message.lower():

        # Remove @AI from message before sending to model
        clean_message = message.lower().replace("@ai", "").strip()

        try:
            response = api_key.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": clean_message}
                ]
            )

            reply = response.choices[0].message.content

            return jsonify({"response": reply})

        except Exception as e:
            return jsonify({"response": f"Error: {str(e)}"}), 500

    else:
        # If no @AI → just return message without AI reply
        return jsonify({"response": None})'''


'''def chat():
    data = request.get_json()
    print("Incoming Data:", data)

    if not data:
        return jsonify({"response": "Invalid request"}), 400

    user_name = data.get("user")
    message = data.get("message")

    if not user_name or not message:
        return jsonify({"response": "Missing user or message"}), 400

    # Trigger check
    if "@ai" not in message.lower():
        return jsonify({"response": None})  # MUST return something

    # Remove trigger
    clean_message = message.lower().replace("@ai", "").strip()

    # Rule-based responses
    if clean_message in greeting_key:
        reply = "Hello! 👋 How can I assist you?"
    elif clean_message in help_key:
        reply = "I can help with greetings, bug updates, and AI queries."
    elif clean_message in bug_key:
        reply = "🐞 Bug Report #2026\nStatus: In Progress\nEstimated Fix: 48 hours"
    else:
        reply = get_ai_response(clean_message)

    return jsonify({"response": reply})  # FINAL RETURN
'''

'''@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_name = data["user"]
    message = data["message"]

    # store user message:
    users[user_name].append({"sender": "user", "text": message})

    #trigger check:
    if "@AI" not in message.lower():
        return jsonify({"response": None})
    
    #remove trigger:
    clean_message = message.lower().replace("@AI", "").strip()

    if clean_message in greeting_key:
        reply = "Hellp ! How can I assist You?"
    
    elif clean_message in help_key:
        reply = "I can help with greetings, bug updates, and AI queries."
    
    elif clean_message in bug_key:
        reply = ("🐞 Bug Report #2026\n"
                 "Status: In Progress\n"
                 "Estimated Fix: 48 hours")
    
    else:
        reply = get_ai_response(clean_message)
    

    users[user_name].append({"sender": "bot", "text": reply})

    return jsonify({"response": reply})'''

if __name__ == "__main__":
    app.run(debug=True)
        

    