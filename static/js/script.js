'use strict';

// Get the animal list from html to make speechRecognition grammar
const word_lst = document.querySelectorAll('.word_display');
let words = []
for (const word of word_lst) {
  const pet = word.innerText;
  words.push(pet);
}
console.log(words);


// Calling Web Speech APIs

const SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
const SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList;
const SpeechRecognitionEvent = window.SpeechRecognitionEvent || webkitSpeechRecognitionEvent;

const recognition = new SpeechRecognition();
const speechRecognitionList = new SpeechGrammarList();
const grammar = '#JSGF V1.0; grammar words; public <word> = ' + words.join(' | ') + ' ;'
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;

recognition.continuous = false;
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

const diagnostic = document.querySelector('.output');
const image = document.querySelector('.word_result img');

document.body.onclick = function () {
  recognition.start();
  console.log('Ready to receive a color command.');
}

recognition.onresult = function (event) {
  // The SpeechRecognitionEvent results property returns a SpeechRecognitionResultList object
  // The SpeechRecognitionResultList object contains SpeechRecognitionResult objects.
  // It has a getter so it can be accessed like an array
  // The first [0] returns the SpeechRecognitionResult at the last position.
  // Each SpeechRecognitionResult object contains SpeechRecognitionAlternative objects that contain individual results.
  // These also have getters so they can be accessed like arrays.
  // The second [0] returns the SpeechRecognitionAlternative at position 0.
  // We then return the transcript property of the SpeechRecognitionAlternative object
  let word = event.results[0][0].transcript;
  word = word.toLowerCase();
  diagnostic.textContent = 'Result received: ' + word + '.';
  if (words.includes(word)) {
    image.setAttribute('src', document.querySelector(`#hidden_word_${word}`).value);
    console.log('Confidence: ' + event.results[0][0].confidence);
  } else {
    image.setAttribute('src', '');
    console.log("Word is not in the lesson.");
  }
}

recognition.onspeechend = function () {
  recognition.stop();
}

recognition.onnomatch = function (event) {
  diagnostic.textContent = "I didn't recognise that word.";
}

recognition.onerror = function (event) {
  diagnostic.textContent = 'Error occurred in recognition: ' + event.error;
}