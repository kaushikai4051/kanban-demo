# Kanban Board

A lightweight Kanban board that runs entirely in the browser with no external dependencies.

## Features

- **3 columns** — To Do, In Progress, Done
- **Drag and drop** — move cards between columns
- **Add cards** — title, description, and tag (Feature, Bug, Design, Docs)
- **Delete cards** — hover a card to reveal the delete button
- **Persistent** — cards are saved to `localStorage` and survive page refresh
- **Dark theme** — easy on the eyes

## Running locally

Requires Python 3 (standard library only).

```bash
python server.py
```

The board opens automatically at `http://localhost:8080`. Press `Ctrl+C` to stop.

## Project structure

```
kanban/
├── index.html   # Full UI — HTML, CSS, and JS in one file
└── server.py    # Zero-dependency Python HTTP server
```
