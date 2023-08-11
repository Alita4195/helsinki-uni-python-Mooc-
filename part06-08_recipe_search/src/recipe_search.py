def recipes_dict (file:str):
	recipes = {}
	index = 0
	with open(file) as new_file:
		index = 0
		key = ""
		for line in new_file:
			if index == 0:
				line = line.strip()
				recipes[line] = []
				key = line
			elif line == "\n":
				index = 0
				continue
			else:
				line = line.strip()
				if line.isdigit():
					recipes[key].append(int(line))
				else:
					recipes[key].append(line)
			index += 1
		return(recipes)

def search_by_name(filename: str, word: str):
	recipes=recipes_dict(filename)
	recipe_list = []
	for key in recipes:
		if word.lower() in key.lower():
			recipe_list.append(key)
	return(recipe_list)


def search_by_time(filename:str, prep_time:int):
	recipes=recipes_dict(filename)
	recipe_list=[]
	for key, value in recipes.items():
		if value[0]<=prep_time:
			recipe_list.append(f"{key}, preparation time {value[0]} min")
	return(recipe_list)

def search_by_ingredient(filename: str, ingredient: str):
	recipes=recipes_dict(filename)
	recipe_list=[]
	for key, value in recipes.items():
		if ingredient in value:
			recipe_list.append(f"{key}, preparation time {value[0]} min")
	return (recipe_list)

if __name__ == "__main__":
	recipes_dict("recipes1.txt")
	search_by_name("recipes1.txt", "cake")
	search_by_time("recipes1.txt", 20)
	search_by_ingredient("recipes1.txt", "eggs")
	





    

        

