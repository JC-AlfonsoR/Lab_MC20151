all: Camilo.wav mi_voz.png mivoz_fft.png

Camilo.wav : grabar.c
	cc grabar.c
	./a.out

mi_voz.png : Camilo.wav
	python grafica_mi_voz.py
	python fft_de_mi_voz.py
