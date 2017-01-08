init python:
    TRACKS = {
        'bohlevtsian'   : 'main',
        'waltz-cymbals' : 'cymbals',
        'waltz-main'    : 'main',
        'waltz-bear'    : 'bear',
    }

## init sound channels
init python:
    for channel in TRACKS:
        renpy.music.register_channel(channel, mixer='music', loop=True, stop_on_mute=False, tight=True, file_prefix='music/', file_suffix='.ogg')

init python:
    def init_sounds():
        for track in TRACKS:
            renpy.music.play(track, channel=track)
        update_sounds()

    def update_sounds():
        print('update')
        volume = {
            'cymbals':  stats.crazy,
            'bear':     stats.bear*2,
            'main':     1.0,
        }
        total_volume = 1.0+stats.bear*0.5+stats.crazy*0.5
        volume = normalize_volume(volume, total_volume * 0.5)
        for track, channel in TRACKS.items():
            renpy.music.set_volume(volume[channel], 0.0, channel=track)

    def normalize_volume(volume, total_volume):
        current_total = sum(volume.values())
        coeff = total_volume / current_total
        return { ch : vol*coeff for ch, vol in volume.items() }
