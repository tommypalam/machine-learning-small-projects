# K-SAT with Simulated Annealing

Solves random K-SAT instances with simulated annealing, then measures how the
probability of finding a satisfying assignment falls as clauses are added, to
locate the algorithmic threshold of 3-SAT.

## The problem

A K-SAT instance has `N` boolean variables and `M` clauses, each clause joining
`K` distinct variables, each possibly negated. The instance is solved when every
clause is satisfied. Variables are stored as spins `x ∈ {−1, +1}` and the cost
is the number of unsatisfied clauses, so a cost of 0 is a solution.

## Files

| File | Purpose |
|---|---|
| `KSAT.py` | `KSAT` class: random instance generation, cost, single-spin-flip moves, and an incremental `compute_delta_cost` that only re-evaluates the clauses containing the flipped variable |
| `SimAnn.py` | `simann`: a generic simulated-annealing solver using the Metropolis rule. It works on any object exposing `init_config`, `cost`, `propose_move`, `compute_delta_cost`, `accept_move` and `copy` |
| `run_ksat.py` | Solves a single instance (`N=200`, `M=200`, `K=3`) and prints the acceptance rate and cost at each temperature |
| `threshold_analysis.py` | Experiments on solving probability versus `M`, split into `# %%` cells |

## Run

```bash
cd ksat-simulated-annealing
python run_ksat.py
```

The run takes about a second and ends with `final cost = 0.0` when the instance
is solved.

`simann` anneals over `anneal_steps` inverse temperatures spaced evenly from
`beta0` to `beta1`, with a final step at `beta = ∞` (greedy descent), running
`mcmc_steps` proposals at each. Pass `debug_delta_cost=True` to check every
incremental cost update against a full recomputation.

## Threshold experiments

`threshold_analysis.py` has three cells, meant to be run one at a time in an
editor that understands `# %%` cells (VS Code, Spyder):

1. **Solving probability.** For `N=200` and `M` from 400 to 1000, solves 30
   instances per value and plots the fraction solved, `P(N, M)`.
2. **Algorithmic threshold.** Scans `M` between 600 and 700 and reports the `M`
   where the solving probability crosses 0.5.
3. **Curve collapse.** Repeats the scan for larger `N` and plots the probability
   against `M/N`, to check that curves for different sizes overlap.

**Known limitation.** Cell 1 runs against `SimAnn.py` as committed. Cells 2 and
3 unpack two return values (`best, _ = SimAnn.simann(...)`) and compare `best`
with `0`, so they expect a variant of `simann` that returns the best cost first.
The committed `simann` returns a single `KSAT` object, so those two cells need
that small adaptation before they run.

## Requirements

`numpy`, `matplotlib`, `tqdm`.
