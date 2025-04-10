document.addEventListener('DOMContentLoaded', function(){
  console.log("Chat Application Loaded");
  setInterval(fetchMessages, 3000);
});

function fetchMessages() {
  fetch('/api/messages')
    .then(response => response.json())
    .then(data => {
      const chat = document.getElementById('chat');
      chat.innerHTML = '';
      data.forEach(function(msg) {
        const li = document.createElement('li');
        li.innerHTML = '<strong>' + msg.username + ':</strong> ' + msg.message;
        chat.appendChild(li);
      });
    });
}