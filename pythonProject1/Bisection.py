import StopFun

#TODO prev_X

def bisection(a, b, f, stop_fun=None, eps=None, max_iteration=None):
    if stop_fun == None:
        stop_fun = StopFun.stop_fun_varB
        eps = 0
    iter_count = 0
    prev_x = a

    x = 0
    while (max_iteration is None or iter_count < max_iteration) and stop_fun((a + b) / 2,
                                                                             prev_x, f, eps):
        x = (a + b) / 2


        if f(a) * f(b) > 0:
            raise ValueError("Wartosci funkcji dla koncow tego przedzialu nie maja przeciwnych znaków")


        elif f(x) * f(b) < 0:
            prev_x = a
            a = x


        else:
            prev_x =b
            b = x

        iter_count += 1

    return x, iter_count, prev_x
