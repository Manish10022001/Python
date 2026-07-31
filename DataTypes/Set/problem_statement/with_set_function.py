# 		===========================================================================
# 			Problem Statement by using sets Functions
# 		===========================================================================
# =>Let us consider
# 		Set of Cricket Players={"Rohit","Virat","Rossum"}
# 		Set of Tennis Players={"Rossum","Travis","Hunter"}
# Answer the Following Queries
# --------------------------------------------------------
cricket_players = {"Virat", "Suresh", "Rossum"}
tennis_players  = {"Travis", "Hunter", "Rossum"}

# 1. Find the Player Names who are playing all the games 
total_players = cricket_players.union(tennis_players)
print(total_players)

# 2. Find the Player Names who are playing  both Cricket and Tennis
total_players = cricket_players.intersection(tennis_players)
print(total_players)

# 3. Find the Player Names who are playing Only Cricket
only_cricket_players = cricket_players.difference(tennis_players)
print(only_cricket_players)

# 4. Find the Player Names who are playing Only Tennis
only_tennis_players = tennis_players.difference(cricket_players)
print(only_tennis_players)

# 5. Find the Player Names who are playing Exclusively Cricket and Tennis.
both_tennis_cricket_players = cricket_players.symmetric_difference(tennis_players)
print(both_tennis_cricket_players)