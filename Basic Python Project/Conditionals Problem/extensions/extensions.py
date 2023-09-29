file_name = input("File name:").lower().replace(" ", "").split(".")
file_extention = {
    "gif": ["image", "gif"],
    "jpg": ["image", "jpeg"],
    "jpeg": ["image", "jpeg"],
    "png": ["image", "png"],
    "pdf": ["application", "pdf"],
    "txt": ["text", "plain"],
    "zip": ["application", "zip"],
}
if len(file_name) == 1 or not (file_name[-1] in file_extention.keys()):
    print("application/octet-stream")
else:
    a = file_extention[file_name[-1]][0]
    b = file_extention[file_name[-1]][1]
    print(f"{a}/{b}")
