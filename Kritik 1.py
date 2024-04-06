def approx_rctan(x):
    if x < 0 or x > 1:
        return "Error!"
    else:
        approximation = 0
        n = 1
        i = -1
        error_bound = 10
        while error_bound >= 0.0001:
            i += 1
            n = 2*i + 1
            approximation += (((-1)**i)*(x**(2*i+1)))/(2*i+1)
            error_bound = (x**(2*n+1))/(2*n+1)
        return (approximation, n, error_bound)


print(approx_rctan(-1))
print(approx_rctan(0))
print(approx_rctan(0.25))
print(approx_rctan(0.5))
print(approx_rctan(0.75))
print(approx_rctan(1))