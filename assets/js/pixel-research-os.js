(function () {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const bootLine = document.querySelector("[data-boot-line]");
  const statusLine = document.querySelector("[data-status-line]");
  const localTime = document.querySelector("[data-local-time]");
  const navLinks = Array.from(document.querySelectorAll(".desktop-nav a[href^='#'], .taskbar-nav a[href^='#']"));
  const windows = Array.from(document.querySelectorAll("[data-window]"));

  function setStatus(text) {
    if (statusLine) statusLine.textContent = text;
  }

  function updateClock() {
    if (!localTime) return;
    const now = new Date();
    const value = new Intl.DateTimeFormat([], {
      hour: "2-digit",
      minute: "2-digit"
    }).format(now);
    localTime.textContent = value;
    localTime.setAttribute("datetime", now.toISOString());
  }

  function runBootLine() {
    if (!bootLine) return;
    if (reducedMotion.matches) {
      bootLine.textContent = "SYSTEM READY.";
      return;
    }
    const states = [
      "BOOTING MINGHAO.EXE...",
      "LOADING RESEARCH MODULES...",
      "MOUNTING PAPER DATABASE...",
      "SYSTEM READY."
    ];
    let index = 0;
    const timer = window.setInterval(() => {
      index += 1;
      bootLine.textContent = states[index] || states[states.length - 1];
      if (index >= states.length - 1) {
        window.clearInterval(timer);
      }
    }, 360);
  }

  function setActiveSection(sectionId) {
    navLinks.forEach((link) => {
      const isActive = link.getAttribute("href") === `#${sectionId}`;
      if (isActive) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    });

    windows.forEach((panel) => {
      const isActive = panel.id === sectionId;
      panel.classList.toggle("active-window", isActive);
      if (isActive) {
        setStatus(`${panel.dataset.window.toUpperCase()} ACTIVE`);
      }
    });
  }

  function observeSections() {
    if (!("IntersectionObserver" in window)) return;
    const sections = navLinks
      .map((link) => document.querySelector(link.getAttribute("href")))
      .filter(Boolean);
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          setActiveSection(entry.target.id);
        }
      });
    }, { rootMargin: "-35% 0px -50% 0px", threshold: 0.01 });
    sections.forEach((section) => observer.observe(section));
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      const target = link.getAttribute("href").slice(1);
      if (target) setActiveSection(target);
    });
  });

  windows.forEach((panel) => {
    panel.addEventListener("focusin", () => setActiveSection(panel.id));
    panel.addEventListener("mouseenter", () => {
      if (!reducedMotion.matches) setStatus(`${panel.dataset.window.toUpperCase()} READY`);
    });
  });

  runBootLine();
  observeSections();
  updateClock();
  if (localTime) window.setInterval(updateClock, 30000);
})();
