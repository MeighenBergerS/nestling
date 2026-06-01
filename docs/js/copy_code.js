document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("pre").forEach(function (pre) {
    var wrapper = document.createElement("div");
    wrapper.className = "clipboard";

    var button = document.createElement("button");
    button.className = "btn-clipboard";
    button.title = "Copy to clipboard";
    button.textContent = "Copy";

    wrapper.appendChild(button);
    pre.insertBefore(wrapper, pre.firstChild);

    button.addEventListener("click", function () {
      var code = pre.querySelector("code");
      var text = code ? code.innerText : pre.innerText;

      navigator.clipboard.writeText(text).then(function () {
        button.textContent = "Copied!";
        setTimeout(function () { button.textContent = "Copy"; }, 2000);
      }).catch(function () {
        var textarea = document.createElement("textarea");
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand("copy");
        document.body.removeChild(textarea);
        button.textContent = "Copied!";
        setTimeout(function () { button.textContent = "Copy"; }, 2000);
      });
    });
  });
});
