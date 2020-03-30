def camel(line):
    new = ""
    for i in range(line):
        index = line.index(i)
        if i != "_":
            new += line[index+1]
            continue
        else:
            new += line[index]
    return new
print(camel("dg_ds_sd"))
