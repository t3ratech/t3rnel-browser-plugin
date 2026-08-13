# Privacy Policy — T3rnel Browser

*Last updated 13 August 2026. Published at https://t3ratech.github.io/t3rnel-browser-plugin/privacy.html*

## The short version

T3rnel Browser collects nothing. There is no account, no analytics, no telemetry, no
error reporting and no tracking. We do not have a server that receives your browsing
data, because we did not build one.

## What is stored, and where

Everything the extension saves is stored locally in your browser, on your device:

- Settings and approval policies
- Screenshot history and visual regression baselines
- Recorded sessions and generated test code
- Vault entries, encrypted with a key derived from your master passphrase — the
  plaintext is never written
- Your licence entitlement, if you buy Pro

None of it is transmitted anywhere. Uninstalling the extension removes it.

## When the extension makes a network request

Three situations, all either initiated by you or obvious from the feature:

| Situation | Where it goes | What is sent |
|---|---|---|
| Activating a Pro licence | `t3rnel-license.t3ratech.workers.dev` | Your licence key and a public key identifying the installation. Once, when you activate. The free tier never contacts it, and after activation your licence is verified offline. |
| Checking links on a page | The links on the page you asked to check | An HTTP HEAD request. Only when you run the link checker. |
| Optional AI analysis | The endpoint you configured | The page data for that request, with your own API key. Off unless you turn it on and supply a key. |

That is the complete list. The inspection and automation features — CSS, screenshots,
Markdown, network and console capture, DOM snapshots, agent tools — send nothing
anywhere.

## Payments

Payment is handled by PayNow. We never see or store your payment details. Our server
stores a one-way hash of your licence key, a hash of your email, and a fingerprint of
each activated installation's public key. It stores no raw licence key after you
collect it, no payment credential and no browsing data.

## Permissions

The extension requests the minimum at install — `activeTab`, `alarms`, `scripting`,
`sidePanel`, `storage`, `tabs`, and loopback host access only. Everything else is
requested at the moment you first use the feature that needs it, with an explanation.
Declining is safe: the feature reports what it needed, and everything else keeps
working.

## Children

T3rnel Browser is a developer tool and is not directed at children under 13.

## Changes

If this policy changes, the revision date above changes with it and the change is
recorded in `CHANGELOG.md`.

## Contact

Open an issue at https://github.com/T3raTech/t3rnel-browser/issues
