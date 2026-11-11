# UBAWESOME editions

PhiBee, the Discovery Jockey, picks nine discoveries every day across Self, Health and Wealth.
Each day is one file: `editions/YYYY-MM-DD.json`.

## How a day goes out

1. The edition is written, checked with `python3 tools/editorial_gate.py editions/<date>.json`, and pushed here by the evening before.
2. From 05:00 Sydney, the Reader site (reader.ubunbound.com) fetches that day's file, checks it again, and stores it. Stored editions never change.
3. At 05:30 Sydney, the email goes to everyone on the list, and the edition appears on the site and in the archive.

No file for the day means no email that day; nothing half-finished is ever sent.

## Rules every edition follows

- Nine categories, one discovery each: crypto, world, nature, meditation, ideas, creator, ayurveda, yoga, strength.
- At least one podcast, with `listen_minutes` (shown with the 3× listening time).
- Every link is HTTPS and goes straight to the experience; nature picks credit the photographer.
- On Mondays, the meditation pick carries a verified Dalai Lama quote of the week (`quote.text`, `quote.by`, `quote.source_url`).
- Editorial picks only. Offers and affiliate links stay separate.
- No bee emoji: the PhiBee logo is the only bee.
