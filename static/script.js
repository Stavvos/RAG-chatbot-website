const BUTTON = document.getElementById("send-btn");
const DROPDOWN = document.getElementById("drop-down");

function sendMessage() { 
    const userInput = document.getElementById("user-input").value;

    // if user input is empty or only contains spaces return
    if (userInput.trim() === "") return;

    // Append the user's message
    appendMessage(userInput, 'user');

    //reset user input text field and show the user that the server is loading an answer for them
    document.getElementById("user-input").value = "";
    document.getElementById("user-input").placeholder = "Generating answer ...";

    //post the data to the python flask server
    fetch('/chat', {
    	method: 'POST',
	headers: {'Content-Type': 'application/json'},
	body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
	appendMessage(data.reply, 'bot');
        document.getElementById("user-input").placeholder = "How can i help you?";
    });
}

function appendMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    messageDiv.textContent = message;

    const chatBox = document.getElementById("chat-box");
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
}

DROPDOWN.addEventListener('change', function(e) {
  document.getElementById("user-input").value = DROPDOWN.value;
});

//call sendMessage() when send button is clicked
BUTTON.addEventListener('click', function(e){
    sendMessage();
});

//call sendMessage function when enter key is pressed
document.addEventListener('keypress', function(e){
  if(e.key === 'Enter'){
      sendMessage();
  }
});
