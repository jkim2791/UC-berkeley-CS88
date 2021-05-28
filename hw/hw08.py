## Review on Dictionary

def merge_dict(d1, d2):
    """Returns a dictionary with two dictionaries merged together. You can assume that the same keys appear in both dictionaries. 

    >>> data8 = {"midterms":1, "projects":3}
    >>> data100 = {"midterms":2, "projects":3}
    >>> combined = merge_dict(data8, data100)
    >>> combined
    {'midterms': 3, 'projects': 6}
    """
    z = {}
    for key_d1, value_d1 in d1.items():
        z.update({key_d1:value_d1})
        for key_d2, value_d2 in d2.items():
            if key_d1 == key_d2:
                val=value_d1+value_d2
                z.update({key_d1:val})
    return z

# Mutation

def merge_dict_mutate(d1, d2):
    """Write a function that merge the second dictionary into the first dictionary. You can assume 
    that the same keys appear in both dictionaries. 

    >>> bank = {"Annie":1000, "David":500}
    >>> new_deposits = {"Annie":700, "David":800}
    >>> merge_dict_mutate(bank, new_deposits)
    >>> bank
    {'Annie': 1700, 'David': 1300}
    """
    for x, y in d1.items():
        for a, b in d2.items():
            if x == a:
                d1.update({x:y+b})

    "SOLUTION HERE"

def list_combine(lst):
    """Write a function that combines all the items in the list into one item and put it as the only item in the list. 

    >>> pokemon = [4, 5, 3, 2, 1, 6]
    >>> list_combine(pokemon)
    >>> pokemon
    [21]
    >>> alphabet = ["a", "b", "c", "d", "e"]
    >>> list_combine(alphabet)
    >>> alphabet
    ['abcde']
    """
    x = False
    while len(lst) >0:
        if not x:
            if type(lst[0]) == int:
                total = 0
                x = True
            else:
                total = ''
                x = True
        else:
            total = total + lst.pop(0)
    lst.append(total)

    

def dict_cycle(dictionary):
    """Write a function that cycles each of the key-value pair such that the key becomes the last
        item in the value list, and the first item of the list becomes the new key. 

    >>> hamster = {"a":["b","c","d"], "w":["x","y","z"]}
    >>> dict_cycle(hamster)
    >>> hamster
    {'b': ['c', 'd', 'a'], 'x': ['y', 'z', 'w']}
    """
    newdict = {}
    for i in dictionary:
        lst = dictionary[i]
        lst += i 
        newdict[lst[0]] = lst[1:]
    dictionary.clear()
    for i in newdict:
        dictionary[i] = newdict[i]

    

def make_gym(a, b, c, d):
    """Returns a pokemon gym (represented by list) of the four pokemons a, b, c, d."""
    return [a, b, c, d]

def gym_size(gym):
    """Returns the size of the gym."""
    return len(gym)

def make_pokemon_set():
    """Returns a dictionary of pokemon methods.

    >>> my_pokemons = make_pokemon_set()
    >>> my_pokemons["add"]("pikachu", "raichu")
    >>> my_pokemons["evolve"]("charmander")
    'charizard'
    >>> my_pokemons["evolve"]("celebi")
    'celebi'
    >>> my_gym = make_gym("charmander", "celebi", "pikachu", "rattata")
    >>> my_pokemons["evolve_all"](my_gym)
    >>> my_gym
    ['charizard', 'celebi', 'raichu', 'raticate']

    """
    
    pokemons = {"charmander":"charmeleon",
            "charmeleon":"charizard",
            "squirtle":"wartortle",
            "wartortle":"blastoise",
            "rattata":"raticate",
            "sandshrew":"sandslash"}

    def add(pokemon, evolution):
        _add_pokemon(pokemons, pokemon, evolution)



        

    def evolve(pokemon):
        return _evolve(pokemons, pokemon)

    def evolve_all(gym):
        _evolve_all(pokemons,gym)
        

    return {"add":add, "evolve":evolve, "evolve_all":evolve_all}

def _add_pokemon(pokemon_set, pokemon, evolution):
    """Takes in a pokemon and the form it evolves to and adds it to the pokemon
    dictionary set. 
    """
    pokemon_set[pokemon] = evolution

    

def _evolve(pokemon_set, pokemon):
    """Takes in a pokemon and returns its final evolved form. Use the pokemon_set to check for 
    what the pokemon should evolve to. If the pokemon is not in the pokemon set, keeps its 
    status as is. 

    """
    """pokemons = {"charmander":"charmeleon",
            "charmeleon":"charizard",
            "squirtle":"wartortle",
            "wartortle":"blastoise",
            "rattata":"raticate",
            "sandshrew":"sandslash"}"""
    evolve = pokemon
    if evolve in pokemon_set:
        while evolve in pokemon_set:
            evolve = pokemon_set.get(evolve)
        return evolve
            
    else:
        return evolve
    
    

def _evolve_all(pokemon_set, gym):
    """Takes in a gym and evolve all the pokemons in the gym. You should be modifying the gym,
    not returning a new gym. Use the evolve function you've defined above!

    """
    i= 0
    while i < len(gym):
        evolving = gym[i]
        evolved = _evolve(pokemon_set,evolving)
        gym[i] = evolved
        i +=1

