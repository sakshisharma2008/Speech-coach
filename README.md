# 🎙️ Speech Coach

An AI-powered speech analysis and delivery feedback system that analyzes a speaker's **pitch, energy, speech rate, pitch variation, and pauses** to identify delivery issues and provide actionable feedback.

> **Hackathon Track:** Track C — Contrastive Speech Analytics & Temporal Flaw Grounding

---

## 📌 Overview

Speech Coach is designed to help speakers improve their public speaking by analyzing **how they deliver a speech**, rather than only analyzing what they say.

The system processes an uploaded speech recording, transcribes it, extracts acoustic features, identifies problematic regions, and provides simple feedback to improve speech delivery.

The long-term goal is to compare an **ideal speech baseline** with a participant's speech and identify exactly **where and why** the participant's delivery deviates from the baseline.

---

## 🎯 Problem Statement

Evaluating spoken performances such as:

* Interpretive Reading
* Declamation
* Extemporaneous Speaking
* Persuasive Oratory

is inherently subjective.

Judges need to evaluate several aspects of delivery, including:

* Speaking speed
* Pitch and intonation
* Vocal energy
* Pausing
* Emphasis
* Vocal clarity

Speech Coach aims to make this evaluation more **measurable, reproducible, and explainable** using audio signal processing and contrastive analysis.

---

## ✨ Current Features

The current prototype supports:

### 🎤 Speech Upload

Upload a speech recording for analysis.

### 📝 Automatic Transcription

The system uses **AssemblyAI** to convert the speech audio into text and obtain timestamps.

### 🎵 Pitch Analysis

The system extracts the speaker's fundamental frequency (F0) and analyzes relative pitch.

### 🔊 Energy Analysis

The system analyzes vocal energy to identify sections where the speaker may be too loud or too quiet.

### ⚡ Speech Rate Analysis

Speech rate is estimated in **words per second** using word timestamps.

### 🎚️ Pitch Variation

The system calculates pitch variation to identify potentially monotone delivery or excessive pitch variation.

### ⏱️ Temporal Flaw Detection

Problematic regions are detected with timestamps.

For example:

```text
12.4s – 15.8s
Issue: Speaking too fast
```

### 💡 Actionable Feedback

The system converts detected issues into simple feedback such as:

```text
Speak a little slower and take short pauses between words.
```

### 📊 Feature Timeline

The system generates a timeline showing speech features over time and highlights problematic regions.

---

## 🧠 How It Works

```text
                Speech Audio
                     │
                     ▼
             Audio Processing
                     │
                     ▼
          Automatic Transcription
               (AssemblyAI)
                     │
                     ▼
             Word/Sentence Timing
                     │
                     ▼
          ┌─────────────────────┐
          │  Feature Extraction │
          └─────────────────────┘
             │    │    │    │
             ▼    ▼    ▼    ▼
           Pitch Energy Rate Pitch
                         Variation
             │
             ▼
       Feature Timeline
             │
             ▼
       Problem Detection
             │
             ▼
      Temporal Flaw Regions
             │
             ▼
       Actionable Feedback
             │
             ▼
        Streamlit Dashboard
```

---

## 🔬 Features Extracted

| Feature             | Purpose                                           |
| ------------------- | ------------------------------------------------- |
| **Pitch / F0**      | Measures fundamental frequency and relative pitch |
| **Energy**          | Measures vocal intensity                          |
| **Speech Rate**     | Estimates words spoken per second                 |
| **Pitch Variation** | Measures variation in vocal pitch                 |
| **Pauses**          | Helps identify hesitation and pacing issues       |
| **Sentence Timing** | Maps speech content to audio time                 |
| **Word Timing**     | Supports temporal analysis                        |

---

## 🧪 Current Analysis Logic

The prototype currently uses predefined ideal ranges for speech characteristics.

Example:

```python
IDEAL = {
    "pitch": (-4, 4),
    "energy": (-6, 6),
    "pitch_var": (1.0, 6.0),
    "rate": (1.8, 3.3),
}
```

When a measured feature falls outside its expected range, the system flags it as a potential delivery issue.

For example:

```text
Speech Rate > Ideal Range
        ↓
Speaking Too Fast
        ↓
Identify Time Region
        ↓
Generate Feedback
```

---

## 🎯 Contrastive Analysis — Planned Core Feature

The final system will move from fixed ideal ranges toward **contrastive speech analysis**.

Instead of analyzing only one recording:

```text
Participant Speech
       ↓
   Analysis
       ↓
   Feedback
```

the system will compare:

```text
          Same Speech / Same Transcript
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Ideal Speech       Participant Speech
          │                   │
          ▼                   ▼
   Feature Extraction   Feature Extraction
          │                   │
          └─────────┬─────────┘
                    ▼
             Feature Comparison
                    │
                    ▼
             Deviation Detection
                    │
                    ▼
            Temporal Grounding
                    │
                    ▼
             Causal Explanation
```

Example:

```text
Time: 12.4s – 15.8s

Ideal speech rate:       3.2 words/sec
Participant speech rate: 5.1 words/sec

Deviation: +59%

Detected issue:
Excessive speaking rate

Feedback:
The speaker is delivering this section significantly
faster than the baseline, which may reduce clarity
and rhetorical emphasis.
```

---

## 📍 Temporal Flaw Grounding

A key objective of the project is to identify **exactly where a delivery flaw occurs**.

Instead of:

> "Your pacing is poor."

the system should provide:

> "A pacing deviation was detected from **12.4s to 15.8s**."

This allows the speaker to replay and improve the exact problematic section.

---

## 📊 Planned Scoring System

The final system will use a reproducible rubric.

| Category           |   Weight |
| ------------------ | -------: |
| Pacing & Rhythm    |      20% |
| Pitch & Intonation |      20% |
| Vocal Energy       |      15% |
| Pausing            |      15% |
| Vocal Clarity      |      15% |
| Emphasis           |      15% |
| **Total**          | **100%** |

The scoring system will compare measured speech features against the ideal baseline and generate explainable scores.

---

## 🗂️ Planned Contrastive Dataset

The project will use paired speech recordings containing the **same transcript but different delivery quality levels**.

Proposed levels:

```text
L0 → Ideal
L1 → Near Perfect
L2 → Moderate Flaw
L3 → Bad
L4 → Extreme Flaw
```

Example:

```text
speech_001/
│
├── transcript.txt
├── ideal.wav
├── near_perfect.wav
├── moderate.wav
├── bad.wav
├── extreme.wav
└── annotations.json
```

The dataset will contain controlled delivery flaws such as:

* Excessive speaking speed
* Very slow delivery
* Reduced pauses
* Excessive pauses
* Monotone pitch
* Excessive pitch variation
* Low vocal energy
* Excessive vocal energy
* Weak emphasis

The transcript remains unchanged so that the system can focus on **delivery differences**.

---

## 🏗️ Project Structure

Current project structure:

```text
speech-coach/
│
├── main/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   └── .gitignore
│
└── .env
```

The planned architecture will expand into:

```text
speech-coach/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── annotations/
│
├── src/
│   ├── preprocessing.py
│   ├── transcription.py
│   ├── alignment.py
│   ├── features.py
│   ├── pitch.py
│   ├── energy.py
│   ├── speech_rate.py
│   ├── pause_detection.py
│   ├── normalization.py
│   ├── comparison.py
│   ├── flaw_detection.py
│   ├── scoring.py
│   └── explanation.py
│
├── notebooks/
│
├── tests/
│
└── docs/
```

---

## 🛠️ Tech Stack

### Programming

* Python

### Audio Processing

* Librosa
* NumPy
* SciPy
* Pandas

### Speech Transcription

* AssemblyAI

### Visualization

* Matplotlib
* Plotly

### Dashboard

* Streamlit

### AI Explanation

* Google Gemini API

### Development

* Git
* GitHub
* VS Code

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/sakshisharma2008/Speech-coach.git
```

Move into the project directory:

```bash
cd Speech-coach/main
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file for API credentials.

Example:

```text
ASSEMBLYAI_API_KEY=your_api_key_here
GEMINI_API_KEY=your_api_key_here
```

**Never commit `.env` or API keys to GitHub.**

The `.gitignore` file should contain:

```text
.env
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
```

---

## ▶️ Running the Application

From the `main` directory:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

## 🔎 Example Feedback

The system can generate feedback such as:

```text
Your voice is too high (may sound tense/anxious).

Your voice is too quiet (may be difficult to hear).

Your voice sounds monotone; vary your pitch on important words.

You are speaking too fast.

Speak a little slower and take short pauses between words.
```

---

## 🎯 Hackathon Objectives

The project focuses on the following major objectives:

### 1. Custom Contrastive Dataset

Create paired ideal and flawed speech recordings using the same transcript.

### 2. Advanced Feature Extraction

Extract:

* FFT
* MFCC
* Pitch/F0
* Energy
* Speech Rate
* Pauses
* Vocal Clarity

### 3. Forced Alignment

Map transcript words and phrases to accurate audio timestamps.

### 4. Temporal Grounding

Identify exact time intervals where significant deviations occur.

### 5. Causal Flaw Explanation

Convert numerical feature deviations into understandable explanations.

### 6. Interactive Dashboard

Provide:

* Audio playback
* Transcript
* Feature graphs
* Flaw timestamps
* Scores
* Feedback

---

## 📈 Future Improvements

Planned improvements include:

* [ ] Ideal-vs-participant contrastive analysis
* [ ] Custom paired speech dataset
* [ ] Forced word-level alignment
* [ ] MFCC extraction
* [ ] FFT/spectral analysis
* [ ] Improved pause detection
* [ ] Speaker-agnostic normalization
* [ ] Temporal flaw severity scoring
* [ ] Automated rubric scoring
* [ ] Gemini-based causal explanations
* [ ] Interactive Plotly timeline
* [ ] Audio region replay
* [ ] Speech comparison dashboard
* [ ] Automated stress testing
* [ ] Unit tests
* [ ] Deployment

---

## 👥 Team Roles

The project can be divided into four major areas:

### Person 1 — Audio & Feature Extraction

Responsible for:

* Audio preprocessing
* Pitch/F0
* Energy
* MFCC
* FFT
* Speech rate
* Pause detection

### Person 2 — Transcription & Alignment

Responsible for:

* Speech transcription
* Word timestamps
* Sentence timestamps
* Forced alignment
* Transcript-audio mapping

### Person 3 — Contrastive Analysis

Responsible for:

* Ideal baseline
* Feature normalization
* Ideal vs participant comparison
* Deviation calculation
* Temporal flaw detection
* Severity scoring

### Person 4 — Dashboard & AI Explanation

Responsible for:

* Streamlit dashboard
* Visualization
* User interface
* Gemini integration
* Human-readable explanations
* Demo and presentation

---

## 🔬 Research Direction

The core research idea is to combine **audio signal processing with contrastive analysis**.

Instead of asking only:

> "Is this speech good or bad?"

Speech Coach aims to answer:

> **"Where does the participant's delivery deviate from the ideal, by how much, and what specific delivery behavior caused the deviation?"**

This makes the feedback more measurable and actionable.

---

## 📜 License

This project is currently developed as a hackathon/research prototype.

License information will be added as the project matures.

---

## 👩‍💻 Contributors

Developed as part of a multimodal AI hackathon project.

**Speech Coach Team**

---

⭐ If you find this project interesting, consider giving the repository a star!
cd C:\Users\rashi\Desktop\project