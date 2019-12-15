from pos_tag_dict import pos_tag_dict
import re
import unicodedata as ud

class PosTag():
    def __init__(self,word_list):
        self.word_list = word_list
        self.dict = pos_tag_dict
    
    def tagging(self):
        res = dict()
        for word in self.word_list:
            if word.lower() in self.dict.keys():
                res[word] = self.dict[word.lower()]
            elif re.search("(\d+(:\d+)+HR)", ud.normalize("NFC",word), re.UNICODE):
                res[word] = "Time"
            else:
                res[word] = "None"
        return res

def test(word_list):
    postag = PosTag(word_list)
    pos_tag_res = postag.tagging()
    print(pos_tag_res)

if __name__ == "__main__":
    import sentence_test
    for x in sentence_test.expect_output:
        test(x)