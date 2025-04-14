import time
import datetime
import threading
import pyttsx3
import requests
from pygame import mixer

engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def play_alarm():
    mixer.init()
    mixer.music.load("earrape_alarm.mp3")
    mixer.music.set_volume(1.0)
    mixer.music.play()


fixed_reminders = {
    "04:30": {"label": "Bangun dan Sholat Subuh", "type": "alarm"},
    "05:00": {"label": "Baca Al Quran dan artinya", "type": "tts"},
    "05:30": {"label": "Baca buku bisnis, disiplin atau pengembangan diri", "type": "tts"},
    "07:30": {"label": "Mulai kerja coding web developer", "type": "tts"},
    "13:00": {"label": "Lanjutan kerja coding project", "type": "tts"},
    "16:00": {"label": "Cek analisa market forex dan entry scalping", "type": "tts"},
    "17:00": {"label": "Waktunya healing sore atau jalan motoran", "type": "tts"},
    "20:30": {"label": "Trading session overlap London dan New York", "type": "tts"},
    "21:30": {"label": "Waktu santai, main game atau nonton", "type": "tts"},
    "22:00": {"label": "Dzikir malam atau baca Quran pendek", "type": "tts"},
}


def get_prayer_times():
    try:
        response = requests.get(
            "https://waktu-sholat.vercel.app/prayer?latitude=-6.595038&longitude=106.816635")
        if response.status_code == 200:
            all_data = response.json()
            now = datetime.datetime.now()
            today_str = f"{now.year}-{now.month}-{now.day}"
            for prayer_day in all_data['prayers']:
                if prayer_day['date'] == today_str:
                    t = prayer_day['time']
                    return {
                        t['dzuhur']: {"label": "Waktu Sholat Dzuhur", "type": "tts"},
                        t['ashar']: {"label": "Waktu Sholat Ashar", "type": "tts"},
                        t['maghrib']: {"label": "Waktu Sholat Maghrib", "type": "tts"},
                        t['isya']: {"label": "Waktu Sholat Isya", "type": "tts"},
                    }
        print("❌ Gagal ambil data waktu sholat.")
        return {}
    except Exception as e:
        print(f"⚠️ Error ambil jadwal sholat: {e}")
        return {}


triggered_today = set()


def reminder_loop():
    print("🔔 Reminder dimulai... jangan ditutup terminal ini.\n")

    sholat_reminders = get_prayer_times()
    reminders = {**fixed_reminders, **sholat_reminders}

    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time in reminders and current_time not in triggered_today:
            reminder = reminders[current_time]
            label = reminder["label"]
            tipe = reminder["type"]

            print(f"[{current_time}] 🔔 {label}")

            if tipe == "alarm":
                threading.Thread(target=play_alarm, daemon=True).start()
            elif tipe == "tts":
                threading.Thread(target=speak, args=(
                    label,), daemon=True).start()

            triggered_today.add(current_time)

        if current_time == "00:00":
            triggered_today.clear()

        time.sleep(10)


if __name__ == "__main__":
    reminder_loop()
