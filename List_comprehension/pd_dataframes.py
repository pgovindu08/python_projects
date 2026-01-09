student_dict = {
    "student": ["Angela","James","Lily"],
    "scores": [56,76,98]
}

for (key,value) in student_dict.items():
    print(value)

import pandas

student_data = pandas.DataFrame(student_dict)
# print(student_data)

# #Loop through a Pandas Data Frame
# for (key,value) in student_data.items():
#     print(value)

for (index, row) in student_data.iterrows():
    if row.student == "Angela":
        print(row.scores)