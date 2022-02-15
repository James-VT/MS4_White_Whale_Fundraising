var amountCustom = document.getElementById('amount-custom');

console.log(typeof amountCustom);

amountCustom.addEventListener("click", uncheckRadio);

function uncheckRadio() {
    // var radio = document.querySelector('input[type=radio]:checked');
    // radio.checked = false;
    // }

    if (document.querySelector('input[type=radio]:checked')) {
        var radio = document.querySelector('input[type=radio]:checked');
        radio.checked = false;
    }
}