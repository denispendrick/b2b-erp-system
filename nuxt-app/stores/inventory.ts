import { defineStore } from 'pinia'

export const useInventoryStore = defineStore('inventory', {
  state: () => ({
    products: [] as any[],
    loading: false
  }),

  actions: {
    async fetchProducts() {
      this.loading = true
      try {
        const { api } = useApi()
        this.products = await api('/api/v1/products/')
      } finally {
        this.loading = false
      }
    },

    async createProduct(productData: any) {
      const { api } = useApi()
      return await api('/api/v1/products/', {
        method: 'POST',
        body: productData
      })
    }
  }
})
