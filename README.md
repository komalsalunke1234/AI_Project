# AI_Project

# AI Medical Chatbot 2.0 (Vision + Voice)

An end-to-end AI healthcare assistant capable of:
- Taking **voice input**
- Accepting **image uploads** (e.g., skin conditions)
- Understanding multimodal inputs via **Groq + Meta LLaMA Vision Models**
- Generating **natural language medical responses**
- Converting text responses back to **speech** with ElevenLabs
- Running through a **Gradio web interface**

---

## 📌 Technical Architecture

The system is divided into **4 phases**:

### **Phase 1: Vision + Language Model (LLM)**
- **Input:** Image and/or transcribed text
- Uses **Groq API** to connect to **Meta LLaMA Vision Model**
- Produces **LLM response** based on user query and image

### **Phase 2: Speech-to-Text (STT)**
- Records user voice input
- Converts voice to text using **STT AI model** (e.g., OpenAI Whisper or Groq STT)
- Passes text to Phase 1

### **Phase 3: Text-to-Speech (TTS)**
- Converts LLM text response into **spoken audio**
- Uses **ElevenLabs API** for natural voice output
- Produces an **audio file** for playback

### **Phase 4: User Interface**
- Built with **Gradio**
- Allows:
  - Voice input
  - Image upload
  - Text output display
  - Audio playback of LLM responses

---

## 🛠 Tech Stack

- **Groq API** — Fast inference for LLaMA vision + language models
- **Meta LLaMA Vision Models** — Multimodal understanding
- **OpenAI / Whisper** — Speech-to-text transcription
- **ElevenLabs** — Text-to-speech voice synthesis
- **Gradio** — Web-based UI for interaction
- **Python** — Core language
- **dotenv** — Environment variable management

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-medical-chatbot-2.0.git
cd ai-medical-chatbot-2.0
