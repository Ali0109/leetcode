from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractEmployee(ABC):
    @abstractmethod
    def create_employee(self):
        pass


class BaseEmployee(AbstractEmployee):
    def __init__(self, name, email, role, is_company_staff, salary_by_hour):
        self._name = name
        self._email = email
        self._role = role
        self._is_company_staff = is_company_staff
        self._salary_by_hour = salary_by_hour

        self.__available_roles = ["developer", "manager", "accountant"]

        if role not in self.__available_roles:
            raise ValueError("Role must be one of %s" % self.__available_roles)

    def __str__(self):
        return f"{self._name} ({self._email})"

    def create_employee(self):
        if self._role == "developer" and self._is_company_staff:
            return CompanyDeveloperEmployee()


class CompanyDeveloperEmployee(BaseEmployee):

    def calculate_payment(self):
        return self._cost


if __name__ == "__main__":
    # create regular manager
    regular_manager = RegularManagerEmployee("Alice Brown", "alice@brown.com", 2000, "Regular Team A")

    # add tasks to team
    regular_manager.add_task_to_team("Task 1")
    regular_manager.add_task_to_team("Task 2")

    # create regular developers
    regular_developer_1 = RegularDeveloperEmployee("John Doe", "john@doe.com", 1000, "Python")
    regular_developer_2 = RegularDeveloperEmployee("Mike Smith", "mike@smith.com", 1200, "JavaScript")

    # add developers to team
    regular_manager.add_developer_to_team(regular_developer_1)
    regular_manager.add_developer_to_team(regular_developer_2)

    # assign tasks to developers
    regular_manager.assign_tasks_to_developers()

    # start a new sprint
    regular_manager.start_sprint()

    # finish the sprint once all the tasks are completed
    regular_manager.finish_sprint()

    # pay employees for their work
    print(f"{regular_manager.name} got payment: {regular_manager.calculate_payment()}")
    print(f"{regular_developer_1.name} got payment: {regular_developer_1.calculate_payment()}")
    print(f"{regular_developer_2.name} got payment: {regular_developer_2.calculate_payment()}")
