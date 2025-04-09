import sys
import os

def main():
    # Your code goes here
    print("Hello, World!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and isinstance(sys.argv[1], str):
        with open(os.path.abspath(sys.argv[0]), "r") as file:
            main()
    else:
        main()

# A placeholder function to serve the purpose
def serve():
    # Your code here
    print("Hello, this is a simple Python script!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and isinstance(sys.argv[1], str):
        with open(os.path.abspath(sys.argv[0]), "r") as file:
            main()
