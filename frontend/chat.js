async function sendMessage() {
    const inputBox = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    
    const userText = inputBox.value;
    if (!userText.trim()) return;
    
    chatBox.innerHTML += `<p><b>You:</b> ${userText}</p>`;
    inputBox.value = '';
    
    const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({query: userText})
    });
    
    const data = await response.json();
    chatBox.innerHTML += `<p><b>Asha:</b> ${data.response}</p>`;
    
    chatBox.scrollTop = chatBox.scrollHeight;
}
