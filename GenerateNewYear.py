from pathlib import Path

def script():
	year = input("Enter year: ").strip()
	while not year.isdigit():
		year = input("Enter year: ").strip()

	folder = Path(year)
	folder.mkdir(parents=True, exist_ok=True)

	for day in range(1, 26):
		python_file = folder / f"{day:02d}_12_{year}.py"
		if not python_file.exists():
			python_file.write_text(
f'''def naive(source):
    file = open(source, "r")
    lines = file.readlines()
    
    count = 0
    
    return count

print("Part 1: ", naive("{year}/input{day}"))
print("--------------------------------")

def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    count = 0
    
    return count

print("Part 2: ", naive2("{year}/input{day}"))
print("--------------------------------")
''', encoding="utf-8", )
		(folder / f"input{day}").touch(exist_ok=True)


script()
