let avatar = "Sniper Roshan";

function selectAvatar(name) {
  avatar = name;
  document.getElementById('selected-avatar').innerText = `Selected: ${name}`;
}

function shoot() {
  fetch('/shoot', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
      document.getElementById('result').innerText = data.message;
      let audio = new Audio(`/static/sounds/${data.result}_hi.mp3`);
      audio.play();
    });
}

setTimeout(() => {
  document.getElementById('splash').style.display = 'none';
}, 3000);
