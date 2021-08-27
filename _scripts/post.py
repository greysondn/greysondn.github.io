#!/env/python
import time
import os

from subprocess import call

# path to
pathTo = "../_posts/"

# get post title
postTitle = input('Enter a title:\n--> ')

# generate file name
fileName = time.strftime("%Y-%m-%d-%H-%M")
fileName = fileName + "-" + postTitle.lower()
fileName = fileName.replace(" ", "-")
fileName = fileName + ".md"

# open file
file = open((pathTo + fileName), 'w')

# write front matter to file...
# ... opening dashes ...
file.write('---')
file.write('\n')

# ... layout ...
file.write("layout:     ")
file.write("post")
file.write("\n")

# ... title ...
file.write("title:      ")
file.write('"' + postTitle + '"')
file.write("\n")

# ... date ...
file.write("date:       ")
file.write(time.strftime("%Y-%m-%d %H:%M"))
file.write("\n")

# ... categories ...
file.write("categories: ")
file.write("[uncategorized]")
file.write("\n")

# ... tags ...
file.write("tags:       ")
file.write("[untagged]")
file.write("\n")

# ... published status ...
file.write("published:  ")
file.write("true")
file.write("\n")

# ... source ...
file.write("source:     ")
file.write("greysondn-ghp"       )
file.write("\n")

# ... closing dashes
file.write("---")
file.write("\n\n\n")

# close file
file.close()

# output filename
print("\n\n-----\n")
print("File seeded at:\n\n")
print((os.path.abspath(pathTo + fileName)) + "\n")
print("------\n\n")
