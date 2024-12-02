from django.shortcuts import render
from .forms import AddressForm
from django.conf import settings
import requests

def get_coordinates(address):
    api_key = "sua_chave_opencage_api"  # Coloque sua chave aqui
    url = f"https://api.opencagedata.com/geocode/v1/json?q={address}&key={api_key}"
    response = requests.get(url).json()

    if response and response['results']:
        geometry = response['results'][0]['geometry']
        return {'lat': geometry['lat'], 'lng': geometry['lng']}
    return None

def get_nearby_places(lat, lng):
    api_key = settings.FOURSQUARE_API_KEY  # Certifique-se de que a chave está no settings
    url = "https://api.foursquare.com/v3/places/nearby"
    headers = {"Authorization": api_key}
    params = {
        "ll": f"{lat},{lng}",
        "radius": 1000,  # Raio de 1 km
        "categories": "16000,17000"  # Exemplo de categorias: restaurantes, cafés
    }

    response = requests.get(url, headers=headers, params=params)
    
    # Verifique a resposta da API para ver o que está sendo retornado
    print(response.json())  # Isso vai te ajudar a verificar a resposta da API no terminal

    return response.json().get('results', [])

def test_home(request):
    places = []  
    form = AddressForm()

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            street = form.cleaned_data['stree']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postal_code = form.cleaned_data['postal_code']
            country = form.cleaned_data['contry']

            address = f"{street}, {city}, {state}, {postal_code}, {country}"
            coordinates = get_coordinates(address)

            if coordinates:
                places = get_nearby_places(coordinates['lat'], coordinates['lng'])
            else:
                form.add_error(None, "Não foi possível encontrar as coordenadas para o endereço fornecido.")

    return render(request, 'home.html', {'form': form, 'places': places})
