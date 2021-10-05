chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        console.log(sender.tab ?
            "from a content script:" + sender.tab.url : 
            "from the extension");
        
        downloadFile({
            filename: "Info.txt",
            content: request.values
        });
    }
);

chrome.runtime.onInstalled.addListener(() => {

//declarativeContent is needed when popup should be opened
    chrome.declarativeContent.onPageChanged.removeRules(undefined, () => {
        chrome.declarativeContent.onPageChanged.addRules([{
            conditions: [new chrome.declarativeContent.PageStateMatcher({

            })
        ],
            actions: [new chrome.declarativeContent.ShowPageAction()]
         }])
    });

});

//load key which is logged at popup.js
chrome.storage.local.get(['key'], function(result) {
    console.log('value currently is ' + result.key);
});

function downloadFile(options) {
    try {
        console.log("In download method");

        if(!options.url) {
            var blob = new Blob([ options.content ], {type : "text/plain;charset=UTF-8"});
            options.url = window.URL.createObjectURL(blob);

            console.log(options.url);
        }

        chrome.downloads.download({
            url: options.url,
            filename: options.filename
        })

        console.log("Downloaded"); 
    } catch (error) {
        console.log(error);
    }
}
