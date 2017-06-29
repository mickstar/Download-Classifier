import classifier.tokens as tokens
from classifier.classifier import Classifier
class MovieClassifier (Classifier):
    def __init__(self):
        pass

    def calculateMovieScore (self, item):
        score = self.calculateSimilarity (item.name.upper(), tokens.movieTokens)
        return (item, score)
