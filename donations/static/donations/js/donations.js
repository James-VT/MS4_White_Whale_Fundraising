var amountCustom = document.getElementById('amount-custom');

const giftAidExplanationButton = document.getElementById("gift-aid-info-button");

const giftAidExplanationParagraph = document.getElementById("gift-aid-explanation");

const detailsInfoButton = document.getElementById("details-info-button");

const detailsInfo = document.getElementById("details-info");

detailsInfoButton.addEventListener("click", showDetailsExplanation);

giftAidExplanationButton.addEventListener("click", showGiftAidExplanation);

amountCustom.addEventListener("click", uncheckRadio);

function uncheckRadio() {

    if (document.querySelector('input[type=radio]:checked')) {
        var radio = document.querySelector('input[type=radio]:checked');
        radio.checked = false;
    }
}

function showGiftAidExplanation() {

    giftAidExplanationParagraph.classList.toggle("gift-aid-explanation-class");

}

function showDetailsExplanation() {
    
    detailsInfo.classList.toggle("details-info-class");

}