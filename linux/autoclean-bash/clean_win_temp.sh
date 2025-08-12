#!/bin/bash

# === 📁 Set temp directories to clean ===
TEMP_DIRS=(
    "/mnt/c/Windows/Temp"
    "/mnt/c/Users/Lenovo/AppData/Local/Temp"
)

# === 🔐 Only allow deletion of these extensions ===
SAFE_EXTENSIONS=("*.tmp" "*.log" "*.bak" "*.old" "*.temp" "*~")

# === 📁 Log directory ===
LOGDIR="/mnt/c/autoclean/logs"
mkdir -p "$LOGDIR"

# === 🕒 Create timestamped log file ===
LOGFILE="$LOGDIR/cleanup_$(date +%F_%H-%M-%S).log"
echo "RDCT 📍 Starting temp cleanup task - $(date)" | tee -a "$LOGFILE"

# === 🧹 Loop through each temp directory ===
for DIR in "${TEMP_DIRS[@]}"; do
  echo "📂 Processing: $DIR" | tee -a "$LOGFILE"

  if [ -d "$DIR" ]; then
    echo "♻️  Cleaning allowed temp file types only in $DIR" | tee -a "$LOGFILE"

    # Loop through each allowed extension
    for ext in "${SAFE_EXTENSIONS[@]}"; do
      find "$DIR" -type f -iname "$ext" | while read -r file; do
        if rm -f "$file" 2>>"$LOGFILE"; then
          echo "✅ Deleted: $file" >> "$LOGFILE"
        else
          echo "⛔ Skipped (locked or permission denied): $file" >> "$LOGFILE"
        fi
      done
    done

    # Clean empty directories
    find "$DIR" -type d -empty -delete 2>>"$LOGFILE"
    echo "✅ Finished cleaning $DIR" | tee -a "$LOGFILE"

  else
    echo "⚠️  Directory not found: $DIR" | tee -a "$LOGFILE"
  fi
done

echo "$(date): ✅ Temp cleanup completed successfully." | tee -a "$LOGFILE"

