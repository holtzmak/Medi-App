from typing import Callable, List

from get_from_csv import get_from_csv
from pomegranate import (
    DiscreteDistribution,
    ConditionalProbabilityTable,
    Node,
    BayesianNetwork,
)


def bayesian_network(get_symptoms_from_user: Callable):
    known_symptoms = get_from_csv("Symptom Probability Tables")
    symptoms = get_symptoms_from_user(  # Maybe this should be somewhere else
        [symptom1 for symptom1, _, _, _ in known_symptoms]
    )
    symptom_distributions, symptom_states = get_symptom_distributions_and_states(
        known_symptoms
    )
    # Collect the models for each disease, predict, then collect top 3 predictions
    # 6 Known diseases at the time of writing
    acne_model = get_bayesian_network_model(
        symptom_distributions=symptom_distributions,
        symptom_states=symptom_states,
        file_name="Acne Full Conditional Probability Table",
        disease_name="acne",
    )
    print(
        "Prediction:",
        acne_model.predict_proba(
            {
                "itching": "1",
                "skin_rash": "0",
                "chills": "1",
                "vomiting": "0",
                "fatigue": "1",
            }
        ),
    )


def get_symptom_distributions_and_states(known_symptoms: List):
    symptom_distributions = []
    symptom_states = []
    for (
        symptom,
        probability,
        not_symptom,
        not_probability,
    ) in known_symptoms:
        symptom_distribution = DiscreteDistribution(
            {"1": float(probability), "0": float(not_probability)}
        )
        symptom_distributions.append(symptom_distribution)
        symptom_states.append((Node(symptom_distribution, name=symptom)))
    return symptom_distributions, symptom_states


def get_bayesian_network_model(
    symptom_distributions: List, symptom_states: List, file_name: str, disease_name: str
):
    disease_conditional_distribution = []
    for (s1, s2, s3, s4, s5, d, p) in get_from_csv(file_name):
        disease_conditional_distribution.append([s1, s2, s3, s4, s5, d, float(p)])
    disease_distribution = ConditionalProbabilityTable(
        disease_conditional_distribution,
        symptom_distributions,
    )
    acne = Node(disease_distribution, name=disease_name)
    model = BayesianNetwork(f"{disease_name} predictor")
    model.add_state(acne)
    for symptom_state in symptom_states:
        model.add_state(symptom_state)
    for symptom_state in symptom_states:
        model.add_edge(symptom_state, acne)
    model.bake()
    return model
