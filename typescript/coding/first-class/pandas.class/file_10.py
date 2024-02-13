try:
    print(x)
except ZeroDivisionError:
    print('It is Error')
except NameError:
    print('Name Error')
except:
    print('Bohat Sari Error')