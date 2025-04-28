const postList = document.getElementById('post-list');
if(postList) {
    loadPosts();
}

async function loadPosts() {
    const response = await fetch('/api/posts');
    if (! response.ok) {
        throw new Error('Failed to load blog posts');
    }
    const posts = await response.json();

    for(let post of posts) {
        const node = document.createElement('div');
        node.classList.add('post');
        node.innerHTML = `
            <div class="title"><a href="/post-detail.html?id=${post.id}">${post.title}</a></div>
            <div class="attribution">By ${post.author} on ${post.posted_date}</div>
            <div class="body">${post.body}</div>
        `;
        postList.appendChild(node);
    }
}