# 📚 AI Book Recommendation System

This project is an AI-powered system that recommends which book you should read next, based on the power of large language models.

## 🚀 Features

- Utilizes LLaMA 3.2 model from [Ollama](https://ollama.com/)
- Custom model built with `createModel.py`
- Interactive recommendation with `useModel.py`

---

## 🧠 Prerequisites

Before getting started, make sure you have the following installed:

### ✅ 1. Install [Ollama](https://ollama.com/)
Ollama lets you run LLMs locally on your machine.

- **macOS:**  
  ```bash
  brew install ollama
  ```

- **Windows:**  
  Download and install from the [official website](https://ollama.com/).

- **Linux (Debian-based):**  
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

> After installing, make sure `ollama` is available in your terminal.

---

### ✅ 2. Pull the LLaMA 3.2 model

```bash
ollama pull llama3.2
```

> This will download and prepare the LLaMA 3.2 model.

---

### ✅ 3. Clone This Repository

```bash
git clone https://github.com/Robben1972/BookRecommender.git
cd BookRecommender
```

---

### ✅ 4. Install Python Requirements

Make sure you have Python 3.8+ and `pip` installed.

```bash
pip install -r requirements.txt
```

---

## 🏗️ Build the Model

Run the following script to prepare your model:

```bash
python createModel.py
```

---

## 📕 Get Your Book Recommendation

After building the model, you can run the recommendation system:

```bash
python useModel.py
```

---

## 📝 License

This project is licensed under the MIT License.

---

## 💡 Feedback & Contributions

Feel free to open issues or pull requests to contribute and improve this project!
