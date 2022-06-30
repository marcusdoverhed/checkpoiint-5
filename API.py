import requests

def get_phone(name):
    r = requests.get('http://localhost:5000/api?action=phone&name=Urban')
    name = r.text
    return name
    
def get_name(phone):
    r = requests.get('http://localhost:5000/api?action=name&phone=0435-4355438')
    phone = r.text
    return phone