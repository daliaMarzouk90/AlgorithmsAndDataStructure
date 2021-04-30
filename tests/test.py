def callback(sum):
    print("Sum = {}".format(sum))

def main(a, b, _callback = None):
    print("adding {} + {}".format(a, b))
    if _callback:
        _callback(a+b)

main(1, 2, callback)