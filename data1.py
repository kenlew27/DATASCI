dates_list = ["February 6, 1992", "February 18, 1992",
"February 27, 1992", "September 6, 1994",
"December 1, 1993"]

months = {"January":"01","February":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}

def dates_to_iso8601(dates_list):
	solution=[]
	for val in dates_list:
		val=val.replace(',','')
		month=val.split(" ")[0]
		day=int(val.split(" ")[1])
		year=val.split(" ")[2]
		solution.append(f"{year}-{months[month]}-{day:02d}")
	return solution



def sort_dates(dates_list):
	solution=[]
	iso=dates_to_iso8601(dates_list)
	for i in range(len(iso)):
		iso[i]=int(iso[i].replace('-',''))
	monthdict = {iso[i]: dates_list[i] for i in range(len(iso))}
	iso.sort()
	for val in iso:
		solution.append(monthdict[val])
	return solution

print(sort_dates(dates_list))