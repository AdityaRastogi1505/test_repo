def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    try:
        with open(filename, 'w') as file:
            file.write(user_input + '\n')
        print("✅ Initial content written successfully.")
    except Exception as e:
        print(f"❌ Error writing to file: {e}")

def append_to_file(filename):
    additional_input = input("Enter additional text to append: ")
    try:
        with open(filename, 'a') as file:
            file.write(additional_input + '\n')
        print("✅ Additional content appended successfully.")
    except Exception as e:
        print(f"❌ Error appending to file: {e}")

def read_file(filename):
    try:
        print("\n📄 Final content of the file:")
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"❌ The file '{filename}' does not exist.")
    except Exception as e:
        print(f"❌ Error reading the file: {e}")

# Main execution
file_name = 'output.txt'
write_to_file(file_name)
append_to_file(file_name)
read_file(file_name)