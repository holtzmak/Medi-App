import sys
from typing import List

from bayesian_network import BayesianNetworkForDiseasePrediction
from get_known_list_from_str import get_known_list_from_str


def get_symptoms_from_user(known_symptoms: List):
    print(
        'Please enter your symptoms separated by spaces (e.g. "itching chills vomiting"): '
    )
    user_symptoms = input()
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
            BayesianNetworkForDiseasePrediction(
                get_symptoms_from_user
            ).predict_with_bayesian_network()
        elif option == "-ann":
            print("TODO: Call ANN implementation")
        elif option == "-h":
            print(
                f"Usage: {sys.argv[0]} [option]\n"
                f"Options and arguments:\n"
                f"-h: Help menu\n"
                f"-bayesnet : Uses Bayesian Network algorithm\n"
                f"-ann : Uses Artificial Neural Network algorithm"
            )
        else:
            print(
                f"You must call this function with arguments\n"
                f"Use {sys.argv[0]} -h for help"
            )
    except IndexError:
        raise SystemExit(
            f"Usage: {sys.argv[0]} [option]\nUse {sys.argv[0]} -h for help"
        )
