class LogicalForm():
    def __init__(self, in_pattern):
        self.pattern = in_pattern
        self.logic_form = {'type': '', 'rest': []}
    
    def get_logical_form(self):
        var = ''
        if 'XE' in self.pattern[0][0]:
            var = self.pattern[0][1] 
        for x in self.pattern:
            if x[0] == 'WH':
                if x[1] == 'RUN_TIME':
                    self.logic_form['type'] = 'THE t'
                    self.logic_form['rest'] += [['RUN_TIME',var,'t']] 
                else:
                    self.logic_form['type'] = 'WH b'
                    self.logic_form['rest'] += [['XE_BUS','b']]
            else:
                if var and x[1] == 'b':
                    tmp = list(x)
                    tmp[1] = var
                    x = tuple(tmp)
                self.logic_form['rest'] += [list(x)]
        return self.logic_form

    def print_logic_form(self):
        rest = list()
        componet = ''
        # print(self.logic_form)
        for x in self.logic_form['rest']:        
            if type(x[-1]) != str:
                tmp = ' (' + ' '.join(y for y in x[-1]) + ')'
                component =  '(' + ' '.join(z for z in x[0:-1]) + tmp + ')'
            else:
                component = '(' + ' '.join(y for y in x) + ')'               
            rest.append(component)
        res_str = '(' + self.logic_form['type'] +  ':(&' + ''.join(com for com in rest) + '))'
        print(res_str)


def test():
    l = [
        [('WH', 'XE_BUS'), ('DEST', 'b', ('NAME', 'h1', '"HUE"')), ('ATIME', 'b', '20:00HR')],
        [('XE BUS', 'b3'), ('NAME','b3' ,'"B3"'), ('FROM_LOC', 'b', ('NAME', 'd1', '"DANANG"')), ('WH', 'RUN_TIME'), ('DEST', 'b', ('NAME', 'h1', '"HUE"'))],
        [('WH', 'XE_BUS'), ('DEST', 'b', ('NAME', 'h1', '"HCMC"'))]
    ]
    for ele in l:
        log_form = LogicalForm(ele)
        log_form.get_logical_form()
        log_form.print_logic_form()
        print(log_form.logic_form)

if __name__ == "__main__":
    test()