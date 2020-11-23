from symptom_and_disease_csv_util import get_symptom_probability_distribution
from symptom_input_util import get_symptom_list_from_user_symptoms


def get_symptom_names_from_symptom_probability_distribution():
    symptom_probability_distribution = get_symptom_probability_distribution()
    known_symptoms = []
    for symptom, p1, not_symptom, p2 in symptom_probability_distribution:
        known_symptoms.append(symptom)
    return known_symptoms


def get_symptoms_from_user():
    print(
        'Please enter your symptoms separated by spaces (e.g. "headache itching fever"): '
    )
    user_symptoms = input()
    known_symptoms = get_symptom_names_from_symptom_probability_distribution()
    user_entered_symptoms = get_symptom_list_from_user_symptoms(
        user_symptoms, known_symptoms
    )
    while user_entered_symptoms is None:
        print("Please input your symptoms again")
        user_symptoms = input()
        user_entered_symptoms = get_symptom_list_from_user_symptoms(
            user_symptoms, known_symptoms
        )
    return user_entered_symptoms


get_symptoms_from_user()
