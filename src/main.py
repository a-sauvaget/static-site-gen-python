from utils import delete_old_public, copy_static_to_public, generate_pages_recursive

def main():
    print("Deleting public directory...")
    delete_old_public("public")
    print("Copying static files to public directory...")
    copy_static_to_public("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()