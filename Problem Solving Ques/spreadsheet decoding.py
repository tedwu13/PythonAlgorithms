def spreadsheet_decoding(str)
    if len(string) == 0:
        return 
    value = 0
    for char in string:
        value = value * 26 + char - 'A' + 1
    return value

