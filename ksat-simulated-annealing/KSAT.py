import numpy as np
from copy import deepcopy

class KSAT:
    def __init__(self, N, M, K, seed = 5):
        if not (isinstance(K, int) and K >= 2):
            raise Exception("k must be an int greater or equal than 2")
        self.K = K
        self.M = M
        self.N = N

        ## Optionally set up the random number generator state
        if seed is not None:
            np.random.seed(seed)
    
        # s is the sign matrix
        s = np.random.choice([-1,1], size=(M,K))
        
        # index is the matrix reporting the index of the K variables of the m-th clause 
        index = np.zeros((M,K), dtype = int)        
        for m in range(M):
            index[m] = np.random.choice(N, size=(K), replace=False)
            
        # Dictionary for keeping track of literals in clauses
        clauses = []   
        for n in range(N):
            clauses.append([i for i, row in enumerate(index) if n in row])
        
        self.s, self.index, self.clauses = s, index, clauses        
        
        ## Inizializza la configurazione
        x = np.ones(N, dtype=int)
        self.x = x
        self.init_config()

    ## Initialize (or reset) the current configuration
    def init_config(self):
        N = self.N 
        self.x[:] = np.random.choice([-1,1], size=(N))
        
        
    ## Definition of the cost function
    # Here you need to complete the function computing the cost using eq.(4) of pdf file
    def cost(self):
        clause_satisfaction = np.prod(
            0.5 * (1 - self.s * self.x[self.index]), axis=1
        )
        # The cost is the sum of unsatisfied clauses
        return np.sum(clause_satisfaction)
        
    
    ## Propose a valid random move. 
    def propose_move(self):
        N = self.N
        move = np.random.choice(N)
        return move
    
    ## Modify the current configuration, accepting the proposed move
    def accept_move(self, move):
        self.x[move] *= -1

    ## Compute the extra cost of the move (new-old, negative means convenient)
    # Here you need complete the compute_delta_cost function as explained in the pdf file
    def compute_delta_cost(self, move):
        # Get the clauses affected by flipping variable `move`
        
        # General edge case inclusion even though the choice of moves will never end in one of these edge cases, due to how they are chosen based on N
        if move < 0 or move >= self.N:
            raise ValueError(f"Invalid move: {move}. Must be between 0 and {self.N-1}")
        affected_clauses = self.clauses[move]
        
        # Compute the current contributions of the affected clauses
        current_contributions = np.prod(
            0.5 * (1 - self.s[affected_clauses] * self.x[self.index[affected_clauses]]),
            axis=1)
        # Simulate flipping the variable
        self.x[move] *= -1
        # Compute the new contributions of the affected clauses
        new_contributions = np.prod(
            0.5 * (1 - self.s[affected_clauses] * self.x[self.index[affected_clauses]]),
            axis=1)
        # Flip the variable back to restore the original state
        self.x[move] *= -1
        # Delta cost is the difference between new and old contributions
        return np.sum(new_contributions - current_contributions)
    

    ## Make an entirely independent duplicate of the current object.
    def copy(self):
        return deepcopy(self)
    
    ## The display function should not be implemented
    def display(self):
        pass
    

    
        

