def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Nicholas Stuckless",
        "student_id": 10091199,
        "pizza_topping": ['BACON', 'CHEESE', 'HAM'],
        "movie": [
            {"title": "dredd",
            "genre": "action"},

            {"title": "year one",
            "genre": "comedy"}
            ],
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"title": "avatar", "genre": "action"}
    about_me["movie"].append(new_movie)
    
    print_student_name_and_id(about_me)
    
    extra_toppings = ("mushroom", "pineapple")
    add_pizza_toppings(about_me, extra_toppings)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"] 
    print(f"My name is {full_name}, but you can call me Sir {first_name}. \nMy student ID is {student_id}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    for topping in toppings:
        about_me["pizza_topping"].append(topping)
    new_list = []
    for topping in about_me["pizza_topping"]:
        topping.lower()
        new_list.append(topping)
    about_me["pizza_topping"] = new_list
       
    about_me["pizza_topping"].sort()
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    topping_list = []
    for topping in about_me["pizza_topping"]:
        topping_list.append(topping)
    print("My favourite toppings are:\n-")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()