# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
    bike_dict={}
    with open(filename) as new_file:
        for line in new_file:
            line=line.replace("\n", "")
            parts=line.split(";")
            if parts[0]=="Longitude":
                continue
            location=parts[3]
            longitude=float(parts[0])
            latitude=float(parts[1])
            bike_dict[location]=(longitude, latitude)
        return(bike_dict)
    
def distance(stations: dict, station1: str, station2: str):
        import math
        x_km=(stations[station1][0]-stations[station2][0])* 55.26
        y_km = (stations[station1][1]-stations[station2][1]) * 111.2
        distance_km = math.sqrt(x_km**2 + y_km**2)
        return(distance_km)

def greatest_distance(stations: dict):
	greatest = 0
	for x in stations:
		for y in stations:
			if distance(stations, x, y) > greatest:
				station1 = x
				station2 = y
				greatest = distance(stations, x, y)
	return(station1, station2, greatest)

if __name__ == "__main__":          
    stations= get_station_data("stations1.csv")
    distance(stations, "Viiskulma", "Kaivopuisto")

    stations= get_station_data("stations2.csv")
    greatest_distance(stations)


    



        