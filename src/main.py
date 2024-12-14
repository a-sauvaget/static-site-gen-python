from utils import delete_old_public, copy_static_to_public, extract_title

def main():
    print("Deleting public directory...")
    delete_old_public("public")
    print("Copying static files to public directory...")
    copy_static_to_public("static", "public")
    extract_title("content/index.md")


if __name__ == "__main__":
    main()