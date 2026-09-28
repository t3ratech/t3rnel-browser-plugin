// Native share for [data-share] buttons: Web Share API (phone share sheet)
// where it exists, clipboard copy where it does not. The static link row
// remains the no-JS fallback.
document.addEventListener("click", async (e) => {
  const b = e.target.closest("[data-share]");
  if (!b) return;
  e.preventDefault();
  const payload = { title: document.title, url: location.href };
  if (navigator.share) {
    try { await navigator.share(payload); } catch { /* dismissed */ }
    return;
  }
  try {
    await navigator.clipboard.writeText(location.href);
    const t = b.textContent; b.textContent = "Link copied ✓";
    setTimeout(() => { b.textContent = t; }, 1600);
  } catch { /* clipboard unavailable — links still there */ }
});
