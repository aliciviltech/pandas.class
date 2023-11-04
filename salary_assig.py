BasicSalary= int(input("Basic_Salay: "))

ConvenienceAllowance= int(BasicSalary*20/100)
print("Convenience_Allowance :", ConvenienceAllowance)

MedicalAllowance= int(BasicSalary*30/100)
print("Medical_Allowance :", MedicalAllowance)

GrossSalary= (BasicSalary + ConvenienceAllowance + MedicalAllowance)
print("Gross_Salary: ", GrossSalary)

Income_Tax= int(GrossSalary*2/100)
print("Income_Tax: ", Income_Tax)

Net_Salary= (GrossSalary - Income_Tax)
print("Net_Salary: ", Net_Salary)


