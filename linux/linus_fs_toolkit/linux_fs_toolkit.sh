#!/bin/bash

# Linux Filesystem Toolkit - Day 1 Project
# Author: theritikbarnwal

mkdir -p ./logs
LOG_FILE="./logs/action_$(date +%F_%T).log"

log_action() {
    echo "$(date) : $1" >> "$LOG_FILE"
}

echo "📁 Welcome to linux FS Toolkit 🔧"
echo "1. Create Folder"
echo "2. Create File"
echo "3. List Files"
echo "4. Rename/Move File"
echo "5. Copy File"
echo "6. Delete Folder"
echo "7. Delete File"
echo "8. Exit"

while true; do
    read -p "➡️ Choose an  option [1-8]: " choice

    case $choice in
        1)
            read -p "Enter folder name: " fname
            mkdir -p "$fname"
            echo "✅ Folder '$fname' created."
            log_action "Created folder: $fname"
            ;;
        2)
            read -p "Enter file name: " fname
            touch "$fname"
            echo "✅ File '$fname' created."
            log_action "Created file: $fname"
            ;;
        3)
            echo "📄 Files:"
            ls -al
            log_action "Listed files."
            ;;
        4)
            read -p "Enter current file name: " old
            read -p "Enter new name or path: " new
            mv "$old" "$new"
            echo "✅ File moved/renamed."
            log_action "Moved/Renamed $old to $new"
            ;;
        5)
            read -p "Enter file to copy: " source
            read -p "Enter destination: " dest
            cp "$source" "$dest"
            echo "✅ File copied."
            log_action "Copied $source to $dest"
            ;;
        6)
            read -p "Enter folder to delete: " folder
            if [ -d "$folder" ]; then
                rm -r -i "$folder"
                echo "🗑️ Folder '$folder' deleted."
                log_action "Deleted folder: $folder"
            else
                echo "❌ Folder '$folder' does not exist."
            fi
            ;;
        7)
            read -p "Enter file to delete: " file
            if [ -f "$file" ]; then
                rm -i "$file"
                echo "🗑️ File '$file' deleted."
                log_action "Deleted file: $file"
            else
                echo "❌ File '$file' does not exist."
            fi
            ;;
        8)
            echo "👋 Exiting... Bye!"
            log_action "Exited toolkit."
            break
            ;;
        *)
            echo "❌ Invalid choice. Try again."
            ;;
    esac
done