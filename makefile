CXX = g++

#CXXFLAGS = -std=c++11 -Wall -Wextra -Werror -g
CXXFLAGS = -std=c++11  -g -O0

SpaceSaving: SpaceSaving.o main.o
	${CXX} $^ -o $@

interSS: interSS.o main.o
	${CXX} $^ -o $@

clean:
	/bin/rm -f SpaceSaving *.o