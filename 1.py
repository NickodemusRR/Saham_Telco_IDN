import pandas as pd 
import matplotlib.pyplot as plt 
from pandas.plotting import register_matplotlib_converters
import matplotlib.dates as mdates

register_matplotlib_converters()

excl = pd.read_csv('EXCL.JK.csv', index_col=False, parse_dates=['Date'])
fren = pd.read_csv('FREN.JK.csv', index_col=False, parse_dates=['Date'])
isat = pd.read_csv('ISAT.JK.csv', index_col=False, parse_dates=['Date'])
tlkm = pd.read_csv('TLKM.JK.csv', index_col=False, parse_dates=['Date'])

# print(excl.head())

plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(10,6))
ax = plt.subplot()
plt.plot(excl['Date'], excl['Close'])
plt.plot(fren['Date'], fren['Close'])
plt.plot(isat['Date'], isat['Close'])
plt.plot(tlkm['Date'], tlkm['Close'])
ax.set_title('Harga Historis Saham Provider Telco Indonesia')

plt.xticks(rotation=60)
ax.set_xlabel('Tanggal')
ax.set_ylabel('Rupiah (IDR)')
legends = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(legends, bbox_to_anchor=(0., 1.0, 1., .102), loc=9, ncol=4, mode="expand", borderaxespad=0.)
ticks = pd.date_range(start='20190315', end='20190616', freq='W', name='point')
myFmt = mdates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(myFmt)
plt.xticks(ticks, rotation=15)
plt.show()