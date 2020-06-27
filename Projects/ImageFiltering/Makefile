CXX=g++
CXXFLAGS=-W -Wall -g
TARGETS=img
SOURCES=$(wildcard *.c)
DIRS=output
OBJECTS=main.o IO.o filter.o matrix.o
RM= rm -rf

all: $(TARGETS)

img : $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o img
	mkdir -p $(DIRS)

main.o: main.cpp
IO.o: IO.cpp hdrs/IO.hh
filter.o: filter.cpp hdrs/filter.hh
matrix.o: matrix.cpp hdrs/matrix.hh

clean: 
	$(RM) $(OBJECTS) $(TARGETS) $(DIRS)
