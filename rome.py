class Roman:
    def convert(self, num):
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""

        for i in range(len(numbers)):
            while num >= numbers[i]:
                result += letters[i]
                num -= numbers[i]

        return result


num = int(input("Enter a number (1-3999): "))

if 1 <= num <= 3999:
    obj = Roman()
    print("Roman numeral:", obj.convert(num))
else:
    print("Please enter a number between 1 and 3999.")