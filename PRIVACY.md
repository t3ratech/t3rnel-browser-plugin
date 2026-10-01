# Privacy Policy — T3rnel Browser

*Last updated 1 October 2026. Published at https://browser.t3ratech.co.zw/privacy.html*

## The short version

T3rnel Browser collects nothing by default. There is no account, no error reporting and
no tracking, and there never has been a server that receives your browsing data. Since
1.3.0 there are two things you can opt into — an anonymous per-tool usage counter and a
newsletter — and both are off until you say otherwise.

## What is stored, and where

Everything the extension saves is stored locally in your browser, on your device:

- Settings and approval policies
- Screenshot history and visual regression baselines
- Recorded sessions and generated test code
- Vault entries, encrypted with a key derived from your master passphrase — the
  plaintext is never written
- Your licence entitlement, if you buy Pro
- On the Free tier, a count of tool uses that decides when the next upgrade or rating prompt appears, and which T3raTech product it features

None of it is transmitted anywhere. Uninstalling the extension removes it.

## When the extension makes a network request

Ten situations, all either initiated by you, behind a switch you control, part of a purchase or licence you started, or read-only:

| Situation | Where it goes | What is sent |
|---|---|---|
| Activating a Pro licence | `t3rnel-wavepay-production.t3ratech.workers.dev` | Your licence key and a public key identifying the installation. Once, when you activate. After activation your licence is verified offline. |
| Buying Pro | `t3rnel-wavepay-production.t3ratech.workers.dev`, then PayNow or PayPal | The email address your licence key goes to and the payment method you chose — only when you press Pay. The payment itself happens on PayNow's or PayPal's own page. |
| Collecting your licence after you pay | `t3rnel-wavepay-production.t3ratech.workers.dev` | A one-time collection code created when you pressed Pay. The extension asks for your key until it arrives — when you return from paying, when the browser starts, and once a minute while the purchase is pending — and stops once it has the key or the checkout expires (24 hours). |
| Keeping an activated licence current | `t3rnel-wavepay-production.t3ratech.workers.dev` | A signature from your installation's key, no more than twice a day and only when fewer than seven days of the current entitlement remain. Between renewals your licence is verified offline. |
| Showing prices and the payment methods on offer | `t3rnel-wavepay-production.t3ratech.workers.dev` | Read-only requests for the current price and the list of available payment methods when a panel, the popup or the setup page opens. Nothing about you or your browsing is sent. |
| Checking links on a page | The links on the page you asked to check | An HTTP HEAD request. Only when you run the link checker. |
| Optional AI analysis | The endpoint you configured | The page data for that request, with your own API key. Off unless you turn it on and supply a key. |
| Finding a local MCP bridge | `127.0.0.1`, ports 17311–17318, on your own machine | A request to the bridge's local health endpoint. It never leaves your device. |
| Newsletter signup | Your own mail client | A `mailto:` compose window to our address — the extension sends nothing itself. |
| Opt-in usage counter | `t3rnel-wavepay-production.t3ratech.workers.dev` and Google Analytics 4 | Anonymous per-tool call counts — that a tool ran and how many times. Off by default; enabling it in Settings or onboarding is the only way anything is sent. No page content, URL, tool argument or identity is ever included. |

That is the complete list. The inspection and automation features — CSS, screenshots,
Markdown, network and console capture, DOM snapshots, agent tools — send nothing
anywhere. The usage counter always records on-device regardless of the toggle; the
toggle only controls whether the anonymous counts are ever reported off-device.

## Payments

Payment is handled by PayNow or PayPal, on their own pages. We never see or store your payment details. Our server
stores a one-way hash of your licence key, a keyed hash of your email, your email address
encrypted (so the payment receipt — which carries your licence key as a backup copy — and
any key recovery reach you), and a fingerprint of each activated installation's public
key. It stores no raw licence key after you collect it, no payment credential and no
browsing data. Paid-purchase records are kept for accounting; abandoned and failed
checkouts are deleted after 90 days.

## Permissions

The extension requests the minimum at install — `activeTab`, `alarms`, `debugger`,
`downloads`, `nativeMessaging`, `scripting`, `sidePanel`, `storage`, `tabs`, and
loopback host access only. (`nativeMessaging` remains only for Session Bridge installs
that predate the WebSocket transport and is scheduled for removal.) Everything else —
site access, history, bookmarks, browsing-data clearing — is requested at the moment
you first use the feature that needs it, with an explanation. Declining is safe: the
feature reports what it needed, and everything else keeps working.

## Children

T3rnel Browser is a developer tool and is not directed at children under 13.

## Changes

If this policy changes, the revision date above changes with it and the change is
recorded in `CHANGELOG.md`.

## Contact

Open an issue at https://github.com/T3raTech/t3rnel-browser/issues
