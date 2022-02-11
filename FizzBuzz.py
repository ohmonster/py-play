#lacks user input
#error boundaries
#tests

#for numbers 1-100, numbers divisible by 5 and 3 display fizzbuzz, by 5 only, buzz, by 3 only fizz, everything else sows the number itself

for num in range(1,101):
    numResult="Fizz" if num%3==0 else ""
    numResult=numResult+"Buzz" if num%5==0 else numResult
    print(str(num) if len(numResult)==0 else numResult)
