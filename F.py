from collections import Counter


def get_pair(s):
    a, b = s.split()
    return (a, int(b))


def multiply_dict(d, n):
    return {k: v * n for k, v in d.items()}


def sum_dicts(d1, d2):
    return Counter(d1) + Counter(d2)


def solveF(recipies, requested, in_fridge):
    to_visit = [name for name,_ in requested]
    optimised_recipies = {}
    
    while to_visit:
        skip = False
        current = to_visit[-1]
        products = recipies[current]
        for product in products:
            if product in recipies and product not in optimised_recipies:
                to_visit.append(product)
                skip = True
        if skip:
            continue
        
        optimised_recipe = {}
        for product, amount in products.items():
            if product not in optimised_recipies:
                optimised_recipe = sum_dicts(optimised_recipe, {product: amount})
            else:
                optimised_recipe = sum_dicts(optimised_recipe, multiply_dict(optimised_recipies[product], amount))

        optimised_recipies[current] = optimised_recipe 
        to_visit.pop()
    
    to_buy = {}
    for food, amount in requested:
        to_buy = sum_dicts(to_buy, multiply_dict(optimised_recipies[food], amount))
    
    
    results = Counter(to_buy) - Counter(in_fridge)
    pairs = [(food, amount) for food, amount in results.items()]
    return [food + ' ' + str(amount) for food, amount in sorted(pairs)]


T = int(input().strip())
for _ in range(T):
    n, k, f = map(int, input().strip().split())
    requested = [get_pair(input().strip()) for _ in range(n)]
    recipies = {}
    for _ in range(k):
        recipe_name, recipe_length = get_pair(input().strip())
        recipe_contents = {}
        for _ in range(recipe_length):
            product_name, product_amount = get_pair(input().strip())
            recipe_contents[product_name] = product_amount
        recipies[recipe_name] = recipe_contents
    in_fridge = dict(get_pair(input().strip()) for _ in range(f))
    
    print(*solveF(recipies, requested, in_fridge), sep='\n')
