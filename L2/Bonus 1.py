x = float(input("Введите число: "))
tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
if x in tpl or abs(x) in tpl:
    print("Число" , x, "присутствует среди элементов")
else:
    print("Число" , x, "отсутствует среди элементов")