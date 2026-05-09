from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_cal():

    text_to_evaluate = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_evaluate)

    return result


if __name__ == '__main__':
    app.run(debug=True)