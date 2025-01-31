from typing import List, Type

from pnpxai.evaluator._evaluator import EvaluationMetric
from pnpxai.evaluator.complexity import Complexity
from pnpxai.evaluator.mu_fidelity import MuFidelity
from pnpxai.evaluator.sensitivity import Sensitivity

AVAILABLE_METRICS: List[Type[EvaluationMetric]] = [Complexity, MuFidelity, Sensitivity]