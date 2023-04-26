def find_palindromes(str_list):
    palindromes = []

    for string in str_list:

        if string == string[::-1]:
            palindromes.append(string)
    return palindromes
