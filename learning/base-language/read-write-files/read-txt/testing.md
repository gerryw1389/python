

print('getcwd:      ', os.getcwd())

print('__file__:    ', __file__)

print('basename:    ', os.path.basename(__file__))


print('dirname:     ', os.path.dirname(__file__))

path = str(sys.argv[0])

print(f"Path is {path}")

split = os.path.split(path)

print(f"split path is: {split}")

dir_name = split[0]

print(f"Dir name is : {dir_name}")

os.chdir(dir_name)

https://diveintopython3.net/comprehensions.html