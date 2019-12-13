import re
import unicodedata as ud
from utils import loadDict 



class Basetokenizer(object):
    def tokenize(self,text):
        """
        Convert a sentence to an array of words
        param text: input sentence
        return: array of words
        """
        pass 

    @staticmethod
    def syllablize(text):
        """
        Split a sentences into an array of syllables
        param text: input sentence
        return: list of syllables
        """

        text = ud.normalize('NFC',text)
        sign = ["==>", "->", "\.\.\.", ">>"]
        digits = "\d+([\.,_]\d+)+"
        special = "\d+(:\d+)+HR"
        email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        web = "^(http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
        datetime = [
            "\d{1,2}\/\d{1,2}(\/\d+)?",
            "\d{1,2}-\d{1,2}(-\d+)?",
        ]
        word = "\w+"
        non_word = "[^\w\s]"
        abbreviations = [
            "[A-ZĐ]+\.",
            "Tp\.",
            "Mr\.", "Mrs\.", "Ms\.",
            "Dr\.", "ThS\."
        ]
        patterns = []
        patterns.extend(abbreviations)
        patterns.extend(sign)
        patterns.extend([special,web, email])
        patterns.extend(datetime)
        patterns.extend([digits, non_word, word])
        patterns = "(" + "|".join(patterns) + ")"
        tokens = re.findall(patterns, text, re.UNICODE)
        return [token[0] for token in tokens]

class Tokenizer(Basetokenizer):
    def __init__(self,complex_words = 'complexwords.txt',complex_words_special = 'complexwordsspec.txt'):
        self.complexWords = list(loadDict(complex_words)) + list(loadDict(complex_words_special))

    def tokenize(self,text):
        """
        Convert a sentence to an array of words
        param text: input sentence
        return: array of words
        """
        print(text)
        syllables = Tokenizer.syllablize(text)
        print(syllables)
        syl_size = len(syllables)
        index = 0
        done = False
        res = list()

        while (index < syl_size and not done):
            curr_word = syllables[index]
            if index == syl_size - 1:#push last single word
                res.append(curr_word)
                done = True
            else:
                next_word = syllables[index + 1]
                complex2words = ' '.join([curr_word.lower(), next_word.lower()])
                if index < syl_size - 2:
                    next_word2nd = syllables[index + 2]
                    complex3words = ' '.join([complex2words,next_word2nd.lower()])
                    if complex3words in self.complexWords:
                        res.append(' '.join([curr_word,next_word,next_word2nd]))
                        index += 3
                        break
                if complex2words in self.complexWords:
                    res.append(' '.join([curr_word, next_word]))
                    index += 2
                else:
                    res.append(curr_word)
                    index += 1
        return res
    
    def busTokenize(self,syllables):
        """
        segment sentence according bus db 
        param syllables (output of tokenize)
        return new list of syllables
        """
        print(syllables)
        special_word = ['thành phố','xe bus', 'xe buýt', 'xe khách', 'xe']
        bus_id = ['b1','b2','b3','b4']
        city_name = ['hồ chí minh', 'đà nẵng', 'huế', 'hà nội']
        index = 0
        while (index < len(syllables) - 1):
            curr_word = syllables[index].lower()
            if curr_word in special_word:
                next_word = syllables[index + 1].lower()
                if curr_word != special_word[0]:
                    print(curr_word + ' ' + next_word)
                    if next_word in bus_id or re.match('\d+',next_word):
                        print(syllables[index:(index+1)])
                        syllables[index:(index+2)] = [syllables[index] + ' ' + syllables[index+1]]
                else:
                    if next_word in city_name:
                        syllables[index:(index+2)] = [syllables[index] + ' ' + syllables[index+1]]
            index += 1
        return syllables
            
toknenize_obj = Tokenizer()
sentence = 'Thời gian xe bus B3 từ Đà Nẵng đến Huế'
token = toknenize_obj.tokenize(sentence)
segmented = toknenize_obj.busTokenize(token)
print(segmented)