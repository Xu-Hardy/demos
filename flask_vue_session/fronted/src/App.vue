<template>
  <div class="container">
    <h1>GitHub SSO with Flask and Vue</h1>
    <div v-if="loggedIn" class="user-info">
      <img :src="user.avatar_url" alt="User Avatar" class="avatar" />
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Name:</strong> {{ user.name }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <button @click="logout" class="logout-btn">Logout</button>
    </div>
    <div v-else>
      <button @click="login" class="login-btn">Login with GitHub</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loggedIn: false,
      user: {
        username: '',
        avatar_url: '',
        name: '',
        email: ''
      }
    };
  },
  created() {
    this.checkLoginStatus();
  },
  methods: {
    async checkLoginStatus() {
      try {
        const response = await axios.get('http://localhost:8000/api/check_login', { withCredentials: true });
        if (response.data.logged_in) {
          this.loggedIn = true;
          this.user = response.data.user;
        }
      } catch (error) {
        console.error('Error checking login status:', error);
      }
    },
    login() {
      window.location.href = 'http://localhost:8000/login';
    },
    async logout() {
      try {
        await axios.get('http://localhost:8000/logout', { withCredentials: true });
        this.loggedIn = false;
        this.user = {
          username: '',
          avatar_url: '',
          name: '',
          email: ''
        };
      } catch (error) {
        console.error('Error logging out:', error);
      }
    }
  }
};
</script>

<style>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 20px;
}

.login-btn, .logout-btn {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border: none;
  border-radius: 5px;
  background-color: #24292e;
  color: white;
}

.login-btn:hover, .logout-btn:hover {
  background-color: #1c1f23;
}
</style>