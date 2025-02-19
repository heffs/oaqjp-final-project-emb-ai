"""This module contains the server code for a web application that 
allows users to enter text to be analysed for emotion.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Responds to GET requests with the following parameters:

    - textToAnalyze: a string to be analyzed for emotion

    Returns a string containing the emotions detected in the given text and
    the dominant emotion if the text is valid for analysis. If the text is
    invalid, returns "Invalid text! Please try again."
    """
    prompt = request.args.get("textToAnalyze")
    response = emotion_detector(prompt)

    emotions = list(response.keys())

    display = ""
    if response["dominant_emotion"] is None:
        display = "Invalid text! Please try again."
    else:
        display = "For the given statement, the system response is "
        for ix, emotion in enumerate(emotions):
            if emotion == "dominant_emotion":
                display = display + f". The dominant emotion is {response[emotion]}."
            else:
                if ix == len(emotions) - 2:
                    display = display + f" and {emotion}: {response[emotion]}"
                elif ix == 0:
                    display = display + f" {emotion}: {response[emotion]}"
                else:
                    display = display + f", {emotion}: {response[emotion]}"
    return display

@app.route("/")
def index_route():
    """Display the home page, which is an HTML template that allows 
    the user to enter text to be analyzed for emotion.
    """
    return render_template('index.html')
