const giftAidExplanationButton = document.getElementById("gift-aid-info-button");

const giftAidExplanationParagraph = document.getElementById("gift-aid-explanation");

const detailsInfoButton = document.getElementById("details-info-button");

const detailsInfo = document.getElementById("details-info");

$('#details-info-button').click(function() {
    event.preventDefault();
    $('#details-info').toggle('fast');
});

$('#gift-aid-info-button').click(function() {
    event.preventDefault();
    $('#gift-aid-explanation').toggle('fast');
});