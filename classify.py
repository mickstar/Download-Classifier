import filesystem.directory as directory
from filesystem.ignored import Ignored
from classifier.main import Classifier
#import classifier.classifier as classifier
from filesystem.item import Item
ignoredDB = Ignored(filename = ".ignored.txt")

def listOfFilesToClassify():
    """Returns a list of files in the current directory to classify"""

    files = directory.listDirectory(path=".", showHidden=False)

    return filter (lambda file : not ignoredDB.isIgnored(file), files)

def main ():
    classifier = Classifier (ignoredDB)
    toClassify = listOfFilesToClassify()
    for filename in toClassify:
        classifier.classify(Item(filename))

if __name__ == '__main__':
    main()
