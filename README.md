
# Audio Enhancement using DeepFilterNet3

[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-blue)](https://jupyter.org/)
[![Built with DeepFilterNet3](https://img.shields.io/badge/Built%20with-DeepFilterNet3-lightgrey)](https://github.com/Rikorose/DeepFilterNet)
[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![Real-Time Capable](https://img.shields.io/badge/Feature-Real--Time--Processing-orange)]()

---

## 📖 Overview
This project demonstrates **speech enhancement** using **DeepFilterNet3**, a state-of-the-art real-time model for **noise suppression** and **voice clarity improvement**.  
It processes audio files to suppress background noise while preserving voice quality — ideal for online meetings, podcast production, voiceovers, and more.

DeepFilterNet3 is lightweight enough to run efficiently on **CPUs** and is compatible with **real-time applications**.

---

## 📂 Project Structure
- `audio_enhancement_deepfilternet3.ipynb`:  
  Jupyter Notebook with:
  - Model setup and initialization
  - Audio file loading
  - DeepFilterNet3 enhancement processing
  - Saving and comparing outputs

---

## 🚀 Features
- Batch processing of multiple `.wav` files
- Real-time ready (low latency)
- Lightweight — runs efficiently on CPU
- Automatic resampling to 16 kHz
- Saves enhanced audio for easy comparison
- Clear and modular notebook structure

---

## 🛠️ Installation
Install the required dependencies:

```bash
pip install deepfilternet librosa soundfile numpy
```
*(The notebook will automatically download DeepFilterNet3 model weights if not already cached.)*

---

## 📋 Usage

1. **Clone the Repository:**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Launch Jupyter Notebook:**
```bash
jupyter notebook
```

3. **Run the Notebook:**
- Open `audio_enhancement_deepfilternet3.ipynb`
- Upload your noisy audio files
- Run each cell sequentially
- Enhanced audio will be saved automatically

---

## 🎧 Example Workflow
| Step | Input | Output |
|:---|:---|:---|
| 1 | `noisy_audio.wav` | Processed `enhanced_audio.wav` |
| 2 | Batch multiple files | Processed outputs for each file |

**Before/After Comparison**: Noticeable reduction in noise with preserved voice quality!

---

## 🎯 Why DeepFilterNet3?
| Aspect | Benefit |
|:--|:--|
| Open Source | Easy to integrate and customize |
| Lightweight | Runs smoothly on standard CPUs |
| Real-time Performance | Suitable for live applications |
| High-Quality Output | Strong noise suppression without voice distortion |

DeepFilterNet3 achieves an excellent balance between **performance**, **quality**, and **efficiency**.

---

## 🛠️ Future Enhancements
- Build a simple GUI (Streamlit or Gradio) for drag-and-drop audio enhancement
- Extend support for stereo and multi-channel audio
- Add microphone live noise suppression
- Add visualization of noise reduction using spectrograms

---

## 📚 References
- [DeepFilterNet GitHub Repository](https://github.com/Rikorose/DeepFilterNet)
- [DeepFilterNet3: Real-Time Single-Channel Speech Enhancement for Online Conferencing](https://arxiv.org/abs/2310.01875)

---

## ⚡ License
This project is intended for educational and demonstration purposes.  
Please refer to the original DeepFilterNet3 [license](https://github.com/Rikorose/DeepFilterNet/blob/main/LICENSE) for detailed usage rights.

---

## ✨ Acknowledgment
Thanks to the developers of DeepFilterNet for making advanced speech enhancement techniques openly accessible to the community.
