from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10, unique=True)
    # Add other employee information fields

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()
    # Add other attendance-related fields

class HR(models.Model):
    name = models.CharField(max_length=100)
    # Add other HR-related fields

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
 

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Add other common expense fields
    receipt = models.ForeignKey('ExpenseReceipt', on_delete=models.SET_NULL, null=True, blank=True, related_name='expense_receipts')

class ExpenseReceipt(models.Model):
    expense = models.OneToOneField(Expense, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='expense_receipts/')
    # Add other receipt-related fields if needed


class OfficeRent(models.Model):
    expense = models.OneToOneField(Expense, on_delete=models.CASCADE)
    

class UtilitiesBills(models.Model):
    bill_type_choices = [
        ('Electricity', 'Electricity'),
        ('Internet', 'Internet'),
        ('Water', 'Water'),
        # Add more bill types as needed
    ]

    bill_type = models.CharField(max_length=20, choices=bill_type_choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    
    # Add foreign keys or relationships to link the bill to relevant departments or managers if needed
    # For example:
    # manager = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bill_type} Bill - {self.date}"
    
class KitchenGroceryExpense(models.Model):
    item_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    
    # Add foreign keys or relationships to link the expense to relevant departments or managers if needed
    # For example:
    # manager = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item_name} Expense - {self.date}"
    
class OfficeMaintenanceExpense(models.Model):
    expense_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    
    # Add foreign keys or relationships to link the expense to relevant departments or managers if needed
    # For example:
    # manager = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.expense_name} Expense - {self.date}"
    
class ElectronicEquipmentExpense(models.Model):
    equipment_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    
    # Add foreign keys or relationships to link the expense to relevant departments or managers if needed
    # For example:
    # manager = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipment_name} Expense - {self.date}"
    

class CompanyIncome(models.Model):
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    
    # Add foreign keys or relationships to link the income to relevant departments or managers if needed
    # For example:
    # manager = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.source} Income - {self.date}"

# Create similar models for other types of expenses
class ManagerExpense(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    finance_manager_charge = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other manager expense-related fields
