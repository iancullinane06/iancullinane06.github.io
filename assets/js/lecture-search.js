(() => {
  const input = document.querySelector("#lecture-search");
  const list = document.querySelector("#lecture-list");
  const status = document.querySelector("#lecture-search-status");

  if (!(input instanceof HTMLInputElement) || !(list instanceof HTMLUListElement) || !(status instanceof HTMLElement)) {
    return;
  }

  const items = Array.from(list.querySelectorAll("li"));
  const normalize = (text) => text.toLocaleLowerCase().replace(/\s+/g, " ").trim();

  const entries = items.map((item, index) => {
    const content = item.dataset.searchContent || "";
    let topics = "";
    const markdownHeading = /^#{1,6}\s+Topics\s*$/im.exec(content);

    if (markdownHeading) {
      const afterTopics = content.slice(markdownHeading.index + markdownHeading[0].length);
      const nextHeading = /^#{1,6}\s+/m.exec(afterTopics);
      topics = normalize(nextHeading ? afterTopics.slice(0, nextHeading.index) : afterTopics);
    } else {
      const htmlHeading = /<h[1-6]\b[^>]*>\s*Topics\s*<\/h[1-6]>/i.exec(content);

      if (htmlHeading) {
        const afterTopics = content.slice(htmlHeading.index + htmlHeading[0].length);
        const nextHeading = /<h[1-6]\b[^>]*>/i.exec(afterTopics);
        topics = normalize(nextHeading ? afterTopics.slice(0, nextHeading.index) : afterTopics);
      }
    }

    return {
      item,
      index,
      content: normalize(content),
      topics
    };
  });

  function updateResults() {
    const terms = normalize(input.value).split(" ").filter(Boolean);
    const matches = entries
      .map((entry) => ({
        ...entry,
        matches: terms.every((term) => entry.content.includes(term)),
        topicMatch: terms.some((term) => entry.topics.includes(term))
      }))
      .filter((entry) => entry.matches)
      .sort((a, b) => Number(b.topicMatch) - Number(a.topicMatch) || a.index - b.index);
    const matchingItems = new Set(matches.map((entry) => entry.item));

    for (const entry of matches) {
      list.append(entry.item);
      entry.item.hidden = false;
    }

    for (const entry of entries) {
      if (!matchingItems.has(entry.item)) {
        entry.item.hidden = true;
      }
    }

    status.textContent = terms.length
      ? `${matches.length} ${matches.length === 1 ? "result" : "results"} found. Topic matches are shown first.`
      : `Showing all ${entries.length} notes.`;
  }

  input.addEventListener("input", updateResults);
  updateResults();
})();
