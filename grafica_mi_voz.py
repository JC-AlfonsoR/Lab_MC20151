# -*- coding: utf-8 -*-
"""

@author: jc
"""

import numpy as np
import matplotlib.pyplot as plt
import scikits.audiolab as audio


import sys
print(sys.version + "\n")

#Leer la sennal del wav
input_signal, sampling_rate, enc = audio.wavread("Camilo.wav")
print (input_signal[0:100000]), sampling_rate, enc

print(np.shape(input_signal))
dt = 1.0/(sampling_rate) # Periodo de muestreo
n = len(input_signal) # Numero de muestras
t = np.linspace(0,n*dt,n) # tiepo [s]

c = len(input_signal[0,:])
f = plt.figure(figsize=(18,5))

for i in range(c):
    plt.subplot(1,c,i+1)
    plt.plot(t,input_signal[:,i],alpha=0.6)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.title("Sennal " + str(i))
    plt.grid()
    
f.savefig('mi_voz.png',dpi=100) # Guardar imagen
print('\n\nPrograma Finalizado\n')