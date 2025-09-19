# Pomodoro CLI Timer 🍭

A cute and effective command-line Pomodoro timer designed to help you stay focused and productive.

## ✨ Features
- ⏳ 25-minute Pomodoro work session
- ☕ 5-minute short breaks
- 🔔 Sound alarm when time’s up
- 🎨 Pastel-colored terminal output
- 🧠 Minimal distraction, keyboard-interrupt safe
- 📱 Works in most terminal environments (Windows, macOS, Linux)

## 🛠️ Requirements
Make sure you have **Python 3** installed.

This script also uses the following Python libraries:
- [`colorama`](https://pypi.org/project/colorama/) 
- [`plyer`](https://pypi.org/project/plyer/) 
- [`playsound`](https://pypi.org/project/playsound/) 

Install dependencies via pip:
`pip install colorama plyer playsound`

## 🚀 How to Run
Clone the repository:
```
git clone https://github.com/its-nixie/pomodoro-cli.git
cd pomodoro-cli
```
Run the script:
`python pomodoro.py`

Press `Ctrl + C` anytime to exit gracefully.

## ⏰ How It Works
- The script runs in a loop of 25-minute work sessions followed by 5-minute short breaks.
- The terminal automatically clears between cycles for a clean experience.
- An alarm sound will alert you when a session ends.

## 💡 Customization
You can change the session durations & the alarm sound by editing the values at the top of the `pomodoro.py` file:
```
WORK_MINUTES = 25
SHORT_BREAK = 5
ALARM_SOUND = "alarm.mp3"
```
