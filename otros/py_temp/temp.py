# vamos a importar librerías para hacer gráficas de series de tiempos
import matplotlib.pyplot as plt
import matplotlib as mpl
label_size = 7
mpl.rcParams['xtick.labelsize'] = label_size
mpl.rcParams['ytick.labelsize'] = label_size
import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import os
import time
import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
#import matplotlib.animation as animation
#import matplotlib.dates as mdates
#import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker

#establecemos el directorio de trabajo
archivo = 'TEMP_1.TXT'
os.chdir('/home/osvaldo13576/Documentos/Github/homeworks8th/otros/py_temp/')
#leemos el archivo temp.txt en este directorio
df = pd.read_csv(archivo, sep=',', header=None, names=['date', 'temp'])
#descartamos la primera fila del df
df = df.iloc[1:]
#convertimos la columna date del formato 'hh:mm:ss' a hh:mm:ss
df['date'] = pd.to_datetime(df['date'], format="'%H:%M:%S'")

#convertimos los datos en formato datetime y solo recueperamos las horas, minutos y segundos
df['date'] = df['date'].dt.strftime('%H:%M:%S')
#convertimos lo anterior a minutos
df['date'] = df['date'].str.split(':').apply(lambda x: int(x[0])*60 + int(x[1]) + int(x[2])/60)
#restemos el tiempo inicial a todo el vector de tiempo
df['date'] = df['date'] - df['date'][1]
#convertimos los datos de temperatura a float
df['temp'] = df['temp'].astype(float)
print(df)
#graficamos
letra = 8
fig, ax = plt.subplots()
plt.figure(figsize=(2,2))
plt.plot(df['date'], df['temp'], color='green', linewidth=0.2,marker='.',markersize=0.2)
plt.xlabel('Tiempo (min)',fontsize=letra)
plt.ylabel('Temperatura (°C)',fontsize=letra)
plt.title('Temperatura ambiente (agua)',fontsize=letra)
plt.ylim(20,25) 
plt.grid()
#guardamos la gráfica en el directorio de trabajo
plt.savefig('temp_agua.pdf')
plt.show()

