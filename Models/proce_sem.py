import sys
#sys.path.insert(0,'../Input/')
from Input import db

class ProceudalSematic():
    def __init__(self,logical_form):
        self.logical_form = logical_form
        self.proc_sem = {'type': '', 'rest': []}

    def get_proc_sem(self):
        if 'THE' in self.logical_form['type']:
            self.proc_sem['type'] = 'FIND-THE ' + ' ?t'
            tmp = ['','','']
            for x in self.logical_form['rest']:
                if 'XE' in x[0]:
                    tmp[0] = x[2][2][1:-1]
                elif 'FROM_LOC' in x:
                    tmp[1] = x[2][2][1:-1]
                elif 'DEST' in x:
                    tmp[2] = x[2][2][1:-1]
            self.proc_sem['rest'] += [['RUN-TIME',tmp[0],tmp[1],tmp[2],'?t']]
        elif 'WH' in self.logical_form['type']:
            self.proc_sem['type'] = 'PRINT-ALL' + ' ?b'
            check = False
            for x in self.logical_form['rest']:
                if 'XE' in x[0]:
                    tmp = [x[0],'?' + x[1]]
                    self.proc_sem['rest'] += [tmp]
                elif x[0] == 'DEST':
                    idx = self.logical_form['rest'].index(x)
                    for i in range(idx + 1,len(self.logical_form['rest'])):
                        if self.logical_form['rest'][i][0] == 'ATIME':
                            check = (True,self.logical_form['rest'][i][2])
                    if check:
                        tmp = ['ATIME','?' + x[1],x[2][2][1:-1],check[1]]
                        self.proc_sem['rest'] += [tmp]
                        break
                    else:
                        tmp = ['ATIME','?' + x[1],x[2][2][1:-1],'?'+'t']
                        self.proc_sem['rest'] += [tmp]
                        break
        return self.proc_sem    

    def print_sem(self):
        buff = [] 
        buff += [self.proc_sem['type']]
        for x in self.proc_sem['rest']:
            if type(x) is str:
                buff += [x]
            else:
                tmp = '(' + ' '.join(item for item in x) + ')'
                buff += [tmp]
        res_str = '(' + ''.join(item for item in buff) + ')'
        return res_str
def test():
    test_list = [
        {'type': 'WH b', 'rest': [['XE_BUS', 'b'], ['DEST', 'b', ('NAME', 'h1', '"HUE"')], ['ATIME', 'b', '20:00HR']]},
        {'type': 'THE t', 'rest': [['XE BUS', 'b3', ('NAME' ,'b3', '"B3"')], ['FROM_LOC', 'b3', ('NAME', 'd1', '"DANANG"')], ['RUN_TIME', 'b3', 't'], ['DEST', 'b3', ('NAME', 'h1', '"HUE"')]]},
        {'type': 'WH b', 'rest': [['XE_BUS', 'b'], ['DEST', 'b', ('NAME', 'h1', '"HCMC"')]]}
    ]
    for x in test_list:
        procedual = ProceudalSematic(x)
        res = procedual.get_proc_sem()
        print(res)
        procedual.print_sem()
if __name__ == "__main__":
    test()


        
        

