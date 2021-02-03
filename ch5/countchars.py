message = 'April is the cruellest month, breeding Lilacs out of the ' \
          'dead land,exit mixing Memory and desire, stirring Dull roots ' \
          'with spring rain.'

count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)