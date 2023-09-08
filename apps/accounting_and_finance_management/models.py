from django.db import models

# Chart Of Accounts Table
class ChartOfAccounts(models.Model):
    AccountID = models.AutoField(primary_key=True)
    AccountNumber = models.CharField(max_length=20, unique=True)
    AccountName = models.CharField(max_length=255, unique=True)
    AccountType = models.CharField(max_length=50)
    Description = models.CharField(max_length=255, null=True)


# Customers Related Tables
class Customers(models.Model):
    ID = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=255, unique=True)
    CustomerAddress = models.CharField(max_length=255)
    ContactPerson = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(max_length=255, unique=True)


class InvoicePayments(models.Model):
    ID = models.AutoField(primary_key=True)
    COA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    TransalctionDate = models.DateField()
    Description = models.CharField(max_length=250)
    Reference = models.CharField(max_length=250)
    TotalAmount = models.DecimalField(max_digits=20, decimal_places=2)


class CustomerInvoices(models.Model):
    ID = models.AutoField(primary_key=True)
    TransalctionDate = models.DateField()
    DueDate = models.DateField()
    Description = models.CharField(max_length=250)
    Reference = models.CharField(max_length=250)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    InvoicePaymentID = models.ForeignKey(InvoicePayments, on_delete=models.CASCADE)
    COA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    Status = models.BooleanField()


class IncommingMoney(models.Models):
    ID = models.AutoField(primary_key=True)
    TransactionDate = models.DateField()
    Description = models.CharField(max_length=255)
    Reference = models.CharField(max_length=250)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    COA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)


class InvoiceLines(models.Model):
    ID = models.AutoField(primary_key=True)
    LineAmount = models.DecimalField(max_digits=10, decimal_places=2)
    InvoiceID = models.ForeignKey(CustomerInvoices, on_delete=models.CASCADE)
    LineCOA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)


class IncommingMoneyLines(models.Model):
    ID = models.AutoField(primary_key=True)
    LineAmount = models.DecimalField(max_digits=10, decimal_places=2)
    IncommingMoneyID = models.ForeignKey(IncommingMoney, on_delete=models.CASCADE)
    LineCOA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)

# Vendors Related Tables
class Vendors(models.Model):
    ID = models.AutoField(primary_key=True)
    VendorName = models.CharField(max_length=255, unique=True)
    VendorAddress = models.CharField(max_length=255)
    ContactPerson = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(max_length=255, unique=True)


class BillPayments(models.Model):
    ID = models.AutoField(primary_key=True)
    COA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    TransactionDate = models.DateField()
    Description = models.CharField(max_length=255)
    Reference = models.CharField(max_length=250)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    

class VendorBills(models.Model):
    ID = models.AutoField(primary_key=True)
    TransalctionDate = models.DateField()
    DueDate = models.DateField()
    Description = models.CharField(max_length=250)
    Reference = models.CharField(max_length=250)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    VendorID = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    BillPaymentID = models.ForeignKey(BillPayments, on_delete=models.CASCADE)
    COA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    Status = models.BooleanField()


class OutgoingMoney(models.Models):
    ID = models.AutoField(primary_key=True)
    TransactionDate = models.DateField()
    Description = models.CharField(max_length=255)
    Reference = models.CharField(max_length=250)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    VendorID = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    COA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)


class BillLines(models.Model):
    ID = models.AutoField(primary_key=True)
    LineAmount = models.DecimalField(max_digits=10, decimal_places=2)
    BillID = models.ForeignKey(VendorBills, on_delete=models.CASCADE)
    LineCOA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)


class OutgoingMoneyLines(models.Model):
    ID = models.AutoField(primary_key=True)
    LineAmount = models.DecimalField(max_digits=10, decimal_places=2)
    IncommingMoneyID = models.ForeignKey(OutgoingMoney, on_delete=models.CASCADE)
    LineCOA_ID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
