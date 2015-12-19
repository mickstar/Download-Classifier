import filesystem.directory
from filesystem.ignored import Ignored
from classifier.tvshow import TvShowClassifier
from classifier.movie import MovieClassifier
import classifier.prompt as prompt
#import classifier.movie as movie

class Classifier:
    THRESHOLD = 0.1

    def __init__ (self, ignoredDatabase):
        self.tvShowClassifier = TvShowClassifier()
        self.movieClassifier = MovieClassifier()
        assert (isinstance (ignoredDatabase, Ignored))
        self.ignoredDatabase = ignoredDatabase

    def classify(self, item):
        (tvshow, tvScore) = self.tvShowClassifier.calculateTVShowScore (item)
        (_, movieScore) = self.movieClassifier.calculateMovieScore (item)

        if (max(tvScore, movieScore) < Classifier.THRESHOLD):
            return self.classifyFromUserInput(item)

        if tvScore > movieScore:
            response = prompt.yesNoPrompt(
                "Is %s'%s'%s %s? (%.2f)"
                %(
                    prompt.color.BOLD,
                    item,
                    prompt.color.END,
                    tvshow,
                    tvScore
                )
            )
            if (response == 'Y'):
                return self.classifyAsTVShow(item, tvshow)
            else:
                return self.classifyFromUserInput(item)
        else:
            print ("Classified as a Movie")
            response = prompt.yesNoPrompt(
                "Is %s'%s'%s a Movie? (%.2f)"
                %(
                    prompt.color.BOLD,
                    item,
                    prompt.color.END,
                    movieScore
                )
            )
            if (response == 'Y'):
                return self.classifyAsMovie(item)
            else:
                return self.classifyFromUserInput(item)


    def classifyAsMovie (self, item):
        filesystem.directory.move (item, "/media/HDD/Movies")
    def classifyAsTVShow (self, item, tvshow):
        filesystem.directory.move (item, "/media/HDD/TV/{0}".format(tvshow))

    def ignoreItem (self, item):
        self.ignoredDatabase.addIgnored (item)

    def classifyFromUserInput(self, item):
        response = prompt.genericPrompt(item, prompt.GENERIC_PROMPT)
        if (response == 'X'):
            import sys
            sys.exit()
        elif response == 'S':
            return
        elif response == 'M':
            self.classifyAsMovie(item)
        elif response == 'O':
            self.ignoreItem(item)
        elif response == 'T':
            import filesystem.directory
            shows = filesystem.directory.getTVShowNames()
            index = prompt.selectPrompt(shows)
            self.classifyAsTVShow (shows[index], item)
        else:
            raise Exception ("Uncatched response code " + response)
