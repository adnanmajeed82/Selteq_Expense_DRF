from django.urls import path
from . import views

urlpatterns = [
    # Add URLs for Employee views
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    
    # Add URLs for Attendance views
    path('attendance/', views.AttendanceListView.as_view(), name='attendance-list'),
    path('attendance/<int:pk>/', views.AttendanceDetailView.as_view(), name='attendance-detail'),
    
    # Add URLs for HR views
    path('hr/', views.HRListView.as_view(), name='hr-list'),
    path('hr/<int:pk>/', views.HRDetailView.as_view(), name='hr-detail'),
    
    # Add URLs for Salary views
    path('salary/', views.SalaryListView.as_view(), name='salary-list'),
    path('salary/<int:pk>/', views.SalaryDetailView.as_view(), name='salary-detail'),
    
    # Add URLs for Expense views
    path('expense/', views.ExpenseListView.as_view(), name='expense-list'),
    path('expense/<int:pk>/', views.ExpenseDetailView.as_view(), name='expense-detail'),
    
    # Add URLs for OfficeRent views
    path('office-rent/', views.OfficeRentListView.as_view(), name='office-rent-list'),
    path('office-rent/<int:pk>/', views.OfficeRentDetailView.as_view(), name='office-rent-detail'),

    # Add URLs for UtilitiesBills views
    path('utilities-bills/', views.UtilitiesBillsListView.as_view(), name='utilities-bills-list'),
    path('utilities-bills/<int:pk>/', views.UtilitiesBillsDetailView.as_view(), name='utilities-bills-detail'),
    
    # Add URLs for KitchenGroceryExpense views
    path('kitchen-grocery-expense/', views.KitchenGroceryExpenseListView.as_view(), name='kitchen-grocery-expense-list'),
    path('kitchen-grocery-expense/<int:pk>/', views.KitchenGroceryExpenseDetailView.as_view(), name='kitchen-grocery-expense-detail'),
    
    # Add URLs for OfficeMaintenanceExpense views
    path('office-maintenance-expense/', views.OfficeMaintenanceExpenseListView.as_view(), name='office-maintenance-expense-list'),
    path('office-maintenance-expense/<int:pk>/', views.OfficeMaintenanceExpenseDetailView.as_view(), name='office-maintenance-expense-detail'),
    
    # Add URLs for ElectronicEquipmentExpense views
    path('electronic-equipment-expense/', views.ElectronicEquipmentExpenseListView.as_view(), name='electronic-equipment-expense-list'),
    path('electronic-equipment-expense/<int:pk>/', views.ElectronicEquipmentExpenseDetailView.as_view(), name='electronic-equipment-expense-detail'),
    
    # Add URLs for ManagerExpense views
    path('manager-expense/', views.ManagerExpenseListView.as_view(), name='manager-expense-list'),
    path('manager-expense/<int:pk>/', views.ManagerExpenseDetailView.as_view(), name='manager-expense-detail'),
    
    # Add URLs for CompanyIncome views
    path('company-income/', views.CompanyIncomeListView.as_view(), name='company-income-list'),
    path('company-income/<int:pk>/', views.CompanyIncomeDetailView.as_view(), name='company-income-detail'),
    
    # Add URLs for ExpenseReceipt views
    path('expense-receipt/', views.ExpenseReceiptListView.as_view(), name='expense-receipt-list'),
    path('expense-receipt/<int:pk>/', views.ExpenseReceiptDetailView.as_view(), name='expense-receipt-detail'),
]
