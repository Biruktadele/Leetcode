"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employe = defaultdict(list)
        for emp in employees:
            employe[emp.id].append(emp.importance)
            employe[emp.id].append(emp.subordinates)

        def totalimportance(employees):
            if not employees:
                return 0
            res = 0
            for ememploye in employees[1]:
                res +=  totalimportance(employe[ememploye])
            return res + employees[0]
        return totalimportance(employe[id])