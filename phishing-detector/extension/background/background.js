async function fetchPageAssessment(tabId, url) {
  try {
    const [{ result }] = await chrome.scripting.executeScript({
      target: { tabId },
      func: () => ({
        html: document.documentElement.outerHTML
      })
    });

    const response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        url,
        html: result.html
      })
    });

    const data = await response.json();
    await chrome.storage.local.set({ latestAssessment: data });

    if (data.risk_score >= 0.7) {
      chrome.action.setBadgeText({ text: "RISK", tabId });
      chrome.action.setBadgeBackgroundColor({ color: "#b91c1c", tabId });
    } else {
      chrome.action.setBadgeText({ text: "", tabId });
    }
  } catch (error) {
    await chrome.storage.local.set({
      latestAssessment: {
        label: "unknown",
        risk_score: 0,
        error: error.message
      }
    });
  }
}

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status !== "complete" || !tab.url?.startsWith("http")) {
    return;
  }

  fetchPageAssessment(tabId, tab.url);
});

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message.type !== "CONTENT_SCAN") {
    return false;
  }

  fetch("http://localhost:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(message.payload)
  })
    .then((response) => response.json())
    .then((data) => {
      chrome.storage.local.set({ latestAssessment: data });
      sendResponse(data);
    })
    .catch((error) => {
      sendResponse({ error: error.message });
    });

  return true;
});
