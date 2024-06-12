def cake(available, recipe):
    portions = []
    for ingredient_name, ingredient_value in recipe.items():
        available_value = available[ingredient_name]
        portion_value = available_value // ingredient_value
        portions.append(portion_value)
    return min(portions)