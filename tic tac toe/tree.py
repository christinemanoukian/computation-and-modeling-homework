import sys
sys.path.append('tic tac toe')
from game import *
from graph import *

# class Node:
#     def __init__(self, index):
#         self.index = index

# class Node:
#     def __init__(self, ):
#         self.state = # state of game
#         self.player = # who's turn it is at this point
#         self.winner = # says if someone has won

class TicTacToeTree:
    def __init__(self):
        self.root_node = Node([[0 for j in range(3)] for i in range(3)]) #does this make the empty board a node is this right
        self.nodes = [self.root_node]
        self.edges = #all the possible moves?
    
    def successor(self, state):
        possible_moves = self.get_children(state)

    def is_terminal(self, state):
        if self.get_children(state) == []: # how do i get the children if i dont know all the game states
            return True
    
    
    # need a method to actually build the tree? Don't know what to do tho. have this so far but dont think its right:
    def build_tree(self):
        queue = self.nodes
        visited = []
        current_node = queue[0]
        if self.is_terminal(current_node) is False:
            children = self.successor(self.current_node)
            for child in children:
                child = Node(child)
                if child not in queue and child not in visited:
                    queue.append(child)
                    self.nodes.append(child)
                visited.append(child)
    
    # i strongly believe this is all wrong but the problem is idek what the end result is supposed to look like. This is just
    # adding all of the possible game states to self.nodes its not showing what takes you where and stuff 
    

# questions:
# what is the point of the tree / what am i actually storing everything in / what is the end result of this class
# what goes in the init function
# what methods do i need
# i have zero clue what the second bullet point means
# do i need my graph class or my game class or both or none
# i legit dont know how to make the layers lol 