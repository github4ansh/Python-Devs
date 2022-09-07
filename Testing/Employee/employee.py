class Employee:
    """
    Employee Class
    """
    raise_amt = 2.3
    HIKE_PROMPT = "What's your expected hike percentage"

    def __init__(self, first: str, last: str, pay: float, mail: str):
        self.first: str = first
        self.last: str = last
        self.pay: float = pay
        self.email: str = mail

    def apply_raise(self):
        self.pay *= self.raise_amt

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, mail):
        if not all(['@' in mail, '.' in mail]):
            raise ValueError
        self._email = mail

    def print_fullname(self):
        full_name = '{} {}'.format(self.first, self.last)
        print(full_name)
        return full_name

    @staticmethod
    def expected_salary_hike():

        invalid_input = True
        while invalid_input:
            required_hike = input(Employee.HIKE_PROMPT)
            if isinstance(required_hike, float):
                invalid_input = False
            else:
                print('Please provide the valid input. (System accepts float value as valid input')
        return required_hike
