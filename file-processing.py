def read_and_write_files(file_name):
    # Read a file, count total and empty lines, handle error if files does not exist
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)

            file.seek(0)  # Reset the file pointer to the start

            total_lines = 0
            empty_lines = 0
            for line in file:
                total_lines += 1
                if line.strip() == "":
                    empty_lines += 1

            print(total_lines)
            print(empty_lines)

    except FileNotFoundError:
        print("Error: File doesn't exist!")


read_and_write_files(r"D:\file-processing1.txt")
