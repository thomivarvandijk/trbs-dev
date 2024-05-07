"""
This file contains the Optimize class that deals with finding the allocation of internal variables that results in the
highest appreciation value
"""
import numpy as np
from core.evaluate import Evaluate
from core.appreciate import Appreciate
from core.utils import get_values_from_target

'''
Waarderingsfunctie moet je vastprikken <--  werkt voor stap 6 & 7 


Gebruiker kiest of je waardering bepaald voor scenario of voor alle scenario's 
Optimaliseer je binnen scenario
Automatisch bepaalde maximum 
'''

class Optimize:
    """This class deals with finding the optimal scenario"""

    def __init__(self, input_dict_with_optimal):
        self.input_dict_with_optimal = input_dict_with_optimal

    def _get_initial_solution(self):
        self.input_dict_with_optimal["decision_makers_options"] = np.append(
            self.input_dict_with_optimal["decision_makers_options"], ["optimal"]
        )
        self.input_dict_with_optimal["decision_makers_option_value"] = np.append(
            self.input_dict_with_optimal["decision_makers_option_value"], [[150000, 150000]], axis=0
        )

    def _format_output(self, output_dict):
        """
        This function returns a dictionary with the total appreciation for each of the scenarios
        """
        optimize_output = {
            scenario: output_dict[scenario]["optimal"]["decision_makers_option_appreciation"]
            for scenario in self.input_dict_with_optimal["scenarios"]
        }
        return optimize_output

    def optimize(self, scenario):
        self._get_initial_solution()
        case_evaluated = {scenario: Evaluate(self.input_dict_with_optimal).evaluate_selected_scenario(scenario)}
        case_appreciation = Appreciate(self.input_dict_with_optimal, case_evaluated)
        case_appreciation.appreciate_all_scenarios()

        print(case_appreciation.output_dict)

        # print(self._format_output(case_appreciation.output_dict))
