alien_0 = {'color': 'green', 'points': '5'}

print(alien_0['color'])
print(alien_0['points'])

# assigning a variable the amount of points assigned when
# shooting down an alient
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# assigning empty alien dictionary key:values
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = '5'

print(alien_0)

# use empty dictionaries when storing user supplied data
# in a dictionary

# modifying values (ex. color)

alien_0 = {'color': 'green'}
print(f"The color of alien_0 is {alien_0['color']}")


alien_0['color'] = 'yellow'
print(f'The alien color is {alien_0['color']}')



alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'


# Move the alien to the right
# Determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
if alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # fast 
    x_increment = 3
    
# new position is old position plus the increment
# assigning new x position variable, add the current x position plus the 
# x increment specified in the if logic above
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'New position: {alien_0}')

## removing key value pairs

alien_0 = {'color': 'green', 'points': '5'}
del alien_0['points']
print(alien_0)

