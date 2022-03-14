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

// Below JS for country field taken from CI's Boutique Ado for same

let countrySelected = $('#id_country').val();
if(!countrySelected) {
    $('#id_country').css('color', '#6c6c6c');
};
$('#id_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#6c6c6c');
    } else {
        $(this).css('color', '#000');
    }
});