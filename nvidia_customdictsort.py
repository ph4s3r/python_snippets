
"""
 Sorting
sorting requirements: sort  FULLNAME in ascending order first, if there are same records with FULLNAME then, 
sort by Total_Points in descending)
Please do not make change on data but just sort

    b = [{u'FULLNAME': u'Utley, Alex', u'Total_Points': 96.0,u'Region': 'US'},
    {u'FULLNAME': u'Russo, Brandon', u'Total_Points': 96.0,u'Region': 'US'},
    {u'FULLNAME': u'Chappell, Justin', u'Total_Points': 96.0,u'Region': 'US'},
    {u'FULLNAME': u'Foster, Toney', u'Total_Points': 80.0,u'Region': 'US'},
    {u'FULLNAME': u'Lawson, Roman', u'Total_Points': 80.0,u'Region': 'JP'},
    {u'FULLNAME': u'Lempke, Sam', u'Total_Points': 80.0,u'Region': 'US'},
    {u'FULLNAME': u'Gnezda, Alex', u'Total_Points': 78.0,u'Region': 'US'},
    {u'FULLNAME': u'Kirks, Damien', u'Total_Points': 78.0,u'Region': 'US'},
    {u'FULLNAME': u'Worden, Tom', u'Total_Points': 78.0,u'Region': 'EU'},
    {u'FULLNAME': u'Korecz, Mike', u'Total_Points': 78.0,u'Region': 'US'},
    {u'FULLNAME': u'Swartz, Brian', u'Total_Points': 66.0,u'Region': 'US'},
    {u'FULLNAME': u'Burgess, Randy', u'Total_Points': 66.0,u'Region': 'EU'},
    {u'FULLNAME': u'Smugala, Ryan', u'Total_Points': 66.0,u'Region': 'US'},
    {u'FULLNAME': u'Harmon, Gary', u'Total_Points': 66.0,u'Region': 'US'},
    {u'FULLNAME': u'Blasinsky, Scott', u'Total_Points': 60.0,u'Region': 'AS'},
    {u'FULLNAME': u'Carter III, Laymon', u'Total_Points': 60.0,u'Region': 'US'},
    {u'FULLNAME': u'Coleman, Johnathan', u'Total_Points': 60.0,u'Region': 'US'},
    {u'FULLNAME': u'Venditti, Nick', u'Total_Points': 60.0,u'Region': 'KM'},
    {u'FULLNAME': u'Blackwell, Devon', u'Total_Points': 60.0,u'Region': 'US'},
    {u'FULLNAME': u'Kovach, Alex', u'Total_Points': 60.0,u'Region': 'US'},
    {u'FULLNAME': u'Kovach, Alex', u'Total_Points': 30.0,u'Region': 'SK'},
    {u'FULLNAME': u'Phil, Alex', u'Total_Points': 30.0,u'Region': 'SK'},
    {u'FULLNAME': u'Bolden, Antonio', u'Total_Points': 60.0,u'Region': 'EU'},
    {u'FULLNAME': u'Chappell, Justin', u'Total_Points': 98.0,u'Region': 'US'}, 
    {u'FULLNAME': u'Smith, Ryan', u'Total_Points': 60.0,u'Region': 'US'}]
"""


#csinaltam az eredeti adatbol egy sima listat amiben csak a nevek vannak, azt egy list.sort() -al rendeztem, majd osszeraktam az egeszet

names = []
for dude in b:
	names.append(dude['FULLNAME'])

sortedb = []
for name in names:
         for dude in b:
             if dude['FULLNAME'] == name:
                 sortedb.append(dude)
