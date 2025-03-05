import torch
import librosa
import numpy as np
import soundfile as sf
import os
from nemo.collections.tts.models import HifiGanModel

# Load HiFi-GAN model
print("🔄 Loading HiFi-GAN model...")
model = HifiGanModel.from_pretrained(model_name="tts_en_lj_hifigan_ft_mixerttsx")
print("✅ HiFi-GAN model loaded successfully!")

# Define file paths
input_audio_path = "ljspeech_sample.wav"  # Make sure this file exists in your directory
output_audio_path = "enhanced_ljspeech.wav"

# Check if input file exists
if not os.path.exists(input_audio_path):
    print(f"❌ ERROR: Input file '{input_audio_path}' not found!")
    exit()

# Load the input audio
print("🎵 Loading input audio...")
wav, sr = librosa.load(input_audio_path, sr=22050)
print(f"✅ Loaded: {input_audio_path} | Sample Rate: {sr} | Length: {len(wav)} samples")

# Convert to Mel spectrogram
print("🎛 Generating Mel spectrogram...")
mel_spectrogram = librosa.feature.melspectrogram(
    y=wav, sr=sr, n_fft=1024, hop_length=256, n_mels=80, fmin=50, fmax=8000, power=2.0
)
mel_spectrogram = np.log1p(mel_spectrogram)  # Log scaling

# Convert to tensor
mel_spectrogram = torch.tensor(mel_spectrogram).unsqueeze(0)

# Run HiFi-GAN for enhancement
print("🚀 Running HiFi-GAN enhancement...")
try:
    enhanced_audio = model.convert_spectrogram_to_audio(spec=mel_spectrogram)
    print(f"✅ Enhanced audio generated! Shape: {enhanced_audio.shape}")
except Exception as e:
    print(f"❌ ERROR during enhancement: {e}")
  

