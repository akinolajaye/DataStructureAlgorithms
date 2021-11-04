class TrieNode:
    def __init__(self):

        self.children={}
        self.end_of_word=False
        


class Trie:
    def __init__(self):
        self.root=TrieNode()
        self.visited={}


    def insert_word(self,word):

        #inserts a word into the trie


        current =self.root
        for char in word:
            if char not in current.children: #if the char is not a child of the current node its on
                current.children[char]=TrieNode() #create a child for that char
            current=current.children[char]
            self.visited[current]=False
        current.end_of_word=True


    def search(self,word):

        current=self.root
        for char in word:
            if char not in current.children:
                return False

            current =current.children[char]

        return current.end_of_word



    def print_trie(self):

        current=self.root

        print(current.children["a"])
        while not current.end_of_word:
            letter=list(current.children.keys())[0]
            print(letter)

            current=current.children[letter]
            



x=Trie()
x.insert_word("apple")
x.insert_word("ape")
x.print_trie()