const path = require('path');
const { loadEnv, oauth1Fetch, appendJsonl } = require('./lib');
loadEnv(path.join(__dirname, '..', '.env'));

async function main() {
  const result = await oauth1Fetch('https://api.twitter.com/1.1/statuses/mentions_timeline.json?count=10&tweet_mode=extended');
  const out = {
    checkedAt: new Date().toISOString(),
    status: result.status,
    mentions: Array.isArray(result.json)
      ? result.json.map(t => ({
          id_str: t.id_str,
          created_at: t.created_at,
          screen_name: t.user?.screen_name,
          full_text: t.full_text || t.text
        }))
      : result.json
  };
  appendJsonl(path.join(__dirname, '..', 'logs', 'mentions.jsonl'), out);
  console.log(JSON.stringify(out, null, 2));
}

main().catch(err => { console.error(err); process.exit(1); });
