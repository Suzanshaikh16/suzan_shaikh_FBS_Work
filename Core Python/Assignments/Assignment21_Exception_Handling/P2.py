class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def accept(self):
        self.model_no = int(input("Enter model number: "))
        self.screen_size = float(input("Enter screen size in inches: "))
        self.price = float(input("Enter price in Rs: "))

        if len(str(self.model_no)) > 4:
            raise Exception("Model number must have at most 4 digits")

        if self.screen_size < 12 or self.screen_size > 70:
            raise Exception("Screen size must be between 12 and 70 inches")

        if self.price < 0 or self.price > 5000:
            raise Exception("Price must be between Rs. 0 and Rs. 5000")

    def display(self):
        print("Model Number:", self.model_no)
        print("Screen Size:", self.screen_size, "inches")
        print("Price: Rs.", self.price)


def main():
    tv = Television()

    try:
        tv.accept()
    except Exception as e:
        print("Error:", e)
        tv.model_no = 0
        tv.screen_size = 0
        tv.price = 0

    print("\nTelevision Details:")
    tv.display()


main()