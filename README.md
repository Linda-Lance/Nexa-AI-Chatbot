# 🤖 Nexa – AI Text & Voice Assistant

Nexa is an **AI-powered chatbot** built with **Streamlit** and **Ollama**, designed to generate intelligent responses from large language models (LLMs).
It uses the **LLaMA 3.2** model to provide accurate and context-aware responses. Nexa also includes **voice output**, so you can read and *listen* to the responses in real-time.

---

## ✨ Features

* 📝 Generate responses using **LLaMA 3.2** via Ollama.
* 🎙️ Text-to-Speech (TTS) – listen to responses directly in the app.
* ⚡ Clean & interactive **Streamlit UI**.
* 🔄 Easy to extend with more models or custom features.
* 🗨️ Named **Nexa AI** – responds with a friendly introduction when asked.

---

## 🛠️ Tech Stack

* [Python 3.10.11](https://www.python.org/)
* [Streamlit](https://streamlit.io/) – for the UI
* [Ollama](https://ollama.ai/) – for LLM integration
* [gTTS](https://pypi.org/project/gTTS/) – for voice output

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/nexa-chatbot.git
cd nexa-chatbot
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit App

```bash
streamlit run app.py
```

---

## 🎯 Output

The output generated using streamlit.

Text:

<img width="794" height="493" alt="Nexa_AI_Text" src="https://github.com/user-attachments/assets/f4e98dc5-c2fd-4168-8eb3-bf6ae023fe29" />

Voice:

<img width="799" height="401" alt="Nexa_AI_Voice" src="https://github.com/user-attachments/assets/7baf7a1d-0183-4907-94d2-a4454d666abb" />


## 📂 Project Structure

```
nexa-chatbot/
│── chat.py               # Main Streamlit application
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
│── response.mp3         # Auto-generated audio file (when TTS is used)
```

---

## ⚡ Usage

1. Enter your **prompt** in the text box.
2. Click **Generate Response**.
3. Read and listen to Nexa’s answer.
4. Ask Nexa its name and it will introduce itself with a friendly greeting.

---

## 🔮 Future Improvements

* 🔊 Real-time **streaming voice output**
* 🎤 Add **speech-to-text** input (voice prompts)
* 🌐 Deploy Nexa online for public use

---

## 👩‍💻 Author

[LinkedIn](https://www.linkedin.com/in/linda--lance/)

[Github](https://github.com/Linda-Lance)

lindalance2210@gmail.com
