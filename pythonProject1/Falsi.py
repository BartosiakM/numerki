import StopFun


def falsi(a, b, f, stop_fun=None, eps=None, max_iteration=None):
    if stop_fun is None:
        stop_fun = StopFun.stop_fun_varB
        eps = 0
    iter_count = 0
    prev_x = a
    x = 0

    if f(b) - f(a) == 0:
        raise ValueError("f(b) - f(a) = 0  Dzielenie przez 0")

    while (max_iteration is None or iter_count < max_iteration) and stop_fun(a - (f(a) / (f(b) - f(a))) * (b - a),
                                                                             prev_x, f, eps):


        x = a - (f(a) / (f(b) - f(a))) * (b - a)


        if f(a) * f(b) > 0:
            raise ValueError("Wartosci funkcji dla koncow tego przedzialu nie maja przeciwnych znaków")

        elif f(x) * f(b) < 0:

            a = x


        else:

            b = x


        prev_x = x
        iter_count += 1

    return x, iter_count, prev_x
