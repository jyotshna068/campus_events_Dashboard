document.querySelectorAll(".delete-btn").forEach(btn => {
    btn.addEventListener("click", function(e) {
        if (!confirm("Delete this item?")) {
            e.preventDefault();
        }
    });
});