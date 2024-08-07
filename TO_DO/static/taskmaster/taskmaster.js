document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.querySelectorAll(".edit-btn");
    editButtons.forEach(button => {
        button.addEventListener("click", function() {
            const taskItem = this.closest("li");
            const taskText = taskItem.querySelector(".task-text");
            const editForm = taskItem.querySelector(".edit-form");
            
            taskText.style.display = "none";
            editForm.style.display = "inline";
        });
    });

    const cancelButtons = document.querySelectorAll(".cancel-btn");
    cancelButtons.forEach(button => {
        button.addEventListener("click", function() {
            const taskItem = this.closest("li");
            const taskText = taskItem.querySelector(".task-text");
            const editForm = taskItem.querySelector(".edit-form");

            taskText.style.display = "inline";
            editForm.style.display = "none";
        });
    });
});