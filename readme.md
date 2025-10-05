# Candy Pop!

A match-3 puzzle game built with Pygame for an advanced programming class project.

## About

Candy Pop is a Candy Crush-style game where players swap adjacent candies to create matches of three or more. The game features special candies, protected tiles, and various power-ups.

## Requirements

- Python 3.x
- Pygame

## How to Run

```bash
python p1.py
```

## Features

- Customizable grid size (rows and columns)
- Blocked spaces that cannot be filled
- Protected tiles that require special attention to clear
- Special candies:
  - **Bomb**: Clears surrounding 3x3 area (created by L/T-shaped matches)
  - **Rainbow**: Clears all candies of a selected color (created by 5+ matches)
  - **Striped**: Clears entire row or column (created by 4 matches)
- Power-ups:
  - Refresh board (limited uses)
  - Change candy color (costs points)
  - Swap any two candies (costs points)
- Save/load game functionality
- Score and timer tracking

## Gameplay

1. Click two adjacent candies to swap them
2. Match 3 or more candies of the same color
3. Create special candies with longer matches
4. Use power-ups strategically to clear protected tiles
5. Game ends when no valid moves remain and refreshes are exhausted

---

*written with AI.*