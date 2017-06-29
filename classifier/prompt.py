
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

GENERIC_PROMPT = (
    ('M', 'Movie'),
    ('T', 'tv show'),
    ('O', 'Other'),
    ('S', 'Skip'),
    ('X', 'Exit')
)

YES_NO_PROMPT = (
    ('Y', 'Yes'),
    ('N', 'No')
)

def genericPrompt (item : str, classes):
    """Takes a filename as well as a tuple of keypresses to filenames
    e.g "Do you love python?", ( ('Y', 'Yes'), ('N', 'No'))
    would generate a prompt like
        What is 'Do you love python' ?
        [Y]es, [N]o >>>
    @Return Always returns the upper of the key pressed.
    """

    keys = [key.upper() for key,_ in classes]
    while True:
        print  ("What is {1}'{0}'{2} ?".format(item, color.BOLD, color.END))
        userInput = input (createQuestionClasses (classes))
        if userInput.upper() in keys:
            return userInput.upper()



def yesNoPrompt (message):
    print (message)
    keys = [key for key,_ in YES_NO_PROMPT]

    while True:
        userInput = input (createQuestionClasses (YES_NO_PROMPT))
        if userInput.upper() in keys:
            return userInput.upper()


def createQuestionClasses (classes) -> str:
    """Very crude function for making prompts such as
        [Y]es, [No], e[X]it >>>
    """

    prompt = ""
    import re
    for key,fullname in classes:
        key = key.upper()
        if (key in fullname.upper()):
            replaceKey = re.compile ( re.escape(key), re.IGNORECASE)
            entry = replaceKey.sub ("[{1}{0}{2}]".format(key, color.BOLD, color.END), fullname, count=1)
        else:
            entry = "[{0}]{1}".format (key, fullname)

        if (prompt == ""):
            prompt += entry
        else:
            prompt += ", " + entry

    return prompt + " >>> "



def selectPrompt (options) -> str:
    """Given a list of stuff such as ["apple", "banana", "cherry"]
    Generates a prompt
        Please select
        [0] - apple
        [1] - banana
        [2] - cherry
        >>>
    @Return the value inside the list, e.g apple.
    """

    while True:
        for index, item in enumerate (options):
            print ("[{0}] {1}".format (index, item))
        userInput = input (">>> ")
        try:
            n = int (userInput)
            return options[n]
        except:
            continue
