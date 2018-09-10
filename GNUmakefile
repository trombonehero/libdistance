# $Id: GNUmakefile,v 1.5 2004/11/29 21:48:08 jose Exp $
#
# GNU Makefile, should work on mingw and other GNU make systems.

AR	?=	ar
ARFLAGS	=	crs
CFLAGS	+=	-g -fPIC

SRCS=	levenshtein.c hamming.c bloom.c needleman_wunsch.c jaccard.c \
	minkowski.c damerau.c
OBJS=	levenshtein.o hamming.o bloom.o needleman_wunsch.o jaccard.o \
	minkowski.o damerau.o

libdistance.a: ${SRCS}
	${CC} ${CFLAGS} -c -I. levenshtein.c
	${CC} ${CFLAGS} -c hamming.c
	${CC} ${CFLAGS} -c bloom.c
	${CC} ${CFLAGS} -c needleman_wunsch.c
	${CC} ${CFLAGS} -c jaccard.c
	${CC} ${CFLAGS} -c minkowski.c
	${CC} ${CFLAGS} -c damerau.c
	${AR} ${ARFLAGS} libdistance.a ${OBJS}

clean:
	${RM} libdistance.a libdistances.so ${OBJS} *.core
