// Below JS for country field taken from CI's Boutique Ado for same

let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#6c6c6c');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#6c6c6c');
    } else {
        $(this).css('color', '#000');
    }
});