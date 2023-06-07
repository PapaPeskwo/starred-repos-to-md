from pathlib import Path

def get_path():
    path_string = input("Enter folder path: ")
    return Path(path_string).expanduser()

def convert_path(path):
    # If the path is not a Path object, convert it to one
    if not isinstance(path, Path):
        path = Path(path)
    
    # Expand user home directory if '~' is used
    path = path.expanduser()

    # Convert backslashes to forward slashes for compatibility
    path_str = str(path)
    return path_str.replace("\\", "/")
