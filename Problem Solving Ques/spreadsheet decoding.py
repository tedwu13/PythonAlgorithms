decoding.py
def spreadsheet_decoding(str)
    if str is null, return

    value = 0
    str.each_char do |c|
        value = value * 26 + c - 'A' + 1
    end
end