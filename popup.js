var running = false
chrome.storage.local.get({isStarted : false}, function (items) {
    running = items.isStarted
    updateGraphic(running);

    // adding listener to your button in popup window
    document.getElementById('press').addEventListener('click', injectTheScript);
});

function updateGraphic(running) {
    var textElement = document.getElementById("htwo");
    var buttonElement = document.getElementById("press");

    if (!running) {
        textElement.style.color = "red";
        textElement.textContent = "Stopped";
        buttonElement.textContent = "Start";
    } else {
        textElement.style.color = "green";
        textElement.textContent = "Started";
        buttonElement.textContent = "Stop";
    }
}

function injectTheScript() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        running = !running;

        // Injects JavaScript code into a page
        chrome.storage.local.set({
            isStarted: running
        }, function () {
            chrome.tabs.executeScript(tabs[0].id, { file: 'utilities.js' });
            updateGraphic(running);
        });
    });
}