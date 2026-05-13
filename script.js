function logEvento(msg) {
  const logDiv = document.getElementById('log');
  const p = document.createElement('p');
  p.textContent = msg;
  logDiv.appendChild(p);
}

function submeti() {
  logEvento("Formulário enviado");
  return false; // impede o envio para teste
}

function resetei() {
  logEvento("Formulário resetado");
}

function saiDoCampo() {
  logEvento("Saí do campo");
}

function mudei() {
  logEvento("Valor do campo foi alterado");
}

function entreiNoCampo() {
  logEvento("Entrei no campo");
}

function selecionei() {
  logEvento("Texto selecionado no campo");
}

function teclaBaixo() {
  logEvento("Tecla pressionada");
}

function teclaCima() {
  logEvento("Tecla liberada");
}

