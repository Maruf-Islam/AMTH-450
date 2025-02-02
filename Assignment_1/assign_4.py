#file_name = input("Enter file name : ")
file_name = 'D:\PythonFiles\Assignment_1\mbox.txt'
total = 0.0
count = 0

try:
    with open(file_name,'r') as file:
        for line in file:
            if line.startswith('X-DSPAM-Confidence:'):
                try:
                    value = float(line.split(":")[1].strip())
                    total += value
                    count += 1
                except ValueError:
                    continue
    if count > 0:
        print(f"Average spam confidence is : {total / count :.4f}")
        print(f"This number of this line is {count}")
    else:
        print("No Valid value found")
except FileNotFoundError:
    print(f"Error: file '{file_name}' not found.")
except Exception as e:
    print(f"An error ouccured: {e}")