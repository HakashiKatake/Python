src = input("Enter the source filename: ")
dest = input("Enter the destination filename: ")
with open(src, 'r') as file_src, open(dest, 'w') as file_dest:
    file_dest.write(file_src.read())