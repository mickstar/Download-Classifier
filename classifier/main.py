import filesystem.directory
from filesystem.ignored import Ignored
from classifier.tvshow import TvShowClassifier
from classifier.movie import MovieClassifier
from classifier.book import BookClassifier
from sys import exit
import classifier.prompt as prompt
#import classifier.movie as movie

class Classifier:
    def __init__ (self, ignoredDatabase):
        self.tvShowClassifier = TvShowClassifier()
        self.movieClassifier = MovieClassifier()
        self.bookClassifier = BookClassifier()
        assert (isinstance (ignoredDatabase, Ignored))
        self.ignoredDatabase = ignoredDatabase

    def classify(self, item):
        bookScore = self.bookClassifier.calculateSimilarity(item)
        if bookScore == 1:
            response = prompt.yesNoPrompt("Is {name} a Book?".format(name=item.name))
            if response == "Y":
                self.classifyAsBook(item)

        else:
            return self.classifyFromUserInput(item)


    def classifyAsMovie (self, item):
        filesystem.directory.move (item.name, "/media/HDD/Movies")
    def classifyAsTVShow (self, item, tvshow):
        filesystem.directory.move (item.name, "/media/HDD/TV/{0}".format(tvshow))

    def classifyAsBook (self, item):
        filesystem.directory.move (item.name, "/media/HDD/Books")

    def ignoreItem (self, item):
        self.ignoredDatabase.addIgnored (item.name)

    def classifyFromUserInput(self, item):
        response = prompt.genericPrompt(item.name, prompt.GENERIC_PROMPT)
        if (response == 'X'):
            exit()
        elif response == 'S':
            return
        elif response == 'M':
            self.classifyAsMovie(item)
        elif response == 'O':
            self.ignoreItem(item)
        elif response == 'T':
            (tvshow, tvScore) = self.tvShowClassifier.calculateTVShowScore (item)
            response = prompt.yesNoPrompt(
                "Is %s'%s'%s %s? (%.2f)"
                %(
                    prompt.color.BOLD,
                    item.name,
                    prompt.color.END,
                    tvshow,
                    tvScore
                )
            )
            if response == "Y":
                    self.classifyAsTVShow(item, tvshow)
            else:
                import filesystem.directory
                shows = filesystem.directory.getTVShowNames()
                show = prompt.selectPrompt(shows)
                self.classifyAsTVShow (item, show)
        else:
            raise Exception ("Uncatched response code " + response)
