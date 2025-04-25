document.addEventListener("DOMContentLoaded", function() {
    updateCartCount();
});

// Function to Add to Cart
function addToCart(productId) {
    fetch("/add_to_cart", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ product_id: productId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("Error: " + data.error);
        } else {
            alert(data.message);
            updateCartCount();
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Failed to add item to cart. Please try again.");
    });
}

// Function to Update Cart Count
function updateCartCount() {
    fetch("/cart_count")  // Fetches only the cart count (create this route in Flask)
    .then(response => response.json())
    .then(data => {
        let cartCountElement = document.getElementById("cart-count");
        if (cartCountElement) {
            cartCountElement.innerText = data.count;
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
