import pandas as pd 
import matplotlib.pyplot as plt 
from pandas.plotting import register_matplotlib_converters
import matplotlib.dates as mdates

register_matplotlib_converters()

excl = pd.read_csv('./datasets/EXCL.JK.csv', index_col=['Date'], parse_dates=['Date'])

# mengambil data untuk bulan April saja
excl = excl.loc['2019-04']
excl = excl.reset_index()

# mengisi data-data kosong saat hari libur bursa
r = pd.date_range(start=excl['Date'].min(), end=excl['Date'].max())
excl = excl.set_index('Date').reindex(r).fillna(method='bfill', axis=0).rename_axis('Date')

fren = pd.read_csv('./datasets/FREN.JK.csv', index_col=['Date'], parse_dates=['Date'])
fren = fren.loc['2019-04']
fren = fren.reset_index()
fren = fren.set_index('Date').reindex(r).fillna(method='bfill', axis=0).rename_axis('Date')

isat = pd.read_csv('./datasets/ISAT.JK.csv', index_col=['Date'], parse_dates=['Date'])
isat = isat.loc['2019-04']
isat = isat.reset_index()
isat = isat.set_index('Date').reindex(r).fillna(method='bfill', axis=0).rename_axis('Date')

tlkm = pd.read_csv('./datasets/TLKM.JK.csv', index_col=['Date'], parse_dates=['Date'])
tlkm = tlkm.loc['2019-04']
tlkm = tlkm.reset_index()
tlkm = tlkm.set_index('Date').reindex(r).fillna(method='bfill', axis=0).rename_axis('Date')

# print(excl)
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(12,8))
plt.plot(excl.loc['2019-04'].index, excl.loc['2019-04']['Close'])
plt.plot(fren.loc['2019-04'].index, fren.loc['2019-04']['Close'])
plt.plot(isat.loc['2019-04'].index, isat.loc['2019-04']['Close'])
plt.plot(tlkm.loc['2019-04'].index, tlkm.loc['2019-04']['Close'])
plt.title('Harga Historis Saham Provider Telco Indonesia (April 2019)')

labels = excl['2019-04'].index
plt.xticks(ticks=labels, labels=labels.date, rotation=35, fontsize=8)
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')

legends = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(legends, bbox_to_anchor=(0., 1.0, 1., .102), loc=9, ncol=4, mode="expand", borderaxespad=0.)

plt.show()