class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value%2!=0

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value%2==0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        return len([i for i in range(1,self.value) if self.value%i==0])<3
        

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        return [i for i in range(1,self.value) if self.value%i==0]

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len([int(i) for i in str(self.value)])

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        sum=0
        for i in str(self.value):
            sum+=int(i)
        return sum

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        const=1
        number=0
        ls=[i for i in str(self.value)]
        for i in ls:
            number+=int(i)*const
            const*=10
        return number

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        const=1
        number=0
        ls=[i for i in str(self.value)]
        for i in ls:
            number+=int(i)*const
            const*=10
        return number==self.value

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return [int(i) for i in str(self.value)]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max([int(i) for i in str(self.value)])

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min([int(i) for i in str(self.value)])

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return sum([int(i) for i in str(self.value)])/len(str(self.value))

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        x = ([int(i) for i in str(self.value)])
        if len(x)%2==0:
            return [x[len(x)//2-1],x[len(x)//2]]

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return [min([int(i) for i in str(self.value)]),max([int(i) for i in str(self.value)])]
        

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        x=[int(i) for i in str(self.value)]
        d=dict()
        for i in x:
            d[i]=str(self.value).count(f"{i}")
        return d
    

# Create a new instance of Number
number = Number(2436)
print(number.get_range())

