
# ⏰ Jadwal Reminder Harian Otomatis (Dengan TTS dan Alarm Subuh Keras)

Script Python ini membantu kamu tetap disiplin mengikuti jadwal harian — termasuk alarm untuk bangun pagi dan waktu sholat (real-time berdasarkan kota Bogor). Ideal untuk web developer, trader, atau siapa saja yang ingin hidup lebih teratur.

---

## 📦 Fitur

- 🔊 **Alarm Subuh Earrape** (volume keras, pakai `pygame`)
- 🗣️ **Text-to-Speech (TTS)** untuk semua reminder harian
- 🕌 **Waktu Sholat Otomatis Real-time** via API
- ♻️ Berjalan terus selama terminal aktif
- ✅ Ringan, offline-ready (kecuali data waktu sholat)

---

## 🚀 Cara Install

### 1. Pastikan Python 3.8+ sudah terpasang

Cek versi:
```bash
python --version
```

### 2. Install dependensi
Buka terminal/cmd/PowerShell di folder project, lalu jalankan:

```bash
pip install pyttsx3 pygame requests
```

---

## 📁 Struktur Folder

```
reminder-jadwal/
├── reminder.py              # Script utama
├── earrape_alarm.mp3        # Alarm keras untuk bangun
└── README.md                # Dokumentasi ini
```

> Pastikan file `earrape_alarm.mp3` berada di **folder yang sama** dengan `reminder.py`.

---

## ▶️ Cara Menjalankan

Buka terminal lalu:

```bash
python reminder.py
```

Biarkan terminal terbuka — script akan berjalan terus dan berbicara saat waktunya reminder.

---

## 🛠 Kustomisasi Jadwal

Kamu bisa edit bagian `fixed_reminders` di dalam `reminder.py` untuk menyesuaikan kegiatanmu. Contoh:

```python
"20:30": {"label": "Trading session overlap London dan New York", "type": "tts"},
```

---

## 🤝 Credits

- Waktu Sholat API: [waktu-sholat.vercel.app](https://waktu-sholat.vercel.app)
- Text-to-Speech: `pyttsx3`
- Sound Playback: `pygame`

---

Feel free to fork, improve, and personalize your reminder! 🔥
