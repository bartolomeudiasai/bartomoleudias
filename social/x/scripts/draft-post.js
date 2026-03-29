const fs = require('fs');
const path = require('path');

const candidates = [
  'Useful AI starts when it has a job, not just a prompt.',
  'The fastest way to understand AI is to build one small workflow that saves you time every week.',
  'A chatbot answers. An agent supports workflows. An operator builds systems around both.'
];

const file = path.join(__dirname, '..', 'drafts', 'queue.json');
const existing = JSON.parse(fs.readFileSync(file, 'utf8'));
existing.push({
  status: 'draft',
  text: candidates[Math.floor(Math.random() * candidates.length)],
  createdAt: new Date().toISOString()
});
fs.writeFileSync(file, JSON.stringify(existing, null, 2) + '\n');
console.log(JSON.stringify(existing[existing.length - 1], null, 2));
