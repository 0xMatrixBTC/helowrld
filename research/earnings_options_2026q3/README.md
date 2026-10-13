# Earnings options screen (Q3 2026 season)

Daily closes from IBKR (2024-10-14 to 2026-10-12, 500 trading days). Option quotes are IBKR closing mids from 2026-10-12.

- `analyze.py`: one-day close-to-close move on each of the last 8 earnings reaction days → `results.txt`
- `replay.py`: buys today's options (ATM straddle and ~10% OTM call), replays each past earnings window over the same number of trading days → `replay_results.txt`

Run: `python3 analyze.py > results.txt && python3 replay.py`

Caveats: 8 events per stock; 2026 earnings dates for COIN/PLTR/AMD/SNAP are estimates; the sample is a strong bull market for PLTR/AMD/INTC, which flatters long calls.
