def read_and_write():
    try:
        # Ask the user for the input filename
        input_file = input("Enter the filename to read: ")

        # Try opening the file in read mode
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Ask the user for the output filename
        output_file = input("Enter the filename to write the modified content: ")

        # Write the modified content to a new file
        with open(output_file, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Successfully wrote modified content to {output_file}")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: The file could not be read or written to.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write()
