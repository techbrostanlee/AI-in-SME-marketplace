document.addEventListener("DOMContentLoaded", function () {
    // Checkout button logic
    document.getElementById("checkout-btn").addEventListener("click", function () {
        fetch("/is_logged_in")  // Check if the user is logged in
            .then(response => response.json())
            .then(data => {
                if (data.logged_in) {
                    window.location.href = "/checkout";  // Proceed to checkout
                } else {
                    window.location.href = "/login";  // Redirect to login/signup
                }
            })
            .catch(error => console.error("Error checking login status:", error));
    });
});

// Function to remove item from cart
function removeFromCart(productId) {
    fetch("/remove_from_cart", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ product_id: productId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.reload();  // Reload page to update cart
        } else {
            alert("Error removing item from cart.");
        }
    })
    .catch(error => console.error("Error removing item:", error));
}
