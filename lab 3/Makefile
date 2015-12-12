figure.png: plotfile.py data.txt
	python plotfile.py data.txt

data.txt: tabulatesin
	./tabulatesin > data.txt

tabulatesin: tabulatesin.c
	gcc -Wall -pedantic -ansi tabulatesin.c -o tabulatesin -lm

clean:
	rm data.txt tabulatesin

plotfile.py:
	wget http://www.soton.ac.uk/~feeg6002/tools/plotfile2.py
	mv plotfile2.py plotfile.py
