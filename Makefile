all: rodcut

CC = gcc
CFLAGS = -Wall

rodcut: rodcut.o 
	gcc -o rodcut $(CFLAGS) rodcut.o 

rodcut.o: rodcut.c 

clean:
	rm -f rodcut *.o
