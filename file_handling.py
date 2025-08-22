def modify_file_content(content):
    """
    Example modification: convert text to uppercase.
    You can change this function to do other modifications.
    """
    return content.upper()


def main():
    # Ask user for input file name
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")


if __name__ == "__main__":
    main()
