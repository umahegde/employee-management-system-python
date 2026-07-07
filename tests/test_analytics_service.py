
from services.analytics_service import DataAnalytics

analytics = DataAnalytics()

class TestAnalyticsService:
    def test_get_total_employees(self):
        employee =  analytics.total_employees()
        assert employee == 4

    def test_get_average_salary(self):
        average = analytics.average_salary_employee()
        assert average == 25000.0

    def test_get_highest_paid_employee(self):
        highest = analytics.highest_salary_employee()
        assert  highest["salary"] == 50000

    def test_get_lowest_paid_employee(self):
        lowest = analytics.lowest_salary_employee()
        assert  lowest["salary"] == 10000
    def test_get_employee_by_department(self):
        result = analytics.employee_by_department('IT')
        assert  result[0]["department"]=='IT'
    def test_get_department_wise_salary(self):
        result = analytics.group_by_department()
        assert result["IT"]== 2




