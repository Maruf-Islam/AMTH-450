filename = "D:\PythonFiles\AMTH-450\Assignment_1\mbox.txt"

try:
    with open(filename, "r") as file:
        sender_counts = {}

        for line in file:
            if line.startswith("From "):
                sender = line.split()[1]  # Extract email
                sender_counts[sender] = sender_counts.get(sender, 0) + 1

    # Find the most prolific sender
    max_sender = max(sender_counts, key=sender_counts.get, default=None)

    if max_sender:
        print(f"Most prolific sender: {max_sender} with {sender_counts[max_sender]} messages")
    else:
        print("No emails found in the file.")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
