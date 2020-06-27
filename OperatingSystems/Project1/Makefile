CC=gcc
OBJECTS=command.o main.o
TARGET=pseudo-shell
SOURCES=command.c main.c
RM= rm -rf

all: $(TARGET)

pseudo-shell: $(OBJECTS)
	$(CC) -o $(TARGET) $^

main.o: main.c
command.o: command.c

clean:
	$(RM) $(OBJECTS) $(TARGET)
