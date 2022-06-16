# vamos a importar librerías para hacer gráficas de series de tiempos
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import time
import datetime
import matplotlib.dates as mdates
#import matplotlib.ticker as ticker
#import matplotlib.animation as animation
#import matplotlib.dates as mdates
#import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker

#establecemos el directorio de trabajo
os.chdir('/home/osvaldo13576/Documentos/Github/homeworks8th/otros/temp_lcd_sd_t/')
#leemos el archivo temp.txt en este directorio
df = pd.read_csv('TEMP.TXT', sep=',', header=None, names=['date', 'temp'])
#descartamos la primera fila del df
df = df.iloc[1:]
#convertimos la columna date del formato 'hh:mm:ss' a hh:mm:ss
df['date'] = pd.to_datetime(df['date'], format="'%H:%M:%S'")

#convertimos los datos en formato datetime y solo recueperamos las horas, minutos y segundos
df['date'] = df['date'].dt.strftime('%H:%M:%S')
#convertimos lo anterior a minutos
df['date'] = df['date'].str.split(':').apply(lambda x: int(x[0])*60 + int(x[1]) + int(x[2])/60)
#convertimos los datos de temperatura a float
df['temp'] = df['temp'].astype(float)
print(df)
#graficamos
plt.plot(df['date'], df['temp'])
plt.xlabel('Tiempo (min)')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura en el LCD')
plt.savefig('temp.png')
plt.show()
#guardamos la gráfica en formato png



