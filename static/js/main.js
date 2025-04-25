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
        alert(data.message);
        updateCartCount();
    })
    .catch(error => console.error("Error:", error));
}

// Function to Update Cart Count
function updateCartCount() {
    fetch("/cart")
    .then(response => response.text())
    .then(html => {
        let parser = new DOMParser();
        let doc = parser.parseFromString(html, "text/html");
        let cartItems = doc.querySelectorAll(".cart-item").length;
        document.getElementById("cart-count").innerText = cartItems;
    })
    .catch(error => console.error("Error:", error));
}
