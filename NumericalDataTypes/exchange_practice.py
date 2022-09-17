#create a python programm to give most efficient exchange possible using only 
#coins
#quarter 25 cents
#nickle 5 centes
#dime 10 cents
#penny 1 cent
#$2.34 exchange
#9 quarters
#0 dimes
# 1 nucles
#4 pennies
# $1.89
# 7 quarters 1 dimes and 0 nickels 4 pennies

dollar = 2.36
dollar_amount = dollar * 100

quarter_value = 25
dime_value= 10
nickle_value= 5
penny = 1

count_of_q = dollar_amount // quarter_value

print(count_of_q)

remaining_exchange_after_q = dollar_amount % quarter_value
 

count_of_dime =remaining_exchange_after_q // dime_value
print(count_of_dime)
remaining_exchange_after_d = remaining_exchange_after_q % dime_value
count_of_nickle = remaining_exchange_after_d // nickle_value

























