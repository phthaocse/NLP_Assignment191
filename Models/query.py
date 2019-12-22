import sys
sys.path.insert(0,'../Output/')
import db

class Query():
    def __init__(self,proc_sem):
        self.proc_sem = proc_sem
        self.answer = []

    def get_answer(self):
        return
