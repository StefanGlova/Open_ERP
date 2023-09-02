from django.db import models

# Create your models here.
class ChartOfAccounts(models.Model):
    AccountID = models.AutoField(primary_key=True)
    AccountNumber = models.CharField(max_length=20, unique=True)
    AccountName = models.CharField(max_length=255, unique=True)
    AccountType = models.CharField(max_length=50)
    Description = models.CharField(max_length=255, null=True)


class Transactions(models.Models):
    TransactionID = models.AutoField(primary_key=True)
    TransactionDate = models.DateField()
    AccountID = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    Description = models.CharField(max_length=255)
    DebitAmount = models.DecimalField(max_digits=10, decimal_places=2)
    CreditAmount = models.DecimalField(max_digits=10, decimal_places=2)


class Vendor(models.Model):
    VendorID = models.AutoField(primary_key=True)
    VendorName = models.CharField(max_length=255, unique=True)
    VendorAddress = models.CharField(max_length=255)
    ContactPerson = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(max_length=255, unique=True)


class Customers(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=255, unique=True)
    CustomerAddress = models.CharField(max_length=255)
    ContactPerson = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(max_length=255, unique=True)


class CustomerInvoices(models.Model):
    InvoiceID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    InvoiceDate = models.DateField()
    DueDate = models.DateField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    VATAmount = models.DecimalField(max_digits=10, decimal_places=2)


class VendorInvoices(models.Model):
    InvoiceID = models.AutoField(primary_key=True)
    VendorID = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    InvoiceDate = models.DateField()
    DueDate = models.DateField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    VATAmount = models.DecimalField(max_digits=10, decimal_places=2)


class IncomingPayments(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    VendorID = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    PaymentDate = models.DateField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)


class OutgoingPayments(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    VendorID = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    PaymentDate = models.DateField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)


class CashAccounts(models.Model):
    CashAccountID = models.AutoField(primary_key=True)
    AccountName = models.CharField(max_length=255)
    Balance = models.DecimalField(max_digits=10, decimal_places=2)


class BankAccounts(models.Model):
    BankAccountID = models.AutoField(primary_key=True)
    AccountName = models.CharField(max_length=255)
    Balance = models.DecimalField(max_digits=10, decimal_places=2)
    BankName = models.CharField(max_length=255)
    AccountNumber = models.CharField(max_length=20)
    SortCode = models.CharField(max_length=20)


class TaxCodes(models.Model):
    TaxCodeID = models.AutoField(primary_key=True)
    Code = models.CharField(max_length=10)
    Description = models.CharField(max_length=255, null=True)
    Rate = models.DecimalField(max_digits=5, decimal_places=2)


class TaxReturns(models.Model):
    TaxReturnID = models.AutoField(primary_key=True)
    Year = models.IntegerField()
    VATReturn = models.DecimalField(max_digits=10, decimal_places=2)
    CorporationTaxReturn = models.DecimalField(max_digits=10, decimal_places=2)
    PayrollTaxReturn = models.DecimalField(max_digits=10, decimal_places=2)

