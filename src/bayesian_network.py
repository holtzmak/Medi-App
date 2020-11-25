import operator
from typing import Callable, List

from get_from_csv import get_from_csv
from pomegranate import (
    DiscreteDistribution,
    ConditionalProbabilityTable,
    Node,
    BayesianNetwork,
)


class BayesianNetworkForDiseasePrediction:
    def __init__(self, get_symptoms_from_user: Callable):
        self.get_symptoms_from_user = get_symptoms_from_user

    # TODO: Make agnostic to symtoms, diseases, filename, etc.
    def predict_with_bayesian_network(self):
        known_symptoms = get_from_csv("Symptom Probability Tables")
        user_symptoms = self.get_full_symptom_set(
            self.get_symptoms_from_user, known_symptoms
        )
        (
            symptom_distributions,
            symptom_states,
        ) = self.get_symptom_distributions_and_states(known_symptoms)
        bayesian_networks_of_diseases = list()
        for disease in [
            "Acne",
            "Allergy",
            "Chicken Pox",
            "Common Cold",
            "Drug Reaction",
            "Psoriasis",
        ]:
            bayesian_networks_of_diseases.append(
                self.get_bayesian_network_model(
                    symptom_distributions=symptom_distributions,
                    symptom_states=symptom_states,
                    file_name=f"{disease} Full Conditional Probability Table",
                    disease_name=disease,
                )
            )
        prediction_results = dict()
        for bayes_net in bayesian_networks_of_diseases:
            symptoms_and_disease_to_predict = list()
            for s in user_symptoms.values():
                symptoms_and_disease_to_predict.append(
                    f"{s}"  # Requires string per API
                )
            symptoms_and_disease_to_predict.append(
                "1"  # Predict the disease as present
            )
            prediction_results[bayes_net.name] = bayes_net.probability(
                [symptoms_and_disease_to_predict]
            )
        print(
            "Top 3 predicted diseases are (disease, probability):",
            sorted(
                prediction_results.items(), key=operator.itemgetter(1), reverse=True
            )[:3],
        )

    # TODO: Make agnostic to number symptoms
    @staticmethod
    def get_full_symptom_set(get_symptoms_from_user: Callable, known_symptoms: List):
        user_symptoms = get_symptoms_from_user([s for s, _, _, _ in known_symptoms])
        symptom_dict = dict()
        for symptom, _, _, _ in known_symptoms:
            symptom_dict[symptom] = 1 if symptom in user_symptoms else 0
        return symptom_dict

    # TODO: Make agnostic to symptoms
    @staticmethod
    def get_symptom_distributions_and_states(known_symptoms: List):
        symptom_distributions = list()
        symptom_states = list()
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

    # TODO: Make agnostic to number symptoms
    @staticmethod
    def get_bayesian_network_model(
        symptom_distributions: List,
        symptom_states: List,
        file_name: str,
        disease_name: str,
    ):
        disease_conditional_distribution = list()
        for (s1, s2, s3, s4, s5, d, p) in get_from_csv(file_name):
            disease_conditional_distribution.append([s1, s2, s3, s4, s5, d, float(p)])
        disease_distribution = ConditionalProbabilityTable(
            disease_conditional_distribution,
            symptom_distributions,
        )
        disease = Node(disease_distribution, name=disease_name)
        model = BayesianNetwork(disease_name)
        model.add_state(disease)
        for symptom_state in symptom_states:
            model.add_state(symptom_state)
            model.add_edge(symptom_state, disease)
        model.bake()
        return model
