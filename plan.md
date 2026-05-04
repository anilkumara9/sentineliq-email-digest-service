Capstone Project

# **Tool-110 — Email Digest Service**


Capstone Tool | Team: Team: 5 Members


Sprint: Monday 14 April 2026 — Friday 9 May 2026 | Demo Day: 9 May 2026


**[!] READ THIS DOCUMENT COMPLETELY BEFORE WRITING A SINGLE LINE OF CODE.** This is your
complete project guide — what to build, the full tech stack, exact folder structure, every task broken down day
by day, GitHub submission steps, Demo Day checklist, and the 8 most common mistakes. Read it twice.


**1. PROJECT OVERVIEW**


You are building **Tool-110 — Email Digest Service** as your internship capstone project. This is a real-world,
AI-powered web application built using an industry-standard tech stack. It will be the strongest item on your resume
when you graduate.

|Tool ID|Tool-110|
|---|---|
|**Tool Name**|Email Digest Service|
|**Tool Type**|Capstone — Focused Tool|
|**Team**|Team: 5 Members|
|**Sprint**|Monday 14 April – Friday 9 May 2026 (20 working days)|
|**Demo Day**|Friday 9 May 2026 — 6-minute live presentation|
|**Backend Port**|8080 | Swagger: http://localhost:8080/swagger-ui.html|
|**AI Port**|5000 | Health: http://localhost:5000/health|
|**Frontend Port**|80 | Access: http://localhost|
|**Repository**|Link will be shared by your mentor before Day 1|



Tool-110 — Email Digest Service | Page 1


**2. TECH STACK**


Use this exact stack. Do not change it. Before Day 2 read the getting-started docs for any technology you are
unfamiliar with: spring.io/guides, console.groq.com/docs, docs.trychroma.com, react.dev, tailwindcss.com,
docs.docker.com/compose.

|Technology|What It Does in This Project|
|---|---|
|**Java 17**|Backend language. Download from adoptium.net|
|**Spring Boot 3.x**|Java framework — REST APIs, security, scheduling|
|**PostgreSQL 15**|Primary database. Run inside Docker|
|**Redis 7**|In-memory cache and AI response cache|
|**Flyway**|DB migrations — every schema change in a numbered SQL file|
|**Spring Security + JWT**|Login and role-based access control|
|**Python 3.11**|AI service language|
|**Flask 3.x**|Python web framework — AI microservice on port 5000|
|**Groq API (LLaMA-3.3-70b)**|AI model — free tier at console.groq.com, no credit card|
|**flask-limiter**|Rate limiting — blocks IPs exceeding 30 req/min|
|**React 18 + Vite**|Frontend framework with fast build tool|
|**Tailwind CSS**|Utility CSS — style with class names|
|**Axios**|HTTP client for React to call the Java backend|
|**Docker + Docker Compose**|Runs all services with one command: docker-compose up|



Tool-110 — Email Digest Service | Page 2


**3. FOLDER STRUCTURE — Create This on Day 1**


Create all folders on Day 1 before writing any code. Use this exact layout throughout the sprint.

```
 your-project-folder/
 |-- backend/ <- Spring Boot project
 | |-- src/main/java/com/internship/tool/
 | | |-- controller/ <- REST endpoints
 | | |-- service/ <- Business logic
 | | |-- repository/ <- DB queries
 | | |-- entity/ <- JPA table models
 | | |-- config/ <- Security, Redis, Mail
 | | +-- exception/ <- Custom exceptions
 | |-- src/main/resources/
 | | |-- db/migration/ <- V1__init.sql, V2__...
 | | +-- application.yml <- All config (env variable references)
 | +-- pom.xml
 |
 |-- ai-service/ <- Flask Python microservice
 | |-- routes/ <- endpoint files
 | |-- services/ <- groq_client.py
 | |-- prompts/ <- prompt template text files
 | |-- app.py
 | |-- Dockerfile
 | +-- requirements.txt
 |
 |-- frontend/ <- React + Vite frontend
 | |-- src/
 | | |-- components/
 | | |-- pages/
 | | |-- services/
 | | +-- App.jsx
 | +-- package.json
 |
 |-- docker-compose.yml
 |-- .env.example
 +-- README.md

```

Tool-110 — Email Digest Service | Page 3


**4. TEAM ROLES**


Your mentor will coordinate teams and guide progress. Each role below has a clear set of responsibilities for the
full sprint.

|Role|Responsibilities|
|---|---|
|**Java Developer 1**|Spring Boot setup, Service layer, JWT auth, Docker Compose, data seeder, README.md,<br>opens Demo Day.|
|**Java Developer 2**|DB schema (Flyway), Repository layer, full React frontend, email notifications, demo video.|
|**AI Developer 1**|Flask setup, prompt templates, /describe and /recommend endpoints, AiServiceClient.java.|
|**AI Developer 2**|GroqClient, /generate-report, security review, prompt tuning, AI docs, AI talking points.|
|**Security Reviewer**|Security testing, validates fixes, presents security features on Demo Day (if assigned).|



**Your Team**

|Member|Role|Contact|
|---|---|---|
|**Member 1**|Role will be confirmed by your mentor before Day 1|Contact your mentor for team WhatsApp<br>group details|
|**Member 2**|Role will be confirmed by your mentor before Day 1|Contact your mentor for team WhatsApp<br>group details|
|**Member 3**|Role will be confirmed by your mentor before Day 1|Contact your mentor for team WhatsApp<br>group details|
|**Member 4**|Role will be confirmed by your mentor before Day 1|Contact your mentor for team WhatsApp<br>group details|
|**Member 5**|Role will be confirmed by your mentor before Day 1|Contact your mentor for team WhatsApp<br>group details|



Tool-110 — Email Digest Service | Page 4


**5. DAY-BY-DAY TASK BREAKDOWN (20 Working Days)**


Each row is one task for one role on one specific day. Complete it fully before end of that working day. If blocked,
tell your team immediately — do not stay stuck silently. Update your status daily: **Not Started** → **In Progress** →
**Completed** → **Blocked**




[YEL] Week 1:
Foundation




[ORN] Week 2: Core
Features [BLU] Week 3: Polish




[GRN] Week 4: Demo
Prep




[PUR] Day 20: Demo
Day







|Day|Date|Track|Role|Task — Complete This Fully Today|Status|
|---|---|---|---|---|---|
|**Day 1**|**Mon Apr**<br>**14**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|
|||**Java**|Java Developer 1|Setup Spring Boot — folder structure, pom.xml,<br>application.yml with ${ENV_VAR} placeholders for DB,<br>Redis, mail, JWT|Not Started|
|||**Java**|Java Developer 2|Write Flyway V1 migration — core table with all required<br>columns, correct types, indexes on key fields|Not Started|
|||**AI**|AI Developer 1|Setup Flask — routes/, services/, prompts/ folders,<br>requirements.txt, app.py entry point|Completed|
|||**AI**|AI Developer 2|Get Groq API key at console.groq.com, store in .env, write<br>test_groq.py and confirm API call works|Not Started|
|**Day 2**|**Tue Apr**<br>**15**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|
|||**Java**|Java Developer 1|Create JPA Entity and Repository — all fields, @Column,<br>@CreatedDate/@LastModifiedDate, custom query methods|Not Started|
|||**Java**|Java Developer 2|Setup React with Vite — install Axios and Tailwind, set API<br>base URL, create pages/ components/ services/ folders|Not Started|
|||**AI**|AI Developer 1|Write primary prompt template — test with 5 real inputs,<br>refine until all 5 outputs are consistently good|Completed|
|||**AI**|AI Developer 2|Implement GroqClient — API call, JSON parsing, 3-retry with<br>backoff, error logging. Create SECURITY.md with 5 threats|Not Started|
|**Day 3**|**Wed Apr**<br>**16**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|
|||**Java**|Java Developer 1|Implement Service layer — business logic, input validation,<br>custom exception classes for each error type|Not Started|
|||**Java**|Java Developer 2|Build list page — table, Axios GET on mount, loading state,<br>empty state. Write Flyway V2 migration for audit_log|Not Started|
|||**AI**|AI Developer 1|Build POST /describe — validate input, load prompt, call<br>Groq, return structured JSON with generated_at|Completed|
|||**AI**|AI Developer 2|Add input sanitisation middleware — strip HTML, detect<br>prompt injection, return 400. Add flask-limiter 30 req/min|Not Started|
|**Day 4**|**Thu Apr**<br>**17**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|
|||**Java**|Java Developer 1|Build REST Controller — GET /all paginated, GET /{id} with<br>404, POST /create with @Valid, all correct status codes|Not Started|


Tool-110 — Email Digest Service | Page 5




|Col1|Col2|Java|Java Developer 2|Build REST — PUT /{id}, DELETE (soft), GET /search?q=.<br>Build create/edit form with validation in React|Not Started|
|---|---|---|---|---|---|
|||**AI**|AI Developer 1|Build POST /recommend — 3 recommendations as JSON<br>array, each with action_type, description, priority|Completed|
|||**AI**|AI Developer 2|Write AiServiceClient.java — RestTemplate calls to all Flask<br>endpoints, 10s timeout, null return on error|Not Started|
|**Day 5**|**Fri Apr**<br>**18**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|**— Week 1 —**|
|||**Java**|Java Developer 1|JWT auth — JwtUtil, JwtAuthFilter, SecurityConfig. Build<br>AuthController: /login, /register, /refresh|Not Started|
|||**Java**|Java Developer 2|React login page — AuthContext, ProtectedRoute, connect<br>list page to real GET /all API with pagination|Not Started|
|||**AI**|AI Developer 1|Integrate AiServiceClient into Service — call AI on create<br>@Async, attach result, handle null gracefully|Completed|
|||**AI**|AI Developer 2|Week 1 security test — empty input, SQL injection, prompt<br>injection on all endpoints. Document in SECURITY.md|Not Started|
|**Day 6**|**Mon Apr**<br>**21**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|
|||**Java**|Java Developer 1|Redis caching — @Cacheable on GETs (10 min TTL),<br>@CacheEvict on writes. RBAC with @PreAuthorize on<br>endpoints|Not Started|
|||**Java**|Java Developer 2|Dashboard — 4 KPI cards from /stats, Recharts chart. Detail<br>page with score badge, Edit/Delete buttons|Not Started|
|||**AI**|AI Developer 1|Build POST /generate-report — structured JSON with title,<br>summary, overview, key items, recommendations|Completed|
|||**AI**|AI Developer 2|Prompt tuning — 10 real inputs per prompt, score accuracy,<br>rewrite any scoring below 7/10|Not Started|
|**Day 7**|**Tue Apr**<br>**22**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|
|||**Java**|Java Developer 1|Email notifications — JavaMailSender, Thymeleaf templates,<br>@Scheduled daily reminder and deadline alert|Not Started|
|||**Java**|Java Developer 2|Search/filter bar — debounced search, status dropdown,<br>date range. Audit logging via Spring AOP on CUD methods|Not Started|
|||**AI**|AI Developer 1|Build GET /health — model, avg response time, uptime. Add<br>Redis AI cache — SHA256 key, 15 min TTL|Completed|
|||**AI**|AI Developer 2|Run OWASP ZAP scan — export report, fix all Critical<br>findings today, plan Medium fixes|Not Started|
|**Day 8**|**Wed Apr**<br>**23**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|
|||**Java**|Java Developer 1|@ControllerAdvice — 404/400/500 consistent JSON. 10<br>JUnit 5 unit tests for Service with Mockito|Not Started|
|||**Java**|Java Developer 2|MockMvc tests — all endpoints, correct status codes. AI<br>panel in UI — loading spinner, formatted response card|Not Started|
|||**AI**|AI Developer 1|Fix all ZAP findings — add security headers, re-scan<br>confirms zero Critical/High remaining|Not Started|


Tool-110 — Email Digest Service | Page 6


|Col1|Col2|AI|AI Developer 2|Write 8 pytest unit tests — mock Groq, test each endpoint<br>format, error handling, injection rejection|Not Started|
|---|---|---|---|---|---|
|**Day 9**|**Thu Apr**<br>**24**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|
|||**Java**|Java Developer 1|docker-compose.yml — all 5 services, healthchecks, test<br>with docker-compose up --build|Not Started|
|||**Java**|Java Developer 2|Swagger/OpenAPI on all endpoints. Add GET /export CSV.<br>File upload POST /upload with type and size validation|Not Started|
|||**AI**|AI Developer 1|Final AI optimisation — all endpoints under 2s average,<br>fallback template on Groq error ({is_fallback: true})|Not Started|
|||**AI**|AI Developer 2|Week 2 security sign-off — JWT, rate limit, injection all<br>verified. PII audit confirms no personal data in prompts|Not Started|
|**Day**<br>**10**|**Fri Apr**<br>**25**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|**— Week 2 —**|
|||**Java**|Java Developer 1|Full integration test — docker-compose down -v then up,<br>walk every feature, fix all bugs found|Not Started|
|||**Java**|Java Developer 2|Data seeder — 15 realistic demo records on startup.<br>Analytics page with Recharts charts and period selector|Not Started|
|||**AI**|AI Developer 1|Write ai-service/README.md — setup, env vars, run<br>instructions, API reference with examples for all 3 endpoints|Completed|
|||**AI**|AI Developer 2|Week 2 AI quality review — 10 fresh inputs per endpoint,<br>score accuracy (target avg >= 4/5). Fix failing prompts|Not Started|
|**Day**<br>**11**|**Mon Apr**<br>**28**|**— Week 3 —**|**— Week 3 —**|**— Week 3 —**|**— Week 3 —**|
|||**Java**|Java Developer 1|Fix all Week 1-2 bugs. Additional tests to reach 80%<br>coverage. UX polish — skeletons, empty states, Error<br>Boundary|Not Started|
|||**Java**|Java Developer 2|Responsive design — 375px/768px/1280px all working.<br>Performance — EXPLAIN ANALYZE, add indexes, fix N+1|Not Started|
|||**AI**|AI Developer 1|Pre-load sentence-transformers at startup. Full ZAP active<br>scan — fix all Critical/High findings|Not Started|
|||**AI**|AI Developer 2|Full E2E test — docker-compose up, all AI integrations<br>working correctly in containerised environment|Not Started|
|**Day**<br>**12**|**Tue Apr**<br>**29**|**— Week 3 —**|**— Week 3 —**|**— Week 3 —**|**— Week 3 —**|
|||**Java**|Java Developer 1|Data seeder upgrade to 30 records. UI brand polish —<br>#1B4F8A primary, Arial font, 8px grid, 44px touch targets|Not Started|
|||**Java**|Java Developer 2|Team code review — no secrets, no TODO comments,<br>standards enforced. Final merge, tag release/v1.0|Not Started|
|||**AI**|AI Developer 1|Seed ChromaDB with 10 domain knowledge documents.<br>Run all prompts against 30 demo records — all outputs<br>demo-ready|Not Started|
|||**AI**|AI Developer 2|Final SECURITY.md — executive summary, all threats,<br>tests, findings fixed, residual risks, team sign-off|Not Started|


Tool-110 — Email Digest Service | Page 7


|Day<br>13|Wed Apr<br>30|— Week 3 —|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||**Java**|Java Developer 1|Write README.md — overview, architecture diagram,<br>prerequisites, setup steps, .env reference table|Not Started|
|||**Java**|Java Developer 2|Record 90-sec demo video — all key features with voice<br>narration, save as demo_video.mp4|Not Started|
|||**AI**|AI Developer 1|Package AI — Dockerfile builds cleanly, requirements.txt<br>exact versions, .env.example complete|Completed|
|||**AI**|AI Developer 2|Final security checklist — all 4 members sign off, commit<br>final SECURITY.md|Not Started|
|**Day**<br>**14**|**Thu May**<br>**1**|**— Week 3 —**|**— Week 3 —**|**— Week 3 —**|**— Week 3 —**|
|||**Java**|Java Developer 1|Demo Rehearsal 1 — full team, stopwatch, complete 6-min<br>presentation, note all issues|Not Started|
|||**Java**|Java Developer 2|Fix all rehearsal issues. Prepare 3 slides — problem,<br>architecture, demo flow (1 min total for slides)|Not Started|
|||**AI**|AI Developer 1|AI dry run on demo machine — all 3 endpoints live, record<br>response times, prepare backup screenshots|Not Started|
|||**AI**|AI Developer 2|Write AI demo script — exact inputs, expected outputs,<br>60-sec tech explanation for non-technical panel|Not Started|
|**Day**<br>**15**|**Fri May 2**|**— Week 3 —**|**— Week 3 —**|**— Week 3 —**|**— Week 3 —**|
|||**Java**|Java Developer 1|Submit GitHub — public, no secrets, one commit per day,<br>share link with mentor|Not Started|
|||**Java**|Java Developer 2|Fresh machine test — clone, create .env, docker-compose<br>up --build, full stack healthy|Not Started|
|||**AI**|AI Developer 1|Submit AI service GitHub link — Dockerfile builds, README<br>complete, share link with mentor|Not Started|
|||**AI**|AI Developer 2|Create 1-page AI summary card — 3 endpoints, tech stack,<br>GitHub link. Print 2 copies for Demo Day|Not Started|
|**Day**<br>**16**|**Mon May**<br>**5**|**— Week 4 —**|**— Week 4 —**|**— Week 4 —**|**— Week 4 —**|
|||**Java**|Java Developer 1|Final bug fix — zero P1/P2 remaining. 5 portfolio<br>screenshots at 1920x1080 for each key screen|Not Started|
|||**Java**|Java Developer 2|Prepare 3 demo scenarios — exact steps, expected output,<br>talking points. Confirm all work on live system|Not Started|
|||**AI**|AI Developer 1|Final performance verify — all endpoints within targets,<br>cache working, fallback working|Not Started|
|||**AI**|AI Developer 2|Print AI talking points card — Groq, prompts explained in<br>plain English. Prepare security talking points|Not Started|
|**Day**<br>**17**|**Tue May**<br>**6**|**— Week 4 —**|**— Week 4 —**|**— Week 4 —**|**— Week 4 —**|
|||**Java**|Java Developer 1|Rehearsal 2 — full team, 6 min target, every member<br>answers 5 key questions without notes|Not Started|


Tool-110 — Email Digest Service | Page 8


|Col1|Col2|Java|Java Developer 2|Final hotfix window — P1/P2 only, re-test after each fix|Not Started|
|---|---|---|---|---|---|
|||**AI**|AI Developer 1|Groq API check — key active, credits sufficient, test all 3<br>endpoints confirmed working|Not Started|
|||**AI**|AI Developer 2|docker-compose down -v then up — fresh seeded state, all<br>records visible, all scenarios confirmed|Not Started|
|**Day**<br>**18**|**Wed May**<br>**7**|**— Week 4 —**|**— Week 4 —**|**— Week 4 —**|**— Week 4 —**|
|||**Java**|Java Developer 1|Final confidence check — each member presents their<br>90-sec section solo, resolve all remaining gaps|Not Started|
|||**Java**|Java Developer 2|Submit final SECURITY.md — professional, complete,<br>accurate. Print 1 copy for Demo Day|Not Started|
|||**AI**|AI Developer 1|DEMO — Open: problem (1 sentence), architecture, launch<br>live tool. Create record, watch AI respond|Not Started|
|||**AI**|AI Developer 2|DEMO — AI Recommend, Generate Report. Explain Flask +<br>Groq in 60 seconds. Show /health endpoint|Not Started|
|**Day**<br>**19**|**Thu May**<br>**8**|**— Week 4 —**|**— Week 4 —**|**— Week 4 —**|**— Week 4 —**|
|||**Java**|Java Developer 1|DEMO — Dashboard KPIs, search/filter, CSV export, audit<br>log, email notification, responsive view|Not Started|
|||**Java**|Java Developer 2|DEMO — Security: 401 without token, 400 on injection,<br>reference SECURITY.md, state findings fixed|Not Started|
|||**AI**|AI Developer 1|Post-demo — push final code, confirm all submissions<br>complete, celebrate the sprint|Not Started|
|||**AI**|AI Developer 2|Post-demo — document lessons learned, note features for<br>future sprints, feedback to mentor|Not Started|
|**Day**<br>**20**|**Fri May 9**|**— Demo —**|**— Demo —**|**— Demo —**|**— Demo —**|
|||**Java**|Java Developer 1|DEMO — Open: problem statement, architecture slide,<br>launch live tool, CRUD demonstration|Not Started|
|||**Java**|Java Developer 2|DEMO — Show UI features: dashboard, search/filter, CSV<br>export, responsive design on mobile|Not Started|
|||**AI**|AI Developer 1|DEMO — Live AI: Describe, Recommend, Generate Report.<br>Explain what AI is doing at each step|Not Started|
|||**AI**|AI Developer 2|DEMO — Explain tech stack. Security: 401 demo, injection<br>rejection, SECURITY.md reference|Not Started|


Tool-110 — Email Digest Service | Page 9




**6. GITHUB — Push Code Every Working Day**


Push your code at the end of every working day. Your mentor will share the repository details before Day 1.







|Ste<br>p|Action|Instructions|
|---|---|---|
|1|**Create Account**|Go to github.com, click Sign Up. Use your personal email. Choose a professional<br>username.|
|2|**Create Repository**|Your mentor will share the exact repository name and URL. Set Visibility to Public. Add<br>README.|
|3|**Install Git**|Download from git-scm.com. In terminal run: git --version to confirm version 2.x or higher.|
|4|**Configure Git**|Run: git config --global user.name 'Your Name' and git config --global user.email<br>'you@email.com'|
|5|**Clone Repo**|Run: git clone [repository URL shared by mentor] then cd into the project folder|
|6|**Add .gitignore**|On Day 1, before any commit: create .gitignore and add: .env target/ node_modules/<br>__pycache__/ chroma_data/|
|7|**Daily Push**|End of every working day: git add . then git commit -m 'Day X — what you did' then git<br>push origin main|
|8|**Verify Online**|After every push: open the repository URL in your browser and confirm the latest files are<br>visible.|


**Commit message format every day: Day X — brief description of what you completed**

**Example:** Day 3 — Implemented Service layer with validation and custom exceptions


Tool-110 — Email Digest Service | Page 10


**7. DEMO DAY CHECKLIST**


Every item must be complete before your 6-minute Demo Day presentation on 9 May 2026.















|Deliverable|What Must Be Submitted or Demonstrated|Done?|
|---|---|---|
|**GitHub Repo**|Public repo (link from mentor). At least 1 commit per working day. No secrets<br>committed.|[ ]|
|**README.md**|Complete setup instructions. ASCII architecture diagram. Prerequisites.<br>Step-by-step setup.|[ ]|
|**docker-compose**|All services defined. Full stack starts with docker-compose up. Tested on a clean<br>machine.|[ ]|
|**Flyway**|All schema changes in numbered files (V1__, V2__, ...). No manual SQL outside<br>migrations.|[ ]|
|**JUnit Tests**|Minimum 10 tests, all passing. JaCoCo coverage >= 80%.|[ ]|
|**Pytest Tests**|Minimum 8 tests, all passing. Groq API mocked — tests run without live network<br>access.|[ ]|
|**Swagger UI**|All endpoints documented at /swagger-ui.html with request/response examples.|[ ]|
|**AI Service**|Flask app with working endpoints. Dockerfile builds. README covers setup.|[ ]|
|**SECURITY.md**|Threat model, tests conducted, findings fixed, residual risks, team sign-off.|[ ]|
|**Demo Data**|30 realistic seeded records on docker-compose up, covering all statuses and<br>ranges.|[ ]|
|**Demo Video**|demo_video.mp4: 90-120 seconds, all key features shown with clear voice<br>narration.|[ ]|


Tool-110 — Email Digest Service | Page 11




**8. DEMO DAY — Friday 9 May 2026**


You have **6 minutes.** The tool must be running live on your laptop. No slides-only presentations. Real features,
real data, live AI calls.

|Segment|Time|What to Do and Say|
|---|---|---|
|**Opening**|1 min|State the problem in one sentence. Show architecture slide. Say 'Let me show you the live<br>tool.'|
|**CRUD Demo**|2 min|Create a record live, watch AI description appear. Show audit log. Search and filter demo.|
|**AI Features**|1.5 min|Click AI Recommend (read aloud). Generate Report. Explain what the AI is doing.|
|**UI + Security**|1 min|Dashboard. CSV export. API call without JWT (show 401). Reference SECURITY.md.|
|**Q&A;**|0.5 min|Every member answers: What does it do? What AI? What security measures?|



Tool-110 — Email Digest Service | Page 12


**9. COMMON MISTAKES — Read This Now**


These 8 mistakes are made every sprint. Avoiding them saves days of wasted work.






|Mistake|Why It Happens and How to Avoid It|
|---|---|
|**[X] Hardcoding secrets in**<br>**config files**|Use ${ENV_VAR} in application.yml and os.getenv() in Python. Actual values go only in<br>.env (which is in .gitignore). If you commit a secret to GitHub, rotate it immediately —<br>deleting the file is not enough.|
|**[X] Committing .env to**<br>**GitHub**|Add .env to .gitignore on Day 1 before any commit. Run git status before every git<br>commit to verify. GitHub scans for exposed keys and will warn you, but by then it is<br>already public.|
|**[X] Not wrapping Groq calls**<br>**in try-except**|The Groq free tier has rate limits and occasional outages. Every call must be in a<br>try-except block. On failure: log the error, return the fallback template with {is_fallback:<br>true}. Never return HTTP 500 because the AI is unavailable.|
|**[X] Not setting up**<br>**docker-compose until Week**<br>**3**|Set it up on Day 5. The most common Demo Day failure is 'works on my laptop but not<br>the demo machine.' Test the full docker-compose stack every day from Day 5 onwards.<br>Discover integration problems early.|
|**[X] Adding features in Week**<br>**4**|Week 4 is for demo preparation only. Feature freeze after Day 15. Every hour building<br>features in Week 4 is an hour not spent making the demo flawless. New ideas go in<br>GitHub Issues labelled post-sprint.|
|**[X] Empty database on**<br>**Demo Day**|Implement the DataLoader seeder on Day 14. On Demo Day: docker-compose down -v<br>then docker-compose up to reset to a clean seeded state. An empty list on Demo Day<br>undermines the entire presentation.|
|**[X] Not reading Groq docs**<br>**before writing AI code**|Spend 30 minutes at console.groq.com/docs before Day 2. Key parameters: model<br>name, temperature (0.3 for factual, 0.7 for creative), max_tokens, and the messages<br>array structure. Misunderstanding temperature alone can waste an entire day.|
|**[X] Skipping the demo dry**<br>**run**|Every team that skips the rehearsal on Day 17 regrets it. Problems are always found in<br>rehearsal that you never noticed before. Do two full rehearsals (Day 17 and Day 19).<br>Use a stopwatch. The time limit is firm.|



Tool-110 — Email Digest Service | Capstone Project | Sprint: 14 April – 9 May 2026


Tool-110 — Email Digest Service | Page 13


