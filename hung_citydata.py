startPoint = {
    'x': -300,
    'y': 50,
    'z': -300
}
endPoint = {
    'x': 0,
    'y': 50,
    'z': 0
}

cityHeight = 50
cityGroundBlock = 1
cityGroundData = 4

officeFileData = "thang_house.csv"
officePlace = [
    {
        "name": "Office Hapulico",
        "x": startPoint['x'] + 50,
        "y": startPoint['y'],
        "z": startPoint['z'] + 50,
    },
    {
        "name": "Office Hapulico",
        "x": startPoint['x'] + 100,
        "y": startPoint['y'],
        "z": startPoint['z'] + 50,
    }
]
main_player = "suka blyat"

street = {
    "x": startPoint['x'] + 1,
    "z": startPoint['y'] + 1,
    "y": startPoint['z'] + 50,
    "width": 9,
    "long": 300,
    "block": 35,
    "data": 7
}

office = {
    "x": startPoint['x'] + 1,
    "z": startPoint['z'] + 1,
    "y": startPoint['y'] + 50,
    "width": 26,
    "floors" : 2,
    "floor_height" : 5,
    "long": 26,
    "block": 155,
    "data": 0
}
