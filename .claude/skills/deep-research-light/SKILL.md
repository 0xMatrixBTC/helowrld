---
name: deep-research-light
description: Fast, single-agent research on a current-events, markets, macro or crypto question, with a cited, structured report. Use when the user types /deep-research-light, or asks for a "quick deep dive", "comprehensive but fast" analysis, or a researched answer that does not need a team of subagents. It checks the question's own premises against fresh sources first, runs a small batch of parallel web searches, flags conflicting data, and gives scenarios with probabilities and the next catalysts to watch.
argument-hint: <research question, in any language>
---

# Deep Research (Light)

A lighter version of full deep research: one agent, about 4–10 searches, one report. No subagents and no workflow. Aim for an answer in a few minutes that a finance-literate reader can act on.

Research question: $ARGUMENTS

## Step 1: Break down the question (no tool calls)

- Rewrite the question as 2–5 sub-questions.
- List every **factual premise** in the question, such as "the rate is 5%", "the Fed hiked in September", or "a December hike is certain". Each premise must be checked in Step 2. Users often mix up related numbers (policy rate vs. 10-year yield, headline vs. core inflation, CPI vs. PCE), so check each one separately.
- Note today's date from the environment. Anything after your training cutoff must come from search, not memory.

## Step 2: Search (parallel, then targeted)

1. **First batch:** send 3–5 `WebSearch` calls in the same turn, one per sub-question or premise. Use `mode: "extended"` for very recent events, prices, market odds and data releases. Use `"standard"` for background facts.
2. **Second batch:** send 1–4 more searches to fill gaps, resolve conflicts, or get counter-evidence against your first conclusion.
3. Use `WebFetch` only for a primary source (central bank statement, official data release). If a fetch fails, move on and say the figure came from secondary reporting.
4. Stop at about 10 searches. Light means light.

Source priority: official sources (central banks, statistics agencies, exchanges, filings), then major financial press, then research and broker notes, then crypto media and blogs. Treat price predictions as opinion, not fact.

## Step 3: Check before writing

- **Premises:** for each premise from Step 1, decide whether it is true, false, or partly true. If it is false, the report must **correct it at the top**, kindly and with the right number.
- **Conflicting data:** when sources disagree (different dates, different odds), give a range, name the source of each number, and say which one is freshest. Never present a stale number as current.
- **Your own numbers:** label every estimate or probability that you produced as your own judgment, for example "(my estimate)".
- **History:** add 1–2 historical comparisons when they help (past rate cycles, past market reactions), and say how long ago each one was.

## Step 4: Write the report

Reply in the **user's language**. Use this structure and leave out sections that don't apply:

1. **One-line conclusions** (3–4 bullets). The premise correction goes first if one is needed.
2. **Current state:** a table of the key numbers, each with what it means.
3. **Core analysis:** answer each sub-question. Show the logic in simple steps, for example a real-rate calculation.
4. **Scenarios:** a table with condition, path and probability (my estimate). The probabilities should add up to about 100%.
5. **Asset or decision impact:** what this means for each asset or choice the user asked about. Include counter-evidence to the user's own view.
6. **Catalysts to watch:** a table of dates, events and why each one matters.
7. **Practical takeaways:** short bullets. For investing topics, add "not investment advice".
8. **Sources:** a markdown link for every URL you relied on.

Style rules:

- Lead with the answer, then the support.
- Use plain words and short sentences. Explain jargon the first time you use it.
- Use tables for numbers and comparisons, not long paragraphs.
- Be direct about uncertainty: give one clear "we don't know X yet" line instead of hedging every sentence.
- If the user asked for something this skill can't do (for example live prices from a broker account), say so in one line.
