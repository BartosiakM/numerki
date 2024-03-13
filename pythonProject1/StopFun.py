def stop_fun_varA(x, prevx, _, eps=0):
    if abs(x - prevx) <= eps:
        return False
    return True


def stop_fun_varB(x, _, f, eps=0):
    if abs(f(x)) <= eps:
        return False
    return True
