
$(function(){
  $('#paste').click(function(){pasteSelection();});
});
function pasteSelection() {
  chrome.tabs.query({active:true, windowId: chrome.windows.WINDOW_ID_CURRENT}, 
  function(tab) {
    chrome.tabs.sendMessage(tab[0].id, {method: "getSelection"}, 
    function(response){
      window.open("http://www.studynotejs.com/index.html?call='" + response.data + "'"); 
    });
  });
}