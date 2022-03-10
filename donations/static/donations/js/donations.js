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

/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');

var style = {
    base: {
        color: '#000',
        fontFamily: "'Roboto', sans-serif;'",
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

card.mount('#card-element', {style: style});