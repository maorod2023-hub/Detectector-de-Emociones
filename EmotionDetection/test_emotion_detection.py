import unittest

from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detection(self):

        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["Dominant"], "joy")

        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2["Dominant"], "anger")

        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3["Dominant"], "disgust")

        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4["Dominant"], "sadness")

        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5["Dominant"], "fear")


if __name__ == "__main__":
    unittest.main()