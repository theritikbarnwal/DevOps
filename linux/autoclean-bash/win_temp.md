Here's a professional, complete `README.md` tailored for your `autoclean-bash` script. It explains what it does, what you learned, and the challenges faced — perfect for your `linux/` folder on GitHub:

---

````markdown
# 🧼 autoclean-bash – Temp File Cleaner for Windows via WSL

## 📌 Overview

`autoclean-bash` is a real-world Bash automation script I developed to clean up temporary files from a **Windows environment** using **Linux (Bash via WSL)**. It targets:

- `C:\Windows\Temp`
- `C:\Users\<User>\AppData\Local\Temp`

The script identifies and deletes only safe file types such as `.tmp`, `.log`, `.bak`, etc., logs all activity, and maintains a proper audit trail.

---

## ⚙️ What the Script Does

- Scans temp directories for files with **specific extensions**
- Deletes only those files considered safe to remove
- Cleans up **empty subdirectories**
- Generates timestamped **log files** for every cleanup task

### 🔧 Safe Extensions Handled

```bash
*.tmp, *.log, *.bak, *.old, *.temp, *~
````

### 🗂️ Logs

All operations are logged under:

```
/mnt/c/autoclean/logs/
```

Each log file includes timestamps, file actions, and errors (if any).

---

## 🧠 What I Learned

| Area                      | Learning                                                                        |
| ------------------------- | ------------------------------------------------------------------------------- |
| **WSL Integration**       | Understood how Bash in WSL interacts with the Windows filesystem (`/mnt/c/...`) |
| **Scripting with Arrays** | Used Bash arrays for directory paths and file extensions                        |
| **Safe File Deletion**    | Restricted deletions using `-iname` filters and only on known temp types        |
| **Logging**               | Built dynamic timestamped logs with `tee`, `mkdir -p`, and `>>` for audit       |
| **Robust Loops**          | Used nested loops for multiple extensions and directories                       |
| **Edge Case Handling**    | Skipped locked/system files, handled missing directories gracefully             |
| **Cleaning Directories**  | Applied `find ... -type d -empty -delete` to remove empty dirs                  |

---

## 🚧 Challenges Faced

| Challenge                    | How I Solved It                                                              |
| ---------------------------- | ---------------------------------------------------------------------------- |
| **Permissions**              | Some files were system-locked; I redirected errors to logs and skipped those |
| **Unsafe Deletion**          | Prevented risky deletions by hard-coding safe file extensions only           |
| **Log Overwrites**           | Solved using timestamp-based unique log filenames                            |
| **Windows Path Translation** | Had to use `/mnt/c/...` format to access Windows paths from Bash             |
| **Empty Directories**        | Added an extra `find -type d -empty -delete` to handle leftover folders      |

---

## 📁 File Structure

```
linux/
├── autoclean-bash             ← Main script
├── sample-log/                ← Example logs (optional)
│   └── cleanup_2025-06-24_17-30-22.log
└── README.md                  ← (This file)
```

---

## 🚀 Usage

### ✅ Make executable:

```bash
chmod +x autoclean-bash
```

### 🧹 Run cleanup:

```bash
./autoclean-bash
```

### 📄 View logs:

```bash
cat /mnt/c/autoclean/logs/cleanup_<timestamp>.log
```

---

## 🧩 Next Steps

* [ ] Add dry-run mode (`--dry-run`) to preview actions
* [ ] Accept custom directories via arguments
* [ ] Add cron job integration (if run in Linux regularly)
* [ ] Integrate email/log reporting

---

## 🔗 Reference

* [WSL Docs – Microsoft](https://learn.microsoft.com/en-us/windows/wsl/)
* [Bash Scripting Guide](https://tldp.org/LDP/abs/html/)

---

> **Author**: Ritik Barnwal
> **Repo**: [theritikbarnwal/DevOps](https://github.com/theritikbarnwal/DevOps)

```

---

Would you also like me to create a `sample-log/` file with example output and errors for better GitHub presentation?
```
