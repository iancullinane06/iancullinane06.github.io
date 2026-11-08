(() => {
  const definitions = document.querySelector(".definitions");
  if (definitions) {
    const toggle = definitions.querySelector(".definitions-toggle");
    toggle.addEventListener("click", () => {
      const open = definitions.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    document.addEventListener("click", (event) => {
      if (!definitions.contains(event.target)) {
        definitions.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
    definitions.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        definitions.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.blur();
      }
    });
  }

  const toc = document.querySelector("[data-page-toc]");
  if (toc) {
    document.querySelectorAll("#main-content h2[id]").forEach((heading) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = `#${encodeURIComponent(heading.id)}`;
      link.textContent = heading.textContent;
      item.append(link);
      toc.append(item);
    });
  }

  document.querySelectorAll("#main-content pre").forEach((pre) => {
    const code = pre.querySelector("code");
    if (!code) return;

    const wrapper = document.createElement("div");
    wrapper.className = "code-block";
    pre.before(wrapper);
    wrapper.append(pre);

    const button = document.createElement("button");
    button.className = "copy-button";
    button.type = "button";
    button.textContent = "Copy";
    button.setAttribute("aria-label", "Copy code");
    wrapper.prepend(button);
    button.addEventListener("click", async () => {
      try {
        if (!navigator.clipboard || !navigator.clipboard.writeText) {
          throw new Error("Clipboard access is unavailable");
        }
        await navigator.clipboard.writeText(code.textContent);
        button.textContent = "Copied!";
        button.setAttribute("aria-label", "Code copied");
      } catch (error) {
        button.textContent = "Copy failed";
        button.setAttribute("aria-label", "Copy failed; select the code to copy it manually");
        console.error("Could not copy code:", error);
      }
      window.setTimeout(() => {
        button.textContent = "Copy";
        button.setAttribute("aria-label", "Copy code");
      }, 2500);
    });
  });

  const search = document.querySelector(".docs-search");
  if (!search) return;
  const input = search.querySelector("input");
  const panel = search.querySelector(".search-panel");
  const results = search.querySelector("#docs-search-results");
  const status = search.querySelector("#docs-search-status");
  let indexPromise;
  let queryVersion = 0;
  const normalize = (text) => text.toLocaleLowerCase().replace(/\s+/g, " ").trim();

  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch(search.dataset.indexUrl).then((response) => {
        if (!response.ok) throw new Error(`Search index returned ${response.status}`);
        return response.json();
      }).catch((error) => {
        indexPromise = null;
        throw error;
      });
    }
    return indexPromise;
  }

  async function updateSearch() {
    const version = ++queryVersion;
    const query = normalize(input.value);
    results.replaceChildren();
    panel.hidden = !query;
    if (!query) return;
    status.textContent = "Searching…";
    try {
      const pages = await loadIndex();
      if (version !== queryVersion) return;
      const terms = query.split(" ");
      const matches = pages.map((page) => {
        const content = normalize(`${page.title} ${page.content}`);
        return { ...page, content, titleMatch: normalize(page.title).includes(query) };
      }).filter((page) => terms.every((term) => page.content.includes(term)))
        .sort((a, b) => Number(b.titleMatch) - Number(a.titleMatch));
      status.textContent = matches.length ? `${matches.length} ${matches.length === 1 ? "page" : "pages"} found` : "No matching pages found.";
      matches.forEach((match) => {
        const item = document.createElement("li");
        const link = document.createElement("a");
        const title = document.createElement("strong");
        const excerpt = document.createElement("span");
        const position = Math.max(0, match.content.indexOf(terms[0]) - 45);
        link.href = match.url;
        title.textContent = match.title;
        excerpt.textContent = `${position ? "…" : ""}${match.content.slice(position, position + 120)}…`;
        link.append(title, excerpt);
        item.append(link);
        results.append(item);
      });
    } catch (error) {
      if (version !== queryVersion) return;
      status.textContent = "Search is unavailable. Try again.";
      console.error("Could not load the documentation search index:", error);
    }
  }

  input.addEventListener("input", updateSearch);
  input.addEventListener("focus", () => {
    if (input.value.trim()) updateSearch();
  });
  search.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      panel.hidden = true;
      input.blur();
    }
  });
  document.addEventListener("click", (event) => {
    if (!search.contains(event.target)) panel.hidden = true;
  });
})();
