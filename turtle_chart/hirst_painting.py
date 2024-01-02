

import colorgram

colors_extract = colorgram.extract('image.jpg', 10)
colors = []
print(colors_extract)

for color in range(len(colors_extract)):
    r = colors_extract[color].rgb.r
    g = colors_extract[color].rgb.g
    b = colors_extract[color].rgb.b
    rgb = (r, g, b)
    colors.append(rgb)
print(colors)

# color_list = [(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 186, 214), (208, 225, 208),
#               (211, 209, 210), (64, 43, 43), (171, 183, 170)]
