# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie={"name":name,"director":director, "year":year, "runtime":runtime}
    database = database.append(movie)
    (database)

if __name__=="__main__":
    add_movie([],"Gone with the Python", "Victor Pything", 2017, 116)
    add_movie([],'The Birds', 'Alfred Hitchcock', 1963, 119)
    