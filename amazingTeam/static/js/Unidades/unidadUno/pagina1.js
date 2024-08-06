// Script para arrastrar y soltar letras en el área del nombre y el hechizo
document.querySelectorAll('.drag-item').forEach(item => {
    item.addEventListener('dragstart', dragStart);
});

document.querySelectorAll('.abecedario td').forEach(item => {
    item.addEventListener('dragstart', dragStart);
});

document.querySelectorAll('#drop-area-name, #drop-area-spell').forEach(area => {
    area.addEventListener('dragover', dragOver);
    area.addEventListener('drop', drop);
});

function dragStart(event) {
    event.dataTransfer.setData('text/plain', event.target.textContent);
    event.dataTransfer.setData('color', window.getComputedStyle(event.target).backgroundColor);
}

function dragOver(event) {
    event.preventDefault();
}

function drop(event) {
    event.preventDefault();
    const letter = event.dataTransfer.getData('text/plain');
    const color = event.dataTransfer.getData('color');

    // Crea un nuevo elemento para la letra arrastrada
    const span = document.createElement('span');
    span.textContent = letter;
    span.classList.add('drag-item');
    span.style.backgroundColor = color;
    span.style.color = '#333'; // Color del texto para contraste

    // Añadir funcionalidad para arrastrar dentro del área de caída
    span.setAttribute('draggable', 'true');
    span.addEventListener('dragstart', dragStart);
    span.addEventListener('click', removeLetter); // Permitir eliminación de letras

    event.target.appendChild(span);
}

function removeLetter(event) {
    event.target.remove();
}

