class Classifier :
    def __init__(self):
        pass

    def calculateSimilarity (self, item, tokens):
        itemTokens = set(item.upper()
                            .replace(".", " ")
                            .replace("-", " ")
                            .split (" "))

        for genericToken in ["OF", "THE", "IS"]:
            if genericToken in itemTokens:
                itemTokens.remove(genericToken)

        nTokens = len (tokens)
        if (nTokens == 0):
            print ("error no tokens bro!", item)
            return 0
        #tokensInItem = map (lambda token : token in item, tokens)
        intersection = len (itemTokens.intersection(tokens))
        union = len (itemTokens) + len (tokens) - intersection
        return (float (intersection) / union )
        #return float (sum (tokensInItem)) / nTokens
