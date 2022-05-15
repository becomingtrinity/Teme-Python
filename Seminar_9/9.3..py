I = [2, 3, 1]
II = [1, 4, 5]
III = ['A', 'q', '#']

print(
    list(
        map(
            lambda a, b, c:(a + b) * c, I, II, III
        )
    )
)