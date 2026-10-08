
#%%
##Solving 3.11##

#Given the scope of this task, I made another change to SimAnn 
# to make the code go faster:
# when the cost = 0, the code is stopped

import matplotlib.pyplot as plt
from SimAnn import simann
from KSAT import KSAT
import time 
from tqdm import tqdm

def solving_probability(totinst, seed = None):
    
    start_time = time.time()
    #Choosing values of M to analyze
    listM = [400, 500, 600, 700, 800, 900, 1000]
    mcmc_steps = [1200, 1500 , 1800, 2100, 2400, 2700, 3000]
    anneal_steps = [40, 40, 40, 40, 40, 40, 40]
    beta0 = [1, 1, 1, 1, 1, 1, 1]
    beta1 = [10, 10, 10, 10, 10, 10, 10]

    #Keeping track of success rate
    probArr = []

    #Outer loop going through every M we chose
    for j in tqdm(range(len(listM))):

        solved = 0

        #Running the program multiple times to collect a meaningful sample
        for i in range(totinst):

            ksat = KSAT(N = 200, M = listM[j], K = 3, seed=seed)

            best = simann(ksat, mcmc_steps = mcmc_steps[j], 
                                            anneal_steps = anneal_steps[j],
                                            beta0 = beta0[j], beta1 = beta1[j],
                                            seed = seed)
        
            if best.cost() == 0:
                solved += 1

        probArr.append(solved/totinst)
    
    total_time = time.time() - start_time  # Calculate total time
    print(f"\nTotal runtime: {total_time:.2f} seconds")
    
    
    #Plot results
    print(f'probArr = {probArr}')
    plt.plot(listM, probArr,  '-o')
    plt.xlabel('M values')
    plt.ylabel('P(N, M)')
    plt.title('3-SAT Solving Probability vs Number of Clauses (N=200)')
    plt.grid(True)
    plt.show()

solving_probability(30)



# %%
##Solving 3.12##

#Identifying the so-called algorithmic threshold M(Alg)(N = 200)
#Using the binary search algorithm
#We'll use the same parameters mcmc, anneal_steps, beta0, beta1, seed
#for each M because the threshold changes on different parameters
#From the previous question we know that the threshold is between 
#M = 600 and M = 700

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import KSAT
import SimAnn

def find_threshold_detailed(N=200, M_min=600, M_max=700, num_points=20, instances_per_point=30, seed=None):
    """
    Find the algorithmic threshold with a detailed probability curve
    """
    # Create evenly spaced M values
    M_values = np.linspace(M_min, M_max, num_points, dtype=int)
    probabilities = []
    
    # For each M, compute success probability
    for M in tqdm(M_values, desc="Testing M values"):
        solved = 0
        mcmc_steps = int(M/2)  # Scale MCMC steps with M
        
        for i in range(instances_per_point):
            # Use different seed for each instance to ensure independence
            instance_seed = seed
            
            ksat = KSAT.KSAT(N=N, M=M, K=3, seed=instance_seed)
            
            best, _ = SimAnn.simann(
                ksat,
                mcmc_steps=mcmc_steps,
                anneal_steps=40,
                beta0=1,
                beta1=10,
                seed=instance_seed
            )
            
            if best == 0:
                solved += 1
        
        prob = solved / instances_per_point
        probabilities.append(prob)
    
    # Find the threshold (M where probability ≈ 0.5)
    threshold_idx = np.argmin(np.abs(np.array(probabilities) - 0.5))
    threshold_M = M_values[threshold_idx]
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(M_values, probabilities, 'bo-', linewidth=2, markersize=8)
    plt.axvline(x=threshold_M, color='r', linestyle='--', label=f'Threshold ≈ {threshold_M}')
    plt.axhline(y=0.5, color='g', linestyle='--', label='P = 0.5')
    
    plt.xlabel('Number of Clauses (M)')
    plt.ylabel('Solving Probability')
    plt.title('3-SAT Algorithmic Threshold Detection (N=200)')
    plt.grid(True)
    plt.legend()
    
    return M_values, probabilities, threshold_M

# Run the improved analysis
M_values, probs, threshold = find_threshold_detailed(
    M_min=600,
    M_max=700,
    num_points=20,
    instances_per_point=30,
    seed=123
)

print(f"Estimated threshold M(Alg) ≈ {threshold}")

# %%

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import KSAT
import SimAnn

def find_threshold_detailed(N=200, M_min=600, M_max=700, num_points=20, instances_per_point=30, seed=None):
    """
    Find the algorithmic threshold with a detailed probability curve
    """
    # Create evenly spaced M values
    M_values = np.linspace(M_min, M_max, num_points, dtype=int)
    probabilities = []
    
    # For each M, compute success probability
    for M in tqdm(M_values, desc="Testing M values"):
        solved = 0
        mcmc_steps = int(M/2)  # Scale MCMC steps with M
        
        for i in range(instances_per_point):
            # Use different seed for each instance to ensure independence
            
            ksat = KSAT.KSAT(N=N, M=M, K=3, seed = seed)
            
            best, _ = SimAnn.simann(
                ksat,
                mcmc_steps=1500,
                anneal_steps=40,
                beta0=1,
                beta1=10,
                seed=5
            )
            
            if best == 0:
                solved += 1
        
        prob = solved / instances_per_point
        probabilities.append(prob)

        if solved/instances_per_point < 0.5:
            break
    
    # Find the threshold (M where probability ≈ 0.5)
    threshold_idx = np.argmin(np.abs(np.array(probabilities) - 0.5))
    threshold_M = M_values[threshold_idx]
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(M_values, probabilities, 'bo-', linewidth=2, markersize=8)
    plt.axvline(x=threshold_M, color='r', linestyle='--', label=f'Threshold ≈ {threshold_M}')
    plt.axhline(y=0.5, color='g', linestyle='--', label='P = 0.5')
    
    plt.xlabel('Number of Clauses (M)')
    plt.ylabel('Solving Probability')
    plt.title(f'3-SAT Algorithmic Threshold Detection (N={N})')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    return M_values, probabilities, threshold_M

plt.clf()

N = [500,600]

threshold_arr = []

colors = ['blue', 'red', 'green', 'purple']

for i in range(len(N)):

    M_values, probs, threshold = find_threshold_detailed(
        N = N[i],
        M_min=int(N[i] * 3),
        M_max=int(N[i] * 3.5),
        num_points=20,
        instances_per_point=30,
        seed=None)

    print(f'For N = {N}: probs = {probs}, M_values = {M_values}, threshold = {threshold}')

    threshold_arr.append(threshold)
    scaled_M = M_values/N[i]
    plt.plot(scaled_M, probs, 'o-', label=f'N={N[i]}', color = colors[i])


plt.ylabel('Solving Probability')
plt.xlabel('Rescaling of M as M/N')
plt.title(f'Collapsing curves')
plt.grid(True)
plt.legend()
plt.show()

print(f"N_values = {N}thresholds ≈ {threshold}")