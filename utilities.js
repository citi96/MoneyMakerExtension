var isStarted = true;

function goToActivityTab() {
    try {
        if (!isStarted) return;
        var topColElement = document.getElementsByClassName("roulette-table-cell_side-top-column")[0];
        var midColElement = document.getElementsByClassName("roulette-table-cell_side-middle-column")[0];
        var botColElement = document.getElementsByClassName("roulette-table-cell_side-bottom-column")[0];

        var topColRect = topColElement.getBoundingClientRect();
        var midColRect = midColElement.getBoundingClientRect();
        var botColRect = botColElement.getBoundingClientRect();

        var lastDrawElement = document.getElementsByClassName("roulette-history-item__value-text4i5PljD88Up2neJ6jtn4S")[0];

        var messageElement = document.getElementsByClassName("dealer-message-text")[0];

        chrome.runtime.sendMessage({
            values:
                "Message: " + messageElement.textContent +
                "\nTopColumn: " + [topColRect.left, topColRect.top].toString() +
                "\nMidColumn: " + [midColRect.left, midColRect.top].toString() +
                "\nBotColumn: " + [botColRect.left, botColRect.top].toString() +
                "\nLastDraw:  " + lastDrawElement.textContent
        }, function (response) {
        });
    } catch (error) {
        console.log(error);
    } finally {
        if (isStarted) {
            setTimeout(goToActivityTab, 5000);
        }
    }
}

chrome.storage.local.get('isStarted', function (items) {
    if (items.isStarted) {
        this.isStarted = true;
        goToActivityTab();
    } else {
        this.isStarted = false;
    }
});
