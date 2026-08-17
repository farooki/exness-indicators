# Exness Indicators

A collection of custom indicators for the **Exness Web Trading Platform**, built using the **Indie programming language**.

The goal of this project is to provide useful chart visualizations and trading-session indicators that make market structure, trading days, weeks, and major Forex sessions easier to identify.

## Indicators

### 📅 Daily Background

Alternates the chart background color for each calendar day.

**File:** `indicators/daily_background.py`

Features:
- Alternating background for each day
- Makes daily boundaries easier to identify
- Useful on intraday charts

---

### 📆 Weekly Background

Alternates the chart background color for each week.

**File:** `indicators/weekly_background.py`

Features:
- Alternating background for each week
- Helps identify weekly market structure
- Useful for intraday and higher-timeframe analysis

---

### 🇦🇺 Sydney Background

Highlights the Sydney trading session.

**File:** `indicators/sydney_background.py`

**Session:** `22:00 – 07:00 UTC`

---

### 🇯🇵 Asia Background

Highlights the Asian/Tokyo trading session.

**File:** `indicators/asia_background.py`

**Session:** `00:00 – 09:00 UTC`

---

### 🇬🇧 London Background

Highlights the London trading session.

**File:** `indicators/london_background.py`

**Session:** `08:00 – 17:00 UTC`

---

### 🇺🇸 New York Background

Highlights the New York trading session.

**File:** `indicators/new_york_background.py`

**Session:** `13:00 – 22:00 UTC`

---

## Project Structure

```text
exness-indicators/
│
├── README.md
│
├── indicators/
│   ├── daily_background.py
│   ├── weekly_background.py
│   ├── sydney_background.py
│   ├── asia_background.py
│   ├── london_background.py
│   └── new_york_background.py
│
└── LICENSE
