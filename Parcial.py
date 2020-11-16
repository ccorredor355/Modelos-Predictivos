# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib as plt
from datetime import datetime
from statsmodels.tsa.stattools import adfuller

TRMd=pd.read_excel('1.1.1.TCM_Serie histórica IQY.xlsx',skiprows=8, header=None,
                   usecols="A,B",names=["Fecha","TRM"],
                   index_col='Fecha').dropna()

#  Convierte los indices al tipo de dato datetime
TRMd.index = pd.to_datetime(TRMd.index)
# Agrupa los valores correpsondiente al ultimo dia de cada mes
TRMm= TRMd.groupby([TRMd.index.year, TRMd.index.month]).tail(1)
TRMm= TRMm.loc['2008':]

TRMm1=TRMm.loc[:'2018-12']
TRMm2=TRMm.loc['2019':'2019-09']

pruebaTRMm=adfuller(TRMm['TRM'])

TRM_estacionaria=TRMm.diff().dropna()
pruebaTRM_estacionaria=adfuller(TRM_estacionaria['TRM'])

#TRM_estacionaria.plot()

TRMm.plot()
TRMd.info()
