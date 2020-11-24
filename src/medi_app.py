import sys
from typing import Callable

from get_from_csv import get_from_csv
from get_known_list_from_str import get_known_list_from_str


# TODO: Export to bayesnet-specific file
def get_symptom_names_from_symptom_probability_distribution():
    return [
        symptom for symptom, _, _, _ in (get_from_csv("Symptom Probability Tables"))
    ]


def get_symptoms_from_user(symptom_name_getter: Callable):
    print(
        'Please enter your symptoms separated by spaces (e.g. "itching chills vomiting"): '
    )
    user_symptoms = input()
    known_symptoms = symptom_name_getter()
    user_entered_symptoms = get_known_list_from_str(user_symptoms, known_symptoms)
    while user_entered_symptoms is None:
        print("Please input your symptoms again")
        user_symptoms = input()
        user_entered_symptoms = get_known_list_from_str(user_symptoms, known_symptoms)
    return user_entered_symptoms


if __name__ == "__main__":
    try:
        option = sys.argv[1]
        if option == "-bayesnet":
            # TODO: Export to bayesnet-specific file
            get_symptoms_from_user(
                get_symptom_names_from_symptom_probability_distribution
            )
        elif option == "-ann":
            print("TODO: Call ANN implementation")
        elif option == "-h":
            print(
                f"""Usage: {sys.argv[0]} [option]
            Options and arguments:
            -h: Help menu
            -bayesnet : Uses Bayesian Network algorithm
            -ann : Uses Artificial Neural Network algorithm"""
            )
        else:
            print("You must call this function with arguments '-bayesnet' or '-ann'")
    except IndexError:
        raise SystemExit(
            f"""Usage: {sys.argv[0]} [option]
            Use {sys.argv[0]} -h for help"""
        )
