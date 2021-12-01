def value(colors):
    band_colors = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]

    return band_colors.index(colors[0]) * 10 + band_colors.index(colors[1])
