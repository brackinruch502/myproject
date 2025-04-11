import math

def calculate_area(length, width):
    area = length * width
    return area

def main():
    try:
        if not (isinstance(length, int) and isinstance(width, int)):
            raise ValueError("Both 'length' and 'width' should be integers.")
        result = calculate_area(length=length, width=width)
        print(f"The area is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the width of rectangle: "))
    main()
