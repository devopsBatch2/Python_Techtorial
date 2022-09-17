
#Create a programm to print True if there is enough ticket for the nba game
#WE will have 2 variables sold tickets and max capacity of the stadium
#if stadium capacity is more than sold tickets we should print True and all other case
#other case we should print False

sold_tickets,max_capacity = 13000 ,1100
is_there_more_ticket = sold_tickets <= max_capacity #True

print("Is there space in the NBA game", is_there_more_ticket , "because we sold",sold_tickets,"we have max capasity of", max_capacity)