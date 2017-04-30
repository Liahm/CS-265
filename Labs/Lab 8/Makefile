#Name: Eric Lee
#Date: 11/13/2016
#Purpose: A make file that compiles C, python and Java and runs them

#Q1
cc = gcc
EXE = foo
JAVAC = javac
JRE = java
PAGER = less
TEST_OUT = test.out
EXP_OUT = expected.out

#Notes - It took me an hour to figure out that TAB was needed for it to work
#correctly. Yea, simple mistake.
#Q13
.PHONY: clean run-py run-c read run-java save-java test-java
#Q2
foo.o : foo.c foo.h
	$(cc) -c foo.c
#Q3
main.o : main.c foo.h
	$(cc) -c main.c
#Q4
$(EXE) : foo.o main.o
	$(cc) -o$(EXE) main.o foo.o
#Q5
run-c : $(EXE)
	./$(EXE)
#Q6
run-py : foo.py
	./foo.py
#Q7
read : README
	$(PAGER) README
#Q8
foo.class : foo.java
	$(JAVAC) foo.java
#Q9
run-java : foo.class
	$(JRE) foo
#Q10
save-java : 
	$(JRE) foo > $(TEST_OUT)
#Q11
test-java :
	-@if diff $(TEST_OUT) $(EXP_OUT) &> /dev/null ; then \
		echo "Passed!" ;\
	else \
		echo "Not the same!" ;\
	fi
#Q12
clean :
	rm -rf foo.o main.o foo.class $(EXE) test.out
