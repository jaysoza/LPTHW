formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# 1. I did not enter the correct number of %r characters in the beginning
# 2. The third line contains a single quote character used as an apostrophe; if removed, the output would match the other 3 lines in the poem. Since the single quote character exists in the string, double quotes are used around the entire line output to signal the line is part of a string.