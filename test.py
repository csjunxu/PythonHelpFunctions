import os

path = 'DIV2K'

for root, dirs, files in os.walk(path):
    print("Root = ", root, "dirs = ", dirs, "files = ", files)