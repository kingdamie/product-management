
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-price]").forEach(function (el) {
        const amount = parseFloat(el.dataset.price);
        if (isNaN(amount)) return;

        el.textContent = "₦" + amount.toLocaleString("en-NG", {
            minimumFractionDigits: 0,
            maximumFractionDigits: 2, 
        });
    });
});
