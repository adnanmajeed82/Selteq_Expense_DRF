from rest_framework import serializers
from .models import Employee, Attendance, HR, Salary, Expense, OfficeRent, UtilitiesBills, KitchenGroceryExpense, OfficeMaintenanceExpense, ElectronicEquipmentExpense, ManagerExpense, CompanyIncome, ExpenseReceipt

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class HRSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = '__all__'

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class OfficeRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeRent
        fields = '__all__'

class UtilitiesBillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilitiesBills
        fields = '__all__'

class KitchenGroceryExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenGroceryExpense
        fields = '__all__'

class OfficeMaintenanceExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeMaintenanceExpense
        fields = '__all__'

class ElectronicEquipmentExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicEquipmentExpense
        fields = '__all__'

class ManagerExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerExpense
        fields = '__all__'

class CompanyIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyIncome
        fields = '__all__'

class ExpenseReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseReceipt
        fields = '__all__'
