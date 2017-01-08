## Room with bears!
screen bear_room:
    default room_zoom = 0.66
    ## For now, we use four images for day/night and normal/crazy
    ## Later on, we might have much more of them, so we'll have
    ## to make a more flexible system
    ## TODO: use custom displayable
    add 'room demo normal night':
        zoom room_zoom
    add 'room demo normal day':
        alpha stats.light
        zoom room_zoom
    ## NOTE: this is incorrect
    add 'room demo crazy night':
        alpha stats.crazy
        zoom room_zoom
    add 'room demo crazy day':
        alpha stats.crazy * stats.light
        zoom room_zoom
