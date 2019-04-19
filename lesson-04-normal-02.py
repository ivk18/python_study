# урок 04, задание 2 (уровень normal)

# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

__author__ = 'Караваев Илья Викторович'

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

################################################
print('Решение с использованием функции "re":' + str('\n'))

def collectRe(s, before=2, after=2):
    import re
    result = []
    pattern = '[a-z]{' + str(before) + '}[A-Z]+[A-Z]{' + str(after) + '}'
    for item in re.findall(pattern, s):
        result.append(item[before:-after])
    return result

print(collectRe(line_2))
print()
print(collectRe(line_2,3,3))
print()
print(collectRe(line_2,1,5))

################################################
print(str('\n') + 'Решение без использования функции "re":' + str('\n'))

def collect(s, before=2, after=2):
    found = []  # список для итогового результата
    bigs = '' # строка для хранения найденной последовательности прописных букв
    i_small = 0     # счетчик строчных букв
    i_big = 0       # счетчик прописных букв
    while s:
        if s[0] != s[0].title(): # если первая буква строки - строчная
            # если последовательность прописных удовлетворяет условию after
            if len(bigs) >= after + 1:
                # добавляем найденную последовательность прописных к списку
                found.append(bigs[:-after])     
            i_small += 1    
            # после добавления обнуляем счетчик прописных
            i_big = 0
            # и строку с найденными прописными буквами
            bigs = ''  
            s = s[1:]   # переходим к следующему символу
        elif s[0] == s[0].title(): # если первая буква строки - прописная
            # если уже найдена хотя бы одна прописная буква или 
            # счетчик строчных удовлетворяет условию before
            if i_small >= before or i_big > 0:
                bigs += s[0]    # добавляем найденную прописную букву
                i_big += 1      # и увеличиваем счетчик прописных
            i_small = 0 # обнуляем счетчик строчных
            s = s[1:]   # переходим к следующему символу
    return found

print(collect(line_2))
print()
print(collect(line_2,3,3))
print()
print(collect(line_2,1,5))
print()
