document.addEventListener("DOMContentLoaded", function () {
  setPypasCliVersion();
});

function setPypasCliVersion() {
  fetch("https://pypi.org/pypi/pypas-cli/json")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const version = data.info.version;
      const versionElement = document.querySelector("#pypas-cli-version");
      if (versionElement) {
        versionElement.textContent = version;
      }
    })
    .catch((error) => {
      console.error("Error fetching pypas-cli version:", error);
    });
}
