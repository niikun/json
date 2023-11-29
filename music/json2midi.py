import json, mido

def main():
    with open("kaeru-uta.json",encoding="utf-8") as f:
        data = json.load(f)
    save_to_midi(data,"kaeru-uta.mid")

def save_to_midi(data, midifile):
    midi = mido.MidiFile()
    track = mido.MidiTrack()
    tm=0
    for v in data:
        note = v["note"]
        length = v["length"]

        if note>=0:
            track.append(mido.Message("note_on", note=note, time=tm))
            track.append(mido.Message("note_off", note=note, time=length))
            tm=0
        else:
            tm += length
            continue

    midi.tracks.append(track)
    midi.save(midifile)

if __name__ == "__main__": main()