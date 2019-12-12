import ast

def loadDict(path):
    with open(path, encoding="utf8") as fr:
        words = fr.read()
        words = ast.literal_eval(words)
    return words

