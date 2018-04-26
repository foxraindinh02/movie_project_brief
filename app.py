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
[]: Show all their movies
[]: Find a movie
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
    user_input = input("Enter  'a' to add a movie, 'l' to see your movie, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command. Please try again')

        user_input = input("Enter  'a' to add a movie, 'l' to see your movie, 'f' to find a movie, and 'q' to quit: ")


def add_movie():
    name = input('Enter the name of the movie: ')
    director = input('Enter the name of the director: ')
    year = int(input('Enter the movie release year: '))

    movie = {
        'name': name,
        'director': director,
        'year': year
    }
    movies.append(movie)


def show_movies():
    if not movies:
        print('The list is empty, you should add the movie first')
    else:
        for movie in movies:
            print(movie)


def find_movie():
    if not movies:
        print('The list is empty, you should add the movie first')
    else:
        movie_search = input('Type the movie name you wanna see: ')
        for movie in movies:
            if movie_search == movie['name']:
                print(f'This is the movie you want to see: {movie}')
            else:
                print('There is no movie which you wanna see!')


menu()

print(movies)