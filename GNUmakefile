# $Id: GNUmakefile,v 1.5 2004/11/29 21:48:08 jose Exp $
#
# GNU Makefile, should work on mingw and other GNU make systems.

SRCS=	levenshtein.c hamming.c bloom.c needleman_wunsch.c jaccard.c \
	minkowski.c damerau.c
OBJS=	levenshtein.o hamming.o bloom.o needleman_wunsch.o jaccard.o \
	minkowski.o damerau.c

libdistance.a: ${SRCS}
	gcc -g -c -I. levenshtein.c
	gcc -g -c hamming.c
	gcc -g -c bloom.c
	gcc -g -c needleman_wunsch.c
	gcc -g -c jaccard.c
	gcc -g -c minkowski.c
	gcc -g -c damerau.c
	ar cq libdistance.a ${OBJS}

clean:
	rm -f libdistance.a libdistances.so ${S_OBJS} ${OBJS} *.core
