(function () {
  var KEY = "t3b-theme", root = document.documentElement;
  function saved() { try { return localStorage.getItem(KEY) || "system"; } catch (e) { return "system"; } }
  function apply(c) {
    if (c === "light" || c === "dark") { root.dataset.theme = c; root.style.colorScheme = c; }
    else { delete root.dataset.theme; root.style.colorScheme = ""; }
    document.querySelectorAll("[data-theme-choice]").forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-theme-choice") === c)); });
  }
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-theme-choice]");
    if (!b) return;
    var c = b.getAttribute("data-theme-choice");
    try { if (c === "system") localStorage.removeItem(KEY); else localStorage.setItem(KEY, c); } catch (err) { /* private mode */ }
    apply(c);
  });
  apply(saved());
})();
