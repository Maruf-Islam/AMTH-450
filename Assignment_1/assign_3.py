unique_words = set()

file = open(r'D:\PythonFiles\AMTH-450\Assignment_1\amth.txt')
for line in file:  # Read line by line
        line = line.rstrip()
        words = line.split()
        for word in words:
            if word:
                unique_words.add(word)  # Using a set avoids duplicates automatically

# Convert to a sorted list
sorted_words = sorted(unique_words)

# Print the result
print("\n".join(sorted_words))
