"""This is a emotion detection app with error handling and 
NLP capabilities
"""

from flask import Flask,request,render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """function renders index html from static folder
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotionDetector(): # pylint: disable=invalid-name
    """function does the text emotion analysis
    """
    textToAnalyze = request.args.get("textToAnalyze") # pylint: disable=invalid-name
    if not textToAnalyze:
        return "Invalid text! Please try again!."
        """return (f"For the given statement, the system response is "
        f"'anger': {None}, "
        f"'disgust': {None}, "
        f"'fear': {None}, "
        f"'joy': {None} and "
        f"'sadness': {None}. "
        f"The dominant emotion is <b>{None}</b>.")"""

    result = emotion_detector(textToAnalyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return (f"For the given statement, the system response is "
    f"'anger': {result['anger']}, "
    f"'disgust': {result['disgust']}, "
    f"'fear': {result['fear']}, "
    f"'joy': {result['joy']} and "
    f"'sadness': {result['sadness']}. "
    f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )

if  __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
