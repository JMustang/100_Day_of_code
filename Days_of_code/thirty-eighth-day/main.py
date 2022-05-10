import requests as req

GENDER = 'male'
WEIGHT_KG = '85'
HEIGHT_CM = '179'
AGE = '35'


API_ID = 'b6ee5294'
API_KEY = 'b6bcecafce4e555bcf764c45087e11dc'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input('Tell me which exercises you did: ')

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

parameters = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}


res = req.post(exercise_endpoint, json=parameters, headers=headers)
result = res.json()
print(result)
