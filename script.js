document.addEventListener('DOMContentLoaded', () => {
  // do something here too but in JS

  // I guess we're going to open a websocket connection if it's available and start reading from the data
  // let's also work out how we're going to display the data if we have it
  
  function openWebSocket() {
    const webSocketURL = "ws://0.0.0.0:8000";

    try {
      const webSocket = new WebSocket(webSocketURL);

      webSocket.onopen = function(openEvent) {
        console.log("WebSocket is now open", JSON.stringify(openEvent, null, 4));
      }
      webSocket.onerror = function(errorEvent) {
        console.error("WebSocket encountered a problem", JSON.stringify(errorEvent, null, 4));
      }
      webSocket.onmessage = function(messageEvent) {
        // this is the clever thing
        const wsMsg = messageEvent.data;
        console.log("WebSocket message", wsMsg);
      }

    } catch (exception) {
      console.error(exception);
    }
  }
  // openWebSocket();

  // data things
  
  // DOM things
  const canvas = document.getElementById('canvas');

  // a loop?
    // then iterate through some sort of json data to get the values we're looking for
});
