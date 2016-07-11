# Program to calculate largest Collatz chain
# Author: Lisa Oh

# Initialize the starting number and length of Collatz sequence
INIT_NUMB = 1
INIT_LENGTH = 1

# Create a length dictionary with initial starting number & length
length_dict = {INIT_NUMB:INIT_LENGTH}

# Function to calculate the next number in the Collatz Sequence
def next_numb(n):

    # If the number is even, the next number is n/2
    if (n%2 == 0):
        n = n/2

    # If the number is odd, the next number is (n*3 +1)
    else:
        n = (n*3 + 1)

    return n

# Function to calculate the sequence length of a starting number
def sequence_length(n):

    # If the number is already in the length dictionary, return it's length
    if n in length_dict:
        return length_dict[n]

    # If not, the number's sequence length is 1 more than the sequence length of the next number
    else:
        length = 1 + sequence_length(next_numb(n))

    # If it wasn't already, put the number's length in the length dictionary and return the length
    length_dict[n] = length
    return length


# Function to calculate which starting number under given number produces the longest Collatz sequence
def longest(n):

    # Initialize length and starting number
    length = INIT_LENGTH
    starting_numb = INIT_NUMB

    # Calculate the sequence length of every number up to given number
    for i in xrange(1,n):
        current = sequence_length(i)
        # Keep track of which starting number produces the longest chain
        if current > length:
            length = current
            starting_numb = i
    # Return that starting number
    return starting_numb




def main():
    print longest(1000000)


main()