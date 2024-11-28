//Buttons Working 

//Buttons Working 
document.querySelector('.nav-desktop button:nth-child(1)').addEventListener('click', function() {
  document.getElementById('home').scrollIntoView({ behavior: 'smooth' });
});

document.querySelector('.nav-desktop button:nth-child(2)').addEventListener('click', function() {
  document.getElementById('features').scrollIntoView({ behavior: 'smooth' });
});

document.querySelector('.nav-desktop button:nth-child(3)').addEventListener('click', function() {
  document.getElementById('explore').scrollIntoView({ behavior: 'smooth' });
});

document.querySelector('.nav-desktop button:nth-child(4)').addEventListener('click', function() {
  document.getElementById('about').scrollIntoView({ behavior: 'smooth' });
});

function redirectToUpload() {
  window.location.href = "index.html"; 
}
