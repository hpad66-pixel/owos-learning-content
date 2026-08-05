# One Water AI Granular Curriculum Map

Status: working curriculum review, not approved learner-facing content

## What this file controls

This is the human-readable view of the canonical granular tracker in
`curriculum/one-water-ai-granular-toc.json`. It leaves the approved 64-module numbering
intact, shows the current lesson structure, and places proposed additions beside the
modules where they belong.

## What the review actually contains

- 37 numbered proposals, not 39.
- The source sequence skips 19, 27.
- Item 32 repeats item 3 and should be consolidated, not taught twice.
- 21 additions are materially missing.
- 15 additions are partly covered but need more depth or practice.
- 1 addition is a duplicate.
- Three existing module areas are separately marked for targeted strengthening.
- The review says it checked a 602-page version. This map uses the current 684-page PDF and current module source files.

## Granular numbering

| Pattern | Meaning |
| --- | --- |
| `M40` | Module 40 |
| `M40.03` | Current section 3 inside Module 40 |
| `M40.03a` | Current subsection A under section 3 |
| `M40.P01` | Proposed addition 1 for Module 40 |
| `M40.P01a` | Proposed subtopic A under that addition |
| `ME-033` | Targeted enhancement for an existing module |

The stable IDs make each change traceable without renumbering the course every time the
curriculum is refined.

## Recommended curriculum architecture

1. Keep the 64 canonical modules.
2. Add a Builder Readiness Lab to Module 00 and use it as the entry gate for Part V.
3. Add applied labs inside Modules 32 through 38 for everyday AI work.
4. Add a build-to-production sequence inside Modules 39 through 43 and Module 53.
5. Add role-specific revenue, finance, support, and dashboard labs where the role modules already live.
6. Consolidate overlapping proposals before authoring so the course stays coherent.

## Gap register

| ID | Source | Proposal | Coverage | Decision | Recommended modules | Source page |
| --- | ---: | --- | --- | --- | --- | ---: |
| `GA-001` | 1 | The terminal, from zero | missing | proposed | M00, M40 | 1 |
| `GA-002` | 2 | Git and GitHub: the actual commands | missing | proposed | M40, M53 | 1 |
| `GA-003` | 3 | API keys and the .env file: where your secrets live | missing | proposed | M00, M25, M27, M40, M43 | 1 |
| `GA-004` | 4 | Your code editor: install Cursor or VS Code, and read code you didn't write | missing | proposed | M00, M40 | 2 |
| `GA-005` | 5 | Install a project's parts, and get a download to actually run | missing | proposed | M40, M43 | 2 |
| `GA-006` | 6 | Read an error and fix it | missing | proposed | M40 | 2 |
| `GA-007` | 7 | When not to trust the AI | partial | proposed | M06, M07, M10, M24, M31 | 2 |
| `GA-008` | 8 | Reading a number without getting fooled | missing | proposed | M24, M36, M39 | 3 |
| `GA-009` | 9 | Set up a reusable assistant: Custom GPTs, Projects, Gems | missing | proposed | M32 | 3 |
| `GA-010` | 10 | Drop in a spreadsheet and ask AI about it | missing | proposed | M16, M32, M36 | 3 |
| `GA-011` | 11 | Use AI inside Excel and Google Sheets | missing | proposed | M16, M32 | 4 |
| `GA-012` | 12 | Deep research done right: NotebookLM and Perplexity, hands-on | partial | proposed | M32, M36 | 4 |
| `GA-013` | 13 | Pick the right model and know what it costs (OpenRouter) | missing | proposed | M32, M43 | 4 |
| `GA-014` | 14 | Make audio, video, and finished graphics with AI | partial | proposed | M37 | 4 |
| `GA-015` | 15 | Build one real automation, start to finish | partial | proposed | M38 | 5 |
| `GA-016` | 16 | Turn a meeting into notes, decisions, and action items | missing | proposed | M38, M46 | 5 |
| `GA-017` | 17 | Build your own knowledge base, and let AI handle scheduling | missing | proposed | M32, M36, M38 | 5 |
| `GA-018` | 18 | Show AI what's in front of you: screenshots, photos, PDFs, and voice | partial | proposed | M08, M32, M45 | 6 |
| `GA-020` | 20 | What a web app really is: files, index.html, and localhost | missing | proposed | M39, M40, M43 | 6 |
| `GA-021` | 21 | Turn an idea into a plan: a simple PRD, user stories, a sitemap | missing | proposed | M39, M53 | 6 |
| `GA-022` | 22 | Sketch it first: wireframes in Figma and your own diagram | missing | proposed | M39, M44 | 6 |
| `GA-023` | 23 | From no-code to code, plus basic design and user testing | partial | proposed | M39, M40, M53 | 7 |
| `GA-024` | 24 | Run your own AI locally: Ollama and LM Studio | partial | proposed | M42 | 7 |
| `GA-025` | 25 | Agents for real: connect a tool (MCP) and try computer-use | partial | proposed | M41 | 7 |
| `GA-026` | 26 | Put it online: from your computer to a live link | partial | proposed | M43 | 8 |
| `GA-028` | 28 | What your app costs to run, and how to price it | partial | proposed | M12, M43, M50, M53 | 8 |
| `GA-029` | 29 | Getting found: SEO, showing up in AI answers, and basic analytics | missing | proposed | M36, M39, M50 | 8 |
| `GA-030` | 30 | Give your app a real web address: a domain, DNS, and HTTPS | missing | proposed | M39, M43 | 8 |
| `GA-031` | 31 | From prototype to real product: logins and a real database | missing | proposed | M39, M43 | 8 |
| `GA-032` | 32 | Get an API key without a surprise bill | duplicate | consolidate | M00, M25, M27, M40, M43 | 9 |
| `GA-033` | 33 | Actually build with an AI coding agent | partial | proposed | M40 | 9 |
| `GA-034` | 34 | Set up your sales engine: a CRM, lead capture, and outreach | partial | proposed | M50 | 9 |
| `GA-035` | 35 | Win the work: AI for RFP responses and grant writing | partial | proposed | M49, M63 | 10 |
| `GA-036` | 36 | Run the money with AI: a simple model, a dashboard, bookkeeping, contracts, HR | missing | proposed | M12, M46, M47, M49, M50 | 10 |
| `GA-037` | 37 | Making AI part of your day, and keeping up as it changes | partial | proposed | M32, M52, M53 | 10 |
| `GA-038` | 38 | A support setup: a website chatbot, ticket sorting, and a voice line | partial | proposed | M38, M45, M60 | 10 |
| `GA-039` | 39 | Build a dashboard and ask your data in plain English | missing | proposed | M16, M43, M47 | 11 |

## Targeted enhancements to existing modules

| ID | Modules | Enhancement | Coverage | Source page |
| --- | --- | --- | --- | ---: |
| `ME-033` | M33 | Strengthen prompt, context, and har&#110;ess engineering | partial | 11 |
| `ME-027` | M27 | Add individual privacy mechanics | partial | 11 |
| `ME-006-007` | M06, M07 | Reconcile blank-slate framing with persistent memory | partial | 11 |

## Module-by-module granular contents

### Part O: Front Matter

#### M00. Orientation, Setup & Your Learning Path

Current PDF pages: 20-32

Current sections:

- `M00.01` By the end of this module [instruction]
- `M00.02` How this course works [instruction]
- `M00.03` Getting set up [instruction]
- `M00.04` The placement diagnostic [instruction]
- `M00.05` The rules of the road [instruction]
- `M00.06` Role takeaways [role guidance]
- `M00.07` Glossary [glossary]
- `M00.08` Now you're ready [instruction]
- `M00.09` Sources [evidence]

Proposed additions:

- `M00.P01` The terminal, from zero [missing; proposed; GA-001]
  - `M00.P01a` Opening Terminal (Mac) / PowerShell (Windows)
  - `M00.P01b` Reading the prompt
  - `M00.P01c` Cd, ls, pwd, mkdir, mv, cp, rm, cat, open/start, clear, echo
  - `M00.P01d` Absolute vs relative paths
  - `M00.P01e` The ~ home dir
  - `M00.P01f` Tab-completion
  - `M00.P01g` Running a command vs running a script
  - `M00.P01h` Ctrl-C to stop
  - `M00.P01i` Up-arrow history
- `M00.P02` API keys and the .env file: where your secrets live [missing; proposed; GA-003]
  - `M00.P02a` An API key is a password
  - `M00.P02b` Getting one from the OpenAI/Anthropic/OpenRouter dashboard
  - `M00.P02c` The .env file, environment variables, loading a key
  - `M00.P02d` Key-in-code vs key-in-environment
  - `M00.P02e` .gitignore the .env
  - `M00.P02f` What happens when you push a key to a public repo (scanning bots drain credits)
  - `M00.P02g` Rotating/revoking a leaked key
  - `M00.P02h` Spend caps and rate limits
  - `M00.P02i` Consumer login vs API key
- `M00.P03` Your code editor: install Cursor or VS Code, and read code you didn't write [missing; proposed; GA-004]
  - `M00.P03a` Installing VS Code or Cursor
  - `M00.P03b` Opening a project folder
  - `M00.P03c` The file tree
  - `M00.P03d` The integrated terminal
  - `M00.P03e` Cursor's AI chat and inline edit
  - `M00.P03f` Running the project from the editor
  - `M00.P03g` Reading a file top to bottom: recognizing a function, variable, import, if/loop
  - `M00.P03h` HTML vs CSS vs JS
  - `M00.P03i` Asking the AI to explain a file in plain language before you change it
- `M00.P04` Get an API key without a surprise bill [duplicate; consolidate; GA-032]
  - `M00.P04a` Create an account at platform.openai.com / console.anthropic.com / openrouter.ai and find the 'API keys' page
  - `M00.P04b` Generate a key, copy it once (you can never see it again), and paste it into .env, never into a chat or into the code
  - `M00.P04c` Add a payment method and set a hard monthly usage limit / budget cap BEFORE you build anything
  - `M00.P04d` Read the usage dashboard: what one request cost, tokens in vs out, which model burned the money
  - `M00.P04e` Rotate / revoke a leaked key, and why a key pushed to a public GitHub repo gets drained within minutes (ties to .gitignore)

### Part I: Foundations and Mental Models

#### M01. Why This, Why Now: AI and the World of Water

Current PDF pages: 33-43

Current sections:

- `M01.01` Learning objectives [orientation]
- `M01.02` The 2am pump: data versus intelligence [instruction]
- `M01.03` The state of the water world [instruction]
- `M01.04` Why now, and not five years ago [instruction]
- `M01.05` The three mental models [instruction]
- `M01.06` Trust is the product [instruction]
- `M01.07` The climbing wall, money, and jobs [instruction]
  - `M01.07a` On money [instruction]
  - `M01.07b` On jobs [instruction]
- `M01.08` Knowledge check [assessment]
- `M01.09` Role takeaways [role guidance]
- `M01.10` Glossary [glossary]
- `M01.11` Your first build is coming [instruction]
- `M01.12` Sources [evidence]

#### M02. What AI Actually Is: From 1956 to Today

Current PDF pages: 44-52

Current sections:

- `M02.01` Learning objectives [orientation]
- `M02.02` A short, honest history [instruction]
- `M02.03` The nested circles [instruction]
- `M02.04` Software 1.0, 2.0, 3.0, in depth [instruction]
- `M02.05` The landscape today [instruction]
- `M02.06` Knowledge check [assessment]
- `M02.07` Role takeaways [role guidance]
- `M02.08` Glossary [glossary]
- `M02.09` Next [transition]
- `M02.10` Sources [evidence]

#### M03. The Lexicon of AI: Every Term, Every Token

Current PDF pages: 53-59

Current sections:

- `M03.01` Learning objectives [orientation]
- `M03.02` The core vocabulary [instruction]
- `M03.03` Tokens, and token maxing [instruction]
- `M03.04` Chatbot, agent, agentic [instruction]
- `M03.05` The rest of the words [instruction]
- `M03.06` Knowledge check [assessment]
- `M03.07` Role takeaways [role guidance]
- `M03.08` Glossary [glossary]
- `M03.09` Next [transition]
- `M03.10` Sources [evidence]

#### M04. Under the Hood: How the Machine Turns a Question Into an Answer

Current PDF pages: 60-69

Current sections:

- `M04.01` Learning objectives [orientation]
- `M04.02` From words to numbers [instruction]
- `M04.03` How an answer is produced [instruction]
- `M04.04` Learning the pattern [instruction]
- `M04.05` Probabilistic versus deterministic [instruction]
- `M04.06` Knowledge check [assessment]
- `M04.07` Role takeaways [role guidance]
- `M04.08` Glossary [glossary]
- `M04.09` Next [transition]
- `M04.10` Sources [evidence]

#### M05. How a Model Is Actually Made

Current PDF pages: 70-78

Current sections:

- `M05.01` Learning objectives [orientation]
- `M05.02` Pretraining: reading everything [instruction]
- `M05.03` Supervised fine-tuning: learning the job [instruction]
- `M05.04` Alignment: shaping the judgment [instruction]
- `M05.05` Reasoning training: learning to think [instruction]
- `M05.06` Knowledge check [assessment]
- `M05.07` Role takeaways [role guidance]
- `M05.08` Glossary [glossary]
- `M05.09` Next [transition]
- `M05.10` Sources [evidence]

#### M06. The Psychology of an LLM

Current PDF pages: 79-88

Current sections:

- `M06.01` Learning objectives [orientation]
- `M06.02` Hallucination [instruction]
- `M06.03` The cognitive profile [instruction]
- `M06.04` Working with the grain [instruction]
- `M06.05` Knowledge check [assessment]
- `M06.06` Role takeaways [role guidance]
- `M06.07` Glossary [glossary]
- `M06.08` Next [transition]
- `M06.09` Sources [evidence]

Proposed additions:

- `M06.P01` When not to trust the AI [partial; proposed; GA-007]
  - `M06.P01a` Sycophancy: the model mirrors your framing and validates a leading question
  - `M06.P01b` Countermeasures, don't lead, ask it to argue the opposite/steelman, ask 'what am I getting wrong?', never treat agreement as confirmation
  - `M06.P01c` Over-reliance and automation bias: skill atrophy, offloading judgment on irreversible calls
  - `M06.P01d` Calibrate trust to stakes (low = accept, high = verify or human sign-off)
  - `M06.P01e` Keep a manual baseline
  - `M06.P01f` Cross-model verification as a cheap independent check: paste the same question to a different model and see where they disagree
  - `M06.P01g` The human counterweight to the whole 'delegate to AI' arc

Targeted enhancements:

- `ME-006-007` Reconcile blank-slate framing with persistent memory: Explain product memory, builder memory, provenance, and privacy without implying that model weights remember a conversation.

#### M07. Reasoning Models and Test-Time Compute

Current PDF pages: 89-96

Current sections:

- `M07.01` Learning objectives [orientation]
- `M07.02` The shift to thinking [instruction]
- `M07.03` Test-time compute [instruction]
- `M07.04` When to use which [instruction]
- `M07.05` Knowledge check [assessment]
- `M07.06` Role takeaways [role guidance]
- `M07.07` Glossary [glossary]
- `M07.08` Next [transition]
- `M07.09` Sources [evidence]

Proposed additions:

- `M07.P01` When not to trust the AI [partial; proposed; GA-007]
  - `M07.P01a` Sycophancy: the model mirrors your framing and validates a leading question
  - `M07.P01b` Countermeasures, don't lead, ask it to argue the opposite/steelman, ask 'what am I getting wrong?', never treat agreement as confirmation
  - `M07.P01c` Over-reliance and automation bias: skill atrophy, offloading judgment on irreversible calls
  - `M07.P01d` Calibrate trust to stakes (low = accept, high = verify or human sign-off)
  - `M07.P01e` Keep a manual baseline
  - `M07.P01f` Cross-model verification as a cheap independent check: paste the same question to a different model and see where they disagree
  - `M07.P01g` The human counterweight to the whole 'delegate to AI' arc

Targeted enhancements:

- `ME-006-007` Reconcile blank-slate framing with persistent memory: Explain product memory, builder memory, provenance, and privacy without implying that model weights remember a conversation.

#### M08. How Machines Read and See: OCR, Vision, and Multimodal AI

Current PDF pages: 97-108

Current sections:

- `M08.01` Learning objectives [orientation]
- `M08.02` OCR and document AI [instruction]
- `M08.03` Computer vision [instruction]
- `M08.04` Multimodal models [instruction]
- `M08.05` Water applications [instruction]
- `M08.06` Knowledge check [assessment]
- `M08.07` Role takeaways [role guidance]
- `M08.08` Glossary [glossary]
- `M08.09` Next [transition]
- `M08.10` Sources [evidence]

Proposed additions:

- `M08.P01` Show AI what's in front of you: screenshots, photos, PDFs, and voice [partial; proposed; GA-018]
  - `M08.P01a` Paste a screenshot of an error message, a dashboard, or a chart and ask 'what is this / what's wrong'
  - `M08.P01b` Photograph a nameplate, a gauge, or a handwritten log and have AI transcribe it into a clean table
  - `M08.P01c` Drop a scanned or native PDF (a permit, a spec sheet, a 200-page report) and ask grounded questions of it
  - `M08.P01d` Voice mode in the phone app: talk to ChatGPT/Claude hands-free in the field, on the drive, on a walk
  - `M08.P01e` The trust check: eyeball every extracted number against the source image before you use it (ties to provenance)

#### M09. The LLM as an Operating System

Current PDF pages: 109-118

Current sections:

- `M09.01` Learning objectives [orientation]
- `M09.02` The LLM as an operating system [instruction]
- `M09.03` Front end versus back end [instruction]
- `M09.04` Reading a software architecture diagram [instruction]
- `M09.05` Talking to IT, and where AI sits [instruction]
- `M09.06` Knowledge check [assessment]
- `M09.07` Role takeaways [role guidance]
- `M09.08` Glossary [glossary]
- `M09.09` Next [transition]
- `M09.10` Sources [evidence]

#### M10. The Autonomy Slider: Augmentation vs. Automation

Current PDF pages: 119-127

Current sections:

- `M10.01` Learning objectives [orientation]
- `M10.02` Augmentation versus automation [instruction]
- `M10.03` Human-in-the-loop [instruction]
- `M10.04` Choosing the setting [instruction]
- `M10.05` Knowledge check [assessment]
- `M10.06` Role takeaways [role guidance]
- `M10.07` Glossary [glossary]
- `M10.08` Next [transition]
- `M10.09` Sources [evidence]

Proposed additions:

- `M10.P01` When not to trust the AI [partial; proposed; GA-007]
  - `M10.P01a` Sycophancy: the model mirrors your framing and validates a leading question
  - `M10.P01b` Countermeasures, don't lead, ask it to argue the opposite/steelman, ask 'what am I getting wrong?', never treat agreement as confirmation
  - `M10.P01c` Over-reliance and automation bias: skill atrophy, offloading judgment on irreversible calls
  - `M10.P01d` Calibrate trust to stakes (low = accept, high = verify or human sign-off)
  - `M10.P01e` Keep a manual baseline
  - `M10.P01f` Cross-model verification as a cheap independent check: paste the same question to a different model and see where they disagree
  - `M10.P01g` The human counterweight to the whole 'delegate to AI' arc

#### M11. Superintelligence, Honestly

Current PDF pages: 128-136

Current sections:

- `M11.01` Learning objectives [orientation]
- `M11.02` The terms [instruction]
- `M11.03` The debate [instruction]
- `M11.04` So what for a utility [instruction]
- `M11.05` Knowledge check [assessment]
- `M11.06` Role takeaways [role guidance]
- `M11.07` Glossary [glossary]
- `M11.08` Next [transition]
- `M11.09` Sources [evidence]

#### M12. Jobs, Money, and the Utility

Current PDF pages: 137-147

Current sections:

- `M12.01` Learning objectives [orientation]
- `M12.02` Jobs, honestly [instruction]
- `M12.03` The money case [instruction]
- `M12.04` The transition plan [instruction]
- `M12.05` Knowledge check [assessment]
- `M12.06` Role takeaways [role guidance]
- `M12.07` Glossary [glossary]
- `M12.08` Part One complete [instruction]
- `M12.09` Sources [evidence]

Proposed additions:

- `M12.P01` What your app costs to run, and how to price it [partial; proposed; GA-028]
  - `M12.P01a` Input vs output token pricing
  - `M12.P01b` Read a model's pricing page
  - `M12.P01c` Estimate a monthly API bill
  - `M12.P01d` Cost-per-active-user
  - `M12.P01e` What a DigitalOcean droplet runs
  - `M12.P01f` Turn 'tokens are the meter' into a real spreadsheet forecast as usage grows
  - `M12.P01g` Price the product: subscription tiers, per-seat vs usage, gross margin after API/infra cost, a break-even 'how many customers do I need'
  - `M12.P01h` Use AI to draft and pressure-test pricing options
- `M12.P02` Run the money with AI: a simple model, a dashboard, bookkeeping, contracts, HR [missing; proposed; GA-036]
  - `M12.P02a` Build a 12-month P&L, a cash-flow/runway projection, and unit economics in a sheet with AI doing the formulas
  - `M12.P02b` What a P&L / balance sheet / cash-flow statement even are
  - `M12.P02c` A board-ready KPI scorecard/dashboard from a messy export (Google Sheets / Looker Studio) + an AI-drafted executive summary
  - `M12.P02d` Bookkeeping/month-end: generate and chase invoices, categorize/reconcile transactions, QuickBooks, expense capture from receipts
  - `M12.P02e` Review a contract/NDA/MSA with AI: flag auto-renewal traps, liability caps, IP/data-rights, where legal review stays mandatory
  - `M12.P02f` HR with AI: job descriptions, resume screening, structured interview questions, offer letters, with the fair-hiring cautions

### Part II: Retrieval, Generation and the Data Foundation

#### M13. Generative AI and RAG

Current PDF pages: 148-157

Current sections:

- `M13.01` Learning objectives [orientation]
- `M13.02` Generation versus retrieval [instruction]
- `M13.03` Naive RAG, end to end [instruction]
- `M13.04` Why RAG matters for utilities [instruction]
- `M13.05` Knowledge check [assessment]
- `M13.06` Role takeaways [role guidance]
- `M13.07` Glossary [glossary]
- `M13.08` Next [transition]
- `M13.09` Sources [evidence]

#### M14. The RAG Family, Done Right

Current PDF pages: 158-165

Current sections:

- `M14.01` Learning objectives [orientation]
- `M14.02` Naive RAG's limits [instruction]
- `M14.03` Graph RAG [instruction]
- `M14.04` Hybrid RAG [instruction]
- `M14.05` Choosing [instruction]
- `M14.06` Knowledge check [assessment]
- `M14.07` Role takeaways [role guidance]
- `M14.08` Glossary [glossary]
- `M14.09` Next [transition]
- `M14.10` Sources [evidence]

#### M15. Embeddings and Vector Databases

Current PDF pages: 166-174

Current sections:

- `M15.01` Learning objectives [orientation]
- `M15.02` Embeddings in practice [instruction]
- `M15.03` Chunking [instruction]
- `M15.04` Vector databases [instruction]
- `M15.05` Knowledge check [assessment]
- `M15.06` Role takeaways [role guidance]
- `M15.07` Glossary [glossary]
- `M15.08` Next [transition]
- `M15.09` Sources [evidence]

#### M16. Fix the Data Before You Worship the AI: Data Readiness

Current PDF pages: 175-185

Current sections:

- `M16.01` Learning objectives [orientation]
- `M16.02` What "ready" means [instruction]
- `M16.03` The utility data landscape [instruction]
- `M16.04` The data-to-capital pipeline [instruction]
- `M16.05` Getting ready [instruction]
- `M16.06` Knowledge check [assessment]
- `M16.07` Role takeaways [role guidance]
- `M16.08` Glossary [glossary]
- `M16.09` Next [transition]
- `M16.10` Sources [evidence]

Proposed additions:

- `M16.P01` Drop in a spreadsheet and ask AI about it [missing; proposed; GA-010]
  - `M16.P01a` Drag a .csv/.xlsx into ChatGPT (Code Interpreter) or Claude
  - `M16.P01b` 'what's driving the spike?', 'chart monthly non-revenue water', 'find the outliers'
  - `M16.P01c` Which assistants actually crunch numbers vs just chat
  - `M16.P01d` File-size/row limits
  - `M16.P01e` It writes hidden Python for you
  - `M16.P01f` Downloading the chart / cleaned file back out
  - `M16.P01g` The honest failure mode: it silently miscomputes, re-ask, spot-check one row by hand
- `M16.P02` Use AI inside Excel and Google Sheets [missing; proposed; GA-011]
  - `M16.P02a` Copilot in Excel, Gemini in Google Sheets
  - `M16.P02b` Prompt-to-formula (VLOOKUP/XLOOKUP, SUMIFS, a pivot table)
  - `M16.P02c` 'explain this formula', 'find the error in this sheet'
  - `M16.P02d` The =formula bar, A1/$A$1 refs, CSV vs XLSX
  - `M16.P02e` AI-assisted cleanup on a real file: dedupe rows, standardize 'N. Plant' vs 'North Plant', split a stuck column, flag blanks
  - `M16.P02f` Spot-checking the AI's work, the step before any analysis
- `M16.P03` Build a dashboard and ask your data in plain English [missing; proposed; GA-039]
  - `M16.P03a` A no-code dashboard: connect a Google Sheet/CSV/database in Looker Studio, Power BI, or Metabase
  - `M16.P03b` Drag a field, pick a chart, add a filter, publish a shareable link, auto-refresh
  - `M16.P03c` Ask your database in plain English: text-to-SQL, connect an assistant/tool to a real table (CIS, GL, CMMS, historian)
  - `M16.P03d` Read the generated SQL before trusting it
  - `M16.P03e` Read-only, never UPDATE/DELETE
  - `M16.P03f` Choosing the right chart (trend=line, distribution=histogram) and reading a misleading one
  - `M16.P03g` Insight to recommendation: a one-page decision memo with the evidence, the caveats, and what would change your mind

#### M17. Life Is a Graph: Taxonomy, Ontology, Knowledge Graphs

Current PDF pages: 186-210

Current sections:

- `M17.01` Before we begin [orientation]
- `M17.02` What you will be able to do [orientation]
- `M17.03` Lesson 17.1: A status is not a situation [instruction]
- `M17.04` Lesson 17.2: Five people, one lift station [instruction]
- `M17.05` Lesson 17.3: The Record-and-Reality Method [instruction]
  - `M17.05a` Decide what must be decided [instruction]
  - `M17.05b` Step 1: Decide [instruction]
  - `M17.05c` Step 2: Read [instruction]
  - `M17.05d` Step 3: Listen [instruction]
  - `M17.05e` Step 4: Connect [instruction]
  - `M17.05f` Step 5: Verify [instruction]
- `M17.06` Knowledge check: Record or reality? [assessment]
- `M17.07` Lesson 17.4: The words, defined after the problem [instruction]
- `M17.08` Lesson 17.5: Why a graph instead of another table [instruction]
- `M17.09` Lesson 17.6: Two truths can coexist [instruction]
  - `M17.09a` Work Order 4821: Closed [instruction]
  - `M17.09b` Vibration continued [instruction]
- `M17.10` Lesson 17.7: Reading a utility ontology [instruction]
- `M17.11` Knowledge check: Follow the evidence [assessment]
- `M17.12` Lesson 17.8: The pattern travels [instruction]
- `M17.13` What this means by role [role guidance]
  - `M17.13a` Operator [instruction]
  - `M17.13b` Administrator [instruction]
  - `M17.13c` Engineer [instruction]
  - `M17.13d` Planner or manager [instruction]
  - `M17.13e` Executive or elected official [instruction]
  - `M17.13f` Consultant or vendor [instruction]
- `M17.14` Applied work product: Record-and-Reality Decision Map [work product]
- `M17.15` Final applied check [assessment]
- `M17.16` Frequently asked questions [faq]
  - `M17.16a` Does every document belong in the knowledge graph? [instruction]
  - `M17.16b` Is an operator observation less trustworthy than a sensor reading? [instruction]
  - `M17.16c` Does the knowledge graph replace the computerized maintenance management system or supervisory control and data acquisition system? [instruction]
  - `M17.16d` Is a graph database required to start? [instruction]
  - `M17.16e` Can an artificial-intelligence agent make the final operating decision? [instruction]
  - `M17.16f` What is the difference between more context and structured context? [instruction]
- `M17.17` What to remember [instruction]
- `M17.18` Where this leads [transition]
- `M17.19` Sources and evidence boundary [evidence]

#### M18. The Machinery: GraphDB, Neo4j, RDF, SPARQL, SHACL

Current PDF pages: 211-219

Current sections:

- `M18.01` Learning objectives [orientation]
- `M18.02` Two kinds of graph [instruction]
- `M18.03` GraphDB versus Neo4j [instruction]
- `M18.04` Querying and validating [instruction]
- `M18.05` Deterministic over probabilistic [instruction]
- `M18.06` Knowledge check [assessment]
- `M18.07` Role takeaways [role guidance]
- `M18.08` Glossary [glossary]
- `M18.09` Next [transition]
- `M18.10` Sources [evidence]

#### M19. The One Water Ontology: Operationalizing the Hydrologic Cycle

Current PDF pages: 220-229

Current sections:

- `M19.01` Learning objectives [orientation]
- `M19.02` One Water as a model [instruction]
- `M19.03` The applied ontology [instruction]
- `M19.04` The product suites and the three-tier doctrine [instruction]
- `M19.05` Knowledge check [assessment]
- `M19.06` Role takeaways [role guidance]
- `M19.07` Glossary [glossary]
- `M19.08` Next [transition]
- `M19.09` Sources [evidence]

#### M20. Defragmenting the People

Current PDF pages: 230-240

Current sections:

- `M20.01` Learning objectives [orientation]
- `M20.02` The org chart made the silos [instruction]
- `M20.03` From people to data [instruction]
- `M20.04` Reconnecting [instruction]
- `M20.05` Knowledge check [assessment]
- `M20.06` Role takeaways [role guidance]
- `M20.07` Glossary [glossary]
- `M20.08` Part Two complete → Part Three [instruction]
- `M20.09` Sources [evidence]

### Part III: Governance, Security and Provenance

#### M21. Data Governance from First Principles

Current PDF pages: 241-251

Current sections:

- `M21.01` Learning objectives [orientation]
- `M21.02` What governance means [instruction]
- `M21.03` The components [instruction]
- `M21.04` Governance in a utility [instruction]
- `M21.05` Knowledge check [assessment]
- `M21.06` Role takeaways [role guidance]
- `M21.07` Glossary [glossary]
- `M21.08` Next [transition]
- `M21.09` Sources [evidence]

#### M22. AI Governance: NIST AI RMF, ISO/IEC 42001, Responsible AI

Current PDF pages: 252-261

Current sections:

- `M22.01` Learning objectives [orientation]
- `M22.02` Why AI needs its own governance [instruction]
- `M22.03` NIST AI RMF [instruction]
- `M22.04` ISO/IEC 42001 [instruction]
- `M22.05` Responsible AI, bias, and equity [instruction]
- `M22.06` Knowledge check [assessment]
- `M22.07` Role takeaways [role guidance]
- `M22.08` Glossary [glossary]
- `M22.09` Next [transition]
- `M22.10` Sources [evidence]

#### M23. The ISO Standards Stack and How to Adopt It

Current PDF pages: 262-272

Current sections:

- `M23.01` Learning objectives [orientation]
- `M23.02` The stack [instruction]
- `M23.03` How they interlock [instruction]
- `M23.04` An adoption strategy [instruction]
- `M23.05` Knowledge check [assessment]
- `M23.06` Role takeaways [role guidance]
- `M23.07` Glossary [glossary]
- `M23.08` Next [transition]
- `M23.09` Sources [evidence]

#### M24. Evals: How You Measure Whether It Works

Current PDF pages: 273-282

Current sections:

- `M24.01` Learning objectives [orientation]
- `M24.02` Why evals [instruction]
- `M24.03` Building an eval [instruction]
- `M24.04` Benchmarks and their limits [instruction]
- `M24.05` Knowledge check [assessment]
- `M24.06` Role takeaways [role guidance]
- `M24.07` Glossary [glossary]
- `M24.08` Next [transition]
- `M24.09` Sources [evidence]

Proposed additions:

- `M24.P01` When not to trust the AI [partial; proposed; GA-007]
  - `M24.P01a` Sycophancy: the model mirrors your framing and validates a leading question
  - `M24.P01b` Countermeasures, don't lead, ask it to argue the opposite/steelman, ask 'what am I getting wrong?', never treat agreement as confirmation
  - `M24.P01c` Over-reliance and automation bias: skill atrophy, offloading judgment on irreversible calls
  - `M24.P01d` Calibrate trust to stakes (low = accept, high = verify or human sign-off)
  - `M24.P01e` Keep a manual baseline
  - `M24.P01f` Cross-model verification as a cheap independent check: paste the same question to a different model and see where they disagree
  - `M24.P01g` The human counterweight to the whole 'delegate to AI' arc
- `M24.P02` Reading a number without getting fooled [missing; proposed; GA-008]
  - `M24.P02a` Correlation vs causation
  - `M24.P02b` Outlier
  - `M24.P02c` Sample size ('is 12 data points enough?')
  - `M24.P02d` Base rate
  - `M24.P02e` False precision (4 decimals on garbage)
  - `M24.P02f` Average vs median vs distribution
  - `M24.P02g` 'does this chart's axis lie', truncated y-axis, cherry-picked window, dual axes
  - `M24.P02h` The numeric version of 'verify every output' for a CIO acting on an AI-made chart

#### M25. Cybersecurity for Water: CISA, NIST CSF 2.0, AWIA, WaterISAC, ISO 27001

Current PDF pages: 283-292

Current sections:

- `M25.01` Learning objectives [orientation]
- `M25.02` The threat landscape [instruction]
- `M25.03` NIST CSF 2.0 [instruction]
- `M25.04` Water-specific rules [instruction]
- `M25.05` Securing AI systems [instruction]
- `M25.06` Knowledge check [assessment]
- `M25.07` Role takeaways [role guidance]
- `M25.08` Glossary [glossary]
- `M25.09` Next [transition]
- `M25.10` Sources [evidence]

Proposed additions:

- `M25.P01` API keys and the .env file: where your secrets live [missing; proposed; GA-003]
  - `M25.P01a` An API key is a password
  - `M25.P01b` Getting one from the OpenAI/Anthropic/OpenRouter dashboard
  - `M25.P01c` The .env file, environment variables, loading a key
  - `M25.P01d` Key-in-code vs key-in-environment
  - `M25.P01e` .gitignore the .env
  - `M25.P01f` What happens when you push a key to a public repo (scanning bots drain credits)
  - `M25.P01g` Rotating/revoking a leaked key
  - `M25.P01h` Spend caps and rate limits
  - `M25.P01i` Consumer login vs API key
- `M25.P02` Get an API key without a surprise bill [duplicate; consolidate; GA-032]
  - `M25.P02a` Create an account at platform.openai.com / console.anthropic.com / openrouter.ai and find the 'API keys' page
  - `M25.P02b` Generate a key, copy it once (you can never see it again), and paste it into .env, never into a chat or into the code
  - `M25.P02c` Add a payment method and set a hard monthly usage limit / budget cap BEFORE you build anything
  - `M25.P02d` Read the usage dashboard: what one request cost, tokens in vs out, which model burned the money
  - `M25.P02e` Rotate / revoke a leaked key, and why a key pushed to a public GitHub repo gets drained within minutes (ties to .gitignore)

#### M26. AI Security and Safety: Prompt Injection, OWASP LLM Top 10

Current PDF pages: 293-301

Current sections:

- `M26.01` Learning objectives [orientation]
- `M26.02` New attack surfaces [instruction]
- `M26.03` The OWASP LLM Top 10 [instruction]
- `M26.04` Mitigations [instruction]
- `M26.05` Knowledge check [assessment]
- `M26.06` Role takeaways [role guidance]
- `M26.07` Glossary [glossary]
- `M26.08` Next [transition]
- `M26.09` Sources [evidence]

#### M27. Data Privacy, PII, and Where Your Data Goes

Current PDF pages: 302-312

Current sections:

- `M27.01` Learning objectives [orientation]
- `M27.02` Where your data goes [instruction]
- `M27.03` Privacy law and public records [instruction]
- `M27.04` Sovereignty [instruction]
- `M27.05` Knowledge check [assessment]
- `M27.06` Role takeaways [role guidance]
- `M27.07` Glossary [glossary]
- `M27.08` Next [transition]
- `M27.09` Sources [evidence]

Proposed additions:

- `M27.P01` API keys and the .env file: where your secrets live [missing; proposed; GA-003]
  - `M27.P01a` An API key is a password
  - `M27.P01b` Getting one from the OpenAI/Anthropic/OpenRouter dashboard
  - `M27.P01c` The .env file, environment variables, loading a key
  - `M27.P01d` Key-in-code vs key-in-environment
  - `M27.P01e` .gitignore the .env
  - `M27.P01f` What happens when you push a key to a public repo (scanning bots drain credits)
  - `M27.P01g` Rotating/revoking a leaked key
  - `M27.P01h` Spend caps and rate limits
  - `M27.P01i` Consumer login vs API key
- `M27.P02` Get an API key without a surprise bill [duplicate; consolidate; GA-032]
  - `M27.P02a` Create an account at platform.openai.com / console.anthropic.com / openrouter.ai and find the 'API keys' page
  - `M27.P02b` Generate a key, copy it once (you can never see it again), and paste it into .env, never into a chat or into the code
  - `M27.P02c` Add a payment method and set a hard monthly usage limit / budget cap BEFORE you build anything
  - `M27.P02d` Read the usage dashboard: what one request cost, tokens in vs out, which model burned the money
  - `M27.P02e` Rotate / revoke a leaked key, and why a key pushed to a public GitHub repo gets drained within minutes (ties to .gitignore)

Targeted enhancements:

- `ME-027` Add individual privacy mechanics: Add training controls, temporary chat, memory, connector permissions, and differences among free, paid, and API data handling.

#### M28. The AI Regulation Landscape

Current PDF pages: 313-320

Current sections:

- `M28.01` Learning objectives [orientation]
- `M28.02` The global map [instruction]
- `M28.03` The US picture [instruction]
- `M28.04` Staying current [instruction]
- `M28.05` Knowledge check [assessment]
- `M28.06` Role takeaways [role guidance]
- `M28.07` Glossary [glossary]
- `M28.08` Next [transition]
- `M28.09` Sources [evidence]

#### M29. AI Action Plans and Public-Sector Requirements

Current PDF pages: 321-331

Current sections:

- `M29.01` Learning objectives [orientation]
- `M29.02` The federal frame, and what it requires [instruction]
- `M29.03` Minimum practices for high-impact AI [instruction]
- `M29.04` Writing your action plan [instruction]
- `M29.05` Knowledge check [assessment]
- `M29.06` Role takeaways [role guidance]
- `M29.07` Glossary [glossary]
- `M29.08` Next [transition]
- `M29.09` Sources [evidence]

#### M30. Policy by Design: Writing AI and Data Policies

Current PDF pages: 332-339

Current sections:

- `M30.01` Learning objectives [orientation]
- `M30.02` Anatomy of a policy [instruction]
- `M30.03` From framework to rule [instruction]
- `M30.04` Drafting [instruction]
- `M30.05` Knowledge check [assessment]
- `M30.06` Role takeaways [role guidance]
- `M30.07` Glossary [glossary]
- `M30.08` Next [transition]
- `M30.09` Sources [evidence]

#### M31. Provenance, Trust, and Audit

Current PDF pages: 340-352

Current sections:

- `M31.01` Learning objectives [orientation]
- `M31.02` Provenance as law [instruction]
- `M31.03` Auditability [instruction]
- `M31.04` Trust as the product [instruction]
- `M31.05` Knowledge check [assessment]
- `M31.06` Role takeaways [role guidance]
- `M31.07` Glossary [glossary]
- `M31.08` Next [transition]
- `M31.09` Sources [evidence]

Proposed additions:

- `M31.P01` When not to trust the AI [partial; proposed; GA-007]
  - `M31.P01a` Sycophancy: the model mirrors your framing and validates a leading question
  - `M31.P01b` Countermeasures, don't lead, ask it to argue the opposite/steelman, ask 'what am I getting wrong?', never treat agreement as confirmation
  - `M31.P01c` Over-reliance and automation bias: skill atrophy, offloading judgment on irreversible calls
  - `M31.P01d` Calibrate trust to stakes (low = accept, high = verify or human sign-off)
  - `M31.P01e` Keep a manual baseline
  - `M31.P01f` Cross-model verification as a cheap independent check: paste the same question to a different model and see where they disagree
  - `M31.P01g` The human counterweight to the whole 'delegate to AI' arc

### Part IV: Using AI in Professional Work

#### M32. The Assistants: ChatGPT, Claude, Perplexity, Gemini, Kimi, NotebookLM

Current PDF pages: 353-365

Current sections:

- `M32.01` Learning objectives [orientation]
- `M32.02` The lineup [instruction]
- `M32.03` When to use which [instruction]
- `M32.04` Using them well & safely [instruction]
- `M32.05` Knowledge check [assessment]
- `M32.06` Role takeaways [role guidance]
- `M32.07` Glossary [glossary]
- `M32.08` Next [transition]
- `M32.09` Sources [evidence]

Proposed additions:

- `M32.P01` Set up a reusable assistant: Custom GPTs, Projects, Gems [missing; proposed; GA-009]
  - `M32.P01a` Build a Custom GPT, a ChatGPT/Claude Project, a Gemini Gem: system instructions + uploaded knowledge (SOPs, a rate ordinance, style samples) + persona
  - `M32.P01b` Canvas / Artifacts as the side-by-side editing workspace
  - `M32.P01c` Connectors wiring the assistant to Gmail/Drive
  - `M32.P01d` Re-invoking a saved assistant instead of re-pasting context every time
  - `M32.P01e` When each beats a plain chat
- `M32.P02` Drop in a spreadsheet and ask AI about it [missing; proposed; GA-010]
  - `M32.P02a` Drag a .csv/.xlsx into ChatGPT (Code Interpreter) or Claude
  - `M32.P02b` 'what's driving the spike?', 'chart monthly non-revenue water', 'find the outliers'
  - `M32.P02c` Which assistants actually crunch numbers vs just chat
  - `M32.P02d` File-size/row limits
  - `M32.P02e` It writes hidden Python for you
  - `M32.P02f` Downloading the chart / cleaned file back out
  - `M32.P02g` The honest failure mode: it silently miscomputes, re-ask, spot-check one row by hand
- `M32.P03` Use AI inside Excel and Google Sheets [missing; proposed; GA-011]
  - `M32.P03a` Copilot in Excel, Gemini in Google Sheets
  - `M32.P03b` Prompt-to-formula (VLOOKUP/XLOOKUP, SUMIFS, a pivot table)
  - `M32.P03c` 'explain this formula', 'find the error in this sheet'
  - `M32.P03d` The =formula bar, A1/$A$1 refs, CSV vs XLSX
  - `M32.P03e` AI-assisted cleanup on a real file: dedupe rows, standardize 'N. Plant' vs 'North Plant', split a stuck column, flag blanks
  - `M32.P03f` Spot-checking the AI's work, the step before any analysis
- `M32.P04` Deep research done right: NotebookLM and Perplexity, hands-on [partial; proposed; GA-012]
  - `M32.P04a` ChatGPT/Gemini/Perplexity Deep Research: the model plans, browses many sources, returns a long cited brief
  - `M32.P04b` When vs a normal chat
  - `M32.P04c` Sanity-checking its citations
  - `M32.P04d` NotebookLM end-to-end: create a notebook, upload 20+ PDFs / a Doc / a URL, grounded Q&A with inline citations, Briefing Doc / FAQ / Study Guide, Audio Overview for a commute
  - `M32.P04e` The fastest, source-grounded research win for 'a sector drowning in its own documents'
- `M32.P05` Pick the right model and know what it costs (OpenRouter) [missing; proposed; GA-013]
  - `M32.P05a` OpenRouter: one key + one endpoint to many models
  - `M32.P05b` Route by cost/latency/capability
  - `M32.P05c` Automatic fallback
  - `M32.P05d` OPENROUTER_API_KEY in .env
  - `M32.P05e` Provider key vs ChatGPT subscription
  - `M32.P05f` A dated 2026 model+pricing matrix: Claude Opus/Sonnet/Haiku, GPT-5.x, Gemini 3, Grok, DeepSeek, Llama
  - `M32.P05g` Per-1M-token input vs output pricing
  - `M32.P05h` Free/$20/$200 consumer tiers
  - `M32.P05i` Real-dollar bill intuition: output costs several times input
  - `M32.P05j` A worked 'this RAG run cost ~$X'
  - `M32.P05k` Levers (smaller model, shorter context, prompt caching, batch API)
  - `M32.P05l` Cross-model verification: paste the same question to Claude and ChatGPT, disagreement = your flag to dig in
- `M32.P06` Build your own knowledge base, and let AI handle scheduling [missing; proposed; GA-017]
  - `M32.P06a` Capture in Notion or Obsidian: folders, tags, backlinks
  - `M32.P06b` Notion AI to summarize/query the workspace
  - `M32.P06c` Point NotebookLM / a RAG bot at your Obsidian vault
  - `M32.P06d` Capture-to-retrieval as a system, not ad-hoc files, the personal analog of the enterprise ontology
  - `M32.P06e` Voice capture: phone dictation, superwhisper/Whisper, then AI cleans the transcript into a note
  - `M32.P06f` AI scheduling by name: Calendly to kill the back-and-forth, Reclaim/Motion to defend the calendar
- `M32.P07` Show AI what's in front of you: screenshots, photos, PDFs, and voice [partial; proposed; GA-018]
  - `M32.P07a` Paste a screenshot of an error message, a dashboard, or a chart and ask 'what is this / what's wrong'
  - `M32.P07b` Photograph a nameplate, a gauge, or a handwritten log and have AI transcribe it into a clean table
  - `M32.P07c` Drop a scanned or native PDF (a permit, a spec sheet, a 200-page report) and ask grounded questions of it
  - `M32.P07d` Voice mode in the phone app: talk to ChatGPT/Claude hands-free in the field, on the drive, on a walk
  - `M32.P07e` The trust check: eyeball every extracted number against the source image before you use it (ties to provenance)
- `M32.P08` Making AI part of your day, and keeping up as it changes [partial; proposed; GA-037]
  - `M32.P08a` A keep-up cadence: which changelogs/release notes/newsletters to follow
  - `M32.P08b` Test a new model the week it drops against your own handful of real tasks
  - `M32.P08c` Re-check your go-to tool quarterly ('model half-life')
  - `M32.P08d` A delegation decision rule: hand off the repeatable/low-stakes/draft-quality, keep judgment/relationships/final sign-off
  - `M32.P08e` A daily/weekly loop: triage inbox, draft, review, delegate to an agent, spot-check, built incrementally
  - `M32.P08f` The personal/SMB privacy playbook: turn off training/history, temporary chat, what 'memory' retains, what connecting Gmail/Drive exposes, free vs API data handling

#### M33. Prompt, Context, and Har&#110;ess Engineering, and Token Maxing

Current PDF pages: 366-376

Current sections:

- `M33.01` Learning objectives [orientation]
- `M33.02` Prompt engineering [instruction]
- `M33.03` Context engineering [instruction]
- `M33.04` Har&#110;ess engineering [instruction]
- `M33.05` Token maxing [instruction]
- `M33.06` Knowledge check [assessment]
- `M33.07` Role takeaways [role guidance]
- `M33.08` Glossary [glossary]
- `M33.09` Next [transition]
- `M33.10` Sources [evidence]

Targeted enhancements:

- `ME-033` Strengthen prompt, context, and har&#110;ess engineering: Add a copy-ready prompt skeleton, reasoning-model guidance, anti-hallucination controls, current context-window examples, and model-selection heuristics.

#### M34. Skills That Write Your Prompts

Current PDF pages: 377-392

Current sections:

- `M34.01` Learning objectives [orientation]
- `M34.02` What a prompt-writing skill is [instruction]
- `M34.03` Messy idea in, clean prompt out [instruction]
- `M34.04` The eight skills [instruction]
- `M34.05` Get the starter pack [instruction]
- `M34.06` Watch the stack build a prompt [instruction]
- `M34.07` Do this, not that [instruction]
- `M34.08` The rules your library carries [instruction]
- `M34.09` Role takeaways [role guidance]
- `M34.10` Glossary [glossary]
- `M34.11` Knowledge check [assessment]
- `M34.12` Your capstone [work product]
- `M34.13` Sources [evidence]

#### M35. Fine-Tune vs. RAG vs. Prompt: The Decision Framework

Current PDF pages: 393-402

Current sections:

- `M35.01` Learning objectives [orientation]
- `M35.02` Three ways to specialize [instruction]
- `M35.03` The decision framework [instruction]
- `M35.04` Combining them [instruction]
- `M35.05` Knowledge check [assessment]
- `M35.06` Role takeaways [role guidance]
- `M35.07` Glossary [glossary]
- `M35.08` Next [transition]
- `M35.09` Sources [evidence]

#### M36. Research, Writing, and Voice

Current PDF pages: 403-414

Current sections:

- `M36.01` Learning objectives [orientation]
- `M36.02` Research done right [instruction]
- `M36.03` Writing [instruction]
- `M36.04` Voice & humanizing [instruction]
- `M36.05` Knowledge check [assessment]
- `M36.06` Role takeaways [role guidance]
- `M36.07` Glossary [glossary]
- `M36.08` Next [transition]
- `M36.09` Sources [evidence]

Proposed additions:

- `M36.P01` Reading a number without getting fooled [missing; proposed; GA-008]
  - `M36.P01a` Correlation vs causation
  - `M36.P01b` Outlier
  - `M36.P01c` Sample size ('is 12 data points enough?')
  - `M36.P01d` Base rate
  - `M36.P01e` False precision (4 decimals on garbage)
  - `M36.P01f` Average vs median vs distribution
  - `M36.P01g` 'does this chart's axis lie', truncated y-axis, cherry-picked window, dual axes
  - `M36.P01h` The numeric version of 'verify every output' for a CIO acting on an AI-made chart
- `M36.P02` Drop in a spreadsheet and ask AI about it [missing; proposed; GA-010]
  - `M36.P02a` Drag a .csv/.xlsx into ChatGPT (Code Interpreter) or Claude
  - `M36.P02b` 'what's driving the spike?', 'chart monthly non-revenue water', 'find the outliers'
  - `M36.P02c` Which assistants actually crunch numbers vs just chat
  - `M36.P02d` File-size/row limits
  - `M36.P02e` It writes hidden Python for you
  - `M36.P02f` Downloading the chart / cleaned file back out
  - `M36.P02g` The honest failure mode: it silently miscomputes, re-ask, spot-check one row by hand
- `M36.P03` Deep research done right: NotebookLM and Perplexity, hands-on [partial; proposed; GA-012]
  - `M36.P03a` ChatGPT/Gemini/Perplexity Deep Research: the model plans, browses many sources, returns a long cited brief
  - `M36.P03b` When vs a normal chat
  - `M36.P03c` Sanity-checking its citations
  - `M36.P03d` NotebookLM end-to-end: create a notebook, upload 20+ PDFs / a Doc / a URL, grounded Q&A with inline citations, Briefing Doc / FAQ / Study Guide, Audio Overview for a commute
  - `M36.P03e` The fastest, source-grounded research win for 'a sector drowning in its own documents'
- `M36.P04` Build your own knowledge base, and let AI handle scheduling [missing; proposed; GA-017]
  - `M36.P04a` Capture in Notion or Obsidian: folders, tags, backlinks
  - `M36.P04b` Notion AI to summarize/query the workspace
  - `M36.P04c` Point NotebookLM / a RAG bot at your Obsidian vault
  - `M36.P04d` Capture-to-retrieval as a system, not ad-hoc files, the personal analog of the enterprise ontology
  - `M36.P04e` Voice capture: phone dictation, superwhisper/Whisper, then AI cleans the transcript into a note
  - `M36.P04f` AI scheduling by name: Calendly to kill the back-and-forth, Reclaim/Motion to defend the calendar
- `M36.P05` Getting found: SEO, showing up in AI answers, and basic analytics [missing; proposed; GA-029]
  - `M36.P05a` Classic SEO: keyword research, meta title/description, alt text, headings, sitemap.xml, robots.txt, Google Search Console, page speed
  - `M36.P05b` GEO/AEO, getting cited inside ChatGPT, Perplexity, Google AI Overviews: schema/structured-data markup, an llms.txt file, being the quotable source
  - `M36.P05c` Content analytics: GA4 basics, UTM parameters, traffic/engagement/conversion, open/click rate
  - `M36.P05d` Use AI to read a report and say what to do next
  - `M36.P05e` Wire it to the Module 38 site

#### M37. Image, Vision, and Media Generation

Current PDF pages: 415-426

Current sections:

- `M37.01` Learning objectives [orientation]
- `M37.02` Generating [instruction]
- `M37.03` Vision analysis [instruction]
- `M37.04` Ethics & rights [instruction]
- `M37.05` Knowledge check [assessment]
- `M37.06` Role takeaways [role guidance]
- `M37.07` Glossary [glossary]
- `M37.08` Next [transition]
- `M37.09` Sources [evidence]

Proposed additions:

- `M37.P01` Make audio, video, and finished graphics with AI [partial; proposed; GA-014]
  - `M37.P01a` Audio: text-to-speech + voice cloning (ElevenLabs), music/jingles (Suno, Udio), NotebookLM Audio Overview, dubbing, realtime voice (ChatGPT Advanced Voice, Gemini Live)
  - `M37.P01b` Video: text-to-video vs image-to-video (Sora, Veo 3, Runway Gen-4, Kling, Pika)
  - `M37.P01c` Prompt for motion/camera
  - `M37.P01d` 9:16 vs 16:9
  - `M37.P01e` Clip length
  - `M37.P01f` Credit cost
  - `M37.P01g` Talking-avatar (HeyGen, Synthesia)
  - `M37.P01h` The current image matrix (Midjourney, Flux, Ideogram, Firefly)
  - `M37.P01i` Design for non-designers: Canva templates + Brand Kit + Magic Studio
  - `M37.P01j` A one-pager/deck/social graphic
  - `M37.P01k` The disclosure rule for public utility comms

#### M38. Workflows and Automations: Email, Calendars, Scheduling, Chatbots

Current PDF pages: 427-441

Current sections:

- `M38.01` Learning objectives [orientation]
- `M38.02` Automation basics [instruction]
- `M38.03` Personal automations [instruction]
- `M38.04` Your own chatbot [instruction]
- `M38.05` Knowledge check [assessment]
- `M38.06` Role takeaways [role guidance]
- `M38.07` Glossary [glossary]
- `M38.08` Next [transition]
- `M38.09` Sources [evidence]

Proposed additions:

- `M38.P01` Build one real automation, start to finish [partial; proposed; GA-015]
  - `M38.P01a` Create a Zapier or N8N
  - `M38.P01b` A Gmail 'new email' trigger
  - `M38.P01c` The OAuth 'allow access' authorize screen and permission scopes
  - `M38.P01d` An AI action step (OpenAI/Claude) that summarizes/drafts
  - `M38.P01e` A Filter so it only fires on the right mail
  - `M38.P01f` A Test
  - `M38.P01g` Reading the run log
  - `M38.P01h` Toggle On
  - `M38.P01i` What an integration vs an API key actually is
  - `M38.P01j` Where a personal automation stores its secrets
  - `M38.P01k` Revoking a connection
  - `M38.P01l` Webhooks
  - `M38.P01m` From inbox to a ranked to-do list: push action items into Todoist/ClickUp/To Do
- `M38.P02` Turn a meeting into notes, decisions, and action items [missing; proposed; GA-016]
  - `M38.P02a` An AI notetaker (Otter, Fireflies, Granola, Fathom, Zoom AI Companion, Teams/Copilot) joins a council or vendor call
  - `M38.P02b` Raw transcript to structured minutes, a decisions list, and owner-tagged action items
  - `M38.P02c` Draft the follow-up email
  - `M38.P02d` Push the action items + contact update into a CRM via Zapier/n8n (close the meeting-to-follow-up loop)
  - `M38.P02e` The bot-joins-the-call mechanics and the accuracy/privacy caveats of recording others
- `M38.P03` Build your own knowledge base, and let AI handle scheduling [missing; proposed; GA-017]
  - `M38.P03a` Capture in Notion or Obsidian: folders, tags, backlinks
  - `M38.P03b` Notion AI to summarize/query the workspace
  - `M38.P03c` Point NotebookLM / a RAG bot at your Obsidian vault
  - `M38.P03d` Capture-to-retrieval as a system, not ad-hoc files, the personal analog of the enterprise ontology
  - `M38.P03e` Voice capture: phone dictation, superwhisper/Whisper, then AI cleans the transcript into a note
  - `M38.P03f` AI scheduling by name: Calendly to kill the back-and-forth, Reclaim/Motion to defend the calendar
- `M38.P04` A support setup: a website chatbot, ticket sorting, and a voice line [partial; proposed; GA-038]
  - `M38.P04a` Ingest your docs/FAQ into a knowledge base
  - `M38.P04b` Wire a grounded bot (Chatbase/Voiceflow or a custom RAG app)
  - `M38.P04c` Paste the <script> embed into index.html
  - `M38.P04d` Set the human-escalation handoff
  - `M38.P04e` Test live
  - `M38.P04f` Support-ticket triage: an AI classifier tags topic + urgency + sentiment and routes the frustrated/complex ones to a human
  - `M38.P04g` A voice agent (Vapi/Retell) for call deflection ('why is my bill high', 'when is water back on'), always a path to a person
  - `M38.P04h` Multilingual outbound: detect, translate, keep a human review gate for high-stakes messages, the equity requirement Module 59 names

### Part V: Building AI Systems

#### M39. No-Code and Low-Code Building: Lovable, Bolt, Replit, Vector Shift

Current PDF pages: 442-455

Current sections:

- `M39.01` Learning objectives [orientation]
- `M39.02` The no-code/low-code shift [instruction]
- `M39.03` Building in Lovable [instruction]
- `M39.04` The alternatives [instruction]
- `M39.05` Ship it [instruction]
- `M39.06` Knowledge check [assessment]
- `M39.07` Role takeaways [role guidance]
- `M39.08` Glossary [glossary]
- `M39.09` Next [transition]
- `M39.10` Sources [evidence]

Proposed additions:

- `M39.P01` Reading a number without getting fooled [missing; proposed; GA-008]
  - `M39.P01a` Correlation vs causation
  - `M39.P01b` Outlier
  - `M39.P01c` Sample size ('is 12 data points enough?')
  - `M39.P01d` Base rate
  - `M39.P01e` False precision (4 decimals on garbage)
  - `M39.P01f` Average vs median vs distribution
  - `M39.P01g` 'does this chart's axis lie', truncated y-axis, cherry-picked window, dual axes
  - `M39.P01h` The numeric version of 'verify every output' for a CIO acting on an AI-made chart
- `M39.P02` What a web app really is: files, index.html, and localhost [missing; proposed; GA-020]
  - `M39.P02a` A project folder
  - `M39.P02b` Index.html as the entry point the browser opens
  - `M39.P02c` Static files (HTML/CSS/JS) vs assets
  - `M39.P02d` Building one static page by hand (or one Claude writes) and opening it in a browser
  - `M39.P02e` Localhost and localhost:3000
  - `M39.P02f` What a port is
  - `M39.P02g` Npm run dev / the dev server
  - `M39.P02h` Why the app 'dies' when you close the terminal
  - `M39.P02i` Refresh to see changes
  - `M39.P02j` Anatomy of a Lovable/Bolt export
- `M39.P03` Turn an idea into a plan: a simple PRD, user stories, a sitemap [missing; proposed; GA-021]
  - `M39.P03a` Discovery / problem-framing: jobs-to-be-done, a one-page problem brief (who hurts, how often, what it costs, what 'solved' looks like), decide whether to build at all
  - `M39.P03b` Write a PRD / build brief: the problem, the user, the screens, the data, the one thing it must do
  - `M39.P03c` In-scope vs out-of-scope
  - `M39.P03d` Acceptance criteria
  - `M39.P03e` User stories ('as a field crew member I want to...'), the user flow (screen to screen), a sitemap of pages
  - `M39.P03f` Have Claude/ChatGPT turn a rough idea into a structured PRD you paste into the builder as the opening prompt
- `M39.P04` Sketch it first: wireframes in Figma and your own diagram [missing; proposed; GA-022]
  - `M39.P04a` Wireframe (lo-fi boxes) vs mockup (hi-fi)
  - `M39.P04b` Figma / FigJam frames and components
  - `M39.P04c` Sketch screens first, then prompt the builder from the picture
  - `M39.P04d` Figma-to-code: paste a screenshot into Lovable/Bolt, Figma Make, v0 from an image
  - `M39.P04e` Draw your OWN architecture / data-flow diagram: components, where the model sits, where data lives, Excalidraw, draw.io, Mermaid (```mermaid fences), or ask Claude to generate one
  - `M39.P04f` The diagram doubles as a patent figure and a spec for a developer
- `M39.P05` From no-code to code, plus basic design and user testing [partial; proposed; GA-023]
  - `M39.P05a` When a project outgrows no-code: export/connect the Lovable app to a GitHub repo, open it in Cursor/Claude Code, harden it
  - `M39.P05b` UX fundamentals for non-designers: visual hierarchy, whitespace, one primary action per screen, mobile-responsive
  - `M39.P05c` Prompt for it ('make this responsive', 'clearer hierarchy')
  - `M39.P05d` Real user testing: put the MVP in front of an operator/field crew, watch them use it, capture feedback, iterate
  - `M39.P05e` The seam that gets you to a patentable, deployable system
- `M39.P06` Getting found: SEO, showing up in AI answers, and basic analytics [missing; proposed; GA-029]
  - `M39.P06a` Classic SEO: keyword research, meta title/description, alt text, headings, sitemap.xml, robots.txt, Google Search Console, page speed
  - `M39.P06b` GEO/AEO, getting cited inside ChatGPT, Perplexity, Google AI Overviews: schema/structured-data markup, an llms.txt file, being the quotable source
  - `M39.P06c` Content analytics: GA4 basics, UTM parameters, traffic/engagement/conversion, open/click rate
  - `M39.P06d` Use AI to read a report and say what to do next
  - `M39.P06e` Wire it to the Module 38 site
- `M39.P07` Give your app a real web address: a domain, DNS, and HTTPS [missing; proposed; GA-030]
  - `M39.P07a` Buy a domain at Namecheap / Cloudflare / GoDaddy
  - `M39.P07b` What .com vs .ai costs and the auto-renewal price trap
  - `M39.P07c` The only DNS records you actually touch: an A record (points to an IP / DigitalOcean droplet) and a CNAME (points to vercel/netlify), and what 'propagation / TTL' means when it doesn't work yet
  - `M39.P07d` Attach the domain to your deploy: 'Add custom domain' in Vercel/Netlify, or set the A record on the droplet from Module 42
  - `M39.P07e` Free HTTPS/SSL (Let's Encrypt / auto-provisioned) and why the padlock matters for a government buyer
  - `M39.P07f` Stand up you@yourdomain email and where MX records live
  - `M39.P07g` Read a 'site won't load' failure: nameservers not switched, wrong record, browser/DNS cache
- `M39.P08` From prototype to real product: logins and a real database [missing; proposed; GA-031]
  - `M39.P08a` What a relational database is in plain terms, tables, rows, columns, and how it differs from the vector/graph DBs taught for RAG
  - `M39.P08b` Stand up a free Postgres in Supabase
  - `M39.P08c` Create a table
  - `M39.P08d` Add and read a row from the dashboard
  - `M39.P08e` Add sign-up / log-in with Supabase Auth or Clerk: email+password, magic link, 'Sign in with Google'
  - `M39.P08f` Wire the front end to the database
  - `M39.P08g` Put the DB URL and service key in .env (ties to the secrets item), never in the code
  - `M39.P08h` Row-level security so user A can't read user B's rows, the beginner mistake that leaks everyone's data
  - `M39.P08i` When you actually need a backend vs. when Airtable or a Google Sheet is enough

#### M40. Building With AI: Claude Code, Skills, Codex, the IDE, Vibe → Agentic

Current PDF pages: 456-472

Current sections:

- `M40.01` Learning objectives [orientation]
- `M40.02` The AI-assisted IDE [instruction]
- `M40.03` Claude Code, Skills, Codex [instruction]
- `M40.04` Vibe to agentic engineering [instruction]
- `M40.05` Knowledge check [assessment]
- `M40.06` Role takeaways [role guidance]
- `M40.07` Glossary [glossary]
- `M40.08` Next [transition]
- `M40.09` Sources [evidence]

Proposed additions:

- `M40.P01` The terminal, from zero [missing; proposed; GA-001]
  - `M40.P01a` Opening Terminal (Mac) / PowerShell (Windows)
  - `M40.P01b` Reading the prompt
  - `M40.P01c` Cd, ls, pwd, mkdir, mv, cp, rm, cat, open/start, clear, echo
  - `M40.P01d` Absolute vs relative paths
  - `M40.P01e` The ~ home dir
  - `M40.P01f` Tab-completion
  - `M40.P01g` Running a command vs running a script
  - `M40.P01h` Ctrl-C to stop
  - `M40.P01i` Up-arrow history
- `M40.P02` Git and GitHub: the actual commands [missing; proposed; GA-002]
  - `M40.P02a` Git init, status, add, commit -m, log, push, pull, clone
  - `M40.P02b` Making a GitHub account and a repo
  - `M40.P02c` The remote (origin)
  - `M40.P02d` The first push
  - `M40.P02e` Branches and a pull request in plain terms
  - `M40.P02f` .gitignore and why API keys / .env never get committed
- `M40.P03` API keys and the .env file: where your secrets live [missing; proposed; GA-003]
  - `M40.P03a` An API key is a password
  - `M40.P03b` Getting one from the OpenAI/Anthropic/OpenRouter dashboard
  - `M40.P03c` The .env file, environment variables, loading a key
  - `M40.P03d` Key-in-code vs key-in-environment
  - `M40.P03e` .gitignore the .env
  - `M40.P03f` What happens when you push a key to a public repo (scanning bots drain credits)
  - `M40.P03g` Rotating/revoking a leaked key
  - `M40.P03h` Spend caps and rate limits
  - `M40.P03i` Consumer login vs API key
- `M40.P04` Your code editor: install Cursor or VS Code, and read code you didn't write [missing; proposed; GA-004]
  - `M40.P04a` Installing VS Code or Cursor
  - `M40.P04b` Opening a project folder
  - `M40.P04c` The file tree
  - `M40.P04d` The integrated terminal
  - `M40.P04e` Cursor's AI chat and inline edit
  - `M40.P04f` Running the project from the editor
  - `M40.P04g` Reading a file top to bottom: recognizing a function, variable, import, if/loop
  - `M40.P04h` HTML vs CSS vs JS
  - `M40.P04i` Asking the AI to explain a file in plain language before you change it
- `M40.P05` Install a project's parts, and get a download to actually run [missing; proposed; GA-005]
  - `M40.P05a` What a package/library is
  - `M40.P05b` Npm install and pip install
  - `M40.P05c` Package.json / requirements.txt
  - `M40.P05d` The node_modules folder
  - `M40.P05e` A Python virtual environment (venv) and why versions get pinned
  - `M40.P05f` 'installing dependencies', the step that blocks running any cloned repo
- `M40.P06` Read an error and fix it [missing; proposed; GA-006]
  - `M40.P06a` Reading a stack trace: finding the error type and the line number
  - `M40.P06b` Pasting the error into Claude/Cursor to fix it
  - `M40.P06c` Print/console debugging
  - `M40.P06d` The browser DevTools console
  - `M40.P06e` The everyday errors: module not found, port already in use, syntax error, missing key
  - `M40.P06f` Module 39 warns AI code 'can be quietly wrong' but never teaches reading what the machine says
- `M40.P07` What a web app really is: files, index.html, and localhost [missing; proposed; GA-020]
  - `M40.P07a` A project folder
  - `M40.P07b` Index.html as the entry point the browser opens
  - `M40.P07c` Static files (HTML/CSS/JS) vs assets
  - `M40.P07d` Building one static page by hand (or one Claude writes) and opening it in a browser
  - `M40.P07e` Localhost and localhost:3000
  - `M40.P07f` What a port is
  - `M40.P07g` Npm run dev / the dev server
  - `M40.P07h` Why the app 'dies' when you close the terminal
  - `M40.P07i` Refresh to see changes
  - `M40.P07j` Anatomy of a Lovable/Bolt export
- `M40.P08` From no-code to code, plus basic design and user testing [partial; proposed; GA-023]
  - `M40.P08a` When a project outgrows no-code: export/connect the Lovable app to a GitHub repo, open it in Cursor/Claude Code, harden it
  - `M40.P08b` UX fundamentals for non-designers: visual hierarchy, whitespace, one primary action per screen, mobile-responsive
  - `M40.P08c` Prompt for it ('make this responsive', 'clearer hierarchy')
  - `M40.P08d` Real user testing: put the MVP in front of an operator/field crew, watch them use it, capture feedback, iterate
  - `M40.P08e` The seam that gets you to a patentable, deployable system
- `M40.P09` Get an API key without a surprise bill [duplicate; consolidate; GA-032]
  - `M40.P09a` Create an account at platform.openai.com / console.anthropic.com / openrouter.ai and find the 'API keys' page
  - `M40.P09b` Generate a key, copy it once (you can never see it again), and paste it into .env, never into a chat or into the code
  - `M40.P09c` Add a payment method and set a hard monthly usage limit / budget cap BEFORE you build anything
  - `M40.P09d` Read the usage dashboard: what one request cost, tokens in vs out, which model burned the money
  - `M40.P09e` Rotate / revoke a leaked key, and why a key pushed to a public GitHub repo gets drained within minutes (ties to .gitignore)
- `M40.P10` Actually build with an AI coding agent [partial; proposed; GA-033]
  - `M40.P10a` Give the agent real context: open the folder/repo, point it at the right files, state the goal AND the constraints (not a one-line prompt)
  - `M40.P10b` Plan-then-edit: ask for a plan first, approve it, then let it write
  - `M40.P10c` Read the diff before you accept it
  - `M40.P10d` Commit as save-points so you can `git revert` the moment the agent breaks a working app (ties to the Git lab)
  - `M40.P10e` Paste the actual error back until it's fixed
  - `M40.P10f` Recognize when to stop and start a fresh context instead of arguing
  - `M40.P10g` Rules/convention files so the agent stays on your patterns
  - `M40.P10h` When to hand a task to no-code vs. write code

#### M41. Agents, Agentic Nests, and Orchestration

Current PDF pages: 473-486

Current sections:

- `M41.01` Learning objectives [orientation]
- `M41.02` What an agent is [instruction]
- `M41.03` Multi-agent & nests [instruction]
- `M41.04` Connecting tools & the framework landscape [instruction]
- `M41.05` Risk & the hype discount [instruction]
- `M41.06` Knowledge check [assessment]
- `M41.07` Role takeaways [role guidance]
- `M41.08` Glossary [glossary]
- `M41.09` Next [transition]
- `M41.10` Sources [evidence]

Proposed additions:

- `M41.P01` Agents for real: connect a tool (MCP) and try computer-use [partial; proposed; GA-025]
  - `M41.P01a` Install/enable an MCP server
  - `M41.P01b` Edit the config (Claude Desktop / .mcp.json)
  - `M41.P01c` Local vs remote MCP
  - `M41.P01d` Connectors to Gmail/Drive/Slack
  - `M41.P01e` Test the tool shows up
  - `M41.P01f` The agent-builder landscape, dated: n8n vs Zapier vs Make (a chooser), and the code frameworks (LangGraph, CrewAI) + vendor SDKs (OpenAI Agents SDK, Claude Agent SDK)
  - `M41.P01g` Computer-use / browser agents: OpenAI Operator, Anthropic computer-use, Claude-for-Chrome, what they do, why they're fragile, the human-in-the-loop rule for live systems

#### M42. Open vs. Closed Models and Running Locally

Current PDF pages: 487-499

Current sections:

- `M42.01` Learning objectives [orientation]
- `M42.02` Open vs. closed [instruction]
- `M42.03` Running locally [instruction]
- `M42.04` Why a utility might self-host [instruction]
- `M42.05` Knowledge check [assessment]
- `M42.06` Role takeaways [role guidance]
- `M42.07` Glossary [glossary]
- `M42.08` Next [transition]
- `M42.09` Sources [evidence]

Proposed additions:

- `M42.P01` Run your own AI locally: Ollama and LM Studio [partial; proposed; GA-024]
  - `M42.P01a` Installing Ollama
  - `M42.P01b` Ollama pull llama3, ollama run
  - `M42.P01c` The local API at localhost:11434
  - `M42.P01d` LM Studio's GUI as the no-terminal option
  - `M42.P01e` Picking a model and a quant (GGUF, 7B vs 70B)
  - `M42.P01f` Real hardware sizing: how much RAM/VRAM per model size
  - `M42.P01g` Pointing your app at the local model instead of a cloud API, the SoulOS Module 41 increment

#### M43. The Infrastructure: Containers, Docker, DigitalOcean, Deployment, Scaling Laws

Current PDF pages: 500-517

Current sections:

- `M43.01` Learning objectives [orientation]
- `M43.02` Containers [instruction]
- `M43.03` Deploying [instruction]
- `M43.04` Compute, scaling laws & cost [instruction]
- `M43.05` Knowledge check [assessment]
- `M43.06` Role takeaways [role guidance]
- `M43.07` Glossary [glossary]
- `M43.08` Next [transition]
- `M43.09` Sources [evidence]

Proposed additions:

- `M43.P01` API keys and the .env file: where your secrets live [missing; proposed; GA-003]
  - `M43.P01a` An API key is a password
  - `M43.P01b` Getting one from the OpenAI/Anthropic/OpenRouter dashboard
  - `M43.P01c` The .env file, environment variables, loading a key
  - `M43.P01d` Key-in-code vs key-in-environment
  - `M43.P01e` .gitignore the .env
  - `M43.P01f` What happens when you push a key to a public repo (scanning bots drain credits)
  - `M43.P01g` Rotating/revoking a leaked key
  - `M43.P01h` Spend caps and rate limits
  - `M43.P01i` Consumer login vs API key
- `M43.P02` Install a project's parts, and get a download to actually run [missing; proposed; GA-005]
  - `M43.P02a` What a package/library is
  - `M43.P02b` Npm install and pip install
  - `M43.P02c` Package.json / requirements.txt
  - `M43.P02d` The node_modules folder
  - `M43.P02e` A Python virtual environment (venv) and why versions get pinned
  - `M43.P02f` 'installing dependencies', the step that blocks running any cloned repo
- `M43.P03` Pick the right model and know what it costs (OpenRouter) [missing; proposed; GA-013]
  - `M43.P03a` OpenRouter: one key + one endpoint to many models
  - `M43.P03b` Route by cost/latency/capability
  - `M43.P03c` Automatic fallback
  - `M43.P03d` OPENROUTER_API_KEY in .env
  - `M43.P03e` Provider key vs ChatGPT subscription
  - `M43.P03f` A dated 2026 model+pricing matrix: Claude Opus/Sonnet/Haiku, GPT-5.x, Gemini 3, Grok, DeepSeek, Llama
  - `M43.P03g` Per-1M-token input vs output pricing
  - `M43.P03h` Free/$20/$200 consumer tiers
  - `M43.P03i` Real-dollar bill intuition: output costs several times input
  - `M43.P03j` A worked 'this RAG run cost ~$X'
  - `M43.P03k` Levers (smaller model, shorter context, prompt caching, batch API)
  - `M43.P03l` Cross-model verification: paste the same question to Claude and ChatGPT, disagreement = your flag to dig in
- `M43.P04` What a web app really is: files, index.html, and localhost [missing; proposed; GA-020]
  - `M43.P04a` A project folder
  - `M43.P04b` Index.html as the entry point the browser opens
  - `M43.P04c` Static files (HTML/CSS/JS) vs assets
  - `M43.P04d` Building one static page by hand (or one Claude writes) and opening it in a browser
  - `M43.P04e` Localhost and localhost:3000
  - `M43.P04f` What a port is
  - `M43.P04g` Npm run dev / the dev server
  - `M43.P04h` Why the app 'dies' when you close the terminal
  - `M43.P04i` Refresh to see changes
  - `M43.P04j` Anatomy of a Lovable/Bolt export
- `M43.P05` Put it online: from your computer to a live link [partial; proposed; GA-026]
  - `M43.P05a` Publish a Lovable/Bolt app and point a custom domain at it
  - `M43.P05b` A one-click deploy (Vercel/Netlify)
  - `M43.P05c` A Dockerfile, docker build / docker run
  - `M43.P05d` SSH into a DigitalOcean droplet
  - `M43.P05e` Setting env vars in production (not the .env you kept local)
  - `M43.P05f` Dev vs staging vs production
  - `M43.P05g` The step that comes after running it on your own machine
- `M43.P06` What your app costs to run, and how to price it [partial; proposed; GA-028]
  - `M43.P06a` Input vs output token pricing
  - `M43.P06b` Read a model's pricing page
  - `M43.P06c` Estimate a monthly API bill
  - `M43.P06d` Cost-per-active-user
  - `M43.P06e` What a DigitalOcean droplet runs
  - `M43.P06f` Turn 'tokens are the meter' into a real spreadsheet forecast as usage grows
  - `M43.P06g` Price the product: subscription tiers, per-seat vs usage, gross margin after API/infra cost, a break-even 'how many customers do I need'
  - `M43.P06h` Use AI to draft and pressure-test pricing options
- `M43.P07` Give your app a real web address: a domain, DNS, and HTTPS [missing; proposed; GA-030]
  - `M43.P07a` Buy a domain at Namecheap / Cloudflare / GoDaddy
  - `M43.P07b` What .com vs .ai costs and the auto-renewal price trap
  - `M43.P07c` The only DNS records you actually touch: an A record (points to an IP / DigitalOcean droplet) and a CNAME (points to vercel/netlify), and what 'propagation / TTL' means when it doesn't work yet
  - `M43.P07d` Attach the domain to your deploy: 'Add custom domain' in Vercel/Netlify, or set the A record on the droplet from Module 42
  - `M43.P07e` Free HTTPS/SSL (Let's Encrypt / auto-provisioned) and why the padlock matters for a government buyer
  - `M43.P07f` Stand up you@yourdomain email and where MX records live
  - `M43.P07g` Read a 'site won't load' failure: nameservers not switched, wrong record, browser/DNS cache
- `M43.P08` From prototype to real product: logins and a real database [missing; proposed; GA-031]
  - `M43.P08a` What a relational database is in plain terms, tables, rows, columns, and how it differs from the vector/graph DBs taught for RAG
  - `M43.P08b` Stand up a free Postgres in Supabase
  - `M43.P08c` Create a table
  - `M43.P08d` Add and read a row from the dashboard
  - `M43.P08e` Add sign-up / log-in with Supabase Auth or Clerk: email+password, magic link, 'Sign in with Google'
  - `M43.P08f` Wire the front end to the database
  - `M43.P08g` Put the DB URL and service key in .env (ties to the secrets item), never in the code
  - `M43.P08h` Row-level security so user A can't read user B's rows, the beginner mistake that leaks everyone's data
  - `M43.P08i` When you actually need a backend vs. when Airtable or a Google Sheet is enough
- `M43.P09` Get an API key without a surprise bill [duplicate; consolidate; GA-032]
  - `M43.P09a` Create an account at platform.openai.com / console.anthropic.com / openrouter.ai and find the 'API keys' page
  - `M43.P09b` Generate a key, copy it once (you can never see it again), and paste it into .env, never into a chat or into the code
  - `M43.P09c` Add a payment method and set a hard monthly usage limit / budget cap BEFORE you build anything
  - `M43.P09d` Read the usage dashboard: what one request cost, tokens in vs out, which model burned the money
  - `M43.P09e` Rotate / revoke a leaked key, and why a key pushed to a public GitHub repo gets drained within minutes (ties to .gitignore)
- `M43.P10` Build a dashboard and ask your data in plain English [missing; proposed; GA-039]
  - `M43.P10a` A no-code dashboard: connect a Google Sheet/CSV/database in Looker Studio, Power BI, or Metabase
  - `M43.P10b` Drag a field, pick a chart, add a filter, publish a shareable link, auto-refresh
  - `M43.P10c` Ask your database in plain English: text-to-SQL, connect an assistant/tool to a real table (CIS, GL, CMMS, historian)
  - `M43.P10d` Read the generated SQL before trusting it
  - `M43.P10e` Read-only, never UPDATE/DELETE
  - `M43.P10f` Choosing the right chart (trend=line, distribution=histogram) and reading a misleading one
  - `M43.P10g` Insight to recommendation: a one-page decision memo with the evidence, the caveats, and what would change your mind

#### M44. Innovation and Patents: Writing Patents With AI

Current PDF pages: 518-529

Current sections:

- `M44.01` Learning objectives [orientation]
- `M44.02` Innovation research [instruction]
- `M44.03` Patent basics [instruction]
- `M44.04` Drafting with AI [instruction]
- `M44.05` Knowledge check [assessment]
- `M44.06` Role takeaways [role guidance]
- `M44.07` Glossary [glossary]
- `M44.08` Next [transition]
- `M44.09` Sources [evidence]

Proposed additions:

- `M44.P01` Sketch it first: wireframes in Figma and your own diagram [missing; proposed; GA-022]
  - `M44.P01a` Wireframe (lo-fi boxes) vs mockup (hi-fi)
  - `M44.P01b` Figma / FigJam frames and components
  - `M44.P01c` Sketch screens first, then prompt the builder from the picture
  - `M44.P01d` Figma-to-code: paste a screenshot into Lovable/Bolt, Figma Make, v0 from an image
  - `M44.P01e` Draw your OWN architecture / data-flow diagram: components, where the model sits, where data lives, Excalidraw, draw.io, Mermaid (```mermaid fences), or ask Claude to generate one
  - `M44.P01f` The diagram doubles as a patent figure and a spec for a developer

### Part VI: Role-Based Practice

#### M45. The Operator and Administrator

Current PDF pages: 530-543

Current sections:

- `M45.01` Learning objectives [orientation]
- `M45.02` AI at the desk and the plant [instruction]
- `M45.03` Capturing what's in your head [instruction]
- `M45.04` Safety and judgment [instruction]
- `M45.05` Knowledge check [assessment]
- `M45.06` Role takeaways [role guidance]
- `M45.07` Glossary [glossary]
- `M45.08` Next [transition]
- `M45.09` Sources [evidence]

Proposed additions:

- `M45.P01` Show AI what's in front of you: screenshots, photos, PDFs, and voice [partial; proposed; GA-018]
  - `M45.P01a` Paste a screenshot of an error message, a dashboard, or a chart and ask 'what is this / what's wrong'
  - `M45.P01b` Photograph a nameplate, a gauge, or a handwritten log and have AI transcribe it into a clean table
  - `M45.P01c` Drop a scanned or native PDF (a permit, a spec sheet, a 200-page report) and ask grounded questions of it
  - `M45.P01d` Voice mode in the phone app: talk to ChatGPT/Claude hands-free in the field, on the drive, on a walk
  - `M45.P01e` The trust check: eyeball every extracted number against the source image before you use it (ties to provenance)
- `M45.P02` A support setup: a website chatbot, ticket sorting, and a voice line [partial; proposed; GA-038]
  - `M45.P02a` Ingest your docs/FAQ into a knowledge base
  - `M45.P02b` Wire a grounded bot (Chatbase/Voiceflow or a custom RAG app)
  - `M45.P02c` Paste the <script> embed into index.html
  - `M45.P02d` Set the human-escalation handoff
  - `M45.P02e` Test live
  - `M45.P02f` Support-ticket triage: an AI classifier tags topic + urgency + sentiment and routes the frustrated/complex ones to a human
  - `M45.P02g` A voice agent (Vapi/Retell) for call deflection ('why is my bill high', 'when is water back on'), always a path to a person
  - `M45.P02h` Multilingual outbound: detect, translate, keep a human review gate for high-stakes messages, the equity requirement Module 59 names

#### M46. The Manager

Current PDF pages: 544-556

Current sections:

- `M46.01` Learning objectives [orientation]
- `M46.02` Leading adoption [instruction]
- `M46.03` Connecting the work [instruction]
- `M46.04` Managing risk and quality [instruction]
- `M46.05` Knowledge check [assessment]
- `M46.06` Role takeaways [role guidance]
- `M46.07` Glossary [glossary]
- `M46.08` Next [transition]
- `M46.09` Sources [evidence]

Proposed additions:

- `M46.P01` Turn a meeting into notes, decisions, and action items [missing; proposed; GA-016]
  - `M46.P01a` An AI notetaker (Otter, Fireflies, Granola, Fathom, Zoom AI Companion, Teams/Copilot) joins a council or vendor call
  - `M46.P01b` Raw transcript to structured minutes, a decisions list, and owner-tagged action items
  - `M46.P01c` Draft the follow-up email
  - `M46.P01d` Push the action items + contact update into a CRM via Zapier/n8n (close the meeting-to-follow-up loop)
  - `M46.P01e` The bot-joins-the-call mechanics and the accuracy/privacy caveats of recording others
- `M46.P02` Run the money with AI: a simple model, a dashboard, bookkeeping, contracts, HR [missing; proposed; GA-036]
  - `M46.P02a` Build a 12-month P&L, a cash-flow/runway projection, and unit economics in a sheet with AI doing the formulas
  - `M46.P02b` What a P&L / balance sheet / cash-flow statement even are
  - `M46.P02c` A board-ready KPI scorecard/dashboard from a messy export (Google Sheets / Looker Studio) + an AI-drafted executive summary
  - `M46.P02d` Bookkeeping/month-end: generate and chase invoices, categorize/reconcile transactions, QuickBooks, expense capture from receipts
  - `M46.P02e` Review a contract/NDA/MSA with AI: flag auto-renewal traps, liability caps, IP/data-rights, where legal review stays mandatory
  - `M46.P02f` HR with AI: job descriptions, resume screening, structured interview questions, offer letters, with the fair-hiring cautions

#### M47. The Executive

Current PDF pages: 557-567

Current sections:

- `M47.01` Learning objectives [orientation]
- `M47.02` Setting strategy [instruction]
- `M47.03` Organizational readiness (McKinsey 7S) [instruction]
- `M47.04` Governing the program [instruction]
- `M47.05` Knowledge check [assessment]
- `M47.06` Role takeaways [role guidance]
- `M47.07` Glossary [glossary]
- `M47.08` Next [transition]
- `M47.09` Sources [evidence]

Proposed additions:

- `M47.P01` Run the money with AI: a simple model, a dashboard, bookkeeping, contracts, HR [missing; proposed; GA-036]
  - `M47.P01a` Build a 12-month P&L, a cash-flow/runway projection, and unit economics in a sheet with AI doing the formulas
  - `M47.P01b` What a P&L / balance sheet / cash-flow statement even are
  - `M47.P01c` A board-ready KPI scorecard/dashboard from a messy export (Google Sheets / Looker Studio) + an AI-drafted executive summary
  - `M47.P01d` Bookkeeping/month-end: generate and chase invoices, categorize/reconcile transactions, QuickBooks, expense capture from receipts
  - `M47.P01e` Review a contract/NDA/MSA with AI: flag auto-renewal traps, liability caps, IP/data-rights, where legal review stays mandatory
  - `M47.P01f` HR with AI: job descriptions, resume screening, structured interview questions, offer letters, with the fair-hiring cautions
- `M47.P02` Build a dashboard and ask your data in plain English [missing; proposed; GA-039]
  - `M47.P02a` A no-code dashboard: connect a Google Sheet/CSV/database in Looker Studio, Power BI, or Metabase
  - `M47.P02b` Drag a field, pick a chart, add a filter, publish a shareable link, auto-refresh
  - `M47.P02c` Ask your database in plain English: text-to-SQL, connect an assistant/tool to a real table (CIS, GL, CMMS, historian)
  - `M47.P02d` Read the generated SQL before trusting it
  - `M47.P02e` Read-only, never UPDATE/DELETE
  - `M47.P02f` Choosing the right chart (trend=line, distribution=histogram) and reading a misleading one
  - `M47.P02g` Insight to recommendation: a one-page decision memo with the evidence, the caveats, and what would change your mind

#### M48. The Elected Official: Mayors, Council, Commissioners

Current PDF pages: 568-579

Current sections:

- `M48.01` Learning objectives [orientation]
- `M48.02` What you need to know [instruction]
- `M48.03` Funding and governance [instruction]
- `M48.04` The questions to ask [instruction]
- `M48.05` Knowledge check [assessment]
- `M48.06` Role takeaways [role guidance]
- `M48.07` Glossary [glossary]
- `M48.08` Next [transition]
- `M48.09` Sources [evidence]

#### M49. The Consultant

Current PDF pages: 580-588

Current sections:

- `M49.01` Learning objectives [orientation]
- `M49.02` The advisor role [instruction]
- `M49.03` AI-augmented delivery [instruction]
- `M49.04` Ethics and value [instruction]
- `M49.05` Knowledge check [assessment]
- `M49.06` Role takeaways [role guidance]
- `M49.07` Glossary [glossary]
- `M49.08` Next [transition]
- `M49.09` Sources [evidence]

Proposed additions:

- `M49.P01` Win the work: AI for RFP responses and grant writing [partial; proposed; GA-035]
  - `M49.P01a` Point AI at a government RFP PDF, extract the requirements matrix, draft grounded responses from a reusable proof library, assemble a proposal, with provenance so nothing is fabricated
  - `M49.P01b` A pricing sheet and a compliance matrix against the solicitation
  - `M49.P01c` Grant/funding writing: read a NOFO, check eligibility, build the budget narrative + table, draft grounded in the funder's criteria
  - `M49.P01d` SRF and federal infrastructure money
  - `M49.P01e` The sell-side mirror of Module 62's buy-side procurement
- `M49.P02` Run the money with AI: a simple model, a dashboard, bookkeeping, contracts, HR [missing; proposed; GA-036]
  - `M49.P02a` Build a 12-month P&L, a cash-flow/runway projection, and unit economics in a sheet with AI doing the formulas
  - `M49.P02b` What a P&L / balance sheet / cash-flow statement even are
  - `M49.P02c` A board-ready KPI scorecard/dashboard from a messy export (Google Sheets / Looker Studio) + an AI-drafted executive summary
  - `M49.P02d` Bookkeeping/month-end: generate and chase invoices, categorize/reconcile transactions, QuickBooks, expense capture from receipts
  - `M49.P02e` Review a contract/NDA/MSA with AI: flag auto-renewal traps, liability caps, IP/data-rights, where legal review stays mandatory
  - `M49.P02f` HR with AI: job descriptions, resume screening, structured interview questions, offer letters, with the fair-hiring cautions

#### M50. The Vendor: AI-Driven Sales, Marketing, Customer Service, Lead Management

Current PDF pages: 589-603

Current sections:

- `M50.01` Learning objectives [orientation]
- `M50.02` Know the buyer [instruction]
- `M50.03` AI go-to-market [instruction]
- `M50.04` Customer service, honestly [instruction]
- `M50.05` Knowledge check [assessment]
- `M50.06` Role takeaways [role guidance]
- `M50.07` Glossary [glossary]
- `M50.08` Next [transition]
- `M50.09` Sources [evidence]

Proposed additions:

- `M50.P01` What your app costs to run, and how to price it [partial; proposed; GA-028]
  - `M50.P01a` Input vs output token pricing
  - `M50.P01b` Read a model's pricing page
  - `M50.P01c` Estimate a monthly API bill
  - `M50.P01d` Cost-per-active-user
  - `M50.P01e` What a DigitalOcean droplet runs
  - `M50.P01f` Turn 'tokens are the meter' into a real spreadsheet forecast as usage grows
  - `M50.P01g` Price the product: subscription tiers, per-seat vs usage, gross margin after API/infra cost, a break-even 'how many customers do I need'
  - `M50.P01h` Use AI to draft and pressure-test pricing options
- `M50.P02` Getting found: SEO, showing up in AI answers, and basic analytics [missing; proposed; GA-029]
  - `M50.P02a` Classic SEO: keyword research, meta title/description, alt text, headings, sitemap.xml, robots.txt, Google Search Console, page speed
  - `M50.P02b` GEO/AEO, getting cited inside ChatGPT, Perplexity, Google AI Overviews: schema/structured-data markup, an llms.txt file, being the quotable source
  - `M50.P02c` Content analytics: GA4 basics, UTM parameters, traffic/engagement/conversion, open/click rate
  - `M50.P02d` Use AI to read a report and say what to do next
  - `M50.P02e` Wire it to the Module 38 site
- `M50.P03` Set up your sales engine: a CRM, lead capture, and outreach [partial; proposed; GA-034]
  - `M50.P03a` Stand up a free HubSpot (or Pipedrive): pipeline stages, deals, contacts, companies, import a CSV, deal-stage automation
  - `M50.P03b` A lead-capture landing page/form (Lovable/Framer or index.html + a form service) that routes submissions into the CRM with an auto-reply
  - `M50.P03c` A nurture/drip sequence
  - `M50.P03d` Lead scoring (fit + intent rubric, AI classifies and routes hot/warm/cold)
- `M50.P04` Run the money with AI: a simple model, a dashboard, bookkeeping, contracts, HR [missing; proposed; GA-036]
  - `M50.P04a` Build a 12-month P&L, a cash-flow/runway projection, and unit economics in a sheet with AI doing the formulas
  - `M50.P04b` What a P&L / balance sheet / cash-flow statement even are
  - `M50.P04c` A board-ready KPI scorecard/dashboard from a messy export (Google Sheets / Looker Studio) + an AI-drafted executive summary
  - `M50.P04d` Bookkeeping/month-end: generate and chase invoices, categorize/reconcile transactions, QuickBooks, expense capture from receipts
  - `M50.P04e` Review a contract/NDA/MSA with AI: flag auto-renewal traps, liability caps, IP/data-rights, where legal review stays mandatory
  - `M50.P04f` HR with AI: job descriptions, resume screening, structured interview questions, offer letters, with the fair-hiring cautions

#### M51. The CIO, CISO, and Chief AI Officer: The Summit

Current PDF pages: 604-617

Current sections:

- `M51.01` Learning objectives [orientation]
- `M51.02` The governance seat [instruction]
- `M51.03` The security seat [instruction]
- `M51.04` The architecture seat [instruction]
- `M51.05` Leading the program [instruction]
- `M51.06` Knowledge check [assessment]
- `M51.07` Role takeaways [role guidance]
- `M51.08` Glossary [glossary]
- `M51.09` Next [transition]
- `M51.10` Sources [evidence]

### Part VII: The Human Layer and Capstones

#### M52. Change Management and Adoption

Current PDF pages: 618-627

Current sections:

- `M52.01` Learning objectives [orientation]
- `M52.02` Why adoption fails [instruction]
- `M52.03` The 7S lens on change [instruction]
- `M52.04` Workforce transition [instruction]
- `M52.05` Knowledge check [assessment]
- `M52.06` Role takeaways [role guidance]
- `M52.07` Glossary [glossary]
- `M52.08` Next [transition]
- `M52.09` Sources [evidence]

Proposed additions:

- `M52.P01` Making AI part of your day, and keeping up as it changes [partial; proposed; GA-037]
  - `M52.P01a` A keep-up cadence: which changelogs/release notes/newsletters to follow
  - `M52.P01b` Test a new model the week it drops against your own handful of real tasks
  - `M52.P01c` Re-check your go-to tool quarterly ('model half-life')
  - `M52.P01d` A delegation decision rule: hand off the repeatable/low-stakes/draft-quality, keep judgment/relationships/final sign-off
  - `M52.P01e` A daily/weekly loop: triage inbox, draft, review, delegate to an agent, spot-check, built incrementally
  - `M52.P01f` The personal/SMB privacy playbook: turn off training/history, temporary chat, what 'memory' retains, what connecting Gmail/Drive exposes, free vs API data handling

#### M53. The Capstone Studio

Current PDF pages: 628-643

Current sections:

- `M53.01` Learning objectives [orientation]
- `M53.02` Portfolio assembly [instruction]
- `M53.03` Presentation [instruction]
- `M53.04` Reflection [instruction]
- `M53.05` Knowledge check [assessment]
- `M53.06` Role takeaways [role guidance]
- `M53.07` Glossary [glossary]
- `M53.08` Next [transition]
- `M53.09` Sources [evidence]

Proposed additions:

- `M53.P01` Git and GitHub: the actual commands [missing; proposed; GA-002]
  - `M53.P01a` Git init, status, add, commit -m, log, push, pull, clone
  - `M53.P01b` Making a GitHub account and a repo
  - `M53.P01c` The remote (origin)
  - `M53.P01d` The first push
  - `M53.P01e` Branches and a pull request in plain terms
  - `M53.P01f` .gitignore and why API keys / .env never get committed
- `M53.P02` Turn an idea into a plan: a simple PRD, user stories, a sitemap [missing; proposed; GA-021]
  - `M53.P02a` Discovery / problem-framing: jobs-to-be-done, a one-page problem brief (who hurts, how often, what it costs, what 'solved' looks like), decide whether to build at all
  - `M53.P02b` Write a PRD / build brief: the problem, the user, the screens, the data, the one thing it must do
  - `M53.P02c` In-scope vs out-of-scope
  - `M53.P02d` Acceptance criteria
  - `M53.P02e` User stories ('as a field crew member I want to...'), the user flow (screen to screen), a sitemap of pages
  - `M53.P02f` Have Claude/ChatGPT turn a rough idea into a structured PRD you paste into the builder as the opening prompt
- `M53.P03` From no-code to code, plus basic design and user testing [partial; proposed; GA-023]
  - `M53.P03a` When a project outgrows no-code: export/connect the Lovable app to a GitHub repo, open it in Cursor/Claude Code, harden it
  - `M53.P03b` UX fundamentals for non-designers: visual hierarchy, whitespace, one primary action per screen, mobile-responsive
  - `M53.P03c` Prompt for it ('make this responsive', 'clearer hierarchy')
  - `M53.P03d` Real user testing: put the MVP in front of an operator/field crew, watch them use it, capture feedback, iterate
  - `M53.P03e` The seam that gets you to a patentable, deployable system
- `M53.P04` What your app costs to run, and how to price it [partial; proposed; GA-028]
  - `M53.P04a` Input vs output token pricing
  - `M53.P04b` Read a model's pricing page
  - `M53.P04c` Estimate a monthly API bill
  - `M53.P04d` Cost-per-active-user
  - `M53.P04e` What a DigitalOcean droplet runs
  - `M53.P04f` Turn 'tokens are the meter' into a real spreadsheet forecast as usage grows
  - `M53.P04g` Price the product: subscription tiers, per-seat vs usage, gross margin after API/infra cost, a break-even 'how many customers do I need'
  - `M53.P04h` Use AI to draft and pressure-test pricing options
- `M53.P05` Making AI part of your day, and keeping up as it changes [partial; proposed; GA-037]
  - `M53.P05a` A keep-up cadence: which changelogs/release notes/newsletters to follow
  - `M53.P05b` Test a new model the week it drops against your own handful of real tasks
  - `M53.P05c` Re-check your go-to tool quarterly ('model half-life')
  - `M53.P05d` A delegation decision rule: hand off the repeatable/low-stakes/draft-quality, keep judgment/relationships/final sign-off
  - `M53.P05e` A daily/weekly loop: triage inbox, draft, review, delegate to an agent, spot-check, built incrementally
  - `M53.P05f` The personal/SMB privacy playbook: turn off training/history, temporary chat, what 'memory' retains, what connecting Gmail/Drive exposes, free vs API data handling

### Part VIII: AI Across the Water Lifecycle

#### M54. Leak & Burst Detection and Non-Revenue Water

Current PDF pages: 644-653

Current sections:

- `M54.01` Learning objectives [orientation]
- `M54.02` The NRW problem [instruction]
- `M54.03` AI detection methods [instruction]
- `M54.04` Detection to action [instruction]
- `M54.05` Knowledge check [assessment]
- `M54.06` Role takeaways [role guidance]
- `M54.07` Glossary [glossary]
- `M54.08` Next [transition]
- `M54.09` Sources [evidence]

#### M55. Predictive & Condition-Based Maintenance and Asset Management (EAM)

Current PDF pages: 654-662

Current sections:

- `M55.01` Learning objectives [orientation]
- `M55.02` The maintenance spectrum [instruction]
- `M55.03` AI for prediction [instruction]
- `M55.04` Asset management & capital [instruction]
- `M55.05` Knowledge check [assessment]
- `M55.06` Role takeaways [role guidance]
- `M55.07` Glossary [glossary]
- `M55.08` Next [transition]
- `M55.09` Sources [evidence]

#### M56. Treatment & Process Optimization

Current PDF pages: 663-676

Current sections:

- `M56.01` Learning objectives [orientation]
- `M56.02` The process [instruction]
- `M56.03` AI optimization [instruction]
- `M56.04` Safety and control [instruction]
- `M56.05` Knowledge check [assessment]
- `M56.06` Role takeaways [role guidance]
- `M56.07` Glossary [glossary]
- `M56.08` Next [transition]
- `M56.09` Sources [evidence]

#### M57. Demand Forecasting and Hydraulic/Network Modeling

Current PDF pages: 677-690

Current sections:

- `M57.01` Learning objectives [orientation]
- `M57.02` Demand forecasting [instruction]
- `M57.03` Hydraulic modeling + AI [instruction]
- `M57.04` Applications [instruction]
- `M57.05` Knowledge check [assessment]
- `M57.06` Role takeaways [role guidance]
- `M57.07` Glossary [glossary]
- `M57.08` Next [transition]
- `M57.09` Sources [evidence]

#### M58. Stormwater, CSO/SSO and Flood/Overflow Prediction

Current PDF pages: 691-704

Current sections:

- `M58.01` Learning objectives [orientation]
- `M58.02` The problem [instruction]
- `M58.03` Prediction [instruction]
- `M58.04` Compliance link [instruction]
- `M58.05` Knowledge check [assessment]
- `M58.06` Role takeaways [role guidance]
- `M58.07` Glossary [glossary]
- `M58.08` Next [transition]
- `M58.09` Sources [evidence]

#### M59. Regulatory Compliance, Reporting & Consent-Decree Management

Current PDF pages: 705-718

Current sections:

- `M59.01` Learning objectives [orientation]
- `M59.02` The regulatory load [instruction]
- `M59.03` AI for compliance [instruction]
- `M59.04` Provenance for regulators [instruction]
- `M59.05` Knowledge check [assessment]
- `M59.06` Role takeaways [role guidance]
- `M59.07` Glossary [glossary]
- `M59.08` Next [transition]
- `M59.09` Sources [evidence]

#### M60. Customer, Billing/CIS & Community Engagement

Current PDF pages: 719-732

Current sections:

- `M60.01` Learning objectives [orientation]
- `M60.02` Customer service [instruction]
- `M60.03` Billing and CIS [instruction]
- `M60.04` Community and equity [instruction]
- `M60.05` Knowledge check [assessment]
- `M60.06` Role takeaways [role guidance]
- `M60.07` Glossary [glossary]
- `M60.08` Next [transition]
- `M60.09` Sources [evidence]

Proposed additions:

- `M60.P01` A support setup: a website chatbot, ticket sorting, and a voice line [partial; proposed; GA-038]
  - `M60.P01a` Ingest your docs/FAQ into a knowledge base
  - `M60.P01b` Wire a grounded bot (Chatbase/Voiceflow or a custom RAG app)
  - `M60.P01c` Paste the <script> embed into index.html
  - `M60.P01d` Set the human-escalation handoff
  - `M60.P01e` Test live
  - `M60.P01f` Support-ticket triage: an AI classifier tags topic + urgency + sentiment and routes the frustrated/complex ones to a human
  - `M60.P01g` A voice agent (Vapi/Retell) for call deflection ('why is my bill high', 'when is water back on'), always a path to a person
  - `M60.P01h` Multilingual outbound: detect, translate, keep a human review gate for high-stakes messages, the equity requirement Module 59 names

#### M61. Digital Twins and the Decision Twin

Current PDF pages: 733-743

Current sections:

- `M61.01` Learning objectives [orientation]
- `M61.02` What a twin is [instruction]
- `M61.03` Digital twin vs. Decision Twin [instruction]
- `M61.04` Value vs. hype [instruction]
- `M61.05` Knowledge check [assessment]
- `M61.06` Role takeaways [role guidance]
- `M61.07` Glossary [glossary]
- `M61.08` Next [transition]
- `M61.09` Sources [evidence]

#### M62. AI Sustainability: The Water & Energy Footprint of AI

Current PDF pages: 744-758

Current sections:

- `M62.01` Learning objectives [orientation]
- `M62.02` The footprint [instruction]
- `M62.03` Why water utilities should care [instruction]
- `M62.04` Greener choices [instruction]
- `M62.05` Knowledge check [assessment]
- `M62.06` Role takeaways [role guidance]
- `M62.07` Glossary [glossary]
- `M62.08` Next [transition]
- `M62.09` Sources [evidence]

#### M63. Buying AI: Procurement & Vendor Evaluation

Current PDF pages: 759-769

Current sections:

- `M63.01` Learning objectives [orientation]
- `M63.02` Evaluating claims [instruction]
- `M63.03` RFPs and requirements [instruction]
- `M63.04` Contracting [instruction]
- `M63.05` Knowledge check [assessment]
- `M63.06` Role takeaways [role guidance]
- `M63.07` Glossary [glossary]
- `M63.08` The content is complete [instruction]
- `M63.09` Sources [evidence]

Proposed additions:

- `M63.P01` Win the work: AI for RFP responses and grant writing [partial; proposed; GA-035]
  - `M63.P01a` Point AI at a government RFP PDF, extract the requirements matrix, draft grounded responses from a reusable proof library, assemble a proposal, with provenance so nothing is fabricated
  - `M63.P01b` A pricing sheet and a compliance matrix against the solicitation
  - `M63.P01c` Grant/funding writing: read a NOFO, check eligibility, build the budget narrative + table, draft grounded in the funder's criteria
  - `M63.P01d` SRF and federal infrastructure money
  - `M63.P01e` The sell-side mirror of Module 62's buy-side procurement

## Revision history

| Date | Version | Change |
| --- | --- | --- |
| 2026-08-04 | 0.1 | Established the stable granular hierarchy and mapped the uploaded gap analysis against the current 64 modules and 684-page curriculum. |
