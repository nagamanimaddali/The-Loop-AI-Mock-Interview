from flask import Flask, request, jsonify
from flask_cors import CORS
from gemini import generate_question, generate_next_question, generate_report

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "The Loop Backend is Running!"


@app.route("/startInterview", methods=["POST"])
def start_interview():

    try:
        data = request.get_json()

        topic = data["topic"]
        difficulty = data["difficulty"]
        style = data["style"]
        questions = data["questions"]

        question = generate_question(topic, difficulty, style)

        return jsonify({
            "message": "Interview Started Successfully!",
            "question": question,
            "topic": topic,
            "difficulty": difficulty,
            "style": style,
            "questions": questions
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500
    
@app.route("/nextQuestion", methods=["POST"])
def next_question():

    try:
        data = request.get_json()

        previous_question = data["question"]
        user_answer = data["answer"]

        next_question = generate_next_question(
            previous_question,
            user_answer
        )

        return jsonify({
            "question": next_question
        })

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


@app.route("/generateReport", methods=["POST"])
def report():

    try:
        data = request.get_json()

        history = data["history"]

        report = generate_report(history)

        return jsonify(report)

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)