def str_to_int(value_str):
    value_int = 0
    testr_str_len = len(value_str)
    for i in range(len(value_str)):
        code_value = ord(value_str[i]) - ord('0')
        value_int += code_value * 10 ** testr_str_len
        testr_str_len -= 1
    return testr_str_len
