# Life Expectancy Forecast with ARIMA

Fits ARIMA models of increasing moving-average order to a life-expectancy time
series and plots their 10-step forecasts together. Written for a statistics
group project.

## What the script does

`arima_forecast.py`:

1. Loads a single-column time series from a CSV file.
2. Holds out the last 10 observations as a test set and trains on the rest.
3. Fits five models, `ARIMA(8, 1, q)` for `q = 4, 6, 8, 10, 12`, and prints the
   full summary of the first.
4. Forecasts 10 steps ahead with each model and appends the forecasts to the
   series, one block after another.
5. Plots the extended series (x-axis: years 2019–2069, y-axis: life expectancy).

Each forecast block has a fixed constant added to it (`+3`, `+5`, `+10`, `+14`,
`+17`) before it is appended. These offsets are hard-coded in the script, not
estimated from the data.

The commented-out lines are the exploratory steps used to choose the model
order: log transform, first differencing, ACF and PACF plots, the augmented
Dickey-Fuller stationarity test, and residual diagnostics.

## Data

The dataset (`NewProvaARIMA.csv`) is **not included** in this repository. The
script reads it from an absolute path on the original machine:

```python
df = pd.read_csv(r'c:\Users\Utente\Desktop\BOCCONI\...\NewProvaARIMA.csv')
```

To run it, change that line to point at a CSV holding one numeric column of
yearly values.

## Run

```bash
cd life-expectancy-arima
python arima_forecast.py
```

## Requirements

`pandas`, `numpy`, `matplotlib`, `statsmodels`.
