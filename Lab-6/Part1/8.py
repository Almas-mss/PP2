import  os
path = r"C:\Users\tantr\OneDrive\Рабочий стол\Ерназар\wham.mp4"
isExist = os.access(path, os.F_OK)
if not isExist:
    print("Current directory doesn't exist")
else:
    print("Checks if the path exists",isExist)
    print("Checks if the path readable", os.access(path,os.R_OK))
    print("Checks if the path is writable",os.access(path,os.W_OK))
    print("Checks if the path is executable",os.access(path,os.X_OK))
    if  os.access(path,os.R_OK) and os.access(path,os.W_OK) and os.access(path, os.X_OK):
        os.remove(path)
