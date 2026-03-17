"""Flask server for emotion detection API."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion():
    """Takes a message and returns the message"""
    result = request.args.get("textToAnalyze")
    analysis = emotion_detector(result)
    if analysis['dominant_emotion'] is not None:
        return (
            f"For the given statement, the system response is "
            f"'anger': {analysis['anger']}, "
            f"'disgust': {analysis['disgust']}, "
            f"'fear': {analysis['fear']}, "
            f"'joy': {analysis['joy']}, "
            f"'sadness': {analysis['sadness']}. "
            f"The dominant emotion is {analysis['dominant_emotion']}."
        )
    return "Invalid text! Please try again!"
@app.route("/")
def render_index_page():
    """This gives the user the base website"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
