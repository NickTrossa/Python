import os
path = os.path
print(path)

currentpath = os.getcwd()
print(currentpath)

print(os.path.dirname(os.path.realpath("testdirectorio.py")))

print(os.path.realpath("testdirectorio.py"))

print("##########################")

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file directory and name")
path, file = os.path.split(full_path)
print(path + ' --> ' + file + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

print(bpy.context.space_data.text.filepath)


