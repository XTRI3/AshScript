import ashscript

while True:
    text = input('ashscript > ')
    result, error = ashscript.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)