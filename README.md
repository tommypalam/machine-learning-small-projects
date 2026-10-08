# Machine Learning Small Projects

Three small, self-contained projects in optimisation, time-series forecasting
and supervised learning, written during my studies at Bocconi University. Each
lives in its own folder with its own README.

| Project | What it does | Techniques | Entry point |
|---|---|---|---|
| [ksat-simulated-annealing](ksat-simulated-annealing/) | Solves random K-SAT instances and locates the algorithmic threshold of 3-SAT | Simulated annealing, Metropolis MCMC | `run_ksat.py` |
| [life-expectancy-arima](life-expectancy-arima/) | Forecasts a life-expectancy time series under several model orders | ARIMA (`statsmodels`) | `arima_forecast.py` |
| [player-value-xgboost](player-value-xgboost/) | Predicts football players' market value from their attributes | XGBoost, per-position models, 5-fold CV | `player_value_xgboost.ipynb` |

## Setup

Python 3.10 or newer.

```bash
git clone https://github.com/tommypalam/machine-learning-small-projects.git
cd machine-learning-small-projects
pip install -r requirements.txt
```

## Data availability

Only the K-SAT project runs out of the box: it generates its own random
instances. The ARIMA and XGBoost projects read CSV files that are **not
included** in this repository, and their scripts still point at the original
absolute Windows paths. Each project's README says which files are needed and
which lines to change.

## Repository layout

```
machine-learning-small-projects/
├── ksat-simulated-annealing/
│   ├── KSAT.py                  # K-SAT problem class (cost, moves, delta cost)
│   ├── SimAnn.py                # generic simulated-annealing solver
│   ├── run_ksat.py              # solve one instance
│   └── threshold_analysis.py    # solving probability and threshold experiments
├── life-expectancy-arima/
│   └── arima_forecast.py        # ARIMA fits and 10-step forecasts
├── player-value-xgboost/
│   └── player_value_xgboost.ipynb
├── requirements.txt
└── README.md
```
