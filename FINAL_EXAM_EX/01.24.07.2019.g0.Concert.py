line = input()
bands = {}
time = {}
while line != "start of concert":
    data = line.split("; ")
    command = data[0]
    band_name = data[1]
    if command == "Add":
        names = data[2].split(", ")
        bands.setdefault(band_name, [])
        for name in names:
            if name not in bands[band_name]:
                bands[band_name].append(name)

    elif command == "Play":
        minutes = int(data[2])
        time.setdefault(band_name, 0)
        time[band_name] += minutes

    line = input()

time = dict(sorted(time.items(), key=lambda x: (-x[1], x[0])))
band_to_print = input()
total_time = sum(time.values())
print(f"Total time: {total_time}")
for k, v in time.items():
    print(f"{k} -> {v}")
print(band_to_print)
for person in bands[band_to_print]:
    print(f"=> {person}")
