"""Emotion detection module using Watson NLP API.

This module provides functionality to analyze emotions in text using IBM Watson's NLP service.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def analyze_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if not result or result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 200

    response = {
        "anger": result.get('anger', 0),
        "disgust": result.get('disgust', 0),
        "fear": result.get('fear', 0),
        "joy": result.get('joy', 0),
        "sadness": result.get('sadness', 0),
        "dominant_emotion": result.get('dominant_emotion', 'unknown')
    }
    formatted_response = (
        f"For a given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']},  "
        f"'sadness': {response['sadness']}。"
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return jsonify({
        "raw_response": response,
        "formatted_response": formatted_response
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)