class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

if __name__ == "__main__":
    my_class = MyClass()
    my_class.add_data("Hello")
    print(my_class.get_data())
