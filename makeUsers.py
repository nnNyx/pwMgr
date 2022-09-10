from dbQueries import make_user
from main import generatePassword

userList = [
    ("zeljkomimirovic", "zeljko@gmail.com", "instagram", generatePassword(15)),
    ("zeljkic123", "zeljko@gmail.com", "twitter", generatePassword(25)),
    ("ivanhorvat", "ivan@gmail.com", "instagram", generatePassword(40)),
    ("stefan12", "stefan@gmail.com", "w3schools", generatePassword(50)),
    ("isuskrist75", "leo.lelo@gmail.com", "wordle", generatePassword(40)),
    ("stefan12", "stefan@gmail.com", "gtaguessr", generatePassword(30)),
    ("dynamitelarry63", "dynamitelarry63@gmail.com", "league", generatePassword(63)),
    ("flyingraccoon52", "flying.raccoon@tempmail.net", "league", generatePassword(52)),
    ("spunchbop", "bob.gaming@hotmail.co.uk", "krustykrab", generatePassword(30)),
    ("milivoj", "milivoj.netrebamu@mail", "facebook", generatePassword(63)),
    ("anit39", "anita.herceg@gmail.com", "facebook", generatePassword(20)),
    ("stanimir", "stanimir.horvat@gmail.com", "facebook", generatePassword(60)),
    ("boromir", "boromir.prvasic@gmail.com", "facebook", generatePassword(49)),
    ("supermartin29", "martin.anic@gmail.com", "facebook", generatePassword(29)),
    ("jablanap123", "jablana.pelic@gmail.com", "facebook", generatePassword(39)),
]

for i in userList:
    username, email, site, password = i
    make_user(username, email, site, password)
