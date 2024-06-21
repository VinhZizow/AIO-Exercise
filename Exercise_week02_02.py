# CHARACTER COUNTING

# Chuỗi cho trước
word = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac tristique augue, eget facilisis risus. Sed scelerisque volutpat est, non varius nulla eleifend pulvinar. Curabitur mauris magna, egestas sed dui a, cursus sollicitudin leo. Phasellus lacinia ullamcorper nibh nec facilisis. Donec sed sem vitae lacus blandit tincidunt sed et massa. Sed ut efficitur metus. Morbi id luctus quam."

# Hàm character counting
char_dict = {}

for char in word:
    if char in char_dict:
        char_dict[char] += 1
    if char not in char_dict:
        char_dict[char] = 1

print(char_dict)

