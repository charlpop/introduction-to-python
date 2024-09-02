# # def sort_string(strings):
#     strings.sort()
#     strings.sort(key=len)
#     return strings
# string_list = ["emma", "muideen", "blessing", "zainab", "richard", "mr richard", "damilola"]
# sorted_list = sort_string(string_list)
# print(string_list, "string_list")
# # print(sorted_list, "sorted_list")

def sort_list(strings):
  return sorted(strings, key = lambda s: (len(s), s))
string_list = ["emma", "muideen", "blessing", "zainab", "richard", "mr richard", "damilola"]
sorted_list = sorted(string_list)

print(string_list, "string_list")
print(sorted_list, "sorted_list")
