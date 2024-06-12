def cake(available, recipe):
    portions = []
    for ingredient_name, ingredient_value in recipe.items():
        available_value = available.get(ingredient_name, 0)
        portion_value = available_value // ingredient_value
        portions.append(portion_value)
        
    return min(portions)