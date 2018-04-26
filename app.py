"""
- Enter  'a' to add a movie, 'l' to see your movie, 'f' to find a movie, and 'q' to quit:

- Add movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[x]: Decide where to store the movie
[x]: Show the user the main interface and get their input
[x]: What is the format of a movie
[x]: Allow users to add movies
[x]: Show all their movies
[x]: Find a movie
[x]: Stop running the program when they type 'q'
"""


movies = []

"""
- List format:
movies = {
    'name': ... {str}
    'director': ... {str}
    'year': ... {int}
}
"""


def menu():
    user_input = input("\nEnter  'a' to add a movie, 'l' to see your movie, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command. Please try again')

        user_input = input("Enter  'a' to add a movie, 'l' to see your movie, 'f' to find a movie, and 'q' to quit: ")


def add_movie():
    name = input('Enter the name of the movie: ')
    director = input('Enter the name of the director: ')
    year = input('Enter the movie release year: ')

    movie = {
        'name': name,
        'director': director,
        'year': year
    }
    movies.append(movie)


def show_movies(movies_list):
    if not movies:
        print('The list is empty, you should add the movie first')
    else:
        for movie in movies_list:
            show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    if not movies:
        print('The list is empty, you should add the movie first')
    else:
        find_by = input('What property of the movie are you looking for? ')
        looking_for = input('What are you searching for? ')

        found_movies = find_movie_by_attribute(movies, looking_for, lambda x: x[find_by])

        show_movies(found_movies)


def find_movie_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()

print(movies)