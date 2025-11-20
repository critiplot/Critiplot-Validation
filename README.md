
# Critiplot Validation Instructions

This guide shows how to validate **Critiplot** in Python versions **3.11, 3.12, and 3.13**. 
_(Recommended: Use Python 3.13 Version)_

---

## 1. Navigate to the project folder

```bash
cd validation
```

---

## 2. Install the desired Python versions (macOS / Homebrew)

```bash
brew install python@3.11
brew install python@3.12
brew install python@3.13
```

> **Note:** You only need to install the versions you plan to test.

---

## 3. Link the Python version you want to use

```bash
brew link python@3.11 --force
brew link python@3.12 --force
# Optional: brew link python@3.13 --force
```

---

## 4. Check the Python version

```bash
python3.11 --version
python3.12 --version
python3.13 --version
```

---

## 5. Create a virtual environment using the desired Python version

```bash
python3.11 -m venv validation
python3.12 -m venv validation
python3.13 -m venv validation
```

---

## 6. Activate the virtual environment

```bash
source validation/bin/activate
```

---

## 7. Install Critiplot

```bash
pip install critiplot
```

---

## 8. Run the application

```bash
python app.py
```

---


Please visit to get more Info & see Repo: https://github.com/aurumz-rgb/Critiplot-main


![Preview](assets/preview1.png)

