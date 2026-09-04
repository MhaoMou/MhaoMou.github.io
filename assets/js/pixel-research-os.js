(function () {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const bootLine = document.querySelector("[data-boot-line]");
  const navLinks = Array.from(document.querySelectorAll(".desktop-nav a"));
  const sections = navLinks
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  if (bootLine && !reducedMotion.matches) {
    const states = [
      "BOOTING MINGHAO.EXE...",
      "LOADING RESEARCH MODULES...",
      "READY."
    ];
    let index = 0;
    const timer = window.setInterval(() => {
      index += 1;
      bootLine.textContent = states[index] || states[states.length - 1];
      if (index >= states.length - 1) {
        window.clearInterval(timer);
      }
    }, 420);
  } else if (bootLine) {
    bootLine.textContent = "READY.";
  }

  if ("IntersectionObserver" in window && navLinks.length && sections.length) {
    const linkById = new Map(
      navLinks.map((link) => [link.getAttribute("href").slice(1), link])
    );
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const link = linkById.get(entry.target.id);
        if (!link) return;
        if (entry.isIntersecting) {
          navLinks.forEach((item) => item.removeAttribute("aria-current"));
          link.setAttribute("aria-current", "location");
        }
      });
    }, { rootMargin: "-35% 0px -55% 0px", threshold: 0.01 });
    sections.forEach((section) => observer.observe(section));
  }
})();
