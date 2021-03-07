document.addEventListener('DOMContentLoaded', () => {
  // do something here too but in JS

  // I guess we're going to open a websocket connection if it's available and start reading from the data
  // let's also work out how we're going to display the data if we have it
  
  const PORT = 9001;
  const PROTOCOL = "ws://";
  const LOCATION = "0.0.0.0";
  let i = 0;
  // DOM things
  const canvas = document.getElementById('canvas');
  const code = document.getElementById('code');

  function openWebSocket() {
    const webSocketURL = PROTOCOL + LOCATION + ":" + PORT + "/";
    try {
      const webSocket = new WebSocket(webSocketURL);

      webSocket.onopen = function(openEvent) {
        console.log("WebSocket is now open", JSON.stringify(openEvent, ["message", "arguments", "type", "name"]));
      }
      webSocket.onerror = function(errorEvent) {
        console.error("WebSocket encountered a problem", JSON.stringify(errorEvent, ["message", "arguments", "type", "name"]));
      }
      webSocket.onmessage = function(messageEvent) {
        const wsMsg = messageEvent.data;
        code.textContent = wsMsg;
      }

    } catch (exception) {
      console.error(exception);
    }
  }
  openWebSocket();

});
