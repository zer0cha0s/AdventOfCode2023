# read input file
file = open('./Day_2/input.txt').read()

# Set vars
red_count = 12
blue_count = 14
green_count = 13
total = 0

for game in file.split('\n'):
    if game:
        game_check = "pass"
        game_info = game.split(': ')[1].split('; ')
        for info in game_info:
            counts = info.split(', ')
            total_red = 0
            total_green = 0
            total_blue = 0
            for count in counts:
                num, colour = count.split()
                if colour == 'red':
                    total_red += int(num)
                elif colour == 'green':
                    total_green += int(num)
                elif colour == 'blue':
                    total_blue += int(num)
            if total_red > red_count or total_green > green_count or total_blue > blue_count:
                game_check = "fail"
                break  # Break loop as game is impossible
        if game_check == "pass":
            result = game.split(':')[0]
            total += int(result.split()[1])
            #print(f"Conditions met: {game.split(':')[0]}")

print('Part 1:', total)

# Reset variables
total = 0

for game in file.split('\n'):
    red_values = []
    green_values = []
    blue_values = []

    game_info = game.split(': ')[1].split('; ')
    for info in game_info:
        counts = info.split(', ')
        for count in counts:
            num, color = count.split()
            if color == 'red':
                red_values.append(int(num))
            elif color == 'green':
                green_values.append(int(num))
            elif color == 'blue':
                blue_values.append(int(num))

    game_power = max(red_values) * max(green_values) * max(blue_values)
    total += game_power

print('Part 2:', total)