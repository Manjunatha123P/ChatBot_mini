from flask import Flask, render_template, request, jsonify,redirect,url_for, request,send_file, url_for,send_from_directory
import re
import long_responses as long
app = Flask(__name__, static_url_path='/static')


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello! How can I assist you today?', ['hello', 'hey', 'sup', 'heyo','hi','hii'], single_response=True)
    response('sorry for inconvenience im still in developing stage', ['why'], single_response=True)
    response('Dear user i dont know about you!,and to say that i cant remember your name', ['my'],required_words=['my'], single_response=True)
    response('sorry for incoinvenice', ['understand'], single_response=True)
    response('Hey! Im here to assist you', ['hey'], single_response=True)
    response('im an virtual machine, i dont need to eat', ['eat','Eat'], single_response=True)
    response('Hi! Whats on your mind?', ['How it going'],required_words=['going'],single_response=True)
    response('Sorry about that! Can you please rephrase or provide more context?', ['understand'], single_response=True)
    response('im an chatbot created by jpnce students', ['who','you','name'], single_response=True)
    response('i dont know', ['know'], single_response=True)
    response('Goodbye! If you need anything in the future, feel free to reach out. Have a great day!', ['bye', 'goodbye','seeyou'], single_response=True)
    response('I\'m doing fine, and you?', ['doing','how'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Im doing well, thanks for asking!', ['who'], single_response=True)
    response('Thank you!', ['good','appreciate','welldone'])
    response('I love you too', ['i', 'love', 'you'], required_words=['love'])
    response('I understand that you might be feeling frustrated or upset, but Im a bot i dont care about human emotions', ['hate'], required_words=['hate'])
    response('Today is a nice day', ['nice', 'weather'], required_words=['weather'])
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_HELP, ['help', 'assist',], required_words=['need','help'])
    response(long.R_JOKE, ['joke','laugh'])
    response(long.R_GENDER, ['gender', 'male', 'female'], required_words=['gender'])
    response(long.R_JPNCE, ['jpnc','jpnce','JPNCE','Jpnce','Jpnc'])
    response('<a href="/cse2-2">Click here for cse syllabus</a>', ['cse','CSE'] , single_response=True)
    response('<a href="/OS">Click here for OS notes</a>', ['OS','os'], single_response=True)
    response('<a href="/SE">Click here for SE NOTES</a>', ['software engineering','SE'],required_words=['notes'], single_response=True)
    response('<a href="/BEFA">Click here for BEFA NOTES</a>', ['BEFA','befa'],required_words=['notes'], single_response=True)
    response('<a href="/DBMS">Click here for DBMS NOTES</a>', ['DBMS','dbms'], single_response=True)
    response('<a href="/DM">Click here for DM NOTES</a>', ['dm','DM','Dm'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return best_match if highest_prob_list[best_match] > 0 else long.unknown() # Default to help if no match

def get_response(user_input):
    split_message = re.findall(r'\b\w+\b', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Global variable to hold the condition
condition_flag = False

# Define the route for the home page (/) and (/welcome)
@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

# Define a route to handle the button click and set the condition
@app.route("/set_condition", methods=["POST"])
def set_condition():
    global condition_flag
    if request.form.get("condition") == "true":
        condition_flag = True
    else:
        condition_flag = False
    return redirect(url_for("handle_condition"))

# Define a route to handle the condition and perform redirection
@app.route("/handle_condition")
def handle_condition():
    global condition_flag
    if condition_flag:
        return redirect(url_for("index"))  # Redirect to /index route
    else:
        return redirect(url_for("welcome"))  # Redirect back to /welcome route if condition is false

# Define the route for the index page (/index)
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/OS")
def oslab():
    return render_template("OS.html")


@app.route("/SE")
def SE():
    return render_template("SE.html")

@app.route("/DM")
def DM():
    return render_template("DM.html")

@app.route("/DBMS")
def DBMS():
    return render_template("DBMS.html")

@app.route("/BEFA")
def BEFA():
    return render_template("BEFA.html")

@app.route("/cse2-2")
def cse2():
    return render_template("cse2-2.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return jsonify({"response": get_response(user_text)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
