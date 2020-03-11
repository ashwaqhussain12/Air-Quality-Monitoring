
import pandas as pd
import numpy as np
import plotly
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

import warnings
warnings.filterwarnings("ignore")

from fbprophet import Prophet

data3 = pd.read_csv('PRSA_data.csv')
#data3 = data3.PM_2point5.fillna(72, inplace=True)
#print(data3.head())
data3['datep'] = data3[data3.columns[1:4]].apply(lambda x: '-'.join(x.astype(str)),axis=1)

data5 = pd.read_csv('PRSA_data.csv', parse_dates = [['year', 'month', 'day', 'hour']])

#templst = list(data3['PRES'])
#print(templst)
#dfp = pd.DataFrame(templst)

temp = data3[['datep','pm2.5']]
temp.columns = ['ds','y']
temp['PRES'] = data3['PRES']
temp['DEWP'] = data3['DEWP']
temp['TEMP'] = data3['TEMP']
temp['Iws'] = data3['Iws']

#temp.y.plot()
plt.plot(temp.y)
print(temp.head())

# initializing the fbprophet model and fitting the data
model = Prophet()
#model.add_regressor('PRES', standardize = "auto", mode='additive')
model.add_regressor('PRES')
#model.add_regressor('DEWP')
#model.add_regressor('TEMP')
#model.add_regressor('IWS')
model.fit(temp)


temp_pres = data3[['datep', 'PRES']]
temp_pres.columns = ['ds','y']

# initializing the fbprophet model and fitting the data
model = Prophet()
model.fit(temp_pres)

#creating a separate dataframe for predicted values
future_data_pres = model.make_future_dataframe(periods=12, freq = 'm')
forecast_data_pres = model.predict(future_data_pres)

def pres_temp(ds):
    date = (pd.to_datetime(ds)).date()
    
    if temp[date:].empty:
        return (forecast_data_pres[date:]['yhat']).values[0]
    else:
        return (temp[date:]['PRES']).values[0]
    
    return 0

#print(forecast_data_pres.head())

#creating a separate dataframe for predicted values
future_data = model.make_future_dataframe(periods=12, freq = 'm')
future_data['PRES'] = future_data['ds'].apply(pres_temp)
#forecast_data = model.predict(future_data.drop(columns='y'))
forecast_data = model.predict(future_data)

print(forecast_data[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
