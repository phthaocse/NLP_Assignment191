from . import converEngdict

class GrammaticalRelation():

    def __init__(self,dependency):
        self.dep_gram = dependency#list  
        self.var = list()
        self.logic_form = list()

    def var_gen(self,obj,add = None):
        if add:
            self.var.append(obj)
            return obj
        else:
            count = 1
            var_name = obj[0].lower() + str(count)
            for name in self.var:
                if var_name == name:
                    count += 1
            var_name = obj[0].lower() + str(count)
            self.var.append(var_name)
            return var_name

    def rule2gm(self,rule):
        res = str()
        logi = ''
        dict1 = converEngdict.dict1
        if rule[0] == 'ROOT':
            res = '(s1 PRED ' + dict1[rule[2][0].lower()].upper() + ')(s1 TNS PRE)'
        elif rule[0] == 'amod':
            if rule[2][1] == 'Name_bus':
                var = self.var_gen(rule[2][0].lower(),'add') 
                res = '(s1 LSUBJ ' + dict1[rule[1][0].lower()].upper() + '(NAME ' + var + ' "'+rule[2][0]+'"))'
                logi = ('XE BUS',var,('NAME',var,'"' + rule[2][0] + '"'))
            else:
                res = '(s1 LSUBJ ' + dict1[rule[1][0].lower()].upper() + ')(NAME ' + self.var_gen('WH_BUS') + ' WH_BUS)'
                logi = ('WH','XE_BUS')
        elif rule[0] == 'nsubj':
            res = '(s1 LSUBJ ' + dict1[rule[2][0].lower()].upper() + ')'
        elif rule[0] == 'dobj':
            var = self.var_gen(dict1[rule[2][0].lower()])
            city = '"' + dict1[rule[2][0].lower()].upper() + '"'
            res = '(s1 LOBJ THANHPHO(NAME ' +  var + ' ' + city + '))'        
            logi = ('DEST','b',('NAME',var,city))
        elif rule[0] == 'nmod':
            #TODO
            if rule[2][1] == "Time":
                res = '(s1 ATIME ' + rule[2][0] + ')'
                logi = ('ATIME','b',rule[2][0])
            elif rule[2][1] == "WH_time":
                res = '(s1 RUN_TIME WH)'
                logi = ('WH','RUN_TIME')
            else:
                var = self.var_gen(dict1[rule[2][0].lower()])
                city = '"' + dict1[rule[2][0].lower()].upper() + '"'
                res = '(s1 FROM_LOC THANHPHO(NAME ' +  var  + ' ' + city + '))'
                logi = ('FROM_LOC','b',('NAME',var,city))
        if logi:
            self.logic_form.append(logi)
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
            main = self.rule2gm(self.dep_gram[int(idx)])
            res.append(main)

        return res,self.logic_form
    


def test():
    rule =  [[('ROOT', 'root', ('đến', 'V'), -2, 2), ('nsubj', ('đến', 'V'), ('Xe bus', 'N_sub'), -1, 0), ('amod', ('Xe bus', 'N_sub'), ('nào', 'WH'), 0, 1), ('dobj', ('đến', 'V'), ('thành phố Huế', 'Name'), 2, 3), ('nmod', ('đến', 'V'), ('20:00HR', 'Time'), 2, 5), ('case', ('thành phố Huế', 'Name'), ('lúc', 'P'), 3, 4)],
            [('ROOT', 'root', ('đến', 'V'), -2, 5), ('nsubj', ('đến', 'V'), ('xe bus', 'N_sub'), -1, 1), ('amod', ('xe bus', 'N_sub'), ('B3', 'Name_bus'), 1, 2), ('nmod', ('xe bus', 'N_sub'), ('Đà Nẵng', 'Name'), 1, 4), ('case', ('Đà Nẵng', 'Name'), ('từ', 'P'), 4, 3), ('nmod', ('đến', 'V'), ('Thời gian', 'WH_time'), 5, 0), ('dobj', ('đến', 'V'), ('Huế', 'Name'), 5, 6)],
            [('ROOT', 'root', ('đến', 'V'), -2, 2), ('nsubj', ('đến', 'V'), ('Xe bus', 'N_sub'), -1, 0), ('amod', ('Xe bus', 'N_sub'), ('nào', 'WH'), 0, 1), ('dobj', ('đến', 'V'), ('thành phố Hồ Chí Minh', 'Name'), 2, 3)]]
    for x in rule:
        gr = GrammaticalRelation(x)
        res = gr.convertFromDep()
        for y in res:
            print(y)
        print("----------------------------")
        print(gr.logic_form)
if __name__ == "__main__":
   test()