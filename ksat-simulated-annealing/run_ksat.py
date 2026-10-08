from SimAnn import simann
from KSAT import KSAT



## Generate a problem to solve.
# This generate a K-SAT instance with N=100 variables and M=350 Clauses
ksat = KSAT(200, 200, 3, seed=13)

## Optimize it.
best = simann(ksat,
                     mcmc_steps = 3000, anneal_steps = 40,
                     beta0 = 1, beta1 = 10.0,
                     seed = 5,
                     debug_delta_cost = False) # set to True to enable the check
                    
                  
