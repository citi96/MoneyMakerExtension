/**
 * Gets the desired element on the client page and clicks on it
 */
function goToActivityTab() {
    try {
        //var oElement = document.getElementsByClassName("roulette-table-cell_side-top-column")[0];
        var element = document.getElementsByClassName("dealer-message-text")[0];
        //var rect = oElement.getBoundingClientRect();
        console.log(element.textContent);
    
        chrome.runtime.sendMessage({values: element.textContent}, function(response) {
            console.log(response.farewell);
        });
    } catch (error) {
        console.log(error);
    }
}

goToActivityTab();
