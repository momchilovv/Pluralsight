movie_program = {'Bad Boys': '09:00pm',
                 'The Grinch': '01:30pm',
                 'The Matrix': '07:45pm',
                 'Special Force': '10:00am'}

print("Currently, we are showing the following movies:")

for movie in movie_program:
    print(movie)

movie = input("Which movie do you want to see?\n")

if movie_program.get(movie):
    print(f"The movie {movie} is scheduled for {movie_program[movie]}.")
else:
    print(f"The movie {movie} is not in our current program.")