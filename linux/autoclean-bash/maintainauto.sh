#!/bin/bash

# 📁 Set the base directory (absolute path)
BASEDIR="/root/autoclean-bash"

echo "RDCT 📍 Running DevOps Cleanup Task"

# 1. Backup log file
if [ -f "$BASEDIR/logfile.txt" ]; then
  cp "$BASEDIR/logfile.txt" "$BASEDIR/logs/logfile_$(date +%F_%H-%M-%S).txt"
  echo "✅ logfile.txt backed up."
else
  echo "⚠️  logfile.txt not found!"
fi

# 2. Archive temp files
if [ -f "$BASEDIR/tempfile.txt" ]; then
  mv "$BASEDIR/tempfile.txt" "$BASEDIR/archive/tempfile_$(date +%F).txt"
  echo "📦 tempfile.txt archived."
else
  echo "⚠️  tempfile.txt not found!"
fi

# 3. Move trash file
if [ -f "$BASEDIR/trashfile.txt" ]; then
  mv "$BASEDIR/trashfile.txt" "$BASEDIR/trash/"
  echo "🗑️  trashfile.txt moved to trash."
else
  echo "⚠️  trashfile.txt not found!"
fi

# 4. Logging the operation
echo "$(date): Maintenance Script executed." >> "$BASEDIR/logs/maintenance.log"
