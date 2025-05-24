### **Fizz Buzz** - Write a program that prints the numbers from 1 to 100.But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
numbers = 101
for numbers in range(1,101):
    if numbers%3==0 and numbers%5==0:
        print(numbers,"FizzBuzz")
        # Idk why, but I had to put this "and" comparator in "If". It didn't seem to work when placed elsewhere - i.e. elif
    elif numbers%5==0:
        print(numbers,"Buzz")
    elif numbers%3== 0:
        print(numbers,"Fizz")
    else:
        print(numbers)
# i just googled stuff, and a general rule for checking if a number A is a multiple of a number B, then A/B will return a remainder of 0 (Math).
# So in python, to check multiples of a number is to do a%b, where %==0 (in python, % = "Modulo Operator", returns remainder if A is divided by B)