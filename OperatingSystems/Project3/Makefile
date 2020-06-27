CC=gcc
CFLAGS=-g -pthread -Wall
SOURCES= quacker.c
RM= rm -rf

all: server.exe

server.exe: quacker.c
	$(CC) $(CFLAGS) -o server.exe quacker.c

clean:
	$(RM) server.exe
