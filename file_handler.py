# Prompt the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Attempt to open and read the file
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    # Proceed if no errors occurred
    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Create a new filename (e.g., modified_original.txt)
    new_filename = f"modified_{filename}"

    # Write the modified content to a new file
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Success! Modified file saved as '{new_filename}'.")
    except PermissionError:
        print(f"Error: No permission to write to '{new_filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")
        