"""
This class remembers whether a given item has been previously ignored such that we should no longer attempt to query it.
"""

class Ignored ():
    def __init__(self, filename = "ignored.txt"):
        import os
        if (not os.path.isfile(filename)):
            #create empty file if not exists.
            open (filename, "a").close()

        self.filename = filename
        file = open (filename, "r", encoding='utf-8')
        self.ignoredFiles = set([])
        for item in file:
            self.ignoredFiles.add(item.replace('\n', ''))
        file.close()

    def isIgnored (self, item):
        return item in self.ignoredFiles

    def addIgnored (self, item):
        file = open (self.filename, "ab")
        file.write (item.encode("utf-8") + b"\n")
        file.close()
