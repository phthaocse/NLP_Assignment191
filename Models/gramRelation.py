from converEngdict import dict1,dict2

class GrammaticalRelation():

    def __init__(self,dependency):
        self.dep_gram = self.toDepTree(dependency)#list  

    def rule2gm(self,rule):
        res = str()
        if rule[0] == 'ROOT':
            res = '(s1 PRED ' + dict[rule[1][0]].upper() + ')(s1 TNS PRE)'
        elif rule[0] == 'amod':
            if rule[1][1] == 'Name_bus':
                res = '(s1 LSUBJ ' + dict1[rule[1][0]].upper() + '(NAME' + rule[2][0].lower() + '"'+rule[2][0]+'"))'
            else:
                res = '(s1 LSUBJ' + dict1[rule[1][0]].upper() + '(WH_BUS)'
        elif rule[0] == 'dobj':
            res = '(s1 LOBJ THANHPHO(NAME' +  dict2[rule[2][0]] + dict1[rule[2][0]].upper() + '))'        
        elif rule[0] == 'nmod':
            #TODO
            res = ''

    def convertFromDep(self):
        index = str()
        res = list()
        for x in self.dep_gram:
            if x[0] == 'ROOT':
                index = str(self.dep_gram.index(x)) + index
            elif x[1][1] == 'V':
                index +=  str(self.dep_gram.index(x))
        for idx in index:
            res.append(rule2gm(self.dep_gram[idx]))
        return res