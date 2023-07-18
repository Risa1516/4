# def strcounter(string):
#     for symbol in string:
#         counter = 0 
#         for sub in string:
#             if symbol == sub:
#                 counter += 1
#         print(symbol, counter)

# strcounter('abcccccde')


# def strcounter(string):
#     for symbol in set(string):
#         counter = 0 
#         for sub in string:
#             if symbol == sub:
#                 counter += 1
#         print(symbol, counter)

# strcounter('abcccccde')

def strcounter(string): # сложность O(n)
 syms_counter = {}
 for symbol in string:
     syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
 print(syms_counter)

strcounter('aaabbcdeee')
 