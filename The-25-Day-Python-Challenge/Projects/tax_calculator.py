base_income: float = float(input("Enter your yearly income: $"))
tax_rate: float = float(input("Enter your tax rate percentage: ")) / 100
taxed: float = base_income * tax_rate

print("=" * 40)
print("Income Tax Calculator")
print(40 * "=")
print(f"Base income:          ${base_income}")
print(f"Tax rate:             {tax_rate:.0%}")
print(40 * "-")
print(f"Yearly tax (Base):     ${taxed:.2f}")
print(40 * "=")