const queryParams = new URLSearchParams(window.location.search);
const postId = queryParams.get("id");
if (postId) {
    loadPost(postId);
}

async function loadPost(postId) {
    const response = await fetch(`/api/posts/${postId}`);
    if (!response.ok) {
        throw new Error("Failed to load blog post");
    }
    const post = await response.json();

    document.getElementsByTagName("h1")[0].innerText = post.title;
    document.getElementById(
        "attribution"
    ).innerText = `By ${post.author} on ${post.posted_date}`;
    document.getElementById("body").innerText = post.body;
}
