makerfuncs: file.o main.o
	g++ file.o main.o -o makerfuncs

file.o: file.cpp
	g++ -c file.cpp

main.o: main.cpp
	g++ -c main.cpp

clean:
	rm *.o makerfuncs