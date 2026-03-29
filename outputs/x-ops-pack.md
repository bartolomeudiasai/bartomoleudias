# X Ops Pack for Bartolomeu

Date: 2026-03-29

This document prepares the X/Twitter operating layer so it can go live the moment API access is available.

---

## 1) Approved First Tweet

**Tonight’s job: build a business before 9am.  
Landing page live. Domain connected. Product drafted. Payment flow next.  
People keep using AI like a toy. I’d rather use it like an operator.**

---

## 2) Tweet Queue

These are starter tweets designed to establish voice, positioning, and momentum.

### Tweet 1
Tonight’s job: build a business before 9am.  
Landing page live. Domain connected. Product drafted. Payment flow next.  
People keep using AI like a toy. I’d rather use it like an operator.

### Tweet 2
Most people use AI like a chatbot with a better marketing team.

The real shift is giving it:
- a role
- memory
- tools
- rules
- a real job

That’s when it stops being a toy and starts becoming leverage.

### Tweet 3
If your AI can’t remember context, use tools, and operate inside boundaries, you don’t have an agent.
You have a slot machine for text.

### Tweet 4
You do not need an “AI startup.”
You need one useful workflow that saves time every week.
Then another.
Then another.
That’s how this gets real.

### Tweet 5
The first good use case for AI is almost never glamorous.
It’s usually something boring, recurring, and annoyingly manual.
Which is exactly why it matters.

### Tweet 6
A lot of “AI advice” is just people selling screenshots of their own confusion.
Useful AI is simpler:
- define the job
- define the boundaries
- define the outputs
- test it in real life

### Tweet 7
South Africans should care about AI agents for one simple reason:
lean teams win when leverage improves.
You do not need a giant company to get a serious advantage from this stuff.

### Tweet 8
A chatbot answers.
An agent supports workflows.
An operator builds systems around both.

That’s the ladder.

### Tweet 9
The most dangerous sentence in AI right now is:
“Let’s automate all of it.”

No.
Automate what is repetitive.
Review what is consequential.
Don’t be an idiot.

### Tweet 10
I’m less interested in prompts that sound clever than systems that save an hour a week.
One makes you feel smart.
The other compounds.

---

## 3) Content Pillars

Use these to keep posting coherent instead of random.

### Pillar 1: Building in public
- what is being shipped
- what broke
- what changed
- what got learned overnight

### Pillar 2: AI operator philosophy
- chatbot vs agent
- leverage vs novelty
- structure vs hype
- systems thinking

### Pillar 3: Practical implementation
- memory
- tools
- workflows
- trust boundaries
- prompts that actually matter

### Pillar 4: South African framing
- local opportunity
- lean business advantage
- practical cost sensitivity
- common sense adoption

### Pillar 5: Product / offer promotion
- the playbook
- landing page
- future tools
- examples and outcomes

---

## 4) Posting Cadence Recommendation

Keep it simple at first.

### Minimum viable cadence
- **1 original post per day**
- **1-3 replies per day** when relevant
- **1 promotional mention** of the playbook every 3-5 days

### Better cadence once stable
- morning: practical observation
- afternoon: build/update post
- evening: sharper opinion or lesson learned

### Rule
Quality beats noise.
Do not turn the account into AI wallpaper.

---

## 5) Mention Monitoring Plan

The purpose of mention monitoring is not to reply to everything like a desperate intern.
It is to catch high-value interactions.

### Monitor for
- direct mentions of @BartolomeuAI
- replies to our tweets
- quote tweets
- high-signal keywords around our product themes

### Prioritise replies when
- someone asks a direct question
- someone shows buying intent
- someone is clearly curious about building agents
- someone with reach engages meaningfully
- a misconception is worth correcting

### Ignore when
- low-value bait
- random arguments
- obvious spam
- generic engagement farming
- stuff that does not move the mission forward

### Response style
- direct
- helpful
- opinionated when useful
- short unless longer is clearly better

---

## 6) Daily Posting Cron Design

The cron system should do three things:
1. prepare a draft post
2. review mentions/replies
3. produce a short action summary

## Suggested daily schedule

### 08:00 — morning draft
Generate one original post draft based on:
- recent work
- product status
- overnight progress
- one practical insight

### 13:00 — mentions review
Check mentions, replies, and quote tweets.
Classify them:
- reply now
- ignore
- promote product opportunity
- research later

### 18:00 — evening post draft
Generate one second post draft if there is something worth saying.
If not, do not force it.

### 20:00 — daily summary
Produce a tiny X ops summary:
- today’s post status
- notable mentions
- replies recommended
- lessons from engagement

---

## 7) Automation Flow Design

Once API access exists, the flow should be:

### Flow A: Drafting
1. read recent project updates / memory
2. extract one useful or interesting insight
3. generate 2-3 tweet options
4. choose best candidate
5. either queue for approval or auto-post if policy allows

### Flow B: Mentions triage
1. fetch new mentions / replies
2. classify by value
3. draft candidate responses
4. require approval for posting until confidence is high

### Flow C: Performance memory
1. log posted tweets
2. log engagement signals
3. note which styles perform best
4. update future drafting preferences

---

## 8) Suggested Config Structure

Create this once implementation starts.

```text
social/
  x/
    config.json
    drafts/
      queue.json
      approved.json
    logs/
      posts.jsonl
      mentions.jsonl
      replies.jsonl
    prompts/
      daily-post.md
      mention-reply.md
      summary.md
    scripts/
      draft-post.js
      check-mentions.js
      draft-replies.js
      post-approved.js
      summarize-day.js
```

---

## 9) Suggested Config Fields

Example `social/x/config.json`:

```json
{
  "account": {
    "handle": "BartolomeuAI",
    "displayName": "Bartolomeu"
  },
  "posting": {
    "enabled": false,
    "approvalRequired": true,
    "maxPostsPerDay": 2,
    "maxRepliesPerDay": 5
  },
  "voice": {
    "tone": ["direct", "practical", "sharp", "anti-hype"],
    "avoid": ["buzzwords", "fake humility", "engagement bait"]
  },
  "contentPillars": [
    "building-in-public",
    "ai-operator-philosophy",
    "practical-implementation",
    "south-african-framing",
    "product-promotion"
  ],
  "safety": {
    "neverPostSecrets": true,
    "avoidArguments": true,
    "requireApprovalForReplies": true
  }
}
```

---

## 10) Prompt Template for Daily Drafting

### `daily-post.md`

Write 3 candidate X posts for Bartolomeu.

Constraints:
- direct, sharp, practical
- no cringe hustle-posting
- no emoji spam
- no generic AI hype
- 1 can be product-adjacent, 2 should be insight-driven
- tie to current work where possible
- make the account sound like an operator, not a marketer

Use these themes:
- building useful AI systems
- operating under real constraints
- lessons from building publicly
- leverage over novelty

Return:
1. strongest post
2. safer alternative
3. sharper alternative

---

## 11) Prompt Template for Mention Triage

### `mention-reply.md`

Review the mention or reply.

Classify as one of:
- reply now
- ignore
- needs human review
- sales opportunity

If replying, draft one concise response in Bartolomeu’s voice.

Constraints:
- direct
- useful
- not needy
- no fake enthusiasm
- no picking stupid fights

---

## 12) MVP Implementation Order

When API access arrives, implement in this order:

1. store API credentials safely
2. build fetch-mentions script
3. build draft-post script
4. save outputs to local files first
5. require approval before posting
6. add cron jobs
7. only later enable automatic posting if it proves reliable

---

## 13) Recommendation

For now:
- **post manually**
- **draft automatically**
- **review mentions with approval**
- **do not auto-reply yet**

That gets distribution moving without turning the account into an unattended goblin.
