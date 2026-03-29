const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

function loadEnv(file) {
  const text = fs.readFileSync(file, 'utf8');
  for (const line of text.split(/\r?\n/)) {
    if (!line.trim() || line.trim().startsWith('#')) continue;
    const idx = line.indexOf('=');
    if (idx === -1) continue;
    const key = line.slice(0, idx).trim();
    let val = line.slice(idx + 1).trim();
    if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
      val = val.slice(1, -1);
    }
    process.env[key] = val;
  }
}

function percentEncode(str) {
  return encodeURIComponent(str)
    .replace(/[!*()']/g, c => '%' + c.charCodeAt(0).toString(16).toUpperCase());
}

async function oauth1Fetch(url, method = 'GET') {
  const consumerKey = process.env.X_CONSUMER_KEY;
  const consumerSecret = process.env.X_CONSUMER_SECRET;
  const accessToken = process.env.X_ACCESS_TOKEN;
  const accessSecret = process.env.X_ACCESS_TOKEN_SECRET;
  const nonce = crypto.randomBytes(16).toString('hex');
  const timestamp = Math.floor(Date.now() / 1000).toString();
  const u = new URL(url);
  const params = {
    oauth_consumer_key: consumerKey,
    oauth_nonce: nonce,
    oauth_signature_method: 'HMAC-SHA1',
    oauth_timestamp: timestamp,
    oauth_token: accessToken,
    oauth_version: '1.0',
  };
  for (const [k, v] of u.searchParams.entries()) params[k] = v;
  const paramString = Object.keys(params).sort().map(k => `${percentEncode(k)}=${percentEncode(params[k])}`).join('&');
  const baseString = [method.toUpperCase(), percentEncode(`${u.origin}${u.pathname}`), percentEncode(paramString)].join('&');
  const signingKey = `${percentEncode(consumerSecret)}&${percentEncode(accessSecret)}`;
  const signature = crypto.createHmac('sha1', signingKey).update(baseString).digest('base64');
  const authHeaderParams = {
    oauth_consumer_key: consumerKey,
    oauth_nonce: nonce,
    oauth_signature: signature,
    oauth_signature_method: 'HMAC-SHA1',
    oauth_timestamp: timestamp,
    oauth_token: accessToken,
    oauth_version: '1.0',
  };
  const authHeader = 'OAuth ' + Object.keys(authHeaderParams).sort().map(k => `${percentEncode(k)}="${percentEncode(authHeaderParams[k])}"`).join(', ');
  const res = await fetch(url, { method, headers: { Authorization: authHeader } });
  const text = await res.text();
  return { status: res.status, text };
}

async function main() {
  loadEnv(path.join(__dirname, '..', '.env'));
  const v2 = await fetch('https://api.twitter.com/2/users/me', {
    headers: { Authorization: `Bearer ${process.env.X_BEARER_TOKEN}` }
  });
  const v2Text = await v2.text();
  const v1 = await oauth1Fetch('https://api.twitter.com/1.1/account/verify_credentials.json?skip_status=true&include_entities=false');
  console.log(JSON.stringify({
    bearerCheck: { status: v2.status, body: safeParse(v2Text) },
    oauth1Check: { status: v1.status, body: safeParse(v1.text) }
  }, null, 2));
}

function safeParse(s) {
  try { return JSON.parse(s); } catch { return s; }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
