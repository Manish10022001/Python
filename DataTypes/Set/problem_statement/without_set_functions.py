# ====================================================================================================
# 		Problem Statement --Solve the following Problem without using Set Functions
# 									Use Bitwise Operators
# ====================================================================================================
# =>Let us consider
# 		Set of Cricket Players={"Rohit","Virat","Rossum"}
# 		Set of Tennis Players={"Rossum","Travis","Hunter"}
# Answer the Following Queries
# --------------------------------------------------------
cricket_players = {"Rohit","Virat","Rossum"}
tennis_players = {"Rossum","Travis","Hunter"}

# 1. Find the Player Names who are playing all the games 
tp = cricket_players|tennis_players
print(tp)

# 2. Find the Player Names who are playing  both Cricket and Tennis
tp = cricket_players & tennis_players
print(tp)

# 3. Find the Player Names who are playing Only Cricket
only_cp = cricket_players - tennis_players
print(only_cp)

# 4. Find the Player Names who are playing Only Tennis
only_tp = tennis_players - cricket_players
print(only_tp)

# 5. Find the Player Names who are playing Exclusively Cricket and Tennis.
excl_cp_tp = cricket_players ^ tennis_players
print(excl_cp_tp)