CC=gcc
CFLAGS=-g -Wall
SOURCES= part1.c part2.c part3.c part4.c
RM= rm -rf

all: part1.exe part2.exe part3.exe part4.exe

part1.exe: part1.c
	$(CC) $(CFLAGS) -o part1.exe part1.c

part2.exe: part2.c
	$(CC) $(CFLAGS) -o part2.exe part2.c

part3.exe: part3.c
	$(CC) $(CFLAGS) -o part3.exe part3.c

part4.exe: part4.c
	$(CC) $(CFLAGS) -o part4.exe part4.c

clean:
	$(RM) part1.exe part2.exe part3.exe part4.exe
