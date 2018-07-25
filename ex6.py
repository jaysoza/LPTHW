# The line below defines a variable, included is also a decimal replacement
x = "There are %d types of people." % 10

# The line below defines a variable, so that it may be included in a traceback computation
binary = "binary"

# The line below defines a variable, so that it may be included in a traceback computation.
do_not = "don't"

# The line below defined the character 'y' and includes two substitutions, that are executed in order.
y = "Those who know %s and those who %s." % (binary, do_not)

# The two lines below are self explanitory -- display the contents for each character, except both have been assigned a defined value (or string of characters)
print x 
print y

# The two lines below have words to display when executed while at the same time implementing variable replacement.
print "I said: %r." % x
print "I also said: '%s'." % y

# The two lines are reliant on each other; the word hilarious is defined as False; joke_evaluation is substituted for the value it is defined as.  
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# The print expression will output both and combine them.
print joke_evaluation % hilarious

# The two lines define two values; the following print command combines them into one line.
w = "This is the left side of..."
e = "a string with a right side."

print w + e

# 1. Done
# 2. There are 5 instances of a string inside a string.
# 3. Each instance has a single % character next to another variable
# 4. The print function combines all characters within each double-quote -- the output in this case has w ending in an ellipses then e starting with 'a' which makes the output both coherant and longer in size



