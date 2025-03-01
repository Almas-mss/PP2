import os

put = r"/Users/ulpanmusaeva/PycharmProjects/PP2/Lab-6/Part1"

isExist = os.path.exists(put)
print(f'"Path {put} is {isExist}')
if isExist:
    print(f"PathName: {os.path.dirname(put)}")
    print(f"DirName: {os.path.basename(put)}")