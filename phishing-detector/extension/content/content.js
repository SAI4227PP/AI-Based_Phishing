function collectPageSignals() {
  const html = document.documentElement.outerHTML;
  const hiddenForms = document.querySelectorAll("form[style*='display:none'], form[hidden]").length;
  const iframes = document.querySelectorAll("iframe").length;
  const hasRightClickBlock = html.toLowerCase().includes("contextmenu");
  const hasMouseoverTrap = html.toLowerCase().includes("onmouseover");

  return {
    url: window.location.href,
    html,
    extensionSignals: {
      hiddenForms,
      iframes,
      hasRightClickBlock,
      hasMouseoverTrap
    }
  };
}

chrome.runtime.sendMessage(
  {
    type: "CONTENT_SCAN",
    payload: collectPageSignals()
  },
  () => chrome.runtime.lastError
);
