```
# 🧹 autoclean-bash

**autoclean-bash** is a DevOps automation script written in Bash. It safely handles routine system maintenance tasks like backing up logs, archiving temporary files, and moving trash files — all with safety checks and timestamped logging. Designed to simulate real-world DevOps cleanup jobs.

---

## 📂 Project Structure

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

## ✅ Sample Script Output

### ✔️ Successful Run

```
RDCT 📍 Running DevOps Cleanup Task
✅ logfile.txt backed up.
📦 tempfile.txt archived.
🗑️  trashfile.txt moved to trash.
```

### ⚠️ Partial Run (Missing Files)

```
RDCT 📍 Running DevOps Cleanup Task
✅ logfile.txt backed up.
⚠️  tempfile.txt not found!
⚠️  trashfile.txt not found!
```

---

## 📌 Task Summary

| Step | Task                     | Outcome                    |
| ---- | ------------------------ | -------------------------- |
| 1    | Backup `logfile.txt`     | ✅ Backed up with timestamp |
| 2    | Archive `tempfile.txt`   | ✅ or ⚠️ if missing         |
| 3    | Move `trashfile.txt`     | ✅ or ⚠️ if missing         |
| 4    | Log to `maintenance.log` | ✅ Always appended          |

---

## 📚 Learning Outcomes

By building this script, I practiced and learned:

* ✅ Bash scripting fundamentals (`#!/bin/bash`, `echo`, comments)
* ✅ File existence checks using `if [ -f ... ]`
* ✅ File operations: `mv`, `cp`, `>>` for logs
* ✅ Date and timestamp handling in filenames
* ✅ Directory structure for logs, archive, trash
* ✅ Appending and maintaining logs for auditing
* ✅ Building repeatable, idempotent automation tasks
* ✅ Debugging and verifying automation results

---

## 🧠 About the Project (Theory)

This project simulates a typical DevOps or SRE maintenance routine:

* 🔁 **Log Rotation**: Backing up active logs before overwrite
* 🧹 **Temporary File Cleanup**: Archiving throwaway session data
* 🗑️ **Trash Handling**: Separating garbage files from active space
* 📜 **Audit Trail Logging**: Keeping a log of when cleanup occurred

It reflects tasks that system administrators automate with cron jobs or integrate into CI/CD pipelines to reduce manual intervention.

---

## 🚀 Possible Enhancements

* 🖍️ Add color-coded terminal output (green for success, red for warning)
* ⏱️ Add a cron job to automate daily/weekly execution
* 🧪 Add `--dry-run` mode to preview actions without modifying files
* 🔄 Delete old backups (e.g., older than 7 days)
* 📬 Send alert (email or webhook) on script failure
* 🧩 Turn into a modular Bash utility with flags (`--backup-only`, etc.)

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it for personal or professional purposes.

---

## 👨‍💻 Author

**Ritik Barnwal**
[GitHub](https://github.com/theritikbarnwal) • [LinkedIn](https://linkedin.com/in/ritikbarnwal)
```

### Notes
- The file above is a complete `README.md` that includes the description and project structure from the image, merged with the detailed content you provided earlier.
- If the issue is with viewing it properly (e.g., truncation in your editor or platform), try copying this text into a new file named `README.md` and opening it in a Markdown viewer (e.g., VS Code, GitHub, or a text editor with Markdown support).
- If you meant something different by "get me in one file this is not coming properly" (e.g., combining the project files into a single script or zip), please clarify, and I’ll adjust accordingly!

Let me know if you need further assistance!