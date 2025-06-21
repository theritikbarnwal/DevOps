
---

### 📄 `README.md` for `autoclean-bash`

# 🧹 autoclean-bash

**autoclean-bash** is a DevOps automation script written in Bash. It handles routine system maintenance tasks such as log file backups, temporary file archiving, and trash file cleanup. Designed to simulate real-world automation tasks using cron for scheduling.

---
## 📂 Project Structure (in VM or Ubuntu)

```
autoclean-bash/
├── maintain.sh
├── logs/
├── archive/
├── trash/
├── samplefile.txt
├── logfile.txt
├── tempfile.txt
├── trashfile.txt
```

---

## 🛠 Features

- ✅ Timestamped backup of `logfile.txt` to `logs/`
- 📦 Archive `tempfile.txt` with current date to `archive/`
- 🗑️ Move `trashfile.txt` to `trash/`
- 🧾 Append operation log to `logs/maintenance.log`
- ⏰ Optional automation via `cron` scheduler

---

## 📌 How the Script Works

When executed, the script:
1. Checks if `logfile.txt` exists and backs it up with a timestamp.
2. Archives `tempfile.txt` with a date-based filename.
3. Moves `trashfile.txt` to the trash directory.
4. Logs each run with a timestamp to `logs/maintenance.log`.

---

## 🔧 Manual Usage

Make the script executable:

bash
chmod +x maintain.sh

Run it:

bash
./maintain.sh


---

## 🖥 Sample Output

### ✅ All files found:

```
RDCT 📍 Running DevOps Cleanup Task
✅ logfile.txt backed up.
📦 tempfile.txt archived.
🗑️  trashfile.txt moved to trash.
```

### ⚠️ Missing files:

```
RDCT 📍 Running DevOps Cleanup Task
✅ logfile.txt backed up.
⚠️  tempfile.txt not found!
⚠️  trashfile.txt not found!
```

---

## ⏰ Automating with Cron

To run the script automatically every 2 minutes:

1. Edit the root crontab:

   bash
   crontab -e
   

2. Add the job:

   bash
   */2 * * * * /root/autoclean-bash/maintain.sh >> /root/autoclean-bash/logs/cron_cleanup.log 2>&1


This schedules the cleanup script every 2 minutes and logs output to `cron_cleanup.log`.

Check logs with:

bash
tail -f /root/autoclean-bash/logs/cron_cleanup.log


---

## 📚 Learning Outcomes

This project demonstrates:

* Bash scripting basics (`if`, `echo`, `mv`, `cp`, redirection)
* Timestamped backups
* File path handling with absolute references
* Cron job scheduling and logging
* Writing safe, idempotent system automation tasks

---

## 🚀 Future Enhancements

* 🔄 Log rotation: delete backups older than X days
* ✉️ Email/report on success or failure
* 🎨 Terminal color output
* 🧪 Dry-run support
* 🛠 Flags for custom execution modes (`--backup-only`, etc.)

---

## 👨‍💻 Author

**Ritik Barnwal**