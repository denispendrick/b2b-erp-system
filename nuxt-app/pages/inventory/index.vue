<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-900">Inventory Management</h1>
      <NuxtLink to="/inventory/products/create" class="btn-primary">
        Add Product
      </NuxtLink>
    </div>

    <!-- Tabs -->
    <div class="mb-6 border-b border-gray-200">
      <nav class="-mb-px flex space-x-8">
        <button class="border-primary-500 text-primary-600 whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm">
          Products
        </button>
        <button class="border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm">
          Stock Levels
        </button>
        <button class="border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm">
          Warehouses
        </button>
      </nav>
    </div>

    <!-- Products Table -->
    <div class="card">
      <div class="overflow-x-auto">
        <table class="table">
          <thead>
            <tr>
              <th class="table-header">SKU</th>
              <th class="table-header">Product Name</th>
              <th class="table-header">Category</th>
              <th class="table-header">Unit Price</th>
              <th class="table-header">Stock</th>
              <th class="table-header">Status</th>
              <th class="table-header">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr>
              <td class="table-cell" colspan="7">
                <div class="text-center py-8 text-gray-500">
                  No products found. Click "Add Product" to create your first product.
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
