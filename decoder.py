def decode(code):
    input = code
    output = ' '.join([str(int(num, 8)) for num in input.split(' ',)])
    print(output)
    return output