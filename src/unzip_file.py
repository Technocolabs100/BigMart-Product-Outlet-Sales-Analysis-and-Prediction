import zipfile
import os

def unzip_file(file_path):
    directory = os.path.dirname(file_path)
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(directory)
    print(f"File {file_path} has been successfully unzipped in {directory}.")
