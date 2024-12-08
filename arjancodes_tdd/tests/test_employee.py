import unittest

from arjancodes_tdd.models.employee import Employee

NAME: str = "Gutierre"
EMPLOYEE_ID: int = "1"

class TestEmployeeComputePayout(unittest.TestCase):
    """Test the compute_payout method of the Employtee class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.gutierre = Employee(name=NAME, employee_id=EMPLOYEE_ID)

    def test_employee_payout_returns_a_float(self):
        """Wheter payout returns a float."""
        raise NotImplementedError
    
    def test_employee_payout_no_comission_no_hours(self):
        """Wheter payout is correctly computed in case of no comission and no hours worked."""
        raise NotImplementedError
    
    def test_employee_payout_no_comission(self):
        """Wheter payout is correctly computed in case of no comission and 10 hours worked."""
        raise NotImplementedError
    
    def test_employee_payout_with_comission(self):
        """Wheter payout is corretly computed in case of 10 contracts landed and 10 hours worked."""
        raise NotImplementedError
    
    def test_employee_payout_with_comission_disabled(self):
        """Wheter payout is correctly computed in case of 10 contracts landed and 10 hours worked, but comission is disabled."""
        raise NotImplementedError