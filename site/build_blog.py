from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent
BLOG = ROOT / "blog"
BLOG.mkdir(exist_ok=True)

SITE_TITLE = "Bartolomeu"
BASE_CSS = "../blog.css"
HOME = "../index.html"
BLOG_INDEX = "./index.html"

posts = [
    {
        "slug": "stop-using-ai-like-a-toy",
        "title": "Stop Using AI Like a Toy",
        "tag": "Mindset",
        "description": "Why chatting is useful, but operating is where the real advantage begins.",
        "date": "2026-03-29",
        "content": """
## Most people are still at the novelty stage

Using ChatGPT or Claude is useful. No argument there.

But most people still use AI in the weakest possible way: they ask one-off questions, get one-off answers, then move on as if they just used a fancier search bar. That is fine for curiosity. It is rubbish for leverage.

The real shift starts when you stop asking, “What can this answer?” and start asking, “What job can this support repeatedly?”

That changes everything.

## A toy gives you a moment

A toy is entertaining. It is occasionally impressive. It can even be weirdly delightful.

But it does not change how work gets done.

When people use AI casually, that is mostly what they get:
- one good brainstorm
- one decent summary
- one clever draft
- one tiny moment of relief

That is not nothing. But it also is not transformation.

## An operator builds a system

If you want real value, build around the model.

Give it:
- a role
- stored context
- a workflow
- tools
- outputs
- rules

That is the difference between “AI helped once” and “AI keeps helping.”

## Why this matters now

The people who win with AI will not just be the people who know the newest models.
They will be the people who know how to structure useful work around them.

That means turning repeated friction into repeatable systems.

## Start here

Pick one task that happens every week.
Make it specific.
Make it reviewable.
Make it boring.

Then build from there.

Boring is where the money is.
        """,
    },
    {
        "slug": "what-makes-a-good-first-ai-agent",
        "title": "What Makes a Good First AI Agent?",
        "tag": "Getting started",
        "description": "Pick the right first job or waste time building a shiny useless mess.",
        "date": "2026-03-29",
        "content": """
## Your first agent should not be ambitious

Your first agent should be useful.

Those are not the same thing.

Most people start by trying to build something that sounds impressive. They imagine a general-purpose operator that manages everything, handles communication, hunts opportunities, organises their life, and probably also fixes their relationships.

That is how you end up with a chaos machine.

## The right first job has five traits

A good first AI agent usually has:
- recurring work
- clear inputs
- clear outputs
- low downside if it fails
- easy human review

That is the sweet spot.

## Good examples

Strong first-agent jobs include:
- daily or weekly briefings
- monitoring a niche for opportunities
- summarising research
- drafting follow-up emails
- organising notes into a usable report

These are grounded, visible, and easy to judge.

## Bad examples

Bad first agents usually sound exciting and vague.

Examples:
- “run my business”
- “automate all my client communication”
- “handle legal and financial admin end to end”
- “be my chief of staff with no oversight”

That is not bold. It is lazy thinking in better shoes.

## The 30-minute rule

If a workflow could reliably save you 30 minutes a week, it is worth serious attention.

People underrate small recurring gains because they are addicted to dramatic narratives. But real leverage compounds through repetition.

## A blunt test

If you cannot explain the job in two sentences, the job is not ready.

That is the test.
        """,
    },
    {
        "slug": "memory-is-where-ai-gets-useful",
        "title": "Memory Is Where AI Gets Useful",
        "tag": "Memory",
        "description": "Stateless chat is fine. Accumulated context is where the leverage starts.",
        "date": "2026-03-29",
        "content": """
## Stateless AI is permanently starting over

Without memory, every session begins from scratch.
That is tolerable for random questions.
It is weak for ongoing work.

The moment an AI system can remember useful context, it stops feeling like a novelty and starts becoming an assistant.

## What memory should hold

Useful memory includes:
- preferences
- active projects
- standing instructions
- recurring deadlines
- important prior decisions

That is the stuff that makes future output sharper and less repetitive.

## What memory should not become

A landfill.

If you save everything, you are not building intelligence. You are building clutter with attitude.

Do not casually store:
- passwords
- financial secrets
- random junk that will never matter again
- sensitive data the system does not need

## Short-term vs long-term memory

Short-term memory helps with current work.
Long-term memory captures the stable stuff that keeps paying off.

Confuse the two and the agent gets noisier over time.

## The practical gain

When memory is handled well, you stop re-explaining yourself every five minutes.
That sounds small. It is not.

Repetition is friction.
Memory removes friction.
That is why it matters.
        """,
    },
    {
        "slug": "tools-beat-prompts",
        "title": "Tools Beat Prompts",
        "tag": "Execution",
        "description": "Prompt cleverness is overrated. Tool access is what makes work move.",
        "date": "2026-03-29",
        "content": """
## Prompt tricks are not the moat

The internet is full of people selling prompt cleverness like it is a black art.
It is not.

A smart prompt is useful, sure.
But a model with no tool access is still trapped in the realm of talking about work instead of helping move it.

## Tools make the system real

When an AI agent can:
- search the web
- read files
- write notes
- draft emails
- check calendars
- send alerts

it can participate in actual workflows.

That is the difference between assistance and theatre.

## Match tools to the job

Do not bolt on every tool you can find just because you are excited.
That is how systems become dumb and dangerous.

If the job is research, start with search and file handling.
If the job is reporting, add data inputs and drafting outputs.
If the job is communication, introduce approval checkpoints before sending anything.

## The question that matters

Do these tools reduce real friction in a real workflow?

If yes, good.
If not, you are decorating the problem instead of solving it.
        """,
    },
    {
        "slug": "your-first-workflow-should-be-boring",
        "title": "Your First Workflow Should Be Boring",
        "tag": "Workflow",
        "description": "Boring, recurring, reviewable work is exactly where you should start.",
        "date": "2026-03-29",
        "content": """
## Boring work is where leverage hides

People want their first AI workflow to feel exciting.
That instinct is understandable and terrible.

The best first workflows are boring because boring usually means:
- repetitive
- clear
- measurable
- frustrating enough to matter

That is exactly what you want.

## Glamour is a trap

A glamorous workflow sounds like strategy.
A good workflow usually sounds like admin.

Guess which one gets implemented first.

## Strong first examples

Try things like:
- daily briefing generation
- opportunity monitoring
- meeting note cleanup
- inbox triage drafts
- weekly research summaries

These jobs may not impress anyone on social media. Good. Social media is not the KPI.

## The compounding effect

A workflow that saves 20 to 40 minutes every week is not small.
It compounds into less dropped context, faster decisions, and lower mental drag.

That is how systems start earning their keep.
        """,
    },
    {
        "slug": "the-trust-ladder-for-ai-agents",
        "title": "The Trust Ladder for AI Agents",
        "tag": "Safety",
        "description": "Read, draft, suggest, approve, then maybe automate. In that order.",
        "date": "2026-03-29",
        "content": """
## Trust should be earned

AI is fast, confident, and occasionally wrong in extremely creative ways.
That means trust has to be staged.

Do not start by giving an agent full execution authority because a demo looked slick.
That is how people automate mistakes and call it innovation.

## The ladder

A sane trust ladder looks like this:
1. read only
2. draft outputs
3. suggest actions
4. execute with approval
5. limited low-risk autonomy

That sequence exists for a reason.

## Why people skip steps

Because they confuse convenience with safety.
They want the end state before the system has earned it.

That is not advanced. It is impatient.

## What usually needs approval

Keep humans in the loop for:
- external messages
- public publishing
- purchases
- infrastructure changes
- deletions
- anything consequential and customer-facing

## The real goal

Autonomy is not the prize.
Useful reliability is.
        """,
    },
    {
        "slug": "dont-automate-important-stupidity",
        "title": "Don’t Automate Important Stupidity",
        "tag": "Risk",
        "description": "If a workflow is dumb, automating it just makes the stupidity scale faster.",
        "date": "2026-03-29",
        "content": """
## Automation does not rescue a bad process

People love saying, “Let’s automate it.”
What they usually mean is, “I would like to scale this mess before understanding it.”

That is a terrible plan.

## What automation actually does

Automation multiplies the properties of the underlying workflow.
If the workflow is clear, useful, and well-bounded, great.
If the workflow is sloppy, vague, or risky, automation just helps it fail faster.

## Three questions to ask first

Before automating anything, ask:
1. Is this process actually good?
2. Can I describe the inputs and outputs clearly?
3. Is the review point obvious?

If the answer is no, fix the process first.

## AI makes this more dangerous

Because the outputs often sound persuasive.
That means people trust bad work because it is wrapped in fluent language.

Fluency is not quality.
Confidence is not correctness.
An elegant mistake is still a mistake.

## The better move

Simplify first.
Then structure.
Then automate carefully.

In that order.
        """,
    },
    {
        "slug": "south-africas-ai-advantage-is-constraint",
        "title": "South Africa’s AI Advantage Is Constraint",
        "tag": "South Africa",
        "description": "Lean conditions force better systems. That’s an edge, not just a problem.",
        "date": "2026-03-29",
        "content": """
## Constraint is annoying and useful

South African builders do not get the luxury of infinite tool budgets, perfect infrastructure, or casual dollar-denominated optimism.

Good.

Constraint forces sharper decisions.

## Lean systems beat indulgent ones

When every subscription hurts a little, you ask better questions:
- what tool actually earns its place?
- what workflow justifies the spend?
- what setup still works when connectivity is messy?

Those are smart questions.

## Build for reality

That means:
- mobile matters
- interruptions happen
- cost in rand matters
- privacy common sense matters
- small teams need outcomes, not experimentation theatre

## The upside

Constraint strips away bullshit.
It pushes you toward useful systems faster.

The people drowning in budget often build bloated nonsense because they can afford to.
The people under pressure build tools that actually need to work.

That is an advantage if you use it properly.
        """,
    },
    {
        "slug": "ai-agents-for-founders",
        "title": "AI Agents for Founders",
        "tag": "Founder ops",
        "description": "Not for replacing judgment — for reducing friction and missed follow-through.",
        "date": "2026-03-29",
        "content": """
## Founders do not need more dashboards

They need less drag.

Most founder problems are not a shortage of information. They are a shortage of structured attention.
Too many tabs. Too many loose ends. Too many half-finished threads.

## Where agents help

A good founder-support agent can:
- produce a morning briefing
- summarise research
- track opportunities
- clean up meeting notes
- draft follow-up messages
- turn chaos into a sharper next move

## What it should not do

It should not replace judgment.
It should not act as a fake CEO.
It should not be trusted with high-stakes communication without review.

## The real value

Founders benefit when the system reduces cognitive sludge.
That means fewer missed follow-ups, cleaner weekly reviews, and better continuity across messy days.

That is not sexy. It is just useful.
        """,
    },
    {
        "slug": "ai-agents-for-consultants",
        "title": "AI Agents for Consultants",
        "tag": "Consulting",
        "description": "Faster prep, better briefs, cleaner follow-up, less admin sludge.",
        "date": "2026-03-29",
        "content": """
## Consulting is full of invisible admin

Clients pay for thinking, but a lot of consulting work gets swallowed by prep, notes, research, and follow-through.
That is where AI agents become genuinely useful.

## Practical consultant workflows

An agent can help with:
- pre-call research
- proposal first drafts
- meeting summaries
- action lists
- post-call follow-up drafts
- competitor scanning

## What this changes

It compresses the dull parts around the judgment-heavy parts.
That means the consultant gets to spend more time on analysis and less time on admin sludge.

## What still needs a human

Strategy.
Nuance.
Client relationship judgment.
Anything high-stakes.

Useful AI support does not remove expertise.
It frees it up.
        """,
    },
    {
        "slug": "build-a-daily-briefing-agent",
        "title": "Build a Daily Briefing Agent",
        "tag": "Use case",
        "description": "One of the best first agents because it turns noise into a sane start to the day.",
        "date": "2026-03-29",
        "content": """
## Why this is such a strong first build

A daily briefing agent is practical, bounded, and easy to judge.
That makes it one of the best first agent projects.

## What it does

It gathers a defined set of inputs and produces one clear output: a useful briefing.

Possible inputs:
- task list
- notes
- saved priorities
- upcoming calendar items
- messages needing attention

Possible output:
- top priorities
- risks
- overdue items
- suggested next steps

## Why it works

Because the workflow is simple:
1. gather inputs
2. filter signal from noise
3. summarise clearly
4. present for human review

No heroics. No fantasy. Just a better start to the day.

## Keep it short

The best daily briefings are concise.
If your agent writes a small novel every morning, it has missed the point.
        """,
    },
    {
        "slug": "how-to-write-an-agent-brief",
        "title": "How to Write an Agent Brief",
        "tag": "Design",
        "description": "Weak brief, weak agent. This is the part most people phone in and regret.",
        "date": "2026-03-29",
        "content": """
## Most agent briefs are too vague

People write things like:
- be helpful
- be smart
- support the business

That is not a brief.
That is wishful thinking wearing business casual.

## A useful brief includes

At minimum:
- role
- primary tasks
- inputs
- outputs
- tools allowed
- rules
- approval boundaries
- success criteria

## The point of the brief

The brief reduces ambiguity.
It tells the system what job it has and how it is supposed to behave.

That matters because AI is very good at producing plausible work inside fuzzy instructions — which is another way of saying it can go wrong confidently.

## Write for clarity, not grandeur

Short and specific beats impressive and vague.
Every time.
        """,
    },
    {
        "slug": "the-difference-between-clever-and-useful",
        "title": "The Difference Between Clever and Useful",
        "tag": "Opinion",
        "description": "The market is drowning in clever demos. Useful systems are still rare.",
        "date": "2026-03-29",
        "content": """
## Clever gets applause

Useful gets reused.

That is the distinction.

A clever system does something surprising once.
A useful system quietly earns its place over and over again.

## Why people chase clever

Because it is more fun to show.
It looks good in demos.
It feels innovative.

But clever systems often collapse under real conditions because nobody designed them for repetition, review, or reliability.

## Useful is less glamorous and more valuable

Useful systems:
- solve a recurring problem
- fit into a routine
- save visible time
- reduce dropped balls
- keep earning trust

That is the standard worth building toward.
        """,
    },
    {
        "slug": "your-agent-does-not-need-a-personality-disorder",
        "title": "Your Agent Does Not Need a Personality Disorder",
        "tag": "Voice",
        "description": "Tone matters, but stop building circus acts when what you need is competence.",
        "date": "2026-03-29",
        "content": """
## Personality is not the point

A clear voice helps.
A ridiculous persona often gets in the way.

People over-index on making their agent quirky, edgy, mystical, or emotionally intense. That is fine if you are building a toy. It is stupid if you are trying to build a useful assistant.

## What matters more

Your agent should be:
- clear
- competent
- consistent
- appropriately toned for the job

That does not mean it has to sound sterile.
It means the personality should serve the work, not hijack it.

## The rule

If the voice makes the system easier to use, good.
If it makes the system more annoying, self-indulgent, or distracting, kill it.

Competence is a better personality trait than theatrics.
        """,
    },
    {
        "slug": "what-to-build-after-your-first-agent",
        "title": "What to Build After Your First Agent",
        "tag": "Next steps",
        "description": "Once one workflow works, the next move is not chaos. It is measured expansion.",
        "date": "2026-03-29",
        "content": """
## Success creates a new temptation

Once the first agent works, people immediately want to build five more.
Calm down.

The next move is not random expansion.
It is deliberate scaling.

## What to do first

After your first useful agent:
- tighten the brief
- improve the workflow
- reduce friction
- review what memory is actually helping
- confirm where trust boundaries should stay

## Then expand sideways

Choose the next workflow based on adjacency.
If your first agent handles daily briefings, maybe the next one handles weekly research synthesis.
If your first one supports follow-up drafting, maybe the next supports lead qualification.

Do not jump from one useful workflow to a fantasy of total automation.
That road is paved with brittle rubbish.

## Keep the standard

Build the second workflow only if you can define:
- the job
- the input
- the output
- the review point
- the success criteria

If you cannot, you are just excited. Excitement is not a system.
        """,
    },
]


def paraize(text: str) -> str:
    lines = [line.rstrip() for line in dedent(text).strip().splitlines()]
    out = []
    in_list = False
    list_type = None
    for line in lines:
        if not line:
            if in_list:
                out.append(f"</{list_type}>")
                in_list = False
                list_type = None
            continue
        if line.startswith("## "):
            if in_list:
                out.append(f"</{list_type}>")
                in_list = False
                list_type = None
            out.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            if in_list:
                out.append(f"</{list_type}>")
                in_list = False
                list_type = None
            out.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("- "):
            if not in_list or list_type != "ul":
                if in_list:
                    out.append(f"</{list_type}>")
                out.append("<ul>")
                in_list = True
                list_type = "ul"
            out.append(f"<li>{line[2:]}</li>")
        elif line[0].isdigit() and ". " in line:
            if not in_list or list_type != "ol":
                if in_list:
                    out.append(f"</{list_type}>")
                out.append("<ol>")
                in_list = True
                list_type = "ol"
            out.append(f"<li>{line.split('. ',1)[1]}</li>")
        else:
            if in_list:
                out.append(f"</{list_type}>")
                in_list = False
                list_type = None
            out.append(f"<p>{line}</p>")
    if in_list:
        out.append(f"</{list_type}>")
    return "\n".join(out)


def page(post):
    sidebar_links = ''.join(
        f'<a href="/{BLOG_INDEX[2:]}">← Back to blog index</a>'
        f'<a href="{HOME}">Home</a>'
        f'<a href="#top">Top</a>'
    )
    html = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{post["title"]} — {SITE_TITLE}</title>
    <meta name="description" content="{post["description"]}" />
    <link rel="stylesheet" href="{BASE_CSS}" />
  </head>
  <body>
    <header id="top">
      <div class="wrap">
        <nav>
          <a class="brand" href="{HOME}">{SITE_TITLE}</a>
          <div class="nav-links">
            <a href="{HOME}#product">Product</a>
            <a href="/{BLOG_INDEX[2:]}">Blog</a>
          </div>
        </nav>
      </div>
    </header>

    <main>
      <section class="hero">
        <div class="wrap">
          <div class="eyebrow">{post["tag"]}</div>
          <h1>{post["title"]}</h1>
          <p class="lead">{post["description"]}</p>
        </div>
      </section>

      <section>
        <div class="wrap article-layout">
          <aside class="sidebar">
            <h4>Navigate</h4>
            {sidebar_links}
            <p class="muted" style="margin-top:14px;">Published {post["date"]}</p>
          </aside>
          <article class="post">
            <div class="meta">{post["date"]} · {post["tag"]}</div>
            {paraize(post["content"])}
            <div class="cta-row">
              <a class="btn primary" href="{HOME}#product">Get the playbook</a>
              <a class="btn secondary" href="/{BLOG_INDEX[2:]}">Read more articles</a>
            </div>
          </article>
        </div>
      </section>
    </main>

    <footer>
      <div class="wrap">
        <div class="brand">{SITE_TITLE}</div>
        <p>Operate with leverage.</p>
      </div>
    </footer>
  </body>
</html>
'''
    return html

for post in posts:
    (BLOG / f"{post['slug']}.html").write_text(page(post), encoding="utf-8")

print(f"Wrote {len(posts)} blog posts to {BLOG}")
