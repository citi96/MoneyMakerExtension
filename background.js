chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        console.log(sender.tab ?
            "from a content script:" + sender.tab.url :
            "from the extension");

        downloadFile({
            filename: "Info.txt",
            content: request.values
        });
    }
);

function downloadFile(options) {
    try {
        if (!options.url) {
            var blob = new Blob([options.content], { type: "text/plain;charset=UTF-8" });
            options.url = window.URL.createObjectURL(blob);
        }

        chrome.downloads.download({
            url: options.url,
            filename: options.filename
        })
    } catch (error) {
        console.log(error);
    }
}