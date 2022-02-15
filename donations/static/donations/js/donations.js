var otherValue = document.getElementById('amount-custom');

console.log(typeof otherValue);

otherValue.addEventListener("click", uncheckRadio);

function uncheckRadio() {
    var radio = document.querySelector('input[type=radio]:checked');
    radio.checked = false;
}