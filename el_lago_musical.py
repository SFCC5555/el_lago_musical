# --El lago musical--

animal_sounds = {
    "frog": {"brr", "birip", "brrah", "croac"},
    "dragon_fly": {"fiu", "plop", "pep"},
    "cricket": {"cric-cric", "trri-trri", "bri-bri"},
}

songs = [
    ["brr", "fiu", "cric-cric", "brrah"],
    ["pep", "birip", "trri-trri", "croac"],
    ["bri-bri", "plop", "cric-cric", "brrah"],
]


def start_song(sound):
    all_sounds = set.union(*animal_sounds.values())

    sound = sound.lower()

    if sound in all_sounds:

        try:
            song = next(filter(lambda song: sound in song, songs))
            sound_position = song.index(sound)
            song_complement = ", ".join(song[sound_position + 1 :])
            return song_complement

        except StopIteration:

            return "There is no song with that sound."

    return "The sound doesn't belong to any animal."


if __name__ == "__main__":
    song = start_song("brr")
    print(song)
