# def str_count(data):
#     for sym in data:
#         count = 0
#         for sym2 in data:
#             if sym in sym2:
#                 count += 1
#         print(sym, count)
#
#
# str_count("abcd")

# ------------------------------


# def str_count(data):
#     for sym in set(data):
#         count = 0
#         for sym2 in data:
#             if sym in sym2:
#                 count += 1
#         print(sym, count)
#
#
# str_count("aabcd")

# ------------------------------

def str_count(data):
    sym_count = {}
    for sym in data:
        sym_count[sym] = sym_count.get(sym, 0) + 1
    print(sym_count)


str_count("abbcd")