class TrieNode:
    def __init__(self, char, value=None):
        self.char = char
        self.children = []
        self.terminates = False
        self.value = value

    def __str__(self):
        if self.value is not None:
            return f"word: {self.value}"
        else:
            return f"char: {self.char}"


class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        self.size = 0

    def _find(self, char, array):
        for n in array:
            if n.char == char:
                return n
        return None

    def search(self, word, terminated=True):
        n = self.root
        for c in word:
            child = self._find(c, n.children)
            if not child:
                return None
            n = child
        return n if n.terminates or not terminated else None

    def find_words_that_begin_with(self, prefix):
        n = self.search(prefix, False)
        if not n:
            return []
        words = []
        queue = [n]
        while len(queue) > 0:
            n = queue.pop(0)
            if n.terminates:
                words.append(n.value)
            queue += n.children
        return words

    def insert(self, word):
        if len(word) == 0:
            return
        n = self.root
        for c in word:
            child = self._find(c, n.children)
            if not child:
                new_node = TrieNode(c)
                n.children.append(new_node)
                self.size += 1
                n = new_node
            else:
                n = child
        n.terminates = True
        n.value = word

    def remove(self, word):
        n = self.search(word)
        if n:
            n.terminates = False
            n.value = None


t = Trie()
t.insert("ronaldo")
t.insert("rooney")
t.insert("rodri")
t.insert("abelardo")
t.insert("berbatov")
t.insert("bergkamp")

print(t.search("ro"))
print(t.search("rooney"))
print(t.find_words_that_begin_with("ro"))
print(t.search("rodry"))
print(t.find_words_that_begin_with("berg"))
print(t.find_words_that_begin_with("ber"))
print(t.size)

t.remove("abe")
t.remove("berbatov")
print(t.find_words_that_begin_with("ber"))
t.insert("berbatov")
t.insert("bergkamp")
print(t.find_words_that_begin_with("ber"))
