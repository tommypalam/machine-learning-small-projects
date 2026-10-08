import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import  plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller  
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv(r'c:\Users\Utente\Desktop\BOCCONI\Second Semester\Statistics\Group Project\NewProvaARIMA.csv')
#df.info()
#df.plot()
#plt.show()

#df = np.log(df)
#df.plot()
#plt.show()

msk = (df.index < len(df) - 10)
df_train = df[msk].copy()
df_test = df[~msk].copy()

#df_train_diff = df_train.diff().dropna()
#df_train_diff.plot()
#plt.show()
#acf_original = plot_acf(df_train_diff)
#pacf_original = plot_pacf(df_train_diff)
#plt.show()

#adf_test = adfuller(df_train)
#print(f'p_value: {adf_test[1]}' )

model = ARIMA(df_train, order = (8,1,4))
model_fit = model.fit()
print(model_fit.summary())

#residuals = model_fit.resid[1:]
#fig, ax = plt.subplots(1,2)
#residuals.plot(title = 'Residuals', ax = ax[0])
#residuals.plot(title='Denisty', kind='kde', ax = ax[1])
#plt.show()

forecast_test = model_fit.forecast(steps = 10)
df_forecast = pd.concat([df, forecast_test + 3], ignore_index=True)
df = df_forecast.copy()



model = ARIMA(df_train, order = (8,1,6))
model_fit = model.fit()
#print(model_fit.summary())
forecast_test = model_fit.forecast(steps = 10)
df_forecast = pd.concat([df, forecast_test + 5], ignore_index=True)
df = df_forecast.copy()



model = ARIMA(df_train, order = (8,1,8))
model_fit = model.fit()
#print(model_fit.summary())
forecast_test = model_fit.forecast(steps = 10)
df_forecast = pd.concat([df, forecast_test + 10], ignore_index=True)
df = df_forecast.copy()



model = ARIMA(df_train, order = (8,1,10))
model_fit = model.fit()
#print(model_fit.summary())
forecast_test = model_fit.forecast(steps = 10)
df_forecast = pd.concat([df, forecast_test + 14], ignore_index=True)
df = df_forecast.copy()


model = ARIMA(df_train, order = (8,1,12))
model_fit = model.fit()
#print(model_fit.summary())
forecast_test = model_fit.forecast(steps = 10)
df_forecast = pd.concat([df, forecast_test + 17], ignore_index=True)
df = df_forecast.copy()
plot_object = df.plot()  # Assuming this line generates the plot
plot_object.set_xlabel("Years from 2019-2069")  # Set x-axis label
plot_object.set_ylabel("Life Expe")  # Set y-axis label
plt.show()

