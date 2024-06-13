async function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    const response = await fetch('http://localhost:3000/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });
  
    const data = await response.json();
    if (data.success) {
      document.getElementById('dashboard').classList.remove('hidden');
      document.getElementById('loginForm').classList.add('hidden');
      loadDiscussions();
    } else {
      alert('Login failed!');
    }
  }
  
  async function createPost() {
    const postText = document.getElementById('postText').value;
    const postImage = document.getElementById('postImage').files[0];
    const postTags = document.getElementById('postTags').value.split(',');
  
    const formData = new FormData();
    formData.append('text', postText);
    formData.append('image', postImage);
    formData.append('tags', postTags);
  
    const response = await fetch('http://localhost:3000/api/discussions', {
      method: 'POST',
      body: formData
    });
  
    const data = await response.json();
    if (data.success) {
      alert('Post created successfully!');
      loadDiscussions();
    } else {
      alert('Failed to create post.');
    }
  }
  
  async function searchUsers() {
    const searchUser = document.getElementById('searchUser').value;
  
    const response = await fetch(`http://localhost:3000/api/users?name=${searchUser}`);
    const data = await response.json();
  
    const searchResults = document.getElementById('searchResults');
    searchResults.innerHTML = '';
    data.users.forEach(user => {
      const userDiv = document.createElement('div');
      userDiv.className = 'card shadow-lg compact bg-base-100 p-4 mb-2';
      userDiv.innerHTML = `
        <div class="flex items-center space-x-4">
          <div>
            <h3 class="text-lg font-bold">${user.name}</h3>
            <p>${user.email}</p>
          </div>
        </div>
      `;
      searchResults.appendChild(userDiv);
    });
  }
  
  async function loadDiscussions() {
    const response = await fetch('http://localhost:3000/api/discussions');
    const data = await response.json();
  
    const discussionsDiv = document.getElementById('discussions');
    discussionsDiv.innerHTML = '';
    data.discussions.forEach(discussion => {
      const discussionDiv = document.createElement('div');
      discussionDiv.className = 'card shadow-lg compact bg-base-100 p-4 mb-2';
      discussionDiv.innerHTML = `
        <div>
          <h3 class="text-lg font-bold">${discussion.text}</h3>
          ${discussion.image ? `<img src="${discussion.image}" class="w-full h-auto mt-2">` : ''}
          <p class="mt-2">Tags: ${discussion.tags.join(', ')}</p>
        </div>
      `;
      discussionsDiv.appendChild(discussionDiv);
    });
  }
  