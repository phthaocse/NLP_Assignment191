import ast

def loadDict(path):
    with open(path, encoding="utf8") as fr:
        words = fr.read()
        words = ast.literal_eval(words)
    return words

class Node():
    def __init__(self,data=None,childs=[]):
        self.data = data
        self.childs = childs

class Tree(object):
    def __init__(self, root = Node(),size=0): 
        self.root = root
        if root:
            self.size = 1
        else:
            self.size = 0

    def insert(self,node,parent,curr_node = 1):
        '''
        insert new node to tree
        :param node (Node obj), parent node data
        '''
        if not node or not parent:
            return 
        elif curr_node:
            if curr_node == 1:
                curr_node = self.root
            if curr_node.data == parent:
                if curr_node.childs:
                    curr_node.childs.append(node)
                else:
                    curr_node.childs = [node]
                self.size += 1
                return 
            for child in curr_node.childs:
                self.insert(node,parent,child) 
    
    def printTree(self,curr_node,level = 0):
        if not curr_node:
            return
        else:
            if curr_node:
                if curr_node.childs:
                    for child in curr_node.childs:
                        #print(child)
                        self.printTree(child,level + 1)
                print('\t'*level,curr_node.data)
            else: 
                return

