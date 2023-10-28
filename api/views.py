from rest_framework import generics
from .models import Employee, Attendance, HR, Salary, Expense, OfficeRent, UtilitiesBills, KitchenGroceryExpense, OfficeMaintenanceExpense, ElectronicEquipmentExpense, ManagerExpense, CompanyIncome, ExpenseReceipt
from .serializers import EmployeeSerializer, AttendanceSerializer, HRSerializer, SalarySerializer, ExpenseSerializer, OfficeRentSerializer, UtilitiesBillsSerializer, KitchenGroceryExpenseSerializer, OfficeMaintenanceExpenseSerializer, ElectronicEquipmentExpenseSerializer, ManagerExpenseSerializer, CompanyIncomeSerializer, ExpenseReceiptSerializer
from rest_framework import generics
from .models import ExpenseReceipt
from .serializers import ExpenseReceiptSerializer
from .models import OfficeRent
from .serializers import OfficeRentSerializer
from .models import UtilitiesBills
from .serializers import UtilitiesBillsSerializer
from .models import KitchenGroceryExpense
from .serializers import KitchenGroceryExpenseSerializer
from .models import OfficeMaintenanceExpense
from .serializers import OfficeMaintenanceExpenseSerializer
from .models import ElectronicEquipmentExpense
from .serializers import ElectronicEquipmentExpenseSerializer
from .models import ManagerExpense
from .serializers import ManagerExpenseSerializer
from .models import CompanyIncome
from .serializers import CompanyIncomeSerializer

# Create CRUD views for each model
class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Create similar views for other models
# ...

class AttendanceListView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# Continue creating views for other models

# Create views for HR, Salary, Expense, etc.
class HRListView(generics.ListCreateAPIView):
    queryset = HR.objects.all()
    serializer_class = HRSerializer

class HRDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HR.objects.all()
    serializer_class = HRSerializer

class SalaryListView(generics.ListCreateAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

class SalaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

# Create views for other models in a similar manner

# Example for Expenses
class ExpenseListView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# Create views for OfficeRent, UtilitiesBills, KitchenGroceryExpense, OfficeMaintenanceExpense, ElectronicEquipmentExpense, ManagerExpense, CompanyIncome, and ExpenseReceipt models in a similar manner.

# Create a view for listing and creating OfficeRent objects
class OfficeRentListView(generics.ListCreateAPIView):
    queryset = OfficeRent.objects.all()
    serializer_class = OfficeRentSerializer

# Create a view for retrieving, updating, and deleting OfficeRent instances
class OfficeRentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfficeRent.objects.all()
    serializer_class = OfficeRentSerializer


# Create a view for listing and creating UtilitiesBills objects
class UtilitiesBillsListView(generics.ListCreateAPIView):
    queryset = UtilitiesBills.objects.all()
    serializer_class = UtilitiesBillsSerializer

# Create a view for retrieving, updating, and deleting UtilitiesBills instances
class UtilitiesBillsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UtilitiesBills.objects.all()
    serializer_class = UtilitiesBillsSerializer


# Create a view for listing and creating KitchenGroceryExpense objects
class KitchenGroceryExpenseListView(generics.ListCreateAPIView):
    queryset = KitchenGroceryExpense.objects.all()
    serializer_class = KitchenGroceryExpenseSerializer

# Create a view for retrieving, updating, and deleting KitchenGroceryExpense instances
class KitchenGroceryExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KitchenGroceryExpense.objects.all()
    serializer_class = KitchenGroceryExpenseSerializer

# Create a view for listing and creating OfficeMaintenanceExpense objects
class OfficeMaintenanceExpenseListView(generics.ListCreateAPIView):
    queryset = OfficeMaintenanceExpense.objects.all()
    serializer_class = OfficeMaintenanceExpenseSerializer

# Create a view for retrieving, updating, and deleting OfficeMaintenanceExpense instances
class OfficeMaintenanceExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfficeMaintenanceExpense.objects.all()
    serializer_class = OfficeMaintenanceExpenseSerializer

# Create a view for listing and creating ElectronicEquipmentExpense objects
class ElectronicEquipmentExpenseListView(generics.ListCreateAPIView):
    queryset = ElectronicEquipmentExpense.objects.all()
    serializer_class = ElectronicEquipmentExpenseSerializer

# Create a view for retrieving, updating, and deleting ElectronicEquipmentExpense instances
class ElectronicEquipmentExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElectronicEquipmentExpense.objects.all()
    serializer_class = ElectronicEquipmentExpenseSerializer

# Create a view for listing and creating ManagerExpense objects
class ManagerExpenseListView(generics.ListCreateAPIView):
    queryset = ManagerExpense.objects.all()
    serializer_class = ManagerExpenseSerializer

# Create a view for retrieving, updating, and deleting ManagerExpense instances
class ManagerExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManagerExpense.objects.all()
    serializer_class = ManagerExpenseSerializer

# Create a view for listing and creating CompanyIncome objects
class CompanyIncomeListView(generics.ListCreateAPIView):
    queryset = CompanyIncome.objects.all()
    serializer_class = CompanyIncomeSerializer

# Create a view for retrieving, updating, and deleting CompanyIncome instances
class CompanyIncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyIncome.objects.all()
    serializer_class = CompanyIncomeSerializer

# Create a view for listing and creating ExpenseReceipt objects
class ExpenseReceiptListView(generics.ListCreateAPIView):
    queryset = ExpenseReceipt.objects.all()
    serializer_class = ExpenseReceiptSerializer

# Create a view for retrieving, updating, and deleting ExpenseReceipt instances
class ExpenseReceiptDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpenseReceipt.objects.all()
    serializer_class = ExpenseReceiptSerializer
