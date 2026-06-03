import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working = os.path.abspath(working_directory)
        abs_file = os.path.normpath(os.path.join(abs_working, file_path))
    
        if os.path.commonpath([abs_working, abs_file]) != abs_working:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(abs_file), exist_ok=True)

        with open(abs_file, "w") as f:
            f.write(content)

        return(f'Successfully wrote to "{file_path} ({len(content)} characters written)')
    except Exception as e:
        return f'Error writing file: {e}'
