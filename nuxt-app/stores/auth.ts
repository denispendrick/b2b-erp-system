import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as any,
    token: null as string | null,
    isAuthenticated: false
  }),

  actions: {
    async login(username: string, password: string) {
      const { api } = useApi()

      const formData = new FormData()
      formData.append('username', username)
      formData.append('password', password)

      const response = await api('/api/v1/auth/login', {
        method: 'POST',
        body: formData
      })

      this.token = response.access_token
      this.isAuthenticated = true

      const tokenCookie = useCookie('auth_token')
      tokenCookie.value = response.access_token
    },

    logout() {
      this.user = null
      this.token = null
      this.isAuthenticated = false

      const tokenCookie = useCookie('auth_token')
      tokenCookie.value = null
    }
  }
})
