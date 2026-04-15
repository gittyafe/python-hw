def analyze_list(lst):
    my_set = set()
    sum = 0
    maxi = 0
    mini = lst[0]
    for l in lst:
        sum += l
        my_set.add(l)
        if l > maxi:
            maxi = l
        if l < mini:
            mini = l
    my_set.add(mini)
    my_set.add(maxi)
    my_set.add(sum / len(lst))
    return my_set


print(analyze_list([2, 6, 6, 8, 3, 4, 5, 6]))
f = {"ghh": 788, "htrg": 8, "gtees": 900}


def filter_dict(d, threshold):
    new_l = []
    for k, v in d.items():
        if v > threshold:
            new_l.append(k)
    return new_l


print(filter_dict(f, 20))




# def clean_str(st):
#     new_st = ""
#     for s in st:
#         if s.isnumeric() or s.isalpha():
#             new_st += s
#     return new_st
#
#
# # print(clean_str("5#4gfdd2$^$#"))
#
# def the_popular(st):
#     maxi = 0
#     pop_word = ""
#     arr = st.split(' ')
#     for a in arr:
#         if st.count(a) > maxi:
#             maxi = st.count(a)
#             pop_word = a
#     return pop_word
#
#
# # print(the_popular("ret gfds ret fhdj"))
#
#
#
# def initials(st):
#     arr = st.split(' ')
#     init = ""
#     for a in arr:
#         init += a[0]
#     return init
#
# # print(initials("sdfr gred gf"))

