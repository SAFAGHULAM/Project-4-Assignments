import os

folder = input("Enter folder path: ")
prefix = input("Enter filename prefix: ")

files = os.listdir(folder)
for count, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1]  # keeps file extension
    new_name = f"{prefix}_{count}{ext}"
    
    src = os.path.join(folder, filename)
    dst = os.path.join(folder, new_name)
    
    os.rename(src, dst)
    print(f"Renamed: {filename} → {new_name}")
