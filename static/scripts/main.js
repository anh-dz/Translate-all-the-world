$(function() {
  //Translate text with flask route
  $("#translate").on("click", function(e) {
    e.preventDefault();
    var translateVal = document.getElementById("text-to-translate").value;
    var languageInp = document.getElementById("lang-input").value;
    languageVal = document.getElementById("select-language").value;
    var translateRequest = { 'slang': languageInp, 'text': translateVal, 'to': languageVal }

    if (translateVal !== "") {
      $.ajax({
        url: '/translate-text',
        method: 'POST',
        headers: {
          'Content-Type':'application/json'
        },
        dataType: 'json',
        data: JSON.stringify(translateRequest),
        success: function(data) {
          document.getElementById("translation-result").textContent = data[0];
          document.getElementById("detected-language-result").textContent = data[1];
          if (document.getElementById("detected-language-result").textContent !== ""){
            document.getElementById("detected-language").style.display = "block";
          }

          // Append translation to history table
          var historyTableBody = document.getElementById("history-table-body");
          var newRow = historyTableBody.insertRow();
          var textToTranslateCell = newRow.insertCell(0);
          var translatedTextCell = newRow.insertCell(1);
          var buttonCell = newRow.insertCell(2);

          // Generate a unique row id
          var rowIndex = historyTableBody.rows.length - 1;
          var rowId = 'row-' + rowIndex;

          // Set the id attribute of the row
          newRow.id = rowId;

          textToTranslateCell.textContent = translateVal;
          translatedTextCell.textContent = data[0];
          buttonCell.innerHTML = '<button class="btn btn-primary" style="color: white; background-color: red; border: 0px;" onclick="highlightRow(this)">Đánh dấu</button>';
        }
      });
    };
  });

  // Convert text-to-speech
  $("#text-to-speech").on("click", function(e) {
    e.preventDefault();
    var ttsInput = document.getElementById("translation-result").value;
    var ttsVoice = languageVal;
    var ttsRequest = { 'text': ttsInput, 'voice': ttsVoice }

    var xhr = new XMLHttpRequest();
    xhr.open('post', '/text-to-speech', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.responseType = "blob";
    xhr.onload = function(evt){
      if (xhr.status === 200) {
        audioBlob = new Blob([xhr.response], {type: "audio/mpeg"});
        audioURL = URL.createObjectURL(audioBlob);
        if (audioURL.length > 5){
          var audio = document.getElementById('audio');
          var source = document.getElementById('audio-source');
          source.src = audioURL;
          audio.load();
          audio.play();
        }else{
          console.log("An error occurred getting and playing the audio.")
        }
      }
    }
    xhr.send(JSON.stringify(ttsRequest));
  });
});

function highlightRow(button) {
  var row = button.parentNode.parentNode;
  row.classList.toggle("yellow-row");
}