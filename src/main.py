from symptom_input_util import get_symptom_list_from_user_symptoms


def get_symptoms_from_user():
    print(
        'Please enter your symptoms separated by spaces (e.g. "headache itching fever"): '
    )
    user_symptoms = input()
    # TODO: Get known_symptoms from csv file #8
    user_entered_symptoms = get_symptom_list_from_user_symptoms(
        user_symptoms=user_symptoms, known_symptoms=[]
    )
    while user_entered_symptoms is None:
        print("Please input your symptoms again")
        user_symptoms = input()
        user_entered_symptoms = get_symptom_list_from_user_symptoms(
            user_symptoms=user_symptoms, known_symptoms=[]
        )
    return user_entered_symptoms


get_symptoms_from_user()
