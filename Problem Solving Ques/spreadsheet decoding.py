def spreadsheet_decoding(str)
    if len(string) == 0:
        return 
    value = 0
    for char in string:
        value = value * 26 + char - 'A' + 1
    return value


def spreadsheet_encoding(num):
    
  return '' if num == 0

  result = ''
  while num > 0
    digit = num % 26

    if digit == 0
      result = "#{result}Z"
      num = num / 26 - 1
    else
      value = 'A'.ord + digit - 1
      puts "value: #{value}"
      result = "#{result}#{value.chr}"
      num = num / 26
    end


  end

  result.reverse
end