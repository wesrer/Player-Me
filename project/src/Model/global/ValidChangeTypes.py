# --------------------------------------------------------------
#                          CHANGETYPES
# --------------------------------------------------------------

# add -> add a new mission
# modify -> modify existing mission properties
# delete -> delete existing mission or reward
# view -> view certain properties of current game state
# completed -> view completed missions of subcategories
# done -> mission completed
# start -> start working on a mission
# stop -> stop working on a mission
# details -> view detailed information about a certain aspect of the game state
# drop -> drop an item or pet from inventory or stable
# replace -> replace an equipped item or pet with another one. Returns the object
#            to the inventory

everyMissionChangeType = ['add', 'modify',
                          'delete', 'completed', 'done', 'start', 'stop']

validChangeTypes = {
    't': everyMissionChangeType,
    'task': everyMissionChangeType,
    'q': everyMissionChangeType,
    'quest': everyMissionChangeType,
    'h': everyMissionChangeType,
    'habit': everyMissionChangeType,
    'r': ['add', 'delete', 'modify'],
    'reward': ['add', 'delete', 'modify'],
    'rewards':  ['add', 'delete', 'modify'],
    'completed': ['view', 'clear', 'delete'],
    'profile': ['view', 'details', ],
    'stable': ['view', 'details'],  # inventory for pets
    'lives': ['view'],  # HP
    'hp': ['view'],
    'experience': ['view'],
    'level': ['view'],
    'iventory': ['view', 'details'],
    'item': ['use', 'drop'],
    'pet': ['use', 'drop', 'replace']
}
