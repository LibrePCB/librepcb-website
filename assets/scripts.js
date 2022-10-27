function uncloakMail() {
  var spans = document.getElementsByClassName("cloaked-mail");
  for (var span of spans) {
    const user = span.getAttribute("data-user").split("").reverse().join("");
    const domain = span
      .getAttribute("data-domain")
      .split("")
      .reverse()
      .join("");
    const address = user + "@" + domain;
    var link = document.createElement("a");
    link.href = "mailto:" + address;
    link.innerText = address;
    span.parentElement.insertBefore(link, span);
    span.parentElement.removeChild(span);
  }
}

function getOS() {
  var userAgent = window.navigator.userAgent,
    platform =
      window.navigator?.userAgentData?.platform || window.navigator.platform,
    macosPlatforms = ["Macintosh", "MacIntel", "MacPPC", "Mac68K"],
    windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"],
    os = null;

  if (macosPlatforms.indexOf(platform) !== -1) {
    os = "macos";
  } else if (windowsPlatforms.indexOf(platform) !== -1) {
    os = "windows";
  } else if (/Linux/.test(platform)) {
    os = "linux";
  }

  return os;
}

function disableOtherDownloadButtons() {
  var os = getOS();
  if (os) {
    var buttons = document.getElementsByClassName("btn-download");
    for (var button of buttons) {
      if (!button.classList.contains(os)) {
        button.classList.remove("btn-primary");
        button.classList.add("btn-outline-primary");
      } else {
        button.classList.add("btn-lg");
      }
    }
  }
}

function showDownloadDialog() {
  const dialog = new bootstrap.Modal("#download-dialog");
  dialog.show();
}

function registerDownloadDialog() {
  var links = document.getElementsByClassName("download-link");
  for (var link of links) {
    link.setAttribute("onclick", "showDownloadDialog()");
  }
}

uncloakMail();
disableOtherDownloadButtons();
registerDownloadDialog();
