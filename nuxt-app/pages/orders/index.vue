<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-900">Order Management</h1>
      <div class="flex gap-2">
        <NuxtLink to="/orders/sales/create" class="btn-primary">
          New Sales Order
        </NuxtLink>
        <NuxtLink to="/orders/purchases/create" class="btn-secondary">
          New Purchase Order
        </NuxtLink>
      </div>
    </div>

    <!-- Tabs -->
    <div class="mb-6 border-b border-gray-200">
      <nav class="-mb-px flex space-x-8">
        <button class="border-primary-500 text-primary-600 whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm">
          Sales Orders
        </button>
        <button class="border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm">
          Purchase Orders
        </button>
        <button class="border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm">
          Customers
        </button>
      </nav>
    </div>

    <!-- Orders Table -->
    <div class="card">
      <div class="overflow-x-auto">
        <table class="table">
          <thead>
            <tr>
              <th class="table-header">Order #</th>
              <th class="table-header">Customer</th>
              <th class="table-header">Order Date</th>
              <th class="table-header">Status</th>
              <th class="table-header">Total Amount</th>
              <th class="table-header">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr>
              <td class="table-cell" colspan="6">
                <div class="text-center py-8 text-gray-500">
                  No orders found. Click "New Sales Order" to create your first order.
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
