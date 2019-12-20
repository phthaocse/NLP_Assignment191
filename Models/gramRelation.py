from converEngdict import dict1

class GrammaticalRelation():

    def __init__(self,dependency):
        self.dep_gram = dependency#list  


    def rule2gm(self,rule):
        res = str()
        if rule[0] == 'ROOT':
            res = '(s1 PRED ' + dict1[rule[2][0].lower()].upper() + ')(s1 TNS PRE)'
        elif rule[0] == 'amod':
            if rule[2][1] == 'Name_bus':
                res = '(s1 LSUBJ ' + dict1[rule[1][0].lower()].upper() + '(NAME ' + rule[2][0].lower() + ' "'+rule[2][0]+'"))'
            else:
                res = '(s1 LSUBJ ' + dict1[rule[1][0].lower()].upper() + ')(WH_BUS)'
        elif rule[0] == 'nsubj':
            res = '(s1 LSUBJ ' + dict1[rule[2][0].lower()].upper() + ')'
        elif rule[0] == 'dobj':
            res = '(s1 LOBJ THANHPHO(NAME ' +  rule[2][0][0] + ' "' + dict1[rule[2][0].lower()].upper() + '"))'        
        elif rule[0] == 'nmod':
            #TODO
            if rule[2][1] == "Time":
                res = '(s1 DEST-TIME ' + rule[2][0] + ')'
            elif rule[2][1] == "WH_time":
                res = '(s1 RUN_TIME WH)'
            else:
                res = '(s1 LOBJ THANHPHO(NAME ' +  rule[2][0][0] + ' "' + dict1[rule[2][0].lower()].upper() + '"))'
        return res

    def convertFromDep(self):
        index = str()
        res = list()
        for x in self.dep_gram:
            if x[0] == 'ROOT':
                index = str(self.dep_gram.index(x)) + index
            elif x[1][1] == 'V':
                index +=  str(self.dep_gram.index(x))
            elif x[1][1] == 'N_sub':
                index +=  str(self.dep_gram.index(x))

        for idx in index:
            res.append(self.rule2gm(self.dep_gram[int(idx)]))
        return res

def test():
    rule =  [[('ROOT', 'root', ('đến', 'V'), -2, 2), ('nsubj', ('đến', 'V'), ('Xe bus', 'N_sub'), -1, 0), ('amod', ('Xe bus', 'N_sub'), ('nào', 'WH'), 0, 1), ('dobj', ('đến', 'V'), ('thành phố Huế', 'Name'), 2, 3), ('nmod', ('đến', 'V'), ('lúc 20:00HR', 'Time'), 2, 4)],
            [('ROOT', 'root', ('đến', 'V'), -2, 5), ('nsubj', ('đến', 'V'), ('xe bus', 'N_sub'), -1, 1), ('amod', ('xe bus', 'N_sub'), ('B3', 'Name_bus'), 1, 2), ('nmod', ('xe bus', 'N_sub'), ('Đà Nẵng', 'Name'), 1, 4), ('case', ('Đà Nẵng', 'Name'), ('từ', 'P'), 4, 3), ('nmod', ('đến', 'V'), ('Thời gian', 'WH_time'), 5, 0), ('dobj', ('đến', 'V'), ('Huế', 'Name'), 5, 6)],
            [('ROOT', 'root', ('đến', 'V'), -2, 2), ('nsubj', ('đến', 'V'), ('Xe bus', 'N_sub'), -1, 0), ('amod', ('Xe bus', 'N_sub'), ('nào', 'WH'), 0, 1), ('dobj', ('đến', 'V'), ('thành phố Hồ Chí Minh', 'Name'), 2, 3)]]
    for x in rule:
        gr = GrammaticalRelation(x)
        res = gr.convertFromDep()
        for y in res:
            print(y)
        print("----------------------------")
if __name__ == "__main__":
   test()