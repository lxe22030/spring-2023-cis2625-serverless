def grade(points):
    if points >= 90:
        res='A'
    elif points >=80:
        res='B'
    elif points >=70:
        res='C'
    elif points >= 60:
        res='D'
    else:
        res='F'
        
    print(f'The final grade for the student is {res}.')
    
    
grade(65)

    