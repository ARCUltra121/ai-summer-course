from area import rect_area
try:
    len = float(input("Enter the length:  "))
    wid = float(input("Enter the width:  "))

<<<<<<< HEAD
    rect_area(len, wid)

    def function:
        help = 'help me bro'

except ValueError as ImproperValueError:
    print("Bro give me an actual number... Please...")
except SyntaxError as WeirdCodeError:
    print('Code properly please my bro...')
=======
try:
    len = float(input("Enter the length:  "))
    wid = float(input("Enter the width:  "))
    rect_area(len, wid)
except ValueError as e:
    print(f"{e} You got a ValueError")
except ZeroDivisionError:
    pass
except:
    print("There was some other error")
else:
    print("No errors!!!!")
finally:
    print("This always runs!")
    raise FileNotFoundError

print("The rest of the program!")
>>>>>>> 7c26682009c0fde428e0a563bb6c281d01d34f63
