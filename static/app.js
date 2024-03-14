function enviarConEnter(event) {
  if (event.key === 'Enter') {
      enviarMensaje(); // Llamar a la función enviarMensaje si la tecla presionada es "Enter"
  }
}

function enviarMensaje() {
  var userInput = document.getElementById("user-input").value;
  var chatBox = document.getElementById("chat-box");

  // Mostrar mensaje del usuario
  chatBox.innerHTML += '<div class="user-message" style="text-align: right; margin-bottom: 10px;">' + userInput + '</div>';

  fetch('/predict', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message: userInput }) // Enviar el mensaje al servidor como JSON
  })
  .then(response => response.json())
  .then(data => {
      // Manejar la respuesta del servidor (en este caso, asumiendo que devuelve un JSON con "answer")
      var respuestaBot = data.answer;
      chatBox.innerHTML += '<div class="bot-message" style="text-align: left; margin-bottom: 10px;">' + respuestaBot + '</div>';
      chatBox.scrollTop = chatBox.scrollHeight;

  })
  .catch(error => {
      console.error('Error:', error);
      // Manejar el error en caso de que ocurra
  });

  //Scroll al final
  chatBox.scrollTop = chatBox.scrollHeight;

  // Limpiar el campo de entrada
  document.getElementById("user-input").value = "";
}

