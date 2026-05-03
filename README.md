# 🚀 AI Project Builder

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

> 🔥 Automates end-to-end application development using a **multi-agent AI system**

---

## 📌 Overview

**AI Project Builder** is an intelligent system that takes a simple app idea and automatically:

- 🧠 Plans the architecture  
- 💻 Generates full-stack code  
- 📂 Creates project files  
- 🧪 Tests and reviews code  
- 🛠️ Debugs errors automatically  

👉 It simulates a **real software development team using AI agents**

---

## 🎥 Demo

### 🖥️ UI Preview

![UI](assets/ui.png)

### ⚙️ Pipeline Flow
## Idea → Planner → Developer → Tester → Reviewer → Debugger → Final App

---

## 🧠 Architecture

### Multi-Agent System

| Agent        | Role |
|-------------|------|
| Planner      | Breaks idea into steps |
| Developer    | Generates code |
| Tester       | Finds bugs |
| Reviewer     | Improves code |
| Debugger     | Fixes runtime errors |

---

## ⚙️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Framework:** LangChain  
- **LLM:** Ollama (Local Models)  
- **Execution Engine:** Subprocess (Node/Python runner)

---

## 📁 Project Structure
AI-Project-Builder/
│
├── agents/ # AI agents (planner, developer, etc.)
├── core/ # LLM configuration
├── tools/ # File handling, execution
├── workflows/ # Pipeline logic
├── ui/ # Streamlit UI
├── main.py # Entry point
├── requirements.txt


---

## 🚀 How to Run Locally

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/AI-Project-Builder.git
cd AI-Project-Builder
```
### 2️⃣ Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Install & run Ollama
Pro Tip - Use small models for faster execution
Download: https://ollama.com
```bash
ollama pull llama3.2:1b
ollama serve
```
### 5️⃣ Run UI
```bash
streamlit run ui/app.py
```

### 🧪 Example Usage

## 🖥️ UI Preview
See assets folder in this repo!

Input: 
```bash
Build a todo app using FastAPI
```
Output:
- Generated backend code
- Folder structure
- Auto-debugged version
- Downloadable project
  
### ⚠️ Limitations
- Requires local Ollama setup
- Performance depends on system hardware TIP - use smaller models for less configuration systems
- Generated apps may need minor manual fixes


## 👩‍💻 Developer & Author
- Bhargavi Kanojia
- 🎓 AI & DS Undergrad'27

## 📬 Connect
LinkedIn : https://www.linkedin.com/in/bhargavi-kanojia-245986280/
GitHub: https://github.com/bhargavi1973


