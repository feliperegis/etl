def transform(legacy_data):
    res = {}
    for key, lst in legacy_data.items():
        if len(lst) > 1:
            for char in lst:
                res[char.lower()] = key
        else:
            res[lst[0].lower()] = key
    return res


legacy = {1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 2: ["D", "G"], 3: ["B", "C", "M", "P"],
          4: ["F", "H", "V", "W", "Y"], 5: ["K"], 8: ["J", "X"], 10: ["Q", "Z"]}


print(transform(legacy))