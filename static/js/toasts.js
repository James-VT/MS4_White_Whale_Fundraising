/**
 * Toast script
 * Credit to Boutique Ado, Bootstrap's toasts demo and (former) fellow student pmeeny
 */

let toastElList = [].slice.call(document.querySelectorAll('.toast'));
        let toastList = toastElList.map(function (toastEl) {
        let option = {
            animation: true,
            autohide: false,
        };
        let bsToast = new bootstrap.Toast(toastEl, option);
        bsToast.show();
});