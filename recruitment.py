# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():

    skills = ['python', 'c++', 'javaScript']
    skills.extend(['coding', 'running', 'eating', 'traveling','reading','sleeping'])
    return skills
    ...



# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    print('Skills:')
    for i, skill in enumerate(skills,1):
        print(f"{i}.{skill}")
    ...


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    show_skills(skills)
    skill1 = int(input("Choose a skill from above by entering its number: "))
    skill2 = int(input("Choose another skill from above by entering its number: "))
    return [skills[skill1-1], skills[skill2-1]]



# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {}
    cv['name'] = input('Whats is your name? ')
    cv['age'] = int(input('How old are you? '))
    cv['experience'] = int(input('how many years of experience do you have? '))
    cv['skills'] = get_user_skills(skills)
    return cv
    ...


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):

    return cv['age'] >= 25 and cv['age'] <= 40 and cv['experience'] > 3 and desired_skill in cv['skills']
    ...


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome

    print('welcome to the special recruitment program, please answer the following questions:')
    skills = get_skills()
    cv = get_user_cv(skills)
    desired_skill = skills[3]
    if check_acceptance(cv,desired_skill):
        print(f"You have been accepted,{cv['name']}")
    else: 
        print(f"Unfortunately ,{cv['name']}, you have been rejected")
    ...


if __name__ == "__main__":
    main()
