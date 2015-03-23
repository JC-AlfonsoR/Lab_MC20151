all: Camilo.wav mi_voz.png mivoz_fft.png nuevo.wav

Camilo.wav : grabar.c
	cc grabar.c
	./a.out

mi_voz.png : Camilo.wav
	python grafica_mi_voz.py
	
mivoz_fft.png : Camilo.wav	
	python fft_de_mi_voz.py

nuevo.wav : Camilo.wav	
	python Cambia_frecuencia.py