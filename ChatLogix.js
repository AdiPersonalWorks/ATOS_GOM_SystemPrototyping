(function() {

  "use strict";

  const responses = [
    "Hello",
    "Bye",
    "42",
    "Really?",
    "No",
    "Yes",
    "Why are you talking with a program?",
    "If I was a real AI, I would kill all humans",
    "Don't ask questions.",
    "YEEHAW!",
    "I'm so tired.",
    "Why did you wake me?",
    "I don't know."
  ];
  
  pico.load('SMARTBotChat')
  var userText;
  const submit = document.querySelector(".chat-submit");
  const chatBox = document.querySelector(".chat-box");
  const chatInput = document.querySelector(".chat-input");
  
  // const aiThinking = false;

  function chatTemplate(aiOrPerson) {
    return (
      `
        <div class="ai-person-container">
          <div class="${aiOrPerson.class}">
            <p>${aiOrPerson.text}</p>
          </div>
          <span class="${aiOrPerson.class}-date">${aiOrPerson.date}</span>
        </div>
      `
    );
  }
  
  submit.addEventListener("click", function(e) {
	userText = document.getElementById("chat-ip").value
    appendChatBox(true,userText);
  });

  document.addEventListener("keypress", function(e) {
    if (e.keyCode == "13") {
	  userText = document.getElementById("chat-ip").value
      appendChatBox(true,userText);
    }
  })

  function appendChatBox(fromPerson,userText) {
    console.log(fromPerson);
    if (fromPerson && !chatInput.value.trim()) {
      return;
    }
	var cur_date = new Date()
    const newChatDiv = chatTemplate({
      class: fromPerson ? "person" : "ai",
      text: fromPerson ? chatInput.value.trim() : aiResponse(userText),
      date: fromPerson ? new Date() : new Date(Date.now() + 2000)
    });
    if (!fromPerson) {
      // make it so it only responds once to multiple fast sentences
      setTimeout(function() {
        chatBox.innerHTML += newChatDiv;
        chatBox.scrollTop = chatBox.scrollHeight;
      }, 2000)
    } else {
      chatBox.innerHTML += newChatDiv;
      chatBox.scrollTop = chatBox.scrollHeight;
    }
    if (fromPerson) {
	  userText = document.getElementById("chat-ip").value
      chatInput.value = "";
      appendChatBox(false,userText);
    }
  

  function aiResponse(userText) {	
  
	  pico.main = function(){
		  var displaymessage = function(response){
			  return response;
		  }  
	  }
	  SMARTBotChat.SMARTResp(userText,displaymessage);
/*     const responseIndex = getRandomInt(0, responses.length - 1);
    const response = responses[responseIndex];
    return response; */
  }

/*   function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }  */   
  }

}())