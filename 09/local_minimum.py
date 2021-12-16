input = [2,1,9,9,9,4,3,2,1,0,  3,9,8,7,8,9,4,9,2,1,
        9,8,5,6,7,8,9,8,9,2,   8,7,6,7,8,9,6,7,8,9,  9,8,9,9,9,6,5,6,7,8]

list_of_rows = [input[index:index+10] for index in [0, 10, 20, 30, 40]]

for row_index, row in enumerate(list_of_rows):
    for index, item in enumerate(row):
        subset = []
        # add left and right element to subset
        if index == 0:
            subset = [item, row[index + 1]]
        elif index == 9:
            subset = [row[index - 1], item]
        else:
            subset = [row[index-1], item, row[index+1]]
        # add up and down element to subset
        if row_index == 0:
            subset.append(list_of_rows[row_index+1][index])
        elif row_index == 4:
            subset.append(list_of_rows[row_index-1][index])
        else:
            subset.append(list_of_rows[row_index-1][index])
            subset.append(list_of_rows[row_index+1][index])
        # check if current item is a hot spot
        if item == min(subset):
            print(f"Found hot spot: {item}")
