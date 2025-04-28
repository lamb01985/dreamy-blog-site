const newPost = document.getElementById("new_post"); // get the form element from HTML

if(newPost) {
    newPost.addEventListener("submit", createPost) // attach a handler function called "createPost" to the submit event
} else {
    console.error("Post form not found!");
}

async function createPost(event) {  // TODO: implement the function "createPost"
    event.preventDefault(); // Don't let the from submit in the default way
    // Gather up the post fields from the form
    const formData = new FormData(event.target)
    const title = formData.get("title");
    const author = formData.get("author");
    const content = formData.get("content");

    // Add the current date to the post fields as posted_date
    const today = new Date().toISOString().split("T")[0];  

    const body = JSON.stringify({
        title: title,
        author: author,
        body: content,
        posted_date: today
    });

    const headers = {      // Create the necessary request headers
        Accept: "application/json",
        "Content-Type": "application/json"
    };

    try {
        const response = await fetch("/api/posts", {   // Make a POST request to "/api/posts" to create a new post
            method: "POST",
            headers,
            body: body
        });

        if (!response.ok) {
            throw new Error(`${response.status}`);
        }

        //if response OK, direct user back to homepage
        location.href = "/posts.html";
    } catch (error) {
        console.error("Error creating post", error)
        alert("Error occured creating post! Contact your website administrator.")
    }

}
