from queue import LifoQueue
class ArcEagerParser():
    def __init__(self,word_list):
        self.stack = ['root']
        self.buffer = self.preProcess(word_list)
        self.relation = list()


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
            elif inp[1] == 'WH_time':
                rule = 'nmod'
        elif out[1] == 'N_sub':
            if inp[1] == 'Name':
                rule = 'nmod'
            elif inp[1] == 'Name_bus':
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
                if isValid:
                    self.relation += [(rule,self.buffer[-1],self.stack.pop())]
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
                    self.relation += [(rule,wi,wj)]
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

            
        


def test():
    word_list = [('Hãy cho biết', 'None'), ('xe bus', 'N_sub'), ('B2', 'Name_bus'), ('đến', 'V'), ('thành phố Hà Nội', 'Name'), ('vào thời điểm nào', 'WH_time'), ('?', 'None')]
    dependency_gram = ArcEagerParser(word_list)
    print(dependency_gram.buffer)
    #print(dependency_gram.stack[-1])
    dependency_gram.parsing()
    #print(dependency_gram.relation)

if __name__ == "__main__":
    test()