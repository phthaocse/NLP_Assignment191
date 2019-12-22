import sys
sys.path.insert(0,'../Output/')
import db

class Query():
    def __init__(self,proc_sem):
        self.proc_sem = proc_sem
        self.answer = []

    def get_answer(self):
        res = None
        if 'FIND-THE' in self.proc_sem['type']:
            answer = ''
            check = True
            bus_name = self.proc_sem['rest'][0][1]
            from_city = self.proc_sem['rest'][0][2]
            to_city = self.proc_sem['rest'][0][3]
            if  bus_name in db.bus_db:
                if db.bus_db[bus_name]['ATIME']['CITY'] != to_city or db.bus_db[bus_name]['DTIME']['CITY'] != from_city:
                    check = False
                else:
                    answer = db.bus_db[bus_name]['RUN_TIME']
            else:
                check = False     
            if check:
                res = (True,answer)
            else:
                res = (False,'Không có đối tượng thỏa mãn yêu cầu câu hỏi')
        else:
            answer = []
            bus_name = []
            for x in self.proc_sem['rest']:
                if 'XE' in x[0]:
                    bus_name = [name for name in db.bus_db.keys()]
                elif '?t' in x[-1]:
                    city_name = x[2]
                    for bus in bus_name:
                        if db.bus_db[bus]['ATIME']['CITY'] == city_name:
                            answer += [bus]
                else:
                    city_name = x[2]
                    atime = x[3]
                    for bus in bus_name:
                        if db.bus_db[bus]['ATIME']['CITY'] == city_name and db.bus_db[bus]['ATIME']['TIME'] == atime:
                            answer += [bus]
            if answer:
                res = (True,','.join(ans for ans in answer))
            else:
                res = (False,'Không có đối tượng thỏa mãn yêu cầu câu hỏi')

        return res

def test():
    inp = [
        {'type': 'PRINT-ALL ?b', 'rest': [['XE_BUS', '?b'], ['ATIME', '?b', 'HUE', '24:00HR']]},
        {'type': 'FIND-THE  ?t', 'rest': [['RUN-TIME', 'B3', 'HCMC', 'HUE', '?t']]},
        {'type': 'PRINT-ALL ?b', 'rest': [['XE_BUS', '?b'], ['ATIME', '?b', 'DANANG', '?t']]}
    ]
    for proc in inp:
        query = Query(proc)
        ans = query.get_answer()
        print(ans[1])

if __name__ == "__main__":
    test()
