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
- The meditation slot is UBHAPPY: prepare for take-off. It is about reducing stress and growing happiness, from Lisa's and Kevin's practice: Mahayana Buddhism as taught by the Dalai Lama, Jon Kabat-Zinn's mindfulness, and credible happiness science. No health claims beyond general information, and no products.
- On Mondays, the meditation pick carries a verified Dalai Lama quote of the week (`quote.text`, `quote.by`, `quote.source_url`).
- No repeats: no URL or source from the last 7 editions, and no story, subject, award, event or image from the last 14, even from a different outlet. No photo-competition gallery in the nature slot two days running.
- Say rituals, and never contrast them with habits.
- Editorial picks only. Offers and affiliate links stay separate.
- The ayurveda slot draws from Banyan Botanicals' wellness blog (https://www.banyanbotanicals.com/blogs/wellness) first (Lisa, 23 Nov 2026), until UBUNBOUND's own Ayurvedic feed takes over. Pick one article, not the blog's front page. Write the "why" as general information, never a health claim or cure, and link the article itself, not a product. The no-repeats rule still applies; if every recent article is used, pick another credible Ayurvedic source.
- No bee emoji: the PhiBee logo is the only bee.

## PhiBee's Top 9 on X (from 24 Nov 2026)

- Each afternoon at about 5pm Sydney, the Reader reads the last day's posts from Lisa's X List, plus the latest post this week from each team account (Lisa @onegreenheartU, FABLERATION and RightUp). The candidates for tomorrow are at `https://reader.ubunbound.com/x/candidates/<date>`, team posts first, each with its post id.
- The curation adds an optional `x_top` list to the edition: six picks from the list plus the three team posts, each `{"id": "<post id>", "note": "<PhiBee's one-line note>"}`. Notes say why the post is worth a look, in PhiBee's voice, never a price prediction or advice.
- If the candidates page is empty (X not set up yet, or nothing read), leave `x_top` out. The email simply has no X section that day.
- Team posts are always shown, marked "From our team", even if `x_top` leaves them out. Vary the six: no account twice, and nothing repeated from the last 7 days.
- The email shows the nine as one line each and links to `reader.ubunbound.com/x/<date>`, where each post is shown the way X requires and readers vote for their favourite.
