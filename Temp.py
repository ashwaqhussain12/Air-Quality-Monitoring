
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
#temp.y.plot()
plt.plot(temp.y)
print(temp.head())

# initializing the fbprophet model and fitting the data
model = Prophet()
model.add_regressor(data3['PRES']) #her i am getting an error ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
#model.add_regressor('DEWP')
#model.add_regressor('TEMP')
#model.add_regressor('IWS')
model.fit(temp)

#creating a separate dataframe for predicted values
future_data = model.make_future_dataframe(periods=12, freq = 'm')
forecast_data = model.predict(future_data)

print(forecast_data[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

#print(type(data3))
