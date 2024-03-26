import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => {
    return {
      username: ''
    };
  },
  getters: {
    getUsername: (state) => state.username
  },
  actions: {
    setUsername(name) {
      this.username = name;
    }
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: 'user', 
        storage: localStorage, 
      }
    ]
  }
});