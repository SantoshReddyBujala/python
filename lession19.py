class JustCoolError(Exception):
    pass


a = 2
try:
    raise JustCoolError('This is cool man')
    # print(a)
    # print(a/0)
    # print(a/1)
    # if not type(a) is str:
    # raise TypeError('Only Strings are allowed')
    # raise Exception('I am a custom exception')
except NameError:
    print("NameError something undefined")
except ZeroDivisionError:
    print('Please do not divided by Zero')
except Exception as error:
    print(error)
else:
    print('No Error ✅')
finally:
    print('I am printing without any error')
