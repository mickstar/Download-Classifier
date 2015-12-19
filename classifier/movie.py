import classifier.movieTokenData as movieTokenData
from classifier.classifier import Classifier
class MovieClassifier (Classifier):
    def __init__(self):
        self.movieTokens = movieTokenData.movieTokens

    def calculateMovieScore (self, item):
        score = self.calculateSimilarity (item.upper(), self.movieTokens)
        return (item, score)
