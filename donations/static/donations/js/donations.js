var otherValue = document.getElementById('other-value');

otherValue.addEventListener("click", uncheckRadio);

function uncheckRadio() {
    var radio = document.querySelector('input[type=radio]:checked');
    radio.checked = false;
}