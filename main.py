# This is a sample Python script.



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

hello = "Hello World"

print(hello)




class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def printCat(self):
        print("Name:", self.name, "Age:", self.age, "Color:", self.color)

cat1 = Cat("Tom", 5, "Blue")

cat1.printCat()


def cat():
    return None

cat2 = Cat(name="T", age=75, color="Bliue")

cat2.printCat()
