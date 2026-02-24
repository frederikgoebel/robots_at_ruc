const socket = new WebSocket("ws://localhost:8765");

socket.addEventListener("open", function (event) {
  console.log("WS opened")
});

let received = null;
socket.addEventListener("message", function (event) {
  console.log("Message from server ", event.data);
  received = JSON.parse(event.data);
});

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  if (received) {
    text(received.actual_TCP_force, 50, 50);
    received = null;
  } 

  let scaledX = lerp(-0.2, 0.2, norm(mouseX, 0, width));
  let scaledY = lerp(-0.4, -0.5, norm(mouseY, 0, height));
  package = [scaledX, scaledY, 0.8477664870021936, 0.3206479995337188, -1.781478746031787, 1.7264157201986214]
  console.log("to send:", package);

  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify(package));
  }
  
  circle(mouseX,mouseY, 20);
}
