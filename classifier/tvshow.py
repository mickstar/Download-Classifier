import filesystem.directory as directory
from classifier.classifier import Classifier
class TvShowClassifier (Classifier):
    def __init__ (self):
        self.tvshows = directory.getTVShowNames()
        self.tokens = self.createTokens()

    def calculateTVShowScore (self, item, verbose=False):
        if verbose: print ("Classifying " + item)

        item = item.name.upper()
        scores = list (map (lambda tvshow : (tvshow, self.calculateSimilarity(item, self.tokens[tvshow])), self.tokens.keys()))

        if verbose:
            for (tvshow, score) in scores:
                print ("%.2f %% - %s : %s" %(score*100, tvshow, self.tokens[tvshow]) )

        bestShow, bestScore = max (scores, key = lambda ab : ab[1] )
        if verbose: print ("best is {0} with a score of {1}".format(bestShow, bestScore) )
        return (bestShow, bestScore)

    def createTokens  (self):
        tokens = {}
        for tvshow in self.tvshows:
            tokens [tvshow] = (tvshow.upper()
                                .replace(".", " ")
                                .replace("-", " ")
                                .split (" "))

            # Check to see if tvshow name is smaller than token size
            if len (tokens[tvshow]) == 0:
                tokens[tvshow].append (tvshow)

        return tokens
