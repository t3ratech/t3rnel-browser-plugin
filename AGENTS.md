# AGENTS.md — T3rnel Browser

> What this product is, and the rules for driving a real user's browser. This
> site is the product surface; the tool itself is a browser extension plus a
> local MCP bridge.

## What this is

T3rnel Browser is "DevTools you can talk to" — a browser extension that turns
the browser the user already has (real profile, real sessions, real
extensions) into an automation surface any MCP-speaking agent can drive:
navigate, click, fill, read, screenshot, record, audit, across Chrome, Edge,
Opera, Brave and Firefox. The agent talks to the MCP session bridge
(`npx @t3ratech/mcp-session-bridge`), which drives the extension over the
browser's own channels.

## Interfaces

| Interface | Where | Auth |
|---|---|---|
| MCP bridge (stdio) | `npx -y @t3ratech/mcp-session-bridge` | first connect auto-approved (default) or pairing-gated per Settings |
| Extension | Chrome/Edge/Opera/Firefox stores — links on `/products.html` | store review |
| Docs | `https://browser.t3ratech.co.zw/manual.html` | — |

## Permissions

- Allowed: read, navigate, click, fill, screenshot, record — the full tool
  surface the extension exposes.
- Never: the LLM firewall (`allowlist mode` in Settings) may deny a tool by
  policy; when it does, ask the operator rather than retrying — the denial is
  the product working.
- A pairing prompt, when armed, is a person asking — leave it pending rather
  than working around it.

## Identity and errors

- Tool errors are JSON `{ error: "..." }` naming the action that failed;
  a dead tab or a blocked page (`chrome://`, `chrome-extension://`) refuses
  by name — re-resolve the target rather than assuming success.

## What we will never do

Drive a browser that isn't the operator's, bypass a permission prompt, or
synthesize trusted input the extension did not receive.
