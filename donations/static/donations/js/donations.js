var amountCustom = document.getElementById('amount-custom');

var giftAidExplanationButton = document.getElementById("gift-aid-info-button");

var giftAidExplanationParagraph = document.getElementById("gift-aid-explanation");

var detailsInfoButton = document.getElementById("details-info-button");

var detailsInfo = document.getElementById("details-info");

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
    
    if (giftAidExplanationParagraph.style.display === "none") {
        giftAidExplanationParagraph.style.display = "block";
    } else {
        giftAidExplanationParagraph.style.display = "none";
    }
}

function showDetailsExplanation() {

    if (detailsInfo.style.display === "none") {
        detailsInfo.style.display = "block";
    } else {
        detailsInfo.style.display = "none";
    }
}