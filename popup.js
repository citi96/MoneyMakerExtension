//Start and Stop buttons for logging
const btnStart = document.getElementById("click-start");
const btnStop = document.getElementById("click-stop");

//attempt to get start/stop logging buttons to work--underwork
function Logger(isLogging) {
    console.log(isLogging)
        let logger =''
        if (isLogging){
        
        btnStart.style.display= "block";
        btnStop.style.display= "none";
        
        logger = 'logging' 

    } else {
        
        btnStart.style.display= "none";
        btnStop.style.display= "block";

        logger = 'not logging'
    }
                chrome.storage.local.set({key: logger}, function() {
    console.log('value is set to  ' + logger);

})
}
addRow();

//button to start/stop logging
document.addEventListener("DOMContentLoaded", function () {
    btnStart.addEventListener("click", function() {Logger(true)}); 
    btnStop.addEventListener("click", function() {Logger(false)});
});


//using storage API to save data for last btn pressed--underwork
chrome.storage.local.set({key: Logger()}, function() {
    console.log('value is set to  ' + Logger());
});

chrome.storage.local.get(['key'], function(result) {
    console.log('value currently is ' + result.key);
});

//function to append row to HTML table 
function addRow() {
    const bg = chrome.extension.getBackgroundPage()   
        console.log(bg)

        // Used tabs.query for getBackgroundPage 
        // url is got from tabs.query

   // Object.keys(bg.get).forEach(function (url) {
  chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
          let url = tabs[0].url;
    //get html table
        // Append product to the table
           var table = document.getElementById("tbodyID");
            console.log('heelo')

            var arr = url.split("/");
            var protocoll = arr[0] + "//" + arr[2];

            //inputed data --
            browser= "Google Chrome";
            protocol = protocoll;
            downloads = "example";
            description = "example";
            time = Date.now();


        //put dates in array and replace it and have var as myDate
    // add new row to the table
                  //1 = in the top 
                  //table.rows.length = the end
                  //table.rows.length/2+1 = the center 

            var newRow = table.insertRow(0);

            console.log(table.rows.length)

                  // add cells to the row
                  var browserCell = newRow.insertCell(0);
                  var timeCell = newRow.insertCell(1);
                  var urlCell = newRow.insertCell(2);
                  var protocolCell = newRow.insertCell(3);
                  var downloadsCell = newRow.insertCell(4);
                  var descCell = newRow.insertCell(5);

                  // add the data to the cells

                  urlCell.innerHTML = `${url}`;
                  timeCell.innerHTML = time;
                    browserCell.innerHTML = browser;
                    descCell.innerHTML = description;
                    protocolCell.innerHTML = protocol;
                    downloadsCell.innerHTML = downloads;
                  console.log("works");
     })
            }
