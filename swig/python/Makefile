# $Id: Makefile,v 1.1 2004/11/29 22:10:48 jose Exp $

all: distance.so

distance_wrap.o: ../distance.i
	swig -python -v -o distance_wrap.c ../distance.i
	gcc -c -I../.. -I/usr/local/include/python2.3 -fpic distance_wrap.c

distance.so: distance_wrap.o
	gcc -shared distance_wrap.o ../../libdistance.a -o distance.so
	mv distance.so _distance.so

clean:
	rm -f *.o distance_wrap.c *.so *.core *_wrap.c distance.py
