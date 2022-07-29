'use strict';

// Get the color list from html
const animal_lst = document.querySelectorAll('.animal_display');
let animals = []
for (const animal of animal_lst) {
  const pet = animal.innerText;
  animals.push(pet);
}
console.log(animals);


// Calling Web Speech APIs

const SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
const SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList;
const SpeechRecognitionEvent = window.SpeechRecognitionEvent || webkitSpeechRecognitionEvent;

const recognition = new SpeechRecognition();
const speechRecognitionList = new SpeechGrammarList();
const grammar = '#JSGF V1.0; grammar animals; public <animal> = ' + animals.join(' | ') + ' ;'
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;

recognition.continuous = false;
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

const diagnostic = document.querySelector('.output');
const bg = document.querySelector('.color_change');

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
  let animal = event.results[0][0].transcript;
  animal = animal.toLowerCase();
  diagnostic.textContent = 'Result received: ' + animal + '.';
  if (animals.includes(animal)) {
    // bg.style.backgroundanimal = animal;
    console.log('Confidence: ' + event.results[0][0].confidence);
  } else {
    console.log("Animal is not in the lesson.");
  }
}

recognition.onspeechend = function () {
  recognition.stop();
}

recognition.onnomatch = function (event) {
  diagnostic.textContent = "I didn't recognise that animal.";
}

recognition.onerror = function (event) {
  diagnostic.textContent = 'Error occurred in recognition: ' + event.error;
}