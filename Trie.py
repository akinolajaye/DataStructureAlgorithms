

class TrieNode:
    def __init__(self):
        self.children={}
        self.end_of_word=False


class Trie:
    def __init__(self):
        self.root=TrieNode()

    def add_word(self,word):

        current=self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TrieNode()
            current=current.children[char]
        current.end_of_word=True


    def search(self,word):
        current=self.root

        for char in word:
            if char not in current.children:
                return False
            current=current.children[char]
        return current.end_of_word



x=Trie()
x.add_word("one")
x.add_word("two")
x.add_word("three")
x.add_word("four")
x.add_word("five")
x.add_word("six")
x.add_word("seven")
x.add_word("eight")
x.add_word("nine")

wordlist=sorted(['one','two',"three"])
words="otneheewtro"
wordnew="rfosevuen"

wordchar=([i for i in words])
print(wordchar)
print(wordlist)
s=[]

for word in words:
    # break scrambled word into characters
    chars = sorted(list(word))
    # loop through comparison list
    for compare in wordlist:
        if sorted(list(compare)) == chars:
            s.append(compare)

# create comma separated list of words
print(",".join(s))