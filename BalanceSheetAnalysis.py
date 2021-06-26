import requests
import matplotlib.pyplot as plt

api_key = '(apikey)'

company = 'FB'
years = 2

balance_sheet = requests.get(link)

#print(list(filter(lambda x:x["id_number"]=="CZ1094",balance_sheet)))

#print(balance_sheet.json())
balance_sheet = balance_sheet.json()

'''result = str(balance_sheet[0]['totalCurrentAssets'])             #to show current asset value
print(result)'''

#assets
total_assets = balance_sheet[0]['totalAssets']
print(f'Total  Assets of {company} is {total_assets:,}')

#current assets
total_current_assets = balance_sheet[0]['totalCurrentAssets']
print(f'Total Current Assets of {company} is {total_current_assets:,}')         #, used for seperator in large digits

total_current_liabilities = balance_sheet[0]['totalCurrentLiabilities']
print(f'Total Current Liabilities of {company} is {total_current_liabilities:,}')

total_debt = balance_sheet[0]['totalDebt']
cash_and_equivalents = balance_sheet[0]['cashAndCashEquivalents']
cash_debt_diff = cash_and_equivalents - total_debt
print(f'Cash Debt Difference of {company} is {cash_debt_diff:,}')

#precentage of intangible assets
goodwill_and_intangible = balance_sheet[0]['goodwillAndIntangibleAssets']
percent_intangible = goodwill_and_intangible / total_assets
print(f'Percent of Intangible assets of {company} is {percent_intangible * 100:.2f}%')

#quarterly
years1 = 5
balance_sheet1 = balance_sheet = requests.get(link)
balance_sheet1 = balance_sheet1.json()

assets_q1 = balance_sheet1[4]['totalAssets']
assets_q2 = balance_sheet1 [3]['totalAssets']
assets_q3 = balance_sheet1 [2]['totalAssets']
assets_q4 = balance_sheet1 [1]['totalAssets']

asset_data = [assets_q1,assets_q2,assets_q3,assets_q4]
asset_data = [x / 1000000000 for x in asset_data]

plt.bar([1,2,3,4], asset_data)
plt.title(f'Quartely Assets of {company}')
plt.ylabel('Total Assets(in Billions USD)')
plt.xlabel('Quarters')
plt.xticks([1,2,3,4],['Q1', 'Q2', 'Q3', 'Q4'])
plt.show()

