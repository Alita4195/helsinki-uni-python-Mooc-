def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    item={"name":name,"director":director, "year":year, "runtime":runtime}
    database = [item]
    for i in database:
        print(database)
if __name__=="__main__":
    add_movie([],"Gone with the Python", "Victor Pything", 2017, 116)
