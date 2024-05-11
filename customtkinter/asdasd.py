import os
import llama2

def list_package_contents():
    # Get the directory path of the llama2 package
    package_dir = os.path.dirname(llama2.__file__)
    
    # Print the absolute path to the llama2 package
    print("Path to the llama2 package:", package_dir)
    
    # List and print contents of the llama2 package directory
    package_contents = os.listdir(package_dir)
    print("Contents of llama2 package directory:")
    for content in package_contents:
        print(content)

if __name__ == "__main__":
    list_package_contents()
