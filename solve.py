import json

class TrieNode():
    """Implementation of Trie Node

    add_word(word) adds a word to the TrieNode
    
    check_word(word) checks if a word is in the Trie"""
    def __init__(self) -> None:
        self.children = {}
        self.eow = False
    
    def add_word(self, word):
        """Adds a word to the TrieNode"""
        node = self
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]
    
        node.eow = True    

    def check_word(self, word):
        """Checks if a word is in the Trie"""
        node = self
        
        for c in word:
            if c not in node.children:
                return False
            
            node = node.children[c]
        
        return node.eow

class Board():
    """Implementation of Squaredle board
    Input board as a string, using '/' to indicate the
    end of each row
    
    Solves Squaredle board input via simple DFS comparing against
    a list of valid words"""
    def __init__(self, board_input: str) -> None:
        self.validate_board(board_input)

        rows = board_input.split('/')
        self.board = [list(row) for row in rows]
        
        self.size = len(rows)
        self.words = set()

    def validate_board(self, board_input: str) -> None:
        """Validates a board input (has to be square and at least size 3)"""
        rows = board_input.split('/') # use '/' to separate rows
        l = len(rows[0])
        if not all(len(row)== l for row in rows):
            raise ValueError('Board Input must be square')
        
        if l < 3:
            raise ValueError('Board size must be at least 3')
        
    def dfs(self, position: list, curr_word: str, curr_path: set(), trie: TrieNode()):
        """Runs DFS on a position of the board to search for all possible words"""
        new_trie = trie.children.get(self.board[position[0]][position[1]])
        if new_trie is None:
            return

        updated_word = curr_word + self.board[position[0]][position[1]]
        # Check whether this letter is the end of the word
        if new_trie.eow:
            self.words.add(updated_word)

        curr_path.add(self.encode_position(position))

        for neighbor in self.neighbors(position):
            if self.encode_position(neighbor) not in curr_path:
                # run dfs on neighbor if it has not been used previously
                self.dfs(neighbor, updated_word, curr_path, new_trie)

        curr_path.remove(self.encode_position(position))

    def encode_position(self, position: list):
        """Maps a position (x,y) to a numbered location on the square board
        i.e (0,0) is the top left position of the board -> 1"""
        return self.size * position[0] + position[1] + 1
    
    def neighbors(self, position: list):
        """Returns all (valid) neighboring positions for a certain position"""
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1],[1, 0],[1, 1]]
        neighbors = []
        for direction in directions:
            x = position[0] + direction[0]
            y = position[1] + direction[1]
            if 0 <= x < self.size and 0 <= y < self.size:
                neighbors.append([x, y])

        return neighbors
    
with open('valid_words.json') as f:
        words = json.loads(f.read())

dictionary = TrieNode()
for word in words:
    dictionary.add_word(word)

if __name__ == "__main__":
    board_input = input("Input Squaredle board:") 
    board = Board(board_input)
    for x in range(board.size):
        for y in range(board.size):
            # run dfs from all possible positions on the board
            board.dfs([x,y], "", set(), dictionary)
    
    print(sorted(list(board.words)))