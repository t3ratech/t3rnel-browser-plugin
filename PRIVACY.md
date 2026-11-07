# Privacy Policy — T3rnel Browser

*Last updated 7 November 2026. Published at https://browser.t3ratech.co.zw/privacy.html*

## The short version

T3rnel Browser never sends your browsing data. From 1.4.0 the extension's own tools need an
account — you sign in with a provider the panel offers; the browser-control tools an AI uses to
drive a page need none — and it sends anonymous usage events:
which tool or button was used, where, and how it ended. Those events carry no page content,
no page address, no tool argument, nothing you typed and not your email address. There is
no error reporting, and there never has been a server that receives your browsing data.

## What is stored, and where

Everything the extension saves is stored locally in your browser, on your device:

- Settings and approval policies
- Screenshot history and visual regression baselines
- Recorded sessions and generated test code
- Vault entries, encrypted with a key derived from your master passphrase — the
  plaintext is never written
- Your licence entitlement, if you buy Pro
- Your signed-in account as the service last reported it — an opaque account id, your
  email, the sign-in methods linked to it, your plan, and this browser's seat — and the
  usage events waiting to be sent
- On the Free tier, a count of tool uses that decides when the next upgrade or rating prompt appears, and which T3raTech product it features

Your content — pages, captures, recordings, vault entries, settings — is never transmitted. What is transmitted is listed below. Uninstalling the extension removes everything stored here.

## When the extension makes a network request

These situations, each part of signing in, of your account, of a purchase or licence you started, initiated by you, or read-only:

| Situation | Where it goes | What is sent |
|---|---|---|
| Signing in | `t3rnel-wavepay-production.t3ratech.workers.dev`, and the sign-in provider's own page | The method you chose. The provider's page opens in a browser-controlled window; the provider gives the service a one-time authorisation code, the service reads your verified email from the provider, and sends back your account, plan and seat. The extension never sees your provider password or token. A public key identifying this browser, and a label such as "Chrome on Linux", are filed as your seat. |
| Keeping your account current | `t3rnel-wavepay-production.t3ratech.workers.dev` | A signature from this browser's key, about every six hours while the browser is open. Signing out, or being signed out from another browser, releases the seat. |
| Counting a free use | `t3rnel-wavepay-production.t3ratech.workers.dev` | On a Free account, the name of the tool and a signature from this browser's key, once per call of a free tool. A Pro tool is refused before anything is counted. The service keeps the monthly count, so reinstalling does not reset it. A Pro account is not counted. |
| Activating a Pro licence | `t3rnel-wavepay-production.t3ratech.workers.dev` | Your licence key and a public key identifying the installation. Once, when you activate. After activation your licence is verified offline. |
| Buying Pro | `t3rnel-wavepay-production.t3ratech.workers.dev`, then PayNow or PayPal | The email address your licence key goes to and the payment method you chose — only when you press Pay. The payment itself happens on PayNow's or PayPal's own page. |
| Collecting your licence after you pay | `t3rnel-wavepay-production.t3ratech.workers.dev` | A one-time collection code created when you pressed Pay. The extension asks for your key until it arrives — when you return from paying, when the browser starts, and once a minute while the purchase is pending — and stops once it has the key or the checkout expires (24 hours). |
| Keeping an activated licence current | `t3rnel-wavepay-production.t3ratech.workers.dev` | A signature from your installation's key, no more than twice a day and only when fewer than seven days of the current entitlement remain. Between renewals your licence is verified offline. |
| Showing prices and the payment methods on offer | `t3rnel-wavepay-production.t3ratech.workers.dev` | Read-only requests for the current price and the list of available payment methods when a panel, the popup or the setup page opens. Nothing about you or your browsing is sent. |
| Checking links on a page | The links on the page you asked to check | An HTTP HEAD request. Only when you run the link checker. |
| Optional AI analysis | The endpoint you configured | The page data for that request, with your own API key. Off unless you turn it on and supply a key. |
| Finding a local MCP bridge | `127.0.0.1`, ports 17311–17318, on your own machine | A request to the bridge's local health endpoint. It never leaves your device. |
| Newsletter signup | Your own mail client | A `mailto:` compose window to our address — the extension sends nothing itself. |
| Usage events | `t3rnel-wavepay-production.t3ratech.workers.dev`, which forwards to Google Analytics 4 | One event per tool use and per button press: the name of the tool or control (`quick:fullpage`, `section:settings`), where it was used, how it ended, how long it took, the extension version, the browser, your plan, and an opaque account id so one person's browsers read as one. Never page content, a page address, a tool argument, anything typed into a field, or your email address; the service drops any value that looks like an address or a long number. On Chromium browsers this is part of the product and has no switch. On Firefox it is sent only after you grant Firefox's technical-and-interaction data permission. |

That is the complete list. The inspection and automation features — CSS, screenshots,
Markdown, network and console capture, DOM snapshots, agent tools — send nothing from the
page they ran on; the only thing that leaves is the usage event naming the tool. Local
usage counters also record on-device and are shown in Settings.

## Your account

The service keeps your verified email, the sign-in methods linked to it, one record per
signed-in browser (label, method, when it was first and last seen — up to five) and a count
of free tool uses for the month. It keeps no provider password and no provider token.

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
`downloads`, `identity`, `nativeMessaging`, `notifications`, `scripting`, `sidePanel`,
`storage`, `tabs`, and loopback host access only. (`identity` is used only to open the
sign-in provider's page and receive its redirect; it gives no access to your browser
profile and adds no install warning. `nativeMessaging` remains only for Session Bridge
installs that predate the WebSocket transport and is scheduled for removal.) Everything else —
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
