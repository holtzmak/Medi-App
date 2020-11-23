import unittest

from src.symptom_input_util import get_symptom_list_from_user_symptoms


class TestGetSymptomListFromUserSymptoms(unittest.TestCase):
    def test_user_input_rejected_containing_mistake(self):
        self.assertEqual(
            None,
            get_symptom_list_from_user_symptoms("feaver cough", ["fever", "cough"]),
        )

    def test_user_input_rejected_for_one_symptom(self):
        self.assertEqual(
            None,
            get_symptom_list_from_user_symptoms("itching", ["fever", "cough"]),
        )

    def test_user_input_rejected_for_no_symptom(self):
        self.assertEqual(
            None,
            get_symptom_list_from_user_symptoms("", ["fever", "cough"]),
        )

    def test_user_input_accepted(self):
        self.assertEqual(
            ["fever", "cough"],
            get_symptom_list_from_user_symptoms("fever cough", ["fever", "cough"]),
        )

    def test_user_input_accepted_for_one_symptom(self):
        self.assertEqual(
            ["fever"],
            get_symptom_list_from_user_symptoms("fever", ["fever", "cough"]),
        )


if __name__ == "__main__":
    unittest.main()
