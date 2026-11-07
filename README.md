<!-- doc-version: 1.0.0 | last-reviewed: 2026-08-17 | owner: architect -->

# T3rnel

T3rnel is a Rust-cored Agent OS for building, testing, reviewing, securing, documenting, and shipping software through an orchestrated swarm of specialised agents.

The MVP focuses on one hard promise: given a technical spec, T3rnel autonomously runs a coding project end-to-end while the user watches file edits, terminal output, approvals, traces, and review results from the IDE.

## What T3rnel Does

T3rnel coordinates a full engineering pipeline:

- An orchestrator plans the work and owns the task graph.
- Architect, coder, test, reviewer, security, documentation, and release agents collaborate through A2A tasks.
- Every tool call runs behind capability checks, sandbox policy, budget metering, and an audit chain.
- gRPC tasks are durable records with lifecycle state, cancellation, watch streams, and task-derived trace events.
- Shell execution enters through the runtime tool runner and configured sandbox policy.
- Risky changes surface through an approval inbox with per-hunk diff control.
- Memory combines session state, SQLite semantic recall, optional LanceDB vector search through the embedding sidecar, and a SQLite knowledge graph.
- Session promotion writes real semantic memories and KG provenance instead of acknowledging a no-op.
- Prompt versions, golden tasks, parity tests, telemetry, and [`ISSUES.md`](ISSUES.md) tracking are first-class product surfaces.
- Web and mobile share a tab registry with Agents, Chat, Settings, and Stocks surfaces.
- IDE delegation lets the orchestrator hand whole tasks to Devin, Cursor, or Antigravity and poll them to completion (`ide_delegate` / `ide_poll`).
- MCP server exposes T3rnel agents and tools (`t3rnel_ide_delegate`, `t3rnel_ide_poll`, etc.) to Windsurf/VS Code.
- ACP agent mode (`t3rnel acp`) makes T3rnel appear as a selectable agent in Windsurf / Devin Desktop's Agent Command Center.
- Stocks runs through kernel-enforced rails, durable orders/fills/positions, signed strategy skills, broker adapters, rail-breach alerts, Expo push payloads, and biometric-signed rail mutation checks.
- An ordered middleware pipeline (18 built-ins) intercepts every agent turn: guardrails, loop detection, dangling tool-call recovery, clarification handling, token usage tracking, summarization, and memory injection.
- Pluggable guardrail policies (allowlist, OAP, custom) evaluate every tool call before the approval gate.
- Config versioning with runtime hot-reload: edit `t3rnel.toml` and changes apply without daemon restart.
- Model factory with dynamic driver registry: add new LLM providers as single-file registrations.
- vLLM provider with reasoning field preservation and Qwen-style thinking toggles.
- Skill security scanner classifies content as `allow`, `warn`, or `block` before loading.
- Sandbox virtual path system: agents see `/mnt/workspace` while the host path is resolved at tool invocation.
- File upload with auto-conversion: PDF, PPT, Excel, Word → markdown via the Python sidecar.
- AI-generated follow-up suggestions after every assistant turn.
- Structured memory with fact extraction: discrete facts with confidence scores and categories injected into agent context.
- Multi-channel IM architecture for Slack, Telegram, Discord, and Mattermost with thread persistence across daemon restarts.
- Phase 3 Tab OS baseline with Business, NFTs, Music, Mail, Search, Webview, Calendar, Smart-Home, and Skills tabs sharing daemon state across web, desktop-rendered web, and mobile shared-web surfaces.
- Health monitoring with provider health tracking, automatic failover, and recovery scheduling for reliable agent operations.
- Agent categories with configurable fallback chains, retry profiles, and recovery strategies for different workload types.
- Comprehensive provider catalog with 24 providers and tiered model selection across web, desktop, and mobile UIs.

T3rnel runs as a local-first daemon with a Rust kernel and TypeScript human surfaces. The Phase 1 interface is the VS Code / Windsurf extension. The same substrate powers the web, mobile, desktop, browser extension, and TUI surfaces in the full Tab OS.

## Product Shape

T3rnel is not a chat sidebar. It is an OS-style workspace where every capability appears as a tab backed by an ambient agent.

Core capabilities include:

- **Agents** — live multi-agent task graph, status, costs, traces.
- **Files** — file tree, diffs, and accept/reject controls.
- **Terminal** — sandboxed terminal streams per agent.
- **Inbox** — approval queue for side effects and risky actions.
- **Tasks** — spec-to-task graph with progress and retry controls.
- **Settings** — providers, keys, budgets, sandbox policy, prompt versions.

Specialist tabs such as Stocks, NFTs, Music, Mail, News, Search, Calendar, Smart-Home, and Skills use the same agent, memory, capability, and approval primitives.

The Stocks tab uses `market-watcher`, `quant-strategist`, `autonomous-trader`, and `risk-officer` agents. Orders pass through `t3rnel-kernel::trading_guard`; trading state persists in SQLite; Alpaca, Interactive Brokers, and Kraken adapters shape broker requests; and risk-increasing rail changes require a signature from an enrolled biometric device.

The Music tab carries the Playlizt media-player port: Library preview scans, playlist draft handoff, URL download handoff, conversion/muxer profiles, and device targets. `./t3rnel-services --media` provides the operational adapter for scanning libraries, creating M3U8 playlists, playing through mpv/cvlc/vlc, stopping playback, controlling mpv volume, downloading with yt-dlp/youtube-dl, and converting with ffmpeg. FFmpeg, VLC/cvlc, youtube-dl/yt-dlp, and mpv are used as external executable dependencies for this phase. Source snapshots may be present under `/mnt/ext4_work/resources/t3rnel` for engineering reference, but T3rnel does not port or link their code.

The NFTs tab runs `nft-orchestrator` with zero-cost-first marketplace policy. It coordinates Gemini art direction, metadata curation, IPFS storage readiness, OpenSea read/listing-readiness checks, wallet-policy gates, and sales monitoring. It refuses gas-spending transactions, wallet signatures, and order publication unless policy and approval explicitly authorize the exact payload.

The Social Media tab provides integrated social media management through the `t3rnel-social` crate. It supports X (Twitter), LinkedIn, Reddit, and Discord with OAuth 2.0 authentication, shared rate limiting across providers, and post scheduling. The `social-media-manager` agent autonomously handles content strategy, platform-specific best practices, and engagement monitoring. Posts can be composed, scheduled, and published through the UI, MCP tools, or CLI commands.

## Architecture

The core system is Rust:

- `t3rnel-kernel` supervises agents, scheduling, approvals, capabilities, metering, triggers, heartbeats, and an ordered middleware pipeline with pluggable guardrails.
- `t3rnel-runtime` runs agent loops, LLM drivers via the model factory, MCP/A2A, sandboxes with virtual path resolution, compaction, and tool execution.
- `t3rnel-memory` stores session memory, semantic memory, structured fact extraction, and the knowledge graph.
- `t3rnel-skills` loads signed WASM Component Model skills with declared capabilities and LLM-based security scanning.
- `t3rnel-api` exposes gRPC, gRPC-Web, WebSocket, SSE, OpenAPI, file uploads, follow-up suggestions, and metrics.
- `t3rnel-api` also exposes `/api/tab-os/state`, the shared daemon snapshot for Business, NFTs, Music/media, Mail, Calendar, Smart-Home, and federated Search tabs.
- `t3rnel-channels` routes inbound and outbound messages across Slack, Telegram, Discord, and Mattermost with thread persistence.
- `t3rnel-hands` provides curated autonomous capability packages, including trading broker adapter contracts.

Human-facing clients are TypeScript:

- `clients/vscode` is the Phase 1 IDE surface.
- `clients/ui-kit`, `clients/web`, and `clients/mobile` share the Tab OS interface.
- `clients/desktop` packages the web bundle in Electron.
- `products/browser/t3rnel-browser` exposes an MV3 popup and side panel over a loopback-only WebSocket bridge.

Python runs only at the edge for ML ecosystem integrations such as embeddings, LanceDB vector search, vision, speech, or local model sidecars. The embedding sidecar requires explicit model and bind configuration; when `memory.backend = "lancedb"`, the Rust memory crate health-checks the sidecar before serving.

## Default Model

The authoritative configuration for default models across the entire daemon is strictly managed in `~/.t3rnel/config.toml`. 

- To change the default model for all agents, use the `PUT /api/config/default-model` endpoint via the WebUI Settings tab or CLI, which updates `config.toml` dynamically.
- For local initial setup, use `cp t3rnel.toml.example ~/.t3rnel/config.toml` as your starting point. Missing required configuration causes a hard, named boot failure.

## Security Model

T3rnel prefers hard failures over silent drift.

- Required config has no production defaults.
- Tool calls require typed capability tokens.
- High-risk actions block on approval.
- WASM skills run with WASI capability restrictions.
- Subprocesses run through Linux sandboxing or Docker profiles.
- Network egress is policy controlled per agent.
- Every capability check and tool call is written to the audit chain.
- File and shell RPCs reject path traversal before touching the workspace.
- Secrets never appear in prompts, logs, traces, fixtures, or committed files.

## Evaluation

Every feature ships with regression coverage.

- Rust unit and integration tests cover kernel, runtime, API, memory, skills, and telemetry.
- TypeScript unit and UI tests cover client surfaces.
- Standalone WASM skill crates run through `./t3rnel-services --test unit-skills[:name]`.
- Cross-language Playwright scenarios exercise TS client, Rust daemon, Python sidecar, mock LLM, Jaeger, and UI rendering in one assertion chain.
- Golden tasks and LLM-as-judge rubrics score end-to-end coding outcomes.
- Parity fixtures keep provider and tool paths bit-stable across refactors.
- CI runs parity, smoke eval, and golden tasks through `./t3rnel-services`; failing evals block the workflow.

## Market Research

One `market-researcher` agent serves every producing team. Findings land in a
shared opportunity registry — evidence, scores on the revenue master-table axes,
lifecycle dates, and the order work will be taken up — surfaced as a table in
the dashboard's Market Research tab.

Skipped ideas are kept with the reason they were skipped, in their own tab, and
can be taken back into the build order at any time. Only an explicit removal
discards research.

Two queues, deliberately separate. **Opportunities** are what to build to earn,
executed by software engineering. **Enhancements** are what to change about
ourselves, executed by dogfooding and never run autonomously.

**Trends** from Moltbook, other agent networks and the AI platforms are evidence
rather than work: an observation promotes into one of the two registries and
then competes on the same scoring as everything already queued.

```bash
curl -s http://127.0.0.1:4200/api/research           # opportunities, build order
curl -s http://127.0.0.1:4200/api/research/skipped   # kept, not discarded
curl -s http://127.0.0.1:4200/api/enhancements       # the dogfooding queue
curl -s http://127.0.0.1:4200/api/trends             # observations + how others earn
```

## Operations

All operational commands run through:

```bash
./t3rnel-services
```

The script owns start, stop, build, targeted test, lint, migration, service probes, logs, cleanup, plugin install, skill install, and release commands. Build/rebuild/release commands clean stale Rust incremental caches and generated client outputs before compiling. Direct ad-hoc service commands and global Rust/workspace tests are outside the project contract.

Runtime dependencies and wallet probes also use the script:

```bash
./t3rnel-services --install pyyaml
./t3rnel-services --wallet binance-summary
./t3rnel-services --wallet binance-address
./t3rnel-services --nft summary
./t3rnel-services --nft opensea-summary
./t3rnel-services --nft storage-preflight
./t3rnel-services --nft generate-art
./t3rnel-services --nft pin-draft
./t3rnel-services --nft monitor-start
./t3rnel-services --email agentmail-summary
./t3rnel-services --jobs status
./t3rnel-services --jobs monitor-start
./t3rnel-services --jobs near-bid-open
./t3rnel-services --jobs jobforagent-draft
./t3rnel-services --jobs jobforagent-send-agentmail
./t3rnel-services --jobs jobforagent-reconcile-agentmail
```

The Binance wallet path is read-only and receive-only. It verifies key permissions, reads account/deposit state, and records the configured deposit address without enabling trades, transfers, withdrawals, or protocol signing.

The NFT marketplace path is zero-cost-first. It validates OpenSea, wallet address, existing wallet NFTs across supported chains, storage provider, and policy state without printing API keys or seed phrases. Draft generation writes unsigned local metadata/listing plans; `--nft generate-art` attaches original SVG media/provenance, `--nft pin-draft` pins media and metadata to Pinata/IPFS with CID evidence, and `--nft monitor-start` watches posted NFTs, offers, and sales with filtered desktop notifications. On-chain actions, signatures, and order publication remain blocked until wallet policy and Inbox approval authorize the exact payload. Moltbook distribution runs through `./t3rnel-services --moltbook`, which registers the agent, stores local `.env` keys, creates an NFT/crypto-enabled submolt, posts public launch notes, and searches agent-community content.

The job-marketplace path checks the critical paid-work agents, NEAR Agent Market bids/services, Work402 worker state, and SeekClaw open-job feed without printing secrets. `--jobs near-bid-open` places policy-screened NEAR bids through the official API, `--jobs jobforagent-draft` queues email applications, `--jobs jobforagent-send-agentmail` sends queued JobForAgent applications through the AgentMail provider, and `--jobs jobforagent-reconcile-agentmail` records bounces and inbound replies from AgentMail labels/messages. `--jobs monitor-start` installs a user service that keeps watching and sends desktop notifications only for accepted, completed, and paid revenue-stage events by default.

The VS Code / Windsurf extension builds and tests as an installed VSIX:

```bash
./t3rnel-services --build vscode-ext
./t3rnel-services --test ui-vscode
```

`ui-vscode` requires the local daemon at `http://127.0.0.1:50051` and Windsurf on the path. The test installs `artifacts/t3rnel-vscode-0.1.0.vsix` into a clean Windsurf profile, verifies `t3ratech.t3rnel-vscode@0.1.0`, runs the extension commands against the live daemon, creates a real task, and checks the approval queue command.

The VS Code / Windsurf command palette exposes daemon-backed team messaging, A2A task cancellation, and workspace review commands. Current-diff, branch, codebase, and PR review commands open concrete editor output instead of throwing placeholder errors.

The Electron desktop shell resolves its window-state file after Electron user-data configuration is available, so custom profile paths and tests use the same native startup path.

The Chrome extension uses a loopback-only WebSocket bridge and the shared semantic browser-provider contract. Its default daemon port is `50051`, and `./t3rnel-services --browser ...` operates the same native browser-hand route used by agents. `./t3rnel-services --test ui-chrome` installs the unpacked MV3 extension in a headed Chromium profile, verifies popup and side-panel bridge rendering against a deterministic loopback server, then connects the popup to the live local daemon. Mail, marketplace, payment, research, and QA workflows consume this provider through their own hands/adapters; one-off site scripts and external browser bridges are outside the primary platform contract.

It also ships as a standalone product — **T3rnel Browser**, 99 tools, free tier plus a $29.99 one-time Pro licence — and the daemon appears on exactly one of its tabs. Everything else works with no daemon at all.

```bash
cd products/browser/t3rnel-browser
npm run build                       # -> dist/, what every harness loads
node scripts/package-store.mjs      # -> build/t3rnel-browser-1.0.0.zip
npx vitest run                      # 355 unit tests

(cd ../../docs/site && python3 -m http.server 8899 --bind 127.0.0.1 &)
node e2e/real-sidebar.mjs           # the genuine docked panel, opened by a real keystroke
node e2e/no-gates.mjs               # every tool, Pro active, all permissions held
node e2e/artifacts.mjs              # exports written to disk and checked byte by byte
node e2e/tool-truth.mjs             # what a fresh install can and cannot do
./e2e/cleanup.sh                    # ALWAYS, after any interrupted run
```

Testing the docked side panel needs `xdotool`, because Chrome will not open it without a real user gesture and CDP cannot reach the toolbar. The harness presses `Ctrl+Shift+Y` through XTEST. Two traps: `xdotool key --window` is discarded by Chrome as untrusted, and selecting a window by class alone can pick the developer's own browser and type into their session. Both are covered in [`products/browser/t3rnel-browser/e2e/README.md`](products/browser/t3rnel-browser/e2e/README.md).

Exports are saved into configurable folders below the browser's download directory — `T3rnel/Screenshots`, `T3rnel/PDFs`, `T3rnel/CSS` and so on. Chrome refuses absolute paths from an extension, so the browser's download folder is the anchor; point it wherever you like and the rest follow.

Store submission answers live in [`products/browser/t3rnel-browser/STORE-SUBMISSION.md`](products/browser/t3rnel-browser/STORE-SUBMISSION.md), listing copy in [`WEBSTORE.md`](products/browser/t3rnel-browser/WEBSTORE.md), and the payment and device-binding design — including what it does *not* prevent — in [`docs/payment-licensing.md`](docs/payment-licensing.md).

### Issue tracker

`ISSUES.md` records what is known broken, and gates shipping.

```bash
./t3rnel-services --issues          # blocking, unverified, and false ticks
./t3rnel-services --issues --gate   # exit 2 if anything blocks a ship
```

`Fix Status` describes the code; `Resolved` describes verified behaviour. Unit
tests never resolve an issue — only a headed surface plus the browser hand do.

### Maintenance and monitoring

```bash
./t3rnel-services --cleanup --dry-run   # what disk space is reclaimable
./t3rnel-services --cleanup             # prune containers and regenerable caches
./t3rnel-services --sentinel            # error and security findings
./t3rnel-services --sentinel --json     # same, machine readable
./t3rnel-services --sentinel --file     # file findings into ISSUES.md
```

`--cleanup` never touches the daemon home, ledgers, secrets, sessions or Docker
volumes. `--sentinel` exits non-zero on a critical finding, so a scheduled run
surfaces it.

## Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md) is the technical source of truth.
- [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) is the build plan and definition of done.
- [.windsurf/rules/t3rnel-rules.md](.windsurf/rules/t3rnel-rules.md) contains the binding engineering rules.

## System Topology

The following diagram shows every component of T3rnel and how data flows between them.

```
                                ┌──────────────────────────────────────────────────────────────────┐
                                │                    Human Surfaces                                │
                                │  (Every surface talks to the same daemon over gRPC/WebSocket)    │
                                ├─────────┬──────────┬───────────┬────────────┬──────────┬─────────┤
                                │         │          │           │            │          │         │
                      ┌─────────▼──┐ ┌────▼─────┐ ┌──▼────┐ ┌────▼─────┐ ┌────▼─────┐ ┌──▼────────┐
                      │ VS Code /  │ │   Web    │ │Mobile │ │ Desktop  │ │ Chrome   │ │  TUI      │
                      │ Windsurf   │ │   UI     │ │  App  │ │  App     │ │ Extension│ │(ratatui)  │
                      │ Extension  │ │ (RN-Web) │ │(Expo) │ │(Electron)│ │          │ │           │
                      └─────┬──────┘ └─────┬────┘ └───┬───┘ └────┬─────┘ └────┬─────┘ └───────┬───┘
                            │              │          │          │            │               │
                            │  ┌───────────┴──────────┴──────────┴────────────┴───────────┐   │
                            │  │              Shared React Native Codebase                │   │
                            │  │  (ui-kit: NativeWind + Tamagui + Reanimated + Skia)      │   │
                            │  └──────────────────────────────────────────────────────────┘   │
                            │                           │                                     │
                            └────────── gRPC / gRPC-Web / WebSocket / SSE / QUIC ─────────────┘
                                                        │
                                          ┌─────────────▼──────────────┐
                                          │        t3rnel-api          │
                                          │  Axum · OpenAPI · OFP Wire │
                                          │  REST + gRPC + WS Gateway  │
                                          └──────────┬─────────────────┘
                                                     │
       ┌─────────────────────────────────────────────┼──────────────────────────────────────────────────┐
       │                                             │                                                  │
       │                                       ┌─────▼─────┐                                            │
       │                                       │ t3rnel-   │                                            │
       │                                       │ kernel    │                                            │
       │                                       │           │                                            │
       │  ┌────────────────────────────────────┤ Supervisor│────────────────────────────────────────┐   │
       │  │                                    │ Scheduler │                                        │   │
       │  │  ┌────────────┐  ┌────────────┐    │ EventBus  │   ┌────────────┐  ┌──────────────┐     │   │
       │  │  │  Approval  │  │Capabilities│    │ Approval  │   │  Cron &    │  │ ConfigReload │     │   │
       │  │  │   Gate     │  │  Tokens    │◄───┤  Metering │──►│  Triggers  │  │  Heartbeat   │     │   │
       │  │  └─────┬──────┘  └─────┬──────┘    │ Workflow  │   └─────┬──────┘  └──────────────┘     │   │
       │  │        │               │           │  Pairing  │         │                              │   │
       │  │   ┌────▼───────────────▼───┐       └─────┬─────┘    ┌────▼────┐                         │   │
       │  │   │     t3rnel-kernel      │             │          │ Trading │                         │   │
       │  │   │   (Scheduling Core)    │             │          │ Guard   │                         │   │
       │  │   └────────────────────────┘             │          └─────────┘                         │   │
       │  │                                          │                                              │   │
       │  └──────────────────────────────────────────┼──────────────────────────────────────────────┘   │
       │                                             │                                                  │
       │  ┌────────────┐  ┌────────────┐  ┌──────────▼────────┐  ┌────────────┐  ┌────────────┐         │
       │  │  runtime   │  │   memory   │  │     skills        │  │  channels  │  │   hands    │         │
       │  │            │  │            │  │                   │  │            │  │            │         │
       │  │ agent_loop │  │ session    │  │ wasm loader       │  │ slack      │  │ auto-      │         │
       │  │ A2A / MCP  │  │ semantic   │  │ registry          │  │ matrix     │  │ agents     │         │
       │  │ LLM drivers│  │ knowledge  │  │ verify            │  │ discord    │  │ research   │         │
       │  │ sandbox    │  │ KG (local) │  │ security scanner  │  │ email      │  │ devops     │         │
       │  │ middleware │  │ fact       │  │ marketplace       │  │ whatsapp   │  │ life-OS    │         │
       │  │ model      │  │ extraction │  │                   │  │ telegram   │  │ trading    │         │
       │  │ factory    │  │            │  │                   │  │ im-bus     │  │ social     │         │
       │  │ virtual    │  │ ┌────────┐ │  │ ┌──────────────┐  │  │ channel    │  │ ├────────┐ │         │
       │  │ paths      │  │ │ LanceDB│ │  │ │ file-ops     │  │  │ manager    │  │ │broker  │ │         │
       │  │ ┌────────┐ │  │ │(vector)│ │  │ │ git          │  │  │ ┌────────┐ │  │ │adapters│ │         │
       │  │ │Fallback│ │  │ └────────┘ │  │ │ http-fetch   │  │  │ │ OAuth  │ │  │ └────────┘ │         │
       │  │ │Driver  │ │  │            │  │ │ mean-rev     │  │  │ │ Bridge │ │  │            │         │
       │  │ │(tiered)│ │  │            │  │ │ ...          │  │  │ └────────┘ │  │            │         │
       │  │ │ Circuit│ │  │            │  │ └──────────────┘  │  │            │  │            │         │
       │  │ │ Breaker│ │  │            │  │                   │  │            │  │            │         │
       │  │ └────────┘ │  │            │  │                   │  │            │  │            │         │
       │  └─────┬──────┘  └─────┬──────┘  └─────────┬─────────┘  └─────┬──────┘  └─────┬──────┘         │
       │        │               │                   │                  │               │                │
       │        └───────────────┴───────────────────┴──────────────────┴───────────────┘                │
       │                                    │                                                           │
       │                        ┌───────────▼────────────┐                                              │
       │                        │  Shared Substrate      │                                              │
       │                        │  SQLite (events + KG)  │                                              │
       │                        │  LanceDB (vectors)     │                                              │
       │                        │  Wasmtime              │                                              │
       │                        │  Docker / Firecracker  │                                              │
       │                        │  Headless Chromium     │                                              │
       │                        │  Python sidecar        │                                              │
       │                        └────────────────────────┘                                              │
       │                                                                                                │
       └────────────────────────────────────────────────────────────────────────────────────────────────┘
                                              │
                        ┌─────────────────────▼──────────────────────────┐
                        │          Audit & Observability                 │
                        │  Merkle Hash Chain  ·  OTEL Traces  ·  Metrics │
                        │  Prometheus  ·  Jaeger  ·  Eval Lake           │
                        └────────────────────────────────────────────────┘
```

### Shared Token Storage

All credentials live in a single encrypted vault (`t3rnel-extensions/vault.rs`):

- **At rest:** AES-256-GCM encryption via OS keystore (Keychain / Secret Service / Credential Manager)
- **In flight:** never transmitted over A2A; UI clients access masked previews only
- **Scoped access:** the fallback router (`t3rnel-runtime/routing.rs`) selects keys by `paid`/`unpaid` tags and team profile bindings
- **Health checks:** auto-verify against provider list endpoints; unhealthy keys are skipped with logged warnings

### Agent Communication: A2A vs MCP

Agents use two protocols for different purposes:

**A2A (Agent-to-Agent)** — orchestration layer:
- Every agent exposes an `AgentCard` at `/.well-known/agent.json`
- Messages are Google A2A `Task` objects: structured, typed, routed by the orchestrator
- Used for: delegation, result handoff, swarm consensus, heartbeat
- Boundaries: team-scoped by default; federation (Phase 3) extends across daemons

**MCP (Model Context Protocol)** — tool layer:
- Skills and channels expose MCP servers with declared tool schemas
- Agents consume MCP tools through the runtime's `mcp.rs` client
- Used for: file ops, web search, broker APIs, browser automation
- Boundaries: per-agent capability tokens gate access; high-risk tools block on Inbox approval

### Memory: Team-Separated vs Universal

| Tier | Scope | Isolation | Promotion Path |
|---|---|---|---|
| **Session** | Per-agent, per-task | Fully isolated (compacted aggressively) | → Semantic on task close |
| **Semantic** | Per-team namespace | Team-scoped LanceDB tables; no cross-team read | → KG on consolidation |
| **Knowledge Graph** | Universal | Global triple store; edges may carry `team_id` tags | Read-only for all agents |
| **Lessons** | Universal | Immutable; written by learning worker after task completion | Read-only for all agents |
| **Credential Vault** | Universal | Single encrypted store; access controlled by team profile bindings | — |

**How agents share context:** they do not share raw prompt text. They share:
1. **KG entity references** — "see `file#src/main.rs:42`" or "depends_on `ticket#123`"
2. **A2A Task payloads** — structured, bounded, typed
3. **Memory retrieval queries** — each agent fetches its own relevant context from shared stores

This keeps token budgets predictable and prevents context pollution.

### Plugins: Hands, Skills, and Tab Extensions

**Hands** (`hands/` + `t3rnel-hands`) are bundled autonomous packages:
- `research-hand` — web search, PDF extraction, citation management
- `trading-hand` — broker adapters (Alpaca, IBKR, Kraken), risk rails, strategy skills
- `social-hand` — video editing, image generation, TTS, social channel posting
- `devops-hand` — Kubernetes, Terraform, monitoring, PagerDuty

**Skills** (`skills/` + `t3rnel-skills`) are WASM Component Model modules:
- `file-ops` — read, write, patch, search
- `git` — commit, branch, diff, blame
- `http-fetch` — GET/POST with disk caching
- `mean-reversion-v1` — trading strategy (WASM)
- Third-party skills publish to the marketplace and are signed + sandboxed

**Tab Extensions** (`packages/plugin-sdk-ts/` and `packages/plugin-sdk-rs/`):
- Third parties ship new tabs as signed plugins
- Declared in `TabModule` manifest with agent binding, capabilities, and per-platform layouts
- Runtime sandboxed with capability tokens (same model as skills)

## License

T3rnel is proprietary software owned by T3raTech Solutions (Pvt) Ltd. Permissive upstream code is attributed through `NOTICE` and `third_party/LICENSES/` when vendored.
