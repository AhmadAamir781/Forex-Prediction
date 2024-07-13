function toggleDarkLightMode() {
  var body = document.body;
  var container__ = document.querySelector('.container__');
  var darkModeIcon = document.getElementById('dark-mode-icon');
  var lightModeIcon = document.getElementById('light-mode-icon');
  var additional_content = document.getElementById('additional_content');

  body.classList.toggle("dark-mode");
  container__.classList.toggle("dark-mode-container");

  var isDarkMode = body.classList.contains('dark-mode');

  if (isDarkMode) {
      localStorage.setItem('darkModeEnabled', 'true');
  } else {
      localStorage.removeItem('darkModeEnabled');
  }

  if (isDarkMode) {
      darkModeIcon.style.display = 'none';
      lightModeIcon.style.display = 'inline';
      container__.style.backgroundColor = '#333';
      container__.style.color = '#fff';
      additional_content.style.color = '#fff';
      body.style.backgroundColor = '#000';
      body.style.color = '#fff';
  } else {
      darkModeIcon.style.display = 'inline';
      lightModeIcon.style.display = 'none';
      container__.style.backgroundColor = '#fff';
      container__.style.color = '#333';
      additional_content.style.color = '#333';
      body.style.backgroundColor = '#fff';
      body.style.color = '#333';
  }
}

document.addEventListener('DOMContentLoaded', function() {
  var darkModeEnabled = localStorage.getItem('darkModeEnabled');

  if (darkModeEnabled === 'true') {
      toggleDarkLightMode();
  }
});

document.getElementById('prediction-form').addEventListener('submit', function() {
  document.querySelector('.loader-container').style.display = 'block';
});

window.addEventListener('load', function() {
  document.querySelector('.loader-container').style.display = 'none';
});

function showLoader() {
  document.getElementById('loader-container').style.display = 'block';
}

function displayPredictionPlot() {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/fetch_prediction_plot", true);
  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          var response = JSON.parse(xhr.responseText);
          document.getElementById('prediction-plot-container').innerHTML = response.prediction_plot;
      }
  };
  xhr.send();
}

function togglePredictionVisibility() {
  var predictionDiv = document.querySelector('.prediction11');
  predictionDiv.style.display = 'block';
}

