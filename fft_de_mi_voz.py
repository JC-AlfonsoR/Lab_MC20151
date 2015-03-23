# -*- coding: utf-8 -*-
"""

@author: jc
"""

import numpy as np
import matplotlib.pyplot as plt
import scikits.audiolab as audio
from scipy.fftpack import fft, fftfreq


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

F = np.zeros(np.shape(input_signal)) # prealocacion para transformada de Fourier
# Calcular transformada de Fourier
for i in range(c):
    F[:,i] = fft(input_signal[:,i])/n
#Calcular frecuencias
freq = fftfreq(n,dt)


# para calcular los maximos hago uso de esta funcion con licencia open source
# La funcion esta disponible en https://gist.github.com/endolith/250860
# Al usar 
# maxtab,mintab = peakdet(v,delta,x)
# maxtab es un array nx2. En la segunda columna de maxtab se encuentran los valores maximos locales de v
# tales que son mayores 'delta' unidades que sus vecinos mas cercanos. En la primera columna se maxtab
# se almacenan los valores de 'x' que corresponden a los mismos indices de los maximos hallados en 'v'.
# mintab funciona igual que maxtab, solo que almacena los valores de los minimos locales
from numpy import NaN, Inf, arange, isscalar, asarray, array

def peakdet(v, delta, x = None):
    """
    Converted from MATLAB script at http://billauer.co.il/peakdet.html
    
    Returns two arrays
    
    function [maxtab, mintab]=peakdet(v, delta, x)
    %PEAKDET Detect peaks in a vector
    %        [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
    %        maxima and minima ("peaks") in the vector V.
    %        MAXTAB and MINTAB consists of two columns. Column 1
    %        contains indices in V, and column 2 the found values.
    %      
    %        With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
    %        in MAXTAB and MINTAB are replaced with the corresponding
    %        X-values.
    %
    %        A point is considered a maximum peak if it has the maximal
    %        value, and was preceded (to the left) by a value lower by
    %        DELTA.
    
    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.
    
    """
    maxtab = []
    mintab = []
       
    if x is None:
        x = arange(len(v))
    
    v = asarray(v)
    
    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')
    
    if not isscalar(delta):
        sys.exit('Input argument delta must be a scalar')
    
    if delta <= 0:
        sys.exit('Input argument delta must be positive')
    
    mn, mx = Inf, -Inf
    mnpos, mxpos = NaN, NaN
    
    lookformax = True
    
    for i in arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]
        
        if lookformax:
            if this < mx-delta:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn+delta:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    return array(maxtab), array(mintab)


d = n*10/10000*np.mean(abs(F[:,0]))
#El parametro 'd' sirve para elegir los maximos que tengan una diferencia de almenos 'd' unidades respecto
# a los vecinos mas cercanos. 
# Elijo d = n*15./10e4 esperando obtener del orden de 15 maximos por cada 10000 datos en la señal
f1 = plt.figure(figsize=(18,8))
for i in range(c):
    maxtab, mintab = peakdet(abs(F[:,i]),d,freq)
    plt.subplot(c,1,i)
    plt.plot(freq,abs(F[:,i]))
    plt.plot(maxtab[:,0],abs(maxtab[:,1]),'ro')
    plt.xlim(0,1000)
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Amplitud")
    plt.title("Sennal " + str(i))

f1.savefig('mivoz_fft.png',dpi=100) # Guardar imagen
print('\n\nPrograma Finalizado\n')