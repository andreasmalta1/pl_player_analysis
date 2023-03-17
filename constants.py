COLUMNS = [
    "Player",
    "Nation",
    "Pos",
    "Age",
    "MP",
    "Starts",
    "Min",
    "90s",
    "Gls",
    "Ast",
    "G+A",
    "G-PK",
    "PK",
    "PKatt",
    "CrdY",
    "CrdR",
    "xG",
    "npxG",
    "xAG",
    "npxG+xAG",
    "PrgC",
    "PrgP",
    "PrgR",
    "Gls90",
    "Ast90",
    "G+A90",
    "G-PK90",
    "G+A-PK90",
    "xG90",
    "xAG90",
    "xG+xAG90",
    "npxG90",
    "npxG+xAG90",
]

NINETY_COLUMNS = [
    "Gls90",
    "Ast90",
    "G+A90",
    "G-PK90",
    "G+A-PK90",
    "xG90",
    "xAG90",
    "xG+xAG90",
    "npxG90",
    "npxG+xAG90",
]

AGGREGATOR = {
    "Nation": "first",
    "Pos": "first",
    "Age": "first",
    "MP": "sum",
    "Starts": "sum",
    "Min": "sum",
    "90s": "sum",
    "Gls": "sum",
    "Ast": "sum",
    "G+A": "sum",
    "G-PK": "sum",
    "PK": "sum",
    "PKatt": "sum",
    "CrdY": "sum",
    "CrdR": "sum",
    "xG": "sum",
    "npxG": "sum",
    "xAG": "sum",
    "npxG+xAG": "sum",
    "PrgC": "sum",
    "PrgP": "sum",
    "PrgR": "sum",
    "club_name": "first",
    "club_id": "first",
}

TYPES_DICT = {
    "MP": "int",
    "Starts": "int",
    "Min": "int",
    "90s": "float",
    "Gls": "int",
    "Ast": "int",
    "G+A": "int",
    "G-PK": "int",
    "PK": "int",
    "PKatt": "int",
    "CrdY": "int",
    "CrdR": "int",
    "xG": "float",
    "npxG": "float",
    "xAG": "float",
    "npxG+xAG": "float",
    "PrgC": "int",
    "PrgP": "int",
    "PrgR": "int",
}
