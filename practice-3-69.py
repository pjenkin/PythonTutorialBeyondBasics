temperatures = [10, -20, -289, 100]


def c_to_f(c):
    if c < -273.15:
        # return "That temperature doesn't make sense!"
        return None
    else:
        f = c* 9/5 + 32
        return f


with open('tfile.txt', 'a+') as tfile:
    for t in temperatures:
        #print(c_to_f(t))
        if c_to_f(t) is not None:
            tfile.write(str(c_to_f(t)) + '\n')

