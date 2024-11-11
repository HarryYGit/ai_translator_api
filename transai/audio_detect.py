from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import librosa

class AudioDetector:
    def __init__(self, model_name="facebook/wav2vec2-large-960h"):
        # Initialize the processor and model from Hugging Face
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)
    
    def load_audio(self, file_path):
        """
        Loads and resamples audio file to 16000 Hz using librosa.
        
        Args:
            file_path (str): Path to the audio file.
        
        Returns:
            waveform (numpy.ndarray): Audio waveform.
            sample_rate (int): Audio sample rate (16000 Hz).
        """
        # Load the audio using librosa (automatically resampling to 16000 Hz)
        waveform, sample_rate = librosa.load(file_path, sr=16000)  # Ensure 16kHz sample rate
        return waveform, sample_rate

    def transcribe_audio(self, file_path):
        """
        Converts audio file to text using Wav2Vec2 model.
        
        Args:
            file_path (str): Path to the audio file.
        
        Returns:
            str: Transcription of the audio.
        """
        # Load and preprocess audio
        waveform, sample_rate = self.load_audio(file_path)

        # Process the audio and transcribe
        inputs = self.processor(waveform, sampling_rate=16000, return_tensors="pt", padding=True)
        
        # Run the model to get logits
        with torch.no_grad():
            logits = self.model(**inputs).logits

        # Decode the predicted ids to text
        predicted_ids = logits.argmax(dim=-1)
        transcription = self.processor.decode(predicted_ids[0])

        return transcription

# Example of how to use the AudioDetector class
if __name__ == "__main__":
    audio_detector = AudioDetector()  # Create an instance of the class
    file_path = "/path/to/your/audio/file.mp3"  # Change this to your audio file path
    transcription = audio_detector.transcribe_audio(file_path)
    print("Transcription:", transcription)
