def banner_print(
        string, symbol='=', padding=1, banner_length=40, upper=True):
    string = string.upper() if upper else string
    string = ' ' * padding + string + ' ' * padding
    string = string.center(banner_length, symbol)
    print(string)
