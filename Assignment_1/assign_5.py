count = 0
unique_emails = set()  # Set to store unique email addresses

with open("D:\PythonFiles\Assignment_1\mbox-short.txt", 'r') as file:
    for line in file:
        if line.startswith("From "):  # Ensure it only counts "From ", not "From:"
            words = line.split()
            if len(words) > 1:  # Ensure there is an email in the line
                email = words[1]
                if email not in unique_emails:
                    unique_emails.add(email)  # Add email to set
                    print(email)
                    count += 1

print(f"\nTotal unique count is {count}")
