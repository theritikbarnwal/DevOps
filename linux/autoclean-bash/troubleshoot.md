

---

````markdown
---

## 🐞 Why the Script Failed in Cron but Worked Manually

When running `maintain.sh` manually, it works because:

- You're inside the correct directory (`autoclean-bash/`)
- Your shell session has all required environment variables
- Relative file paths like `logfile.txt`, `logs/`, `archive/` work correctly

However, **cron does not behave the same**:

### ⚠️ Cron's Behavior:
- It runs from the root (`/`) or some unrelated directory
- It doesn't load your `.bashrc` or `.profile`
- It uses a **minimal environment**
- It doesn't know your script's relative path context

### ❌ Original (Broken) Code:
```bash
cp logfile.txt logs/logfile_$(date +%F_%H-%M-%S).txt
mv tempfile.txt archive/tempfile_$(date +%F).txt
````

These commands fail under cron because they assume the script is running from the `autoclean-bash/` directory.

---

### ✅ Fix Applied:

To make it work reliably under cron, we added absolute paths using a `BASEDIR` variable:

```bash
BASEDIR="/root/autoclean-bash"

cp "$BASEDIR/logfile.txt" "$BASEDIR/logs/logfile_$(date +%F_%H-%M-%S).txt"
mv "$BASEDIR/tempfile.txt" "$BASEDIR/archive/tempfile_$(date +%F).txt"
```

Now the script works correctly in **any environment**, including cron, systemd, or CI pipelines.

---