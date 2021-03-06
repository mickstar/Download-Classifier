import classifier.tokens as tokens
import re
from classifier.classifier import Classifier

bookExtensions = [".pdf",".epub", ".mobi"];

SCORE_IS_BOOK = 1
SCORE_IS_NOT_BOOK = 0
class BookClassifier (Classifier):
    def __init__(self):
        pass

    def calculateSimilarity (self, item):
        score = SCORE_IS_NOT_BOOK
        if item.isFile:
            if item.filetype in bookExtensions:
                score = SCORE_IS_BOOK

        else:
            if len (intersection(bookExtensions, item.filetypes)) > 0:
                score = SCORE_IS_BOOK
        return score


def intersection (a, b):
    return list(set(a) & set(b))
