from sonybraviaremote import TV, TVConfig

def on_auth():
    return input('1305')

config = TVConfig('192.168.1.86', 'gab Sony')
tv = TV.connect(config, on_auth)

tv.is_on()  # true/false
tv.wake_up()
tv.power_off()
tv.netflix()
tv.home()
tv.enter()
tv.confirm()
tv.pause()
tv.play()
tv.confirm()
tv.mute()
tv.volume_up()
tv.volume_down()
