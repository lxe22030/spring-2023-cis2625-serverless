
# students = [
#     dict(id=1, score=67),
#     dict(id=2, score=78),
#     dict(id=3, score=77),
#     dict(id=4, score=87),
#     dict(id=5, score=91),
#     dict(id=6, score=69),
# ]

# for student in students:
#     if student['score'] >= 90:
#         student['grade'] = 1
        
        
# for student in students:
#     print(str(student['grade']))
   
points = [67, 78, 77, 87, 91, 69]

for x in range(len(points)):
    if points[x] >= 90:
        print("A")
    elif points[x] >= 80:
        print("B")
    elif points[x] >= 70:
        print("C")
    elif points[x] >= 60:
        print("D")
    else:
        print("F")