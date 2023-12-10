from icecream import ic


def open_input_file():
    with open("d5input.txt", "r") as file:
        data = [item.strip().split("/n/n") for item in file.readlines()]
        # data = file.readlines()
        # for i in data:
            # ic(i)
        return data

input = open_input_file()
# ic(input)

def find_index(input):
    for i in input:
        if 'seeds:' in i[0]:
            index_s = input.index(i)
            # ic(index_s)
        if 'seed-to-soil map:' in i[0]:
            index_ss = input.index(i)
        if 'soil-to-fertilizer map:' in i[0]:
            index_sf = input.index(i)
        if 'fertilizer-to-water map:' in i[0]:
            index_fw = input.index(i)
        if 'water-to-light map:' in i[0]:
            index_wl = input.index(i)
        if 'light-to-temperature map:' in i[0]:
            index_lt = input.index(i)
        if 'temperature-to-humidity map:' in i[0]:
            index_th = input.index(i)
        if 'humidity-to-location map:' in i[0]:
            index_hl = input.index(i)
    index_map = [index_s, index_ss,index_sf, index_fw, index_wl, index_lt, index_th, index_hl]
    return index_map

index_map = find_index(input)
ic(index_map)

seeds = [int(x) for x in input[index_map[0]][0].split()[1:]]
ic(seeds)

def seed_to_soil(input, index1, index2, seeds):
    if index2 == 'null':
        ss_list = input[index1:]
    else:
        ss_list = input[index1:index2]
    # ss_list = ss_list[1:]
    ss_list = [x[0].split() for x in ss_list[1:]]
    ss_list = [[int(n) for n in x] for x in ss_list[:-1]]
    # ic(ss_list)
    destinations = []
    sources = []
    for item in ss_list:
        destination = [n for n in range(item[0],item[0]+item[2])]
        source = [n for n in range(item[1],item[1]+item[2])]
        destinations.append(destination)
        sources.append(source)
    # ic(destinations)
    # ic(sources)
    soil = []
    mapped_seeds = []
    for source in sources:
        ic(source)
        for seed in seeds:
            ic(seed)
            if seed in source:
                s = sources.index(source)
                i = source.index(seed)
                dest = destinations[s][i]
                soil.append(dest)
                mapped_seeds.append(seed)
    for seed in seeds:
        if seed in mapped_seeds:
            pass
        else:
            soil.append(seed)
    return soil


# index_map = [index_s, index_ss,index_sf, index_fw, index_wl, index_lt, index_th, index_hl]

ss = seed_to_soil(input, index_map[1], index_map[2], seeds)
# ic(ss)
sf = seed_to_soil(input, index_map[2], index_map[3], ss)
# ic(sf)
fw = seed_to_soil(input, index_map[3], index_map[4], sf)
# ic(fw)
wl = seed_to_soil(input, index_map[4], index_map[5], fw)
# ic(wl)
lt = seed_to_soil(input, index_map[5], index_map[6], wl)
# ic(lt)
th = seed_to_soil(input, index_map[6], index_map[7], lt)
# ic(th)
hl = seed_to_soil(input, index_map[7], "null", th)
# ic(hl)
ic(min(hl))



