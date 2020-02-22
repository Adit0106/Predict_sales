import pickle

model = pickle.load(open('model.pkl', 'rb'))
rate = int(input('Enter the rate\n'))
sales_in_first_month = int(input('Enter the sales in first month\n'))
sales_in_second_month = int(input('Enter the sales in second month\n'))

sales_in_third_month = model.predict([[rate,
                                       sales_in_first_month,
                                       sales_in_second_month]])

print(f'Sales in third month would be {sales_in_third_month}')
