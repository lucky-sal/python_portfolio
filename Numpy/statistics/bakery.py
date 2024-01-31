import numpy as np

cupcakes = np.array([2, .75, 2, 1, 0.5])
# recipes = np.genfromtxt('recipes.csv', delimiter=',')
recipes = np.array([[2., 0.75, 2., 1., 0.5],
                    [1., 0.125, 1., 1., 0.125],
                    [2.75, 1.5, 1., 0., 1.],
                    [4., 0.5, 2., 2., 0.5]])

print(recipes)

eggs = recipes[:, 2]
print(eggs == 1)

cookies = recipes[2, :]

double_batch = cupcakes * 2

grocery_list = double_batch + cookies
print(f'grocery_list = {grocery_list}')
