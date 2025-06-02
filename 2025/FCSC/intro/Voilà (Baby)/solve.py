from mpd import MPDClient

# commands found in the doc: https://python-mpd2.readthedocs.io/en/latest/topics/commands.html

client = MPDClient()
client.connect("chall.fcsc.fr", 2052)

print(client.status())

print(client.mpd_version)
print(client.listallinfo())