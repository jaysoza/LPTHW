tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

		
#1 escape sequences inserted into another .txt file
#2 no difference observed, talked to moshe and came up w 'single quotes look neater'.
#3 results for: combining escape sequences and format strings to create a more complex format:

test_output = """
Let's see what happens when I do this:
\v up up and away!
\t\v aaaaaaaah TOO HIGH
"""

print test_output