# X automation for Bartolomeu

## Current status
- OAuth 1.0a account auth works
- Posting endpoint is prepared but not live-tested yet
- Mention timeline endpoint is blocked by current X API access tier (code 453)

## Scripts
- `scripts/test-auth.js` — verify auth
- `scripts/draft-post.js` — add a draft tweet to queue
- `scripts/check-mentions.js` — fetch mentions (currently tier-limited)
- `scripts/post-approved.js` — post first approved tweet or dry-run

## Safe operating mode
- Draft automatically
- Post manually or with explicit approval
- Do not auto-reply yet
- Revisit mentions automation once the app has the required access tier
