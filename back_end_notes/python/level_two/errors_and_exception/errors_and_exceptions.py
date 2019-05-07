# Errors and Exceptions

# To open a file use open()
# The second parameter determines what you are doing with the file

# Example
try:
    f = open("simple.txt", "r")
    f.write("Test write to simple text!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA")
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")

print("hello world!")

# Don't need to specify error, can just write except