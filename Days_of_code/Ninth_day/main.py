# py_dict = {
#   "Bug": "An error in program that prevents the program from running as expected.",
#   "Function": "A piece of code that you can easily call over again."
# }

# print(py_dict["Bug"])



# travel_log = {
#   "France": {"cities_visited":[ "Paris", "Lyon", "Marseille"], "total_visits": 3},
#   "Inglaterra": {"cities_visited":["London", "Birmingham", "Liverpool"], "total_visits": 3},
# }

# for country in travel_log:
#   print(country)
#   for city in travel_log[country]:
#     print(city)




# travel_log2 = [
#   {"country": "France", "cities_visited": [ "Paris", "Lyon", "Marseille"], "total_visits": 3},
#   {"country":"Inglaterra", "cities_visited": ["London", "Birmingham", "Liverpool"], "total_visits": 3},
#   ]

# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }


# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }

# # final_dictionary = starting_dictionary.append({"c:" 7})

# # final_dictionary = starting_dictionary += {"c": 7}

# final_dictionary = starting_dictionary["c"] = 7

# print(f"starting_dictionary: {starting_dictionary}") 
# print(f" final_dictionary: {final_dictionary}")


# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# # for key in dict:
# #     dict[key] += 1

# # dict[1] = 4

# # dict["c"] = [1,2,3]
 
 
# print(dict[1])


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])