# 📁 Linux Filesystem Toolkit - Phase 1 DevOps Project

Welcome to my Day 1 DevOps/Linux scripting project — **Linux Filesystem Toolkit**. This script helps manage basic file and folder operations in a terminal-based menu system.

---

## 🧠 Objective

To strengthen foundational Linux and Bash scripting skills as part of **Phase 1 of my DevOps journey**. This script was developed with a strong focus on practicing:

* File and folder manipulation
* Conditional logic and control structures
* Logging and automation basics

---

## 🛠️ How to Run

```bash
chmod +x linux_fs_toolkit.sh
./linux_fs_toolkit.sh
```

* 📦 **Logs** are stored in the `logs/` directory.
* 🕒 Format: `logs/action_YYYY-MM-DD_HH:MM:SS.log`

---

## 📋 Menu Options

```
1. Create Folder
2. Create File
3. List Files
4. Rename/Move File
5. Copy File
6. Delete Folder
7. Delete File
8. Exit
```

---

## ✅ Features Implemented

* Interactive user input
* Logs each action with a timestamp
* Checks if file/folder exists before deletion
* User-friendly messages with emoji indicators

---

## 📚 What I’m Learning

This script marks progress in **Phase 1: Linux Essentials** of my DevOps roadmap.

| Area              | Concepts Practiced                       |
| ----------------- | ---------------------------------------- |
| 💻 Linux Basics   | Filesystem, permissions, CLI navigation  |
| 🐚 Bash Scripting | Loops, case, conditions, user input      |
| 📂 File Commands  | `mkdir`, `touch`, `ls`, `mv`, `cp`, `rm` |
| 📝 Logging        | Timestamps, file redirection with `>>`   |

---

## 🚧 Issues Faced & What I Learned

### 🔹 Issue 1: `rm` command deleted wrong item

* **Problem**: Accidentally deleted a folder that shouldn't have been deleted.
* **Fix**: Added a check using `if [ -d "$folder" ]` before deleting folders.
* **Learning**: Always validate file/folder existence before performing destructive actions.

### 🔹 Issue 2: Tried to delete a folder using file command

* **Problem**: Misplaced `rm -i` for folders and files.
* **Fix**: Separated the logic: `rm -r -i` for folders, `rm -i` for files.
* **Learning**: Differentiating between file and directory deletion is crucial.

### 🔹 Issue 3: Script didn't log actions early on

* **Problem**: No feedback was being stored.
* **Fix**: Added `log_action` function with `>>` to append timestamped entries.
* **Learning**: Logging is essential for traceability and debugging.

---

## 🏗️ Tech Used

* 💻 **Linux** (Tested on Ubuntu 22.04)
* 🐚 **Bash Shell** scripting
* 📁 Linux CLI Commands: `mkdir`, `touch`, `ls`, `mv`, `cp`, `rm`
* 📝 Logging: `>>`, `date`, dynamically named files

---

## 📦 Project Structure

```bash
linux-fs-toolkit/
├── linux_fs_toolkit.sh       # Main bash script
├── logs/                     # Stores action logs (ignored via .gitignore)
│   └── action_*.log          # Timestamped log files
├── .gitignore                # Contains logs/ to exclude log files from repo
└── README.md                 # Documentation (this file)
```

---

## 🚀 What’s Next?

I’ll be pushing new scripts and tools daily as I move through the DevOps phases.

Next step: Deep dive into more Linux CLI tools (`grep`, `awk`, `sed`, etc.) and system commands (`top`, `ps`, `chmod`, etc.).

Stay tuned on [GitHub](https://github.com/theritikbarnwal)!
