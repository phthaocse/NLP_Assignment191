from queue import LifoQueue
class ArcEagerParser():
    def __init__(self,word_list):
        self.stack = ['root']
        self.buffer = word_list[::-1]
        self.relation = dict()
        for x in word_list:
            self.relation[x] = []

    def parsing(self):
        print(self.buffer)
        while (self.buffer or len(self.stack) > 1):
            if self.stack[-1] not in self.relation.values() and self.stack[-1] != 'root':#leftarc
                print('leftarc')
                key = self.buffer[-1]
                if key in self.relation:
                    self.relation[key] += [self.stack.pop()]
                else:
                    self.relation[key] = [self.stack.pop()]
            elif self.buffer[0] not in self.relation.values():#rightarc
                print('rightarc')
                key = self.stack[-1]
                wj = self.buffer.pop()
                if key in self.relation:
                    self.relation[key] += [wj]
                else:
                    self.relation[key] = [wj]
                self.stack.append(wj)
            elif self.stack[-1] in self.relation.values() and self.stack[-1] != 'root':#reduce
                print('reduce')
                self.stack.pop()
            else:#shift
                print('shift')
                if len(self.stack) == 1:
                    self.stack.append(self.buffer.pop()) 
            print(self.stack)
        

def test():
    word_list = ['Happy','children','like','to','play','with','their','friends']
    dependency_gram = ArcEagerParser(word_list)
    print(dependency_gram.relation)
    dependency_gram.parsing()
    print(dependency_gram.relation)

if __name__ == "__main__":
    test()