class Chatbox {
    constructor() {
        // Select DOM elements for buttons and input field
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            inputField: document.querySelector('input')
        }

        // Initial state of the chatbox (closed) and messages array
        this.state = false;
        this.messages = [];
        this.welcome = false; // Tracks if the welcome message has been sent
    }

    display() {
        const {openButton, chatBox, sendButton, inputField} = this.args;

        // Event listener to toggle chatbox state on button click
        openButton.addEventListener('click', () => this.toggleState(chatBox))

        // Event listener for the send button to send a message
        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        // Event listener to send a message when the Enter key is pressed
        inputField.addEventListener("keyup", ({key}) => {
            if (key === "Enter") { this.onSendButton(chatBox) }
        })
    }

    toggleState(chatbox) {
        // Toggle the state of the chatbox (open/closed)
        this.state = !this.state;

        if(this.state) {
            chatbox.classList.add('chatbox--active'); // Add active class to open chatbox

            // Send a welcome message if it hasn't been sent yet
            if (!this.welcome){
                let welcomeMsg = { name: "Bot", message: "Hello! How can I assist you today?" };
                this.messages.push(welcomeMsg);
                this.updateChatText(chatbox); // Update the chat with the welcome message
                this.welcome = true;
            }
        } else {
            chatbox.classList.remove('chatbox--active'); // Remove active class to close chatbox
        }
    }

    onSendButton(chatbox) { 
        // Display the loading dots while processing the message
        chatbox.querySelector('.loading-dots').style.display = 'flex';
        var textField = chatbox.querySelector('input');
        let userInput = textField.value;

        // Alert if the input is empty and stop processing
        if (userInput === "") {
            alert("Please, enter a valid entry.");
            chatbox.querySelector('.loading-dots').style.display = 'none';
            return;
        }

        // Add the user's message to the messages array
        let userMsg = { name: "User", message: userInput };
        this.messages.push(userMsg);

        // Update the chat text before the bot responds
        this.updateChatText(chatbox);
        textField.value = ''; // Clear the input field

        // Send a HTTP POST request to the server with the user's message
        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: userInput }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          }).then(resp => resp.json())
          .then(resp => {
            // Add the bot's response to the messages array
            let botMsg = { name: "Bot", message: resp.answer };
            this.messages.push(botMsg);
            this.updateChatText(chatbox); // Update the chat with the bot's response
            chatbox.querySelector('.loading-dots').style.display = 'none'; // Hide the loading dots

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox);
        });
    }

    updateChatText(chatbox) {
        // Build the HTML for the chat messages
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Bot") {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>';
            } else {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>';
            }
        });

        // Insert the messages HTML into the chatbox
        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}

// Instantiate the Chatbox class and display the chatbox
const chatbox = new Chatbox();
chatbox.display();
