def load_recipe(filename: str):
    recipes=[]

    with open(filename) as file:
       
        block=file.read().split("\n\n")

        for group in block:
            parts=group.split("\n")
            # print(parts)
            # print(parts[1])
            name=parts[0].strip()
            time=int(parts[1].strip())
            ingredients=parts[2:]
            recipes.append((name,time,ingredients))

    
    return recipes


def search_by_name(filename:str,word:str):
    recipes=load_recipe(filename)
   
    return[recipe for recipe,_,_ in recipes if word in recipe.lower()]


def search_by_time(filename:str,prep_time:int):
    recipes=load_recipe(filename)
    
    return[f"{name}, preparation time {time} min" for name,time,_ in recipes if time<=prep_time]


def search_by_ingredient(filename:str,ingredient:str):
    recipes=load_recipe(filename)
    

    return [f'{name}, preparation time {time} min' for name,time,ing in recipes if ingredient in ing]


if __name__=="__main__":
    found_recipes=search_by_name('recipes1.txt','cake')
    found_recipes=search_by_time('recipes1.txt',20)
    found_recipes=search_by_ingredients('recipes1.txt','eggs')
    for recipe in found_recipes:
        print(recipe)
