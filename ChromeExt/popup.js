
$(function(){
  $('#paste').click(function(){pasteSelection();});
});
function pasteSelection() {
  chrome.tabs.query({active:true, windowId: chrome.windows.WINDOW_ID_CURRENT}, 
  function(tab) {
    chrome.tabs.sendMessage(tab[0].id, {method: "getSelection"}, 
    function(response){
      window.open("file:///C:/Users/tchristovich/Documents/.%20SWAMPHACKS%202016/GIT/index.html?call='" + response.data + "'"); 
    });
  });
}