import os


base_path = os.path.dirname(__file__)
filename = os.path.join(base_path, "text_data.txt")

# Q1: Write a program to read the entire content from a txt file and display it to the user.
print("\n--- Q1: Display entire file content ---")
with open(filename, "r") as f:
    data = f.read()
print(data)

# Q2: Write a program to read first n lines from a txt file. Get n as user input.
print("\n--- Q2: Read first n lines ---")
n = int(input("Enter number of lines to read: "))
with open(filename, "r") as f:
    for i in range(n):
        line = f.readline()
        if not line:
            break
        print(line, end="")

# Q3: Write a program to accept input from user and append it to a txt file.
print("\n\n--- Q3: Append text to file ---")
new_text = input("Enter text to append: ")
with open(filename, "a") as f:
    f.write(new_text + "\n")
print("Text appended to", filename)

# Q4: Write a program to read contents from a txt file line by line and store each line into a list.
print("\n--- Q4: Store lines into a list ---")
lines_list = []
with open(filename, "r") as f:
    for line in f:
        lines_list.append(line.strip())
print(lines_list)

# Q5: Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
print("\n--- Q5: Find longest word ---")
with open(filename, "r") as f:
    words = f.read().split()
longest = max(words, key=len)
print("Longest word:", longest)

# Q6: Write a program to count the frequency of a user entered word in a txt file.
print("\n--- Q6: Count frequency of a word ---")
word_to_count = input("Enter a word to count: ").lower()
with open(filename, "r") as f:
    words = f.read().lower().split()
count = words.count(word_to_count)
print(f"The word '{word_to_count}' appears {count} times.")
