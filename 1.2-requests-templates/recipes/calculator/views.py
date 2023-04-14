from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def calculate_recipe_view(request, recipe_name):

    data = DATA[recipe_name]
    servings = request.GET.get('servings', 1)

    if servings:
        result = dict()
        for item, value in data.items():
            new_value = value * int(servings)
            result[item] = round(new_value, 2)
        context = {
            'recipe_name': recipe_name,
            'recipe': result
        }
    else:
        context = {
            'recipe_name': recipe_name,
            'recipe': data
        }

    return render(request, 'calculator/recipe-page.html', context)


def home_view(request):
    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}

    return render(request, 'calculator/home.html', context)