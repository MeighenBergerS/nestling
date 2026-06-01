var copyIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>';
var checkIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("pre code").forEach(function (code) {
    var wrapper = document.createElement("div");
    wrapper.className = "clipboard";

    var button = document.createElement("button");
    button.className = "btn-clipboard";
    button.title = "Copy to clipboard";
    button.innerHTML = copyIcon;

    wrapper.appendChild(button);
    code.insertAdjacentElement("beforebegin", wrapper);
  });

  var clipboard = new ClipboardJS(".btn-clipboard", {
    target: function (trigger) {
      return trigger.closest(".clipboard").nextElementSibling;
    }
  });

  clipboard.on("success", function (e) {
    e.clearSelection();
    e.trigger.innerHTML = checkIcon;
    setTimeout(function () { e.trigger.innerHTML = copyIcon; }, 2000);
  });
});
