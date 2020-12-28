def main():
    length = int(input("Please enter the length: "))
    width = int(input("Please enter the width: "))
    height = int(input("Please enter the height: "))
    surface_area = (length * width) + (length * height) + (height * width)

    return surface_area

print("The surface area is: " , main())