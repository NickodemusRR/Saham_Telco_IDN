import pandas as pd 
import matplotlib.pyplot as plt 

excl = pd.read_csv('EXCL.JK.csv', index_col=False, parse_dates=['Date'])
fren = pd.read_csv('FREN.JK.csv', index_col=False, parse_dates=['Date'])
isat = pd.read_csv('ISAT.JK.csv', index_col=False, parse_dates=['Date'])
tlkm = pd.read_csv('TLKM.JK.csv', index_col=False, parse_dates=['Date'])

# print(excl.head())

plt.style.use('seaborn-darkgrid')
plt.plot(excl['Date'], excl['Close'])
plt.plot(fren['Date'], fren['Close'])
plt.plot(isat['Date'], isat['Close'])
plt.plot(tlkm['Date'], tlkm['Close'])
plt.title('Harga Historis Saham Provider Telco Indonesia')

plt.xticks(rotation=30)
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
legends = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(legends, loc=9, mode='expand', ncol=4)

plt.show()