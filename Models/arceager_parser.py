from queue import LifoQueue
class ArcEagerParser():
    def __init__(self,word_list):
        self.stack = ['root']
        self.buffer = self.preProcess(word_list)
        self.relation = list()
        self.word_list = word_list


    def preProcess(self,word_list):
        res = list()
        for x in word_list:
            if x[1] != 'None':
                res += [x]
        return res[::-1]


    def checkRule(self,out,inp):
        rule = ""
        isValid = False
        if out == 'root':
            if inp[1] == 'V':
                rule = 'ROOT'
        if out[1] == 'V':
            if inp[1] == "N_sub":
                rule = 'nsubj'
            elif inp[1] == 'Name':
                rule = 'dobj'
            elif inp[1] == 'WH_time' or inp[1] == 'Time':
                rule = 'nmod'
        elif out[1] == 'N_sub':
            if inp[1] == 'Name':
                rule = 'nmod'
            elif inp[1] == 'Name_bus' or inp[1] == 'WH':
                rule = 'amod'
        elif out[1] == 'Name':
            if inp[1] == 'P':
                rule = 'case'
        if rule:
            isValid = True
        return isValid, rule

    def leftArc(self):
        if self.buffer:
            if self.stack[-1][0] not in [x[2] for x in self.relation] and self.stack[-1] != 'root':#leftarc
                isValid,rule = self.checkRule(self.buffer[-1],self.stack[-1])
                if rule == 'dobj':
                    return False
                if isValid:
                    if rule == 'nsubj':
                        order1 = -1
                        order2 = self.word_list.index(self.stack[-1])
                    elif self.buffer[-1] != 'root':
                        order1 = self.word_list.index(self.buffer[-1])
                        order2 = self.word_list.index(self.stack[-1])                        
                    else:
                        order1 = -2
                        order2 = self.word_list.index(self.stack[-1])
                    self.relation += [(rule,self.buffer[-1],self.stack.pop(),order1,order2)]
                    print('leftarc')
                    return True
        return False
    
    def rightArc(self):
        if self.buffer:
            if self.buffer[-1][0] not in [x[2] for x in self.relation]:#rightarc
                isValid,rule = self.checkRule(self.stack[-1],self.buffer[-1])   
                if isValid:
                    print('rightarc')
                    wi = self.stack[-1]
                    wj = self.buffer.pop()
                    if rule == "nsubj":
                        order1 = -1
                        order2 = self.word_list.index(wj)                    
                    elif wi != 'root':
                        order1 = self.word_list.index(wi)
                        order2 = self.word_list.index(wj)
                    else:
                        order1 = -2
                        order2 = self.word_list.index(wj)
                    self.relation += [(rule,wi,wj,order1,order2)]
                    self.stack.append(wj)
                    return True
        return False

    def Reduce(self):
        if self.stack[-1] in [x[2] for x in self.relation] and self.stack[-1] != 'root':#reduce
            print('reduce')
            self.stack.pop()
            return True
        return False

    def Shift(self):
        print('shift')
        self.stack.append(self.buffer.pop()) 

    def parsing(self):
        print(self.buffer)
        while (self.buffer or len(self.stack) > 1):
            print("-----------------------------------")
            print(self.stack)
            print(self.buffer)
            print(self.relation)
            print("-----------------------------------")
            if self.leftArc():
                continue
            elif self.rightArc():
                continue
            elif self.Reduce():
                continue
            else:
                self.Shift()
        idx = None
        for x in self.relation:
            if x[0] == 'dobj':
                check = x[2]
        print(check)
        for y in self.relation:
            if y[0] == 'nmod' and y[2] == check:
                idx = self.relation.index(y) 
    
        if idx:
            del self.relation[idx]
        #convert to tree
        self.relation.sort(key = lambda x: (x[3],x[4]))

            
        


def test():
    import tokenlizer 
    import pos_tagging
    sentence1 = "Xe bus nào đến thành phố Huế lúc 20:00HR?"
    sentence2 = "Thời gian xe bus B3 từ Đà Nẵng đến Huế?"
    sentence3 = "Xe bus nào đến thành phố Hồ Chí Minh ?"
    toknenize_obj = tokenlizer.Tokenizer()
    token = toknenize_obj.tokenize(sentence1)
    word_list = toknenize_obj.finalTokenize(token)
    postag = pos_tagging.PosTag(word_list)
    pos_tag_res = postag.tagging()
 
    dependency_gram = ArcEagerParser(pos_tag_res)

    #print(dependency_gram.stack[-1])
    dependency_gram.parsing()

    print(dependency_gram.relation)

if __name__ == "__main__":
    test()