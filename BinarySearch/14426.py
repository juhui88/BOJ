import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.children = {}

    def setData(self,data):
        self.data = data

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self,string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self,string):
        curr_node = self.head
        for char in string:
            if char in curr_node.children.keys():
                curr_node = curr_node.children[char]
            else:
                return False
        return True

N,M = map(int,input().split())
S1 = [input().strip() for _ in range(N)]
S2 = [input().strip() for _ in range(M)]

trie = Trie()
for i in range(N):
    trie.insert(S1[i])
print(sum(trie.search(S2[j]) for j in range(M)))