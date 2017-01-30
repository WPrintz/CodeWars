"""
Sequence generator
https://www.codewars.com/kata/55eee789637477c94200008e
Solved 01-29-2017

Description: 6 kyu

Write a generator sequence_gen ( sequenceGen in JavaScript) that, given the first terms of a sequence will generate a (potentially) infinite amount of terms, where each subsequent term is the sum of the previous x terms where x is the amount of initial arguments (examples of such sequences are the Fibonacci, Tribonacci and Lucas number sequences).

Examples

fib = sequence_gen(0, 1)
fib.next() = 0 # first term (provided)
fib.next() = 1 # second term (provided)
fib.next() = 1 # third term (sum of first and second terms)
fib.next() = 2 # fourth term (sum of second and third terms)
fib.next() = 3 # fifth term (sum of third and fourth terms)
fib.next() = 5 # sixth term (sum of fourth and fifth terms)
fib.next() = 8 # seventh term (sum of fifth and sixth terms)

trib = sequence_gen(0,1,1)
trib.next() = 0 # first term (provided)
trib.next() = 1 # second term (provided)
trib.next() = 1 # third term (provided)
trib.next() = 2 # fourth term (sum of first, second and third terms)
trib.next() = 4 # fifth term (sum of second, third and fourth terms)
trib.next() = 7 # sixth term (sum of third, fourth and fifth terms)

lucas = sequence_gen(2,1)
[lucas.next() for _ in range(10)] = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
Note: You can assume you will get at least one argument and any arguments given will be valid (positive or negative integers) so no error checking is needed."""

def sequence_gen(*args):
    output = []
    if len(output) < len(args):
        for i in args:
            output.append(i)
            yield output[-1]
    while True:
        sumup = sum(output[-len(args):])
        output.append(sumup)
        output.pop(0)
        yield output[-1]