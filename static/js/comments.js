/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the editButtons collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the commentText input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the edit_comment/{commentId} endpoint.
 */

console.log("Comments.js loaded successfully");

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM ready - initializing comment editing");
    
    // Get all edit buttons
    const editButtons = document.getElementsByClassName("btn-edit");
    console.log("Edit buttons found:", editButtons.length);

    // Get all delete buttons
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
    
    // Get form elements
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    
    console.log("Form found:", !!commentForm);
    console.log("Submit button found:", !!submitButton);
    
    // Update debug panel
    const debugElement = document.getElementById("form-field-debug");
    if (debugElement) {
        const allInputs = document.querySelectorAll("input, textarea");
        let debugText = `Script loaded! Found ${allInputs.length} inputs/textareas:<br><br>`;
        
        allInputs.forEach((input, i) => {
            debugText += `${i+1}. ${input.tagName} - name:"${input.name || 'none'}" id:"${input.id || 'none'}"<br>`;
        });
        
        debugElement.innerHTML = debugText;
    }
    
    // Add click handlers to each edit button
    for (let i = 0; i < editButtons.length; i++) {
        const button = editButtons[i];
        
        button.addEventListener("click", function(e) {
            console.log("Edit button clicked!");
            
            // Step 1: Retrieve the associated comment's ID upon click
            const commentId = this.getAttribute("comment_id");
            console.log("Comment ID retrieved:", commentId);
            
            // Step 2: Fetch the content of the corresponding comment
            const commentElement = document.getElementById(`comment${commentId}`);
            if (!commentElement) {
                console.error("Comment element not found:", `comment${commentId}`);
                return;
            }
            
            const commentContent = commentElement.innerText.trim();
            console.log("Comment content fetched:", commentContent);
            
            // Step 3: Populate the commentText input/textarea with the comment's content for editing
            const commentTextArea = document.querySelector("textarea[name='content']") ||
                                  document.querySelector("#id_content") ||
                                  document.querySelector("#commentForm textarea") ||
                                  document.querySelector("textarea");
            
            if (!commentTextArea) {
                console.error("Comment text area not found");
                alert("Error: Could not find comment text field");
                return;
            }
            
            commentTextArea.value = commentContent;
            console.log("Comment text area populated with content");
            
            // Step 4: Update the submit button's text to "Update"
            if (submitButton) {
                submitButton.innerText = "Update";
                submitButton.classList.remove("btn-signup");
                submitButton.classList.add("btn-primary");
                console.log("Submit button text updated to 'Update'");
            }
            
            // Step 5: Set the form's action attribute to the edit_comment/{commentId} endpoint
            if (commentForm) {
                commentForm.setAttribute("action", `edit_comment/${commentId}/`);
                console.log("Form action set to:", `edit_comment/${commentId}/`);
            }
            
            // Additional enhancements
            // Add cancel button
            if (!document.getElementById("cancelBtn")) {
                const cancelBtn = document.createElement("button");
                cancelBtn.type = "button";
                cancelBtn.id = "cancelBtn";
                cancelBtn.className = "btn btn-secondary btn-lg ms-2";
                cancelBtn.innerText = "Cancel";
                
                cancelBtn.onclick = function() {
                    // Reset everything
                    commentTextArea.value = "";
                    submitButton.innerText = "Submit";
                    submitButton.classList.remove("btn-primary");
                    submitButton.classList.add("btn-signup");
                    commentForm.setAttribute("action", "");
                    cancelBtn.remove();
                    console.log("Form reset to initial state");
                };
                
                submitButton.parentNode.appendChild(cancelBtn);
                console.log("Cancel button added");
            }
            
            // Scroll to form and focus
            commentForm.scrollIntoView({ behavior: 'smooth' });
            commentTextArea.focus();
            
            console.log("Edit functionality initialization complete for comment", commentId);
        });
    }
    
    console.log("All edit buttons initialized successfully");
});

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}