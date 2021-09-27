/**
 * Gets the desired element on the client page and clicks on it
 */
function goToActivityTab() {
    var oElement = document.getElementsByClassName("roulette-table-cell_side-top-column")[0];
    var rect = oElement.getBoundingClientRect();
    console.log(rect.left, rect.top, rect.right, rect.bottom);
}

goToActivityTab();
