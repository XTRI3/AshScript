import ashScript

while True:
    text = input('ashscript > ')
    result, error = ashScript.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)