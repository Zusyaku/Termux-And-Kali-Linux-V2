import pyaudio
import wave
import time
def sound_go():
    while True:
        chunk = 1024  
        sample_format = pyaudio.paInt16  
        channels = 2
        fs = 44100  
        seconds = 4
        filename = "output.wav"

        p = pyaudio.PyAudio()  

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  

        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()


        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        time.sleep(120)
