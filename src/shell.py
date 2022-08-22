import AshScript

while True:
    text = input('AshScript > ')
    result, error = AshScript.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)