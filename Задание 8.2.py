class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


chiclo_1 = input("Ввидите делимое: ")
chiclo_2 = input("Ввидите делитель: ")

try:
    chiclo_1 = int(chiclo_1)
    chiclo_2 = int(chiclo_2)
    if chiclo_2 == 0:
        raise MyError("Делить на ноль нельзя!!!")
except MyError as Error:
    print(Error)
except ValueError:
    print("Введено не целое число")
else:
    print(f"Частное равно: {chiclo_1 / chiclo_2}")
