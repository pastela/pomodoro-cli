from colorama import init, Style
from plyer import notification  
import os
import shutil
import time

try:
    from playsound import playsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False

init(autoreset=True)

WORK_MINUTES = 25
SHORT_BREAK = 5
ALARM_SOUND = "alarm.mp3"

def center(text, width=None):
    if width is None:
        width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10,  
    )

def play_alarm():
    if SOUND_AVAILABLE and os.path.exists(ALARM_SOUND):
        try:
            playsound(ALARM_SOUND)
        except Exception as e:
            print(f"\n⚠️ Error playing alarm: {e}")
    else:
        print("\n🔔 Alarm sound not available or missing file.")

def countdown(minutes, label, emoji, color, notify=False):
    total_seconds = minutes * 60
    width = shutil.get_terminal_size((80, 20)).columns
    header = f"{emoji} {label} — {minutes} minutes"
    print(color + Style.BRIGHT + center(header, width))
    
    base_line = "⏳ Time left: "
    total_len = len(base_line) + 5  
    padding = (width - total_len) // 2
    
    PASTEL_BLUE = '\033[38;5;153m'

    try:
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            time_str = f"{mins:02}:{secs:02}"
            print("\r" + " " * padding + PASTEL_BLUE + Style.BRIGHT + base_line + time_str + Style.RESET_ALL, end="", flush=True)
            time.sleep(1)
        print("\r" + " " * padding + PASTEL_BLUE + Style.BRIGHT + base_line + "00:00" + Style.RESET_ALL)
        
        if notify:
            show_notification(f"{label} Ended", f"Time's up for {label.lower()}!")

        play_alarm()
    
    except KeyboardInterrupt:
        PASTEL_RED = '\033[38;5;210m'
        RESET = '\033[0m'
        print(PASTEL_RED + "\n⛔ Interrupted." + RESET)
        exit()

def pomodoro_loop():
    cycle = 1

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            PASTEL_PINK = '\033[95m'  
            RESET = '\033[0m'
            print(PASTEL_PINK + Style.BRIGHT + center(f"POMODORO TIMER — Cycle {cycle} 🍭\n") + RESET)
            
            PASTEL_PURPLE = '\033[38;5;225m'
            countdown(WORK_MINUTES, "Work Session", "☕", PASTEL_PURPLE, notify=True)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            PASTEL_YELLOW = '\033[38;5;229m'
            countdown(SHORT_BREAK, "Short Break", "🍃", PASTEL_YELLOW, notify=True)
            
            cycle += 1

    except KeyboardInterrupt:
        PASTEL_GREEN = '\033[38;5;120m'
        print(PASTEL_GREEN + Style.BRIGHT + "\n👋 Goodbye! Stay productive!" + Style.RESET_ALL)
        exit()
 
if __name__ == "__main__":
    pomodoro_loop()
