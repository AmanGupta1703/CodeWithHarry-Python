#  What are DocStrings?
#  DocStrings are the first line of a function, class, method, or module.
#  They are used to describe what the function, class, method, or module does.
#  They are surrounded by triple quotes.
#  They are used to help other people understand your code.

def square(n):
    """This function returns the square of the number passed to it."""  # It should be the first line of the function. Otherwise, it won't work.
    print(n ** 2)


# Comment VS DocString
# Comment: # This function returns the square of the number passed to it. It helps other people understand your code.
# DocString: """This function returns the square of the number passed to it."""
# It defines what a function does. Comments can't be accessed at runtime, but DocStrings can be accessed at runtime.


square(2)

# How to print DocString??
print(square.__doc__)

# What is PEP 8?
# PEP 8 is a set of guidelines for how to format Python code.
# It was written by Guido van Rossum, Barry Warsaw, and Nick Coagulant.
# PEP stands for Python Enhancement Proposal.
