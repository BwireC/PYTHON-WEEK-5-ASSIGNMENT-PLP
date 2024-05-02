# File Creation: We want to create a file called "my_file.txt" and write some initial content into it.

def create_file():
    try:
        # We open/create the file in write mode ('w').
        with open("my_file.txt", "w") as file:
            # Let's write some lines into the file.
            file.write("This is the first line.\n")  # Here's our first line.
            file.write("31415\n")  # This line includes a mix of numbers and characters.
            file.write("Another line with some text and numbers: 10000\n")  # A third line with more content.
    except PermissionError:
        # Uh oh! Looks like we don't have permission to create the file.
        print("Sorry, I don't have permission to create the file.")
    except Exception as e:
        # Oops! Something unexpected happened.
        print("Oops! Something went wrong:", e)
    finally:
        # Regardless of what happened, let's inform the user that we're done creating the file.
        print("File creation process completed.")


# File Reading and Display: Now, let's read the contents of the file and display them.

def read_file():
    try:
        # We open the file in read mode ('r').
        with open("my_file.txt", "r") as file:
            # Great! We're going to read the contents of the file now.
            print("Contents of my_file.txt:")
            # Let's go through each line in the file and print it out.
            for line in file:
                print(line.strip())  # We use strip() to remove any extra spaces or newline characters.
    except FileNotFoundError:
        # Uh oh! Looks like the file doesn't exist.
        print("Oops! I couldn't find the file.")
    except Exception as e:
        # Oops! Something unexpected happened.
        print("Oops! Something went wrong:", e)
    finally:
        # Let's inform the user that we're done reading the file.
        print("File reading process completed.")


# File Appending: Next, let's add some more content to the file.

def append_to_file():
    try:
        # We open the file in append mode ('a').
        with open("my_file.txt", "a") as file:
            # Now, we'll add some more lines to the file.
            file.write("Appending line 1\n")  # Here's the first line we're adding.
            file.write("Appending line 2\n")  # Second line to append.
            file.write("Appending line 3\n")  # Third line to append.
    except PermissionError:
        # Uh oh! Looks like we don't have permission to append to the file.
        print("Sorry, I don't have permission to append to the file.")
    except Exception as e:
        # Oops! Something unexpected happened.
        print("Oops! Something went wrong:", e)
    finally:
        # Let's inform the user that we're done appending to the file.
        print("File appending process completed.")


# Main function to execute all the tasks.

def main():
    # Let's call our functions to perform the tasks.
    create_file()  # First, we'll create the file and write some initial content.
    read_file()    # Next, we'll read the contents of the file and display them.
    append_to_file()  # Finally, we'll add some more content to the file.

# It all starts here! Let's run our main function to kick things off.
if __name__ == "__main__":
    main()
