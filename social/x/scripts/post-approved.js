const fs = require('fs');
const path = require('path');
const { loadEnv, oauth1Fetch, appendJsonl, readJson } = require('./lib');
loadEnv(path.join(__dirname, '..', '.env'));

async function main() {
  const queueFile = path.join(__dirname, '..', 'drafts', 'queue.json');
  const queue = readJson(queueFile, []);
  const next = queue.find(item => item.status === 'approved-manual' || item.status === 'approved');
  if (!next) {
    console.log(JSON.stringify({ ok: true, message: 'No approved tweets in queue' }, null, 2));
    return;
  }
  if (process.argv.includes('--dry-run')) {
    console.log(JSON.stringify({ ok: true, dryRun: true, tweet: next.text }, null, 2));
    return;
  }
  const body = new URLSearchParams({ status: next.text }).toString();
  const result = await oauth1Fetch('https://api.twitter.com/1.1/statuses/update.json', { method: 'POST', body });
  const log = {
    postedAt: new Date().toISOString(),
    requestText: next.text,
    status: result.status,
    response: result.json
  };
  appendJsonl(path.join(__dirname, '..', 'logs', 'posts.jsonl'), log);
  if (result.status === 200) {
    next.status = 'posted';
    next.postedAt = new Date().toISOString();
    fs.writeFileSync(queueFile, JSON.stringify(queue, null, 2) + '\n');
  }
  console.log(JSON.stringify(log, null, 2));
}

main().catch(err => { console.error(err); process.exit(1); });
