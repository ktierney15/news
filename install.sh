#!/bin/zsh

# build app
source .venv/bin/activate
pyinstaller --onefile --name news src/main.py
deactivate

# run binary to make sure it works
dist/news

# move it to bin and make it executable
sudo rm -f /usr/local/bin/news
sudo mv dist/news /usr/local/bin/
chmod +x /usr/local/bin/news
