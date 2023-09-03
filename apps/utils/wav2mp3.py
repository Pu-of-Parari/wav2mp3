from pydub import AudioSegment
import io


def wav2mp3(wav_data: bytes, bitrate: str):
    audio = AudioSegment.from_file(io.BytesIO(wav_data), format="wav")
    return audio.export(format="mp3", bitrate=bitrate).read()
