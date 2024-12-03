from aocd import get_data

data = get_data(day=1, year=2024)

data_list = data.split('\n')
left_list = []
right_list = []
diff_list = []
similarity_score = 0

for item in data_list:
    temp_index = item.split('   ')
    left_list.append(int(temp_index[0]))
    right_list.append(int(temp_index[1]))

left_list = sorted(left_list)
right_list = sorted(right_list)

for idx, x in enumerate(left_list):
    similarity_score += x * right_list.count(x)
    diff = abs(x - right_list[idx])
    diff_list.append(diff)
    
print("Total difference is: " + str(sum(diff_list)))
print("Similarity score is: " + str(similarity_score))