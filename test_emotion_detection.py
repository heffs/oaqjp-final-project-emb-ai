import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        prompts = [
            "I am glad this happened",
            "I am really mad about this",
            "I feel disgusted just hearing about this",
            "I am so sad about this",
            "I am really afraid that this will happen"
        ]
        expected = [
            "joy", "anger", "disgust", "sadness", "fear"
        ]

        for ix, prompt in enumerate(prompts):
            self.assertEqual(emotion_detector(prompt), expected[ix])

unittest.main()
