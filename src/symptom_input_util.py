from typing import List


def get_symptom_list_from_user_symptoms(user_symptoms: str, known_symptoms: List[str]):
    user_symptom_list = user_symptoms.split()
    if not all(item in known_symptoms for item in user_symptom_list):
        print("One of the symptoms entered was misspelled or is not a known symptom")
        return None
    elif len(user_symptom_list) == 0:
        print("No symptoms were entered")
        return None
    else:
        return user_symptom_list
