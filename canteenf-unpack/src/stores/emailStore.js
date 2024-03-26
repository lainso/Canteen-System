import { defineStore } from 'pinia';

export const useEmailStore = defineStore('emailAddress', {
    state: () => {
        return {
            email: ''
        };
    },
    getters: {
        getEmail: (state) => state.email
    },
    actions: {
        setEmail(address) {
            this.email = address;
        }
    }
});