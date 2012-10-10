# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
   
    closedSet           = set()
    dataStructure       = util.Stack()
    actions             = []
    
    consideredNodeCoord = problem.startState
    dataStructure.push(consideredNodeCoord)

    result = searchHelperFunction(problem, consideredNodeCoord, dataStructure, actions, closedSet)
    
    if result is False:
        raise Exception("No solution exists!")

    print "[Final Path] [%s]" % ", ".join(actions)  
    raw_input("")
    return actions

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def searchHelperFunction(problem, nodeCoordinates, dataStructure=util.Stack(), path=[], closedSet=None):
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    
    nodeLocationIndex       = 0
    nodeArcDirectionIndex   = 1
    nodeArcCostIndex        = 2 

    if problem is None:
        print "No Problem"
        return False

    if problem.isGoalState(nodeCoordinates):
        print "[Success] Reached Goal State at (%s)" % (" ,".join(map(str, nodeCoordinates)))
        return True

    if dataStructure.isEmpty():
        print "[Backtrack] Empty Queue"
        return False    
    
    successors = problem.getSuccessors(nodeCoordinates)
    if not successors:
        print "[Dead-end]" % (" ,".join(map(str, nodeCoordinates)))
        return False

    nodesThisLevel = len(successors)
    for node in successors:
        print "[Child] (%s), [Parent] (%s)" % (" ,".join(map(str, node[nodeLocationIndex])), " ,".join(map(str, nodeCoordinates)))
        dataStructure.push(node)
    
    while nodesThisLevel > 0: 
        destNode = dataStructure.pop()
        destNodeCord = destNode[nodeLocationIndex]
        consideredNodeDir = destNode[nodeArcDirectionIndex]

        if closedSet is not None and destNodeCord in closedSet:
            nodesThisLevel -= 1
            print "[Visited] (%s)" % (", ".join(map(str, destNodeCord)))
            continue

        if consideredNodeDir == "North":
            path.append(n)
        elif consideredNodeDir == "South":
            path.append(s)
        elif consideredNodeDir == "West":
            path.append(w)
        elif consideredNodeDir == "East":
            path.append(e)
        else:
            raise Exception("Unrecognized expression for direction: " + consideredNodeDir)
     
        print "[Expanding] (%s)" % (", ".join(map(str, destNode[nodeLocationIndex]))) 
        print "[Path State] [%s]" % (", ".join(map(str, path)))

        closedSet.add(destNode[nodeLocationIndex])
        result = searchHelperFunction(problem, destNodeCord, dataStructure, path, closedSet)
        
        if result is True:
            return True
        else:
            path.pop()

        nodesThisLevel -= 1
    return False

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


