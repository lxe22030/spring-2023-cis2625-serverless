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
        
    return res
    
"""    
fname = input('What is your first name? ')
lname = input('What is your last name? ')

print(f'Thank you, {fname} {lname}.')
course = input('What course are you taking? ')
p = int(input (f'How many points do you have in {course}? '))
print(f'Your final grade for {course} is {str(grade(p))}.')
"""