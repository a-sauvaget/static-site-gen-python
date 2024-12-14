import os
import shutil

def delete_old_public(src: str):
    '''Delete all the content of the destination directory to ensure that the copy is clean.'''
    shutil.rmtree(src)
    os.mkdir(src)
    print(f"Directory {src} created !")

def copy_static_to_public(src: str, dst: str):
    '''Copy all files and sub-directories from source directory to destination directory.'''
    is_directory_static_exist = os.path.exists("static")
    
    if is_directory_static_exist:
            directory_static = os.listdir("static")
            directory_public = os.listdir("public")
            if directory_public == directory_static:
                print("All files copied to public directory !")
                return
            else:
                for item in os.listdir(src):
                    source_path = os.path.join(src, item)
                    destination_path = os.path.join(dst, item)

                    if os.path.isfile(source_path):
                        shutil.copy(source_path, destination_path)
                        print(f"Copied file: {source_path}")
                    elif os.path.isdir(source_path):
                        os.makedirs(destination_path, exist_ok=True)
                        print(f"Created directory: {destination_path}")
                        copy_static_to_public(source_path, destination_path)
    else:
        raise FileNotFoundError("Static directory does not exist")

def extract_title(markdown: str) -> str:
    '''Extract the title from the markdown file to return it to the html file.'''
    title = ""

    lines = markdown.split("\n")
    for line in lines:
        clean_line = line.strip()
        if clean_line.startswith("#"):
            level = clean_line.count("#")
            if level != 1:
                continue
            else:
                clean_title = clean_line.lstrip("#")
                title += clean_title.strip()
                return title
    if title == "":
        raise Exception("There is no h1 header !")

def generate_page(from_path: str, template_path: str, dest_path: str) -> str:
    ''''''
    pass