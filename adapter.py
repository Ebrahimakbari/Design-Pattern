"""
Adapter Design Pattern:
    The Adapter pattern is a structural design pattern 
    that allows objects with incompatible interfaces to collaborate. 
    It acts as a bridge between two incompatible interfaces
    by wrapping an existing class with a new interface.
"""


class Mp4PService:
    def send_mp4(self, filename: str):
        print(f'sending mp4 file : {filename}')
        return filename


class MediaAdapter:
    def convert_to_mp3(self, filename: str):
        print(f'converting mp4 file to mp3 file : {filename}')
        # convert mp4 to mp3
        return filename


class MediaPlayer:
    def play_mp3(self, filename: str):
        print(f'playing mp3 file : {filename}')


def client():
    mp4service = Mp4PService()
    media_adaptor = MediaAdapter()
    media_player = MediaPlayer()
    filename = mp4service.send_mp4('myfile')
    converted = media_adaptor.convert_to_mp3(filename)
    media_player.play_mp3(converted)


client()


