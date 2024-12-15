import os
import shutil
from markdown_blocks import markdown_to_html_node

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
    '''Generate HTML page from markdown'''
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path) as f:
        file_contents = f.read()
    
    with open(template_path) as t:
        file_template = t.read()

    file_contents_html = markdown_to_html_node(file_contents).to_html()

    page_title = extract_title(file_contents)
    
    template = file_template.replace("{{ Title }}", page_title)
    template = template.replace("{{ Content }}", file_contents_html)

    directory = os.path.dirname(dest_path)
    is_dest_directory_exist = os.path.exists(directory)

    if not is_dest_directory_exist:
        os.makedirs(directory, exist_ok=True)
    
    with open(dest_path, "w") as g:
        g.write(template)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> str:
    '''Generate HTML pages from markdown files'''    
    for item in os.listdir(dir_path_content):
        dir_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        _, extension = os.path.splitext(item)
        
        if extension == '.md':
            old_file_name = os.path.splitext(item)
            new_file_name = old_file_name[0] + ".html"
            new_file_path = os.path.join(dest_dir_path, new_file_name)
            generate_page(dir_path, template_path, new_file_path)
        elif os.path.isdir(dir_path):
            os.makedirs(dest_path, exist_ok=True)
            print(f"Created directory: {dest_path}")
            generate_pages_recursive(dir_path, template_path, dest_path)