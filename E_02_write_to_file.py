# create file to hold data (add .txt extension)
file_name = "write_experiment"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# strings to write to file...
heading = "=== MMF Test ===\n"
content = "Random content"


# list of strings...
to_write = [heading, content]

for item in to_write:
    text_file.write(item)