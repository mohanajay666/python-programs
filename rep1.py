from collections import OrderedDict
list_of_number =[1, 2 ,3 ,3 ,3 ,5 ,5, 5, 6]
duplicate_number = set(list_of_number)
print(duplicate_number)
final_list=list(duplicate_number)
print(final_list)

lib_1 = {"harry potter", "money heist", "dark"}
lib_2 = {"family man", "money heist"}
common = lib_1.clear
print(common)

grocaries = {"bananas":10,"oranges":5}
print(grocaries.get("key"))


contact_num = {"ajay":9618968899, "lohi":{'ph_no':'6300191609','gmail':"lohikonathala@gmail.com"},"mom":7013001849,"dad":9290431650}
print(contact_num["lohi"])



sen = "i am ajay"
count_number = {
  'i':1,
  'am':1,
  'ajay':1
}
print(count_number)
print(list(count_number.values()))
