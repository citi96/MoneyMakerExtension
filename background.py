function background(){
    chrome.runtime.onMessage.addListener(
        function(request, sender, sendResponse) {
            console.log(sender.tab ?
                "from a content script:" + sender.tab.url : 
                "from the extension");
            
            downloadFile({
                filename: "foo.txt",
                content: request.values
            });
      }
    );
}

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