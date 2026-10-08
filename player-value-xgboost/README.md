# Football Player Market Value Prediction with XGBoost

Predicts a football player's market value (`value_eur`) from their attributes,
training a separate XGBoost regressor for each group of playing positions.
Written for a machine-learning course project with a train/test/submission
format.

## Approach

`player_value_xgboost.ipynb` is a single-cell notebook that runs the whole
pipeline:

1. **Preprocessing.** Takes each player's first listed position as their primary
   position, reduces `body_type` to Lean / Normal / Stocky / Other, and one-hot
   encodes both.
2. **Position groups.** Splits players into six groups and trains one model per
   group: fullbacks, centre-backs, midfielders, wingers, forwards, goalkeepers.
   Goalkeepers use only the `goalkeeping_*` attributes; outfield groups use the
   outfield attributes, minus a hand-picked list that is irrelevant to that
   group (for example, heading accuracy for wingers).
3. **Target.** Caps `value_eur` at the 99.5th percentile within each group to
   limit the pull of outliers, then models `log(1 + value)`.
4. **Engineered features.** A body-type score weighted by each body type's
   correlation with value, `age × potential`, a league-level feature
   (`value_eur × league_level` in training, `league_level` at prediction time),
   and a body-type × position interaction.
5. **Feature selection.** Keeps features whose absolute correlation with the
   log target exceeds 0.05.
6. **Model.** `XGBRegressor` with 200 trees, learning rate 0.05, depth 4, and
   0.8 row and column subsampling, evaluated by 5-fold cross-validation. RMSE is
   computed in euros, after undoing the log transform; the fold with the lowest
   validation RMSE supplies the model used for prediction.
7. **Prediction.** Applies the same preprocessing to the test set, predicts per
   group, restores the original row order and writes `submission.csv`.

## Data

The data files are **not included** in this repository. The notebook reads
`train.csv` and `test.csv`, and reads and overwrites `submission.csv`, from an
absolute path on the original machine
(`C:\Users\Utente\Desktop\BOCCONI\Machine Learning\ML Project\Final\`). Update
those four paths before running.

The training set needs `value_eur`, `player_positions`, `body_type`, `age`,
`overall`, `potential`, `league_level` and the FIFA-style attribute columns
(`attacking_*`, `skill_*`, `movement_*`, `power_*`, `mentality_*`,
`defending_*`, `goalkeeping_*`).

## Run

```bash
cd player-value-xgboost
jupyter notebook player_value_xgboost.ipynb
```

## Requirements

`pandas`, `numpy`, `xgboost`, `scikit-learn`, plus `jupyter` to open the
notebook.
