import librosa
import matplotlib.pyplot as plt
from PIL import Image

class ISTm:
    def __init__(self, file):
        self.file = file


    # midi to png
    def Mid_To_Image(self, file):
        Convex = lambda filex: list(i.note for i in __import__('mido').MidiFile(filex) if i.type == 'note_on')
        midio_int_list = Convex(file)
        width = 8
        height = len(midio_int_list) // width
        Img = Image.new('RGB', (width*2, height))
        for i in midio_int_list:
            x = i // width
            y = i % width
            Img.putpixel((x,y), (__import__('random').randint(50,255),__import__('random').randint(50,255),__import__('random').randint(50,255)))
        return Img.save(f"{file}.png")
    # Mid_To_Image("Pac_Man.mid")


    # mp3 to png
    def MP3_To_Image(self, file):
        audio = f"{file}"
        audiox, sr = librosa.load(audio)
        times = librosa.times_like(audiox, sr=sr)
        plt.figure(figsize=(10,4))
        plt.plot(times,audiox)
        plt.xlabel('Time (ms)')
        plt.ylabel('Amplitude')
        plt.title(f"{file}")
        plt.tight_layout()
        plt.savefig(f'{file}.png')
        plt.close()
    # MP3_To_Image('pac-man.mp3')
ISTM = ISTm('self')



# Here Is Call this funcs
ISTM.Mid_To_Image("Pac_Man.mid")

ISTM.MP3_To_Image('pac-man.mp3')