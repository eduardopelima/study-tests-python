from dataclasses import dataclass


@dataclass
class Employee:
    """Basic implementation of an employee"""

    name: str
    employee_id: int
    pay_rate: float = 100.00
    hours_worked: int
    employeer_cost: float = 1000.0
    has_comission: bool = True
    comission: float = 100.0
    contracts_landed: int = 0

    def compute_payout(self) -> float:
        """Compute how much the employee should be paid."""

        raise NotImplementedError

