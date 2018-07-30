from sys import argv, exit

print argv

if len(argv) != 4:
	print "Need to supply 3 arguments!"
	exit(1)

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# READ THE WHOLE LESSON BEFORE PULLING YOUR HAIR OUT TRYING TO UNDERSTAND WHAT WENT WRONG