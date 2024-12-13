month_icom = input("Enter your monthly income: ")
expe_month = input("Enter your total monthly expenses: ")
monthly_incom = float(month_icom)
tot_epe = float(expe_month)
monthly_sav = monthly_incom - tot_epe
print(f"Your monthly savings are {monthly_sav}")
annu_interet = 0.05
projecte_sav = monthly_sav * 12 + monthly_sav *12 * 0.05
print(f"Projected savings after one year, with interest, is: {projecte_sav}")