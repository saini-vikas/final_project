import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad this happened")
        result2 = emotion_detector("I am really mad about this")
        result3 = emotion_detector("I feel disgusted just hearing about this")
        result4 = emotion_detector("I am so sad about this")
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result1["dominant_emotion"], "joy")
        self.assertEqual(result2["dominant_emotion"], "anger")
        self.assertEqual(result3["dominant_emotion"], "disgust")
        self.assertEqual(result4["dominant_emotion"], "sadness")
        self.assertEqual(result5["dominant_emotion"], "fear")
        
unittest.main()