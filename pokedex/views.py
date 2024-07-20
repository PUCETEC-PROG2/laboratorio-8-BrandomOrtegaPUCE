from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

def index(request):
    pokemons = ['charmander', 'pikachu', 'squirtle']
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon):
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        else: 
            form = PokemonForm()
            
        return render(request, 'add_pokemon.html', {'form' : form})