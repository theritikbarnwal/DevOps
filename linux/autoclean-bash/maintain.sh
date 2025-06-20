#!/bin/bash

echo "RDCT 📍 Running DevOps Cleanup Task"

# 1. Backup log file
if [ -f logfile.txt ]; then
  cp logfile.txt logs/logfile_$(date +%F_%H-%M-%S).txt
  echo "✅ logfile.txt backed up."
else
  echo "⚠️  logfile.txt not found!"
fi

# 2. Archive temp files
if [ -f tempfile.txt ]; then
  mv tempfile.txt archive/tempfile_$(date +%F).txt
  echo "📦 tempfile.txt archived."
else
  echo "⚠️  tempfile.txt not found!"
fi

# 3. Move trash file
if [ -f trashfile.txt ]; then
  mv trashfile.txt trash/
  echo "🗑️  trashfile.txt moved to trash."
else
  echo "⚠️  trashfile.txt not found!"
fi

# 4. Logging the operation
echo "$(date): Maintenance Script executed." >> logs/maintenance.log
