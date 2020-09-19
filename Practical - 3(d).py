class Fact:
    def init(self, number):
        self.number = number

    def factorial_iteration(self):
        factorial = 1
        if self.number < 0:
            raise Exception("Factorial of Negative number doesn't exist")
        elif self.number == 0:
            return factorial
        else:
            for i in range(1, self.number + 1):
                factorial = factorial * i
            return factorial

    def factorial_recursion(self, number=None):
        if number is None:
            number = self.number
        if number < 0:
            raise Exception("Factorial of Negative number doesn't exist")
        elif number == 0 or number == 1:
            return 1
        else:
            return number * self.factorial_recursion(number - 1)

    def factors_iteration(self):
        factors = []
        for i in range(1, self.number + 1):
            if self.number % i == 0:
                factors.append(i)
        return factors

    def factors_recursion(self, number=None, lst=None):
        factorial = self.number
        if number is None and lst is None:
            number = self.number
            lst = []
        if number == 0 or number < 0:
            return lst
        elif number == 1:
            lst.append(1)
            return sorted(lst)
        elif factorial % number == 0:
            lst.append(number)
            return self.factors_recursion(number - 1, lst)
        else:
            return self.factors_recursion(number - 1, lst)


if name == 'main':
    fact = Fact(int(input("Enter a number: ")))
    print(fact.factorial_iteration())
    print(fact.factorial_recursion())
    print(fact.factors_iteration())
    print(fact.factors_recursion())
